import argparse
import cv2
import os

def resize_video(input_path, output_path, target_width=512, target_height=288):
    # 비디오 캡쳐 객체 생성
    cap = cv2.VideoCapture(input_path)

    # 비디오 프레임 너비, 높이, FPS 가져오기
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = cap.get(cv2.CAP_PROP_FPS)

    # 비디오 코덱 설정 및 비디오 라이터 생성
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # MP4 코덱 사용
    out = cv2.VideoWriter(output_path, fourcc, fps, (target_width, target_height))

    # 프레임 읽기 및 변환하여 쓰기
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # 프레임 크기 변환
        resized_frame = cv2.resize(frame, (target_width, target_height))

        # 변환된 프레임 쓰기
        out.write(resized_frame)

    # 객체 해제
    cap.release()
    out.release()

if __name__ == "__main__":
    # argparse를 사용하여 명령줄 인자 파싱
    parser = argparse.ArgumentParser(description="Resize video")
    parser.add_argument("--video_name", required=True, help="Input video name")
    args = parser.parse_args()
    

    
    # 입력 및 출력 비디오 경로
    input_video_path = f"./input/{args.video_name}"
    tmp_output_video_path = f"./input/{args.video_name}_tmp.mp4"

    # 너비(width)와 높이(height)
    target_width = 512
    target_height = 288

    # 비디오 크기 변경 함수 호출
    resize_video(input_video_path, tmp_output_video_path, target_width, target_height)

    # 원본 비디오 파일 삭제
    if os.path.exists(input_video_path):
        os.remove(input_video_path)
        
    # 임시 파일을 원본 파일 이름으로 변경
    os.rename(tmp_output_video_path, input_video_path)