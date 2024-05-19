import argparse
import os
import datetime
import shutil
import cv2
from ultralytics import YOLO
from ultralytics.utils.plotting import Annotator, colors
import numpy as np
from PIL import Image

def main(video_name):
    # 모델 경로
    model_path = "./segmentation/models/best.pt"
    # 비디오 경로
    video_path = f"./input/{video_name}" # video name: input.mp4
    
    # YOLO 모델 초기화
    model = YOLO(model_path)  
    
    # 입력 비디오 파일 열기
    cap = cv2.VideoCapture(video_path)

    # 비디오 속성 가져오기
    w, h, fps = (int(cap.get(x)) for x in (cv2.CAP_PROP_FRAME_WIDTH, cv2.CAP_PROP_FRAME_HEIGHT, cv2.CAP_PROP_FPS))
    
    # 결과를 저장할 디렉토리 생성
    output_video_dir = "./tmp"
    output_images_dir = "./tmp/tmp_LaMa_test_images"
    
    os.makedirs(output_video_dir, exist_ok=True)
    os.makedirs(output_images_dir, exist_ok=True)
    
    # 원본 비디오 파일 복사
    original_video_copy_path = os.path.join(output_video_dir, video_name)
    shutil.copy(video_path, original_video_copy_path)

    # 출력 비디오 설정
    segmentation_video_out_path = os.path.join(output_video_dir, 'segmentation.mp4')
    binary_masking_video_out_path = os.path.join(output_video_dir, 'binary_masking.mp4')
    
    # 출력 비디오 설정
    segmentation_video_out = cv2.VideoWriter(segmentation_video_out_path, cv2.VideoWriter_fourcc(*'mp4v'), fps, (w, h))
    binary_masking_video_out = cv2.VideoWriter(binary_masking_video_out_path, cv2.VideoWriter_fourcc(*'mp4v'), fps, (w, h))

    frame_count = 0
    
    while cap.isOpened():
        ret, img = cap.read()
        if not ret:
            print("Video img is empty or video processing has been successfully completed.")
            break

        results = model.predict(img, conf=0.3)
        
        segmentation_img = results[0].plot()
        
        binary_masking_img = np.zeros_like(img, dtype=np.uint8)

        if results[0].masks is not None:
            
            masks = results[0].masks.xy
            
            for mask in masks:
                mask = mask.astype(np.int32)  # 좌표를 정수로 변환
                try:
                    filled_mask = cv2.fillPoly(np.zeros_like(img, dtype=np.uint8), [mask], (255, 255, 255)) # 테두리 점들을 잇고 내부 흰색으로 색칠
                    
                    # 마스크 이미지 내부의 흰색 좌표에 패딩을 주기 위해 팽창 연산 수행
                    kernel_size = 20  # 팽창 커널 크기 설정
                    dilated_mask = cv2.dilate(filled_mask, np.ones((kernel_size, kernel_size), dtype=np.uint8)) # 내부 색칠된 마스크들에 약간의 패딩 더하기
                    
                    # 팽창된 마스크를 마스킹 비디오에 추가
                    binary_masking_img = cv2.bitwise_or(binary_masking_img, dilated_mask)
                except:
                    pass

        segmentation_video_out.write(segmentation_img)
        binary_masking_video_out.write(binary_masking_img)

        # Save segmentation image
        original_image_filename = f"image{frame_count:04d}.png"
        original_image_filepath = os.path.join(output_images_dir, original_image_filename)
        cv2.imwrite(original_image_filepath, img)
        
        # Save binary masking image
        binary_masking_image_filename = f"image{frame_count:04d}_mask000.png"
        binary_masking_image_filepath = os.path.join(output_images_dir, binary_masking_image_filename)
        cv2.imwrite(binary_masking_image_filepath, binary_masking_img)
        
        
        cv2.imshow("blockage", img)
        cv2.imshow("segmentation", segmentation_img)
        cv2.imshow("binary_masking", binary_masking_img)
        
        frame_count += 1
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
                
    # 자원 해제
    cap.release()
    segmentation_video_out.release()
    binary_masking_video_out.release()
    
    cv2.destroyAllWindows()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Perform object detection and binary mask generation on a video using YOLO.")
    parser.add_argument("--video_name", "-v", required=True, help="Name of the video file located in the ../input directory.")
    args = parser.parse_args()
    main(args.video_name)
    if not os.path.exists(f"./input/{args.video_name}"):
        print(f"Error: The video file './input/{args.video_name}' does not exist. Please place the video file in the './input' directory and ensure the name is correct.")
        print("Example usage: python demo.py -v input.mp4")