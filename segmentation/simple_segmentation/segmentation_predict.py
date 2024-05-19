import cv2
from ultralytics import YOLO
from ultralytics.utils.plotting import Annotator, colors
import numpy as np
import argparse

if __name__ == "__main__":
    # Argument parsing
    parser = argparse.ArgumentParser(description="Perform object detection on a video using YOLO.")
    parser.add_argument("--model", "-m", required=True, help="Path to the YOLO model weights file.")
    parser.add_argument("--video", "-v", required=True, help="Path to the input video file.")
    args = parser.parse_args()

    # YOLO 모델 초기화
    model = YOLO(args.model)  
    
    # 입력 비디오 파일 열기
    cap = cv2.VideoCapture(args.video)
    
    # 비디오 속성 가져오기
    w, h, fps = (int(cap.get(x)) for x in (cv2.CAP_PROP_FRAME_WIDTH, cv2.CAP_PROP_FRAME_HEIGHT, cv2.CAP_PROP_FPS))
    
    # 출력 비디오 설정
    segmentation_predict_video_out = cv2.VideoWriter('segmentation_predict_video.avi', cv2.VideoWriter_fourcc(*'MJPG'), fps, (w, h))

    while cap.isOpened():
        ret, img = cap.read()
        if not ret:
            print("Video img is empty or video processing has been successfully completed.")
            break

        # YOLO를 사용하여 객체 탐지 수행
        results = model.predict(img, conf=0.3)
        
        # 객체 탐지 결과를 이미지로 플로팅
        segmentation_img = results[0].plot()
        
        # 출력 비디오에 프레임 쓰기
        segmentation_predict_video_out.write(img)

        # 이미지 표시
        cv2.imshow("original_video_out", img)
        cv2.imshow("segmentation_predict_video_out", segmentation_img)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
                
    # 자원 해제
    cap.release()
    segmentation_predict_video_out.release()
    cv2.destroyAllWindows()
