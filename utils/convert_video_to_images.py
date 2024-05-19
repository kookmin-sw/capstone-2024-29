<<<<<<< HEAD
<<<<<<< HEAD
import cv2
import os
import argparse

def extract_frames(video_path, output_path, start_frame=1):
    # MP4 파일 열기
    video_capture = cv2.VideoCapture(video_path)
    
    # 프레임 번호 초기화
    frame_num = start_frame
    
    # 비디오의 프레임을 읽어 이미지로 저장
    while True:
        success, frame = video_capture.read()
        if not success:
            break
        
        # 이미지 파일명 생성 (예: '00001.jpg', '00002.jpg', ...)
        filename = f"{output_path}/{str(frame_num).zfill(5)}.jpg"
        
        # 이미지 저장
        cv2.imwrite(filename, frame)
        
        frame_num += 1
    
    # 비디오 파일 닫기
    video_capture.release()

if __name__ == "__main__":
    # Argument parsing
    parser = argparse.ArgumentParser(description="Extract frames from a video.")
    parser.add_argument("--video", "-v", required=True, help="Path to the input video file.")
    parser.add_argument("--output", "-o", required=True, help="Path to the output directory where frames will be saved.")
    parser.add_argument("--start_frame", "-s", type=int, default=1, help="Frame number to start extraction (default: 1).")
    args = parser.parse_args()

    # 입력 및 출력 경로 설정
    video_path = args.video
    output_path = args.output
    start_frame = args.start_frame
    
    # 프레임 추출 함수 호출
    extract_frames(video_path, output_path, start_frame)
=======
import cv2
import os
import argparse

def extract_frames(video_path, output_path, start_frame=1):
    # MP4 파일 열기
    video_capture = cv2.VideoCapture(video_path)
    
    # 프레임 번호 초기화
    frame_num = start_frame
    
    # 비디오의 프레임을 읽어 이미지로 저장
    while True:
        success, frame = video_capture.read()
        if not success:
            break
        
        # 이미지 파일명 생성 (예: '00001.jpg', '00002.jpg', ...)
        filename = f"{output_path}/{str(frame_num).zfill(5)}.jpg"
        
        # 이미지 저장
        cv2.imwrite(filename, frame)
        
        frame_num += 1
    
    # 비디오 파일 닫기
    video_capture.release()

if __name__ == "__main__":
    # Argument parsing
    parser = argparse.ArgumentParser(description="Extract frames from a video.")
    parser.add_argument("--video", "-v", required=True, help="Path to the input video file.")
    parser.add_argument("--output", "-o", required=True, help="Path to the output directory where frames will be saved.")
    parser.add_argument("--start_frame", "-s", type=int, default=1, help="Frame number to start extraction (default: 1).")
    args = parser.parse_args()

    # 입력 및 출력 경로 설정
    video_path = args.video
    output_path = args.output
    start_frame = args.start_frame
    
    # 프레임 추출 함수 호출
    extract_frames(video_path, output_path, start_frame)
>>>>>>> 76971c0462add79cbd2d9396a36aecfdf9cbd931
=======
import cv2
import os
import argparse

def extract_frames(video_path, output_path, start_frame=1):
    # MP4 파일 열기
    video_capture = cv2.VideoCapture(video_path)
    
    # 프레임 번호 초기화
    frame_num = start_frame
    
    # 비디오의 프레임을 읽어 이미지로 저장
    while True:
        success, frame = video_capture.read()
        if not success:
            break
        
        # 이미지 파일명 생성 (예: '00001.jpg', '00002.jpg', ...)
        filename = f"{output_path}/{str(frame_num).zfill(5)}.jpg"
        
        # 이미지 저장
        cv2.imwrite(filename, frame)
        
        frame_num += 1
    
    # 비디오 파일 닫기
    video_capture.release()

if __name__ == "__main__":
    # Argument parsing
    parser = argparse.ArgumentParser(description="Extract frames from a video.")
    parser.add_argument("--video", "-v", required=True, help="Path to the input video file.")
    parser.add_argument("--output", "-o", required=True, help="Path to the output directory where frames will be saved.")
    parser.add_argument("--start_frame", "-s", type=int, default=1, help="Frame number to start extraction (default: 1).")
    args = parser.parse_args()

    # 입력 및 출력 경로 설정
    video_path = args.video
    output_path = args.output
    start_frame = args.start_frame
    
    # 프레임 추출 함수 호출
    extract_frames(video_path, output_path, start_frame)
>>>>>>> 76971c0462add79cbd2d9396a36aecfdf9cbd931
