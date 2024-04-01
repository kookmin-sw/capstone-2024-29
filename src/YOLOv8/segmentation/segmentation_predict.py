import cv2
from ultralytics import YOLO
from ultralytics.utils.plotting import Annotator, colors
import numpy as np
from PIL import Image

model = YOLO("../../models/weights/best.pt")  
cap = cv2.VideoCapture("../../input/mud.mp4")
w, h, fps = (int(cap.get(x)) for x in (cv2.CAP_PROP_FRAME_WIDTH, cv2.CAP_PROP_FRAME_HEIGHT, cv2.CAP_PROP_FPS))

segmentation_predict_video_out = cv2.VideoWriter('segmentation_predict_video.avi', cv2.VideoWriter_fourcc(*'MJPG'), fps, (w, h))

while cap.isOpened():
    
    ret, img = cap.read()
    
    if not ret:
        print("Video img is empty or video processing has been successfully completed.")
        break


    results = model.predict(img, conf=0.3)
    
    segmentation_img = results[0].plot()

    segmentation_predict_video_out.write(img)

    cv2.imshow("original_video_out", img)
    cv2.imshow("segmentation_predict_video_out", segmentation_img)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
            
cap.release()
segmentation_predict_video_out.release()
cv2.destroyAllWindows()
