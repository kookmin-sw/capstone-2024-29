import argparse
import cv2
from ultralytics import YOLO
from ultralytics.utils.plotting import Annotator, colors
import numpy as np
import os
from collections import defaultdict

# Argument parsing
parser = argparse.ArgumentParser(description="Process input video with YOLO model and save results.")
parser.add_argument("--input", "-i", required=True, help="Path to the input video file.")
parser.add_argument("--output", "-o", required=True, help="Path to the output directory where processed images will be saved.")
args = parser.parse_args()

track_history = defaultdict(lambda: [])

model = YOLO("../weights/best.pt")   # segmentation model
cap = cv2.VideoCapture(args.input)
w, h, fps = (int(cap.get(x)) for x in (cv2.CAP_PROP_FRAME_WIDTH, cv2.CAP_PROP_FRAME_HEIGHT, cv2.CAP_PROP_FPS))

# Create directory
if not os.path.exists(args.output):
    os.makedirs(args.output)

frame_count = 0

while True:
    ret, img = cap.read()
    if not ret:
        print("Video img is empty or video processing has been successfully completed.")
        break

    original_img = img.copy()
    binary_mask_img = np.zeros_like(img, dtype=np.uint8) # Create black background

    annotator = Annotator(img, line_width=2)

    results = model.track(img, persist=True)

    if results[0].boxes.id is not None and results[0].masks is not None:
        
        masks = results[0].masks.xy
        track_ids = results[0].boxes.id.int().cpu().tolist()

        for mask, track_id in zip(masks, track_ids):
            annotator.seg_bbox(mask=mask,
                               mask_color=colors(track_id, True),
                               track_label=str(track_id))
        
            mask = mask.astype(np.int32)  # Convert coordinates to integers
            filled_mask = cv2.fillPoly(np.zeros_like(img, dtype=np.uint8), [mask], (255, 255, 255)) # Fill inside of contours with white color
            
            # Perform dilation operation to add padding to the inside filled masks
            kernel_size = 40  # Set dilation kernel size
            dilated_mask = cv2.dilate(filled_mask, np.ones((kernel_size, kernel_size), dtype=np.uint8)) # Add slight padding to the inside filled masks
            
            # Add dilated mask to binary mask image
            binary_mask_img = cv2.bitwise_or(binary_mask_img, dilated_mask)
        
        # Save original image
        original_image_filename = f"image{frame_count:03d}.png"
        original_image_filepath = os.path.join(args.output, original_image_filename)
        cv2.imwrite(original_image_filepath, original_img)
        
        # Save binary masking image
        binary_mask_filename = f"image{frame_count:03d}_mask000.png"
        binary_mask_filepath = os.path.join(args.output, binary_mask_filename)
        cv2.imwrite(binary_mask_filepath, binary_mask_img)

    else:
         # Save original image
        original_image_filename = f"image{frame_count:03d}.png"
        original_image_filepath = os.path.join(args.output, original_image_filename)
        cv2.imwrite(original_image_filepath, original_img)
        
        # Save binary masking image
        binary_mask_filename = f"image{frame_count:03d}_mask000.png"
        binary_mask_filepath = os.path.join(args.output, binary_mask_filename)
        cv2.imwrite(binary_mask_filepath, binary_mask_img)
    
    frame_count += 1

    # cv2.imshow("original_video_out", original_img)
    # cv2.imshow("segmentation_video_out", img)
    # cv2.imshow("binary_mask_video_out", binary_mask_img)

    # if cv2.waitKey(1) & 0xFF == ord('q'):
    #     break

cap.release()
cv2.destroyAllWindows()
