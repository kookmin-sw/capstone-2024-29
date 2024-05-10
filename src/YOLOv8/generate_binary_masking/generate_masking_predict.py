import cv2
from ultralytics import YOLO
from ultralytics.utils.plotting import Annotator, colors
import numpy as np
from PIL import Image

model = YOLO("../../models/weights/best.pt")  
cap = cv2.VideoCapture("../../input/mud.mp4")
w, h, fps = (int(cap.get(x)) for x in (cv2.CAP_PROP_FRAME_WIDTH, cv2.CAP_PROP_FRAME_HEIGHT, cv2.CAP_PROP_FPS))

segmentation_predict_video_out = cv2.VideoWriter('segmentation_predict_video.avi', cv2.VideoWriter_fourcc(*'MJPG'), fps, (w, h))
binary_mask_video_out = cv2.VideoWriter('mask_video.avi', cv2.VideoWriter_fourcc(*'MJPG'), fps, (w, h))

while cap.isOpened():
    
    ret, img = cap.read()
    
    if not ret:
        print("Video img is empty or video processing has been successfully completed.")
        break

    results = model.predict(img, conf=0.3)
    
    segmentation_img = results[0].plot()
    
    if results[0].masks is not None:
        
        masks = results[0].masks.xy
        
        for mask in masks:
            mask = mask.astype(np.int32)  # 좌표를 정수로 변환
            filled_mask = cv2.fillPoly(np.zeros_like(img, dtype=np.uint8), [mask], (255, 255, 255)) # 테두리 점들을 잇고 내부 흰색으로 색칠
            
            # 마스크 이미지 내부의 흰색 좌표에 패딩을 주기 위해 팽창 연산 수행
            kernel_size = 20  # 팽창 커널 크기 설정
            dilated_mask = cv2.dilate(filled_mask, np.ones((kernel_size, kernel_size), dtype=np.uint8)) # 내부 색칠된 마스크들에 약간의 패딩 더하기
            
            # 팽창된 마스크를 마스킹 비디오에 추가
            binary_mask_img = cv2.bitwise_or(binary_mask_img, dilated_mask)


    segmentation_predict_video_out.write(img)
    binary_mask_video_out.write(binary_mask_img)

    cv2.imshow("original_video_out", img)
    cv2.imshow("segmentation_predict_video_out", segmentation_img)
    cv2.imshow("binary_mask_video_out", binary_mask_img)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
            
cap.release()
segmentation_predict_video_out.release()
binary_mask_video_out.release()

cv2.destroyAllWindows()
