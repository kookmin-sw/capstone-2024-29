import cv2
from ultralytics import YOLO
from ultralytics.utils.plotting import Annotator, colors
import numpy as np
from PIL import Image

from collections import defaultdict

track_history = defaultdict(lambda: [])

model = YOLO("../../models/weights/best.pt")  
cap = cv2.VideoCapture("../../input/mud.mp4")
w, h, fps = (int(cap.get(x)) for x in (cv2.CAP_PROP_FRAME_WIDTH, cv2.CAP_PROP_FRAME_HEIGHT, cv2.CAP_PROP_FPS))

segmentation_track_video_out = cv2.VideoWriter('../../output/segmentation_track_output.avi', cv2.VideoWriter_fourcc(*'MJPG'), fps, (w, h))

while cap.isOpened():
    
    ret, img = cap.read()
    if not ret:
        print("Video img is empty or video processing has been successfully completed.")
        break

    original_img = img.copy()
    
    annotator = Annotator(img, line_width=2)

    results = model.track(img, persist=True)
    
    segmentation_track_video_out.write(img)
    
    cv2.imshow("original_video_out", original_img)
    cv2.imshow("segmentation_track_video_out", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
segmentation_track_video_out.release()
cv2.destroyAllWindows()
