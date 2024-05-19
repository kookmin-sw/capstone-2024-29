<<<<<<< HEAD
<<<<<<< HEAD
import cv2
import argparse

def convert_video(input_video, output_video, target_fps=15):
    # 입력 비디오 파일 열기
    video_capture = cv2.VideoCapture(input_video)
    
    # 입력 비디오의 프레임 정보 가져오기
    fps = video_capture.get(cv2.CAP_PROP_FPS)
    width = int(video_capture.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(video_capture.get(cv2.CAP_PROP_FRAME_HEIGHT))
    
    # 비디오 저장을 위한 설정
    fourcc = cv2.VideoWriter_fourcc(*'XVID')  # 비디오 코덱 설정
    out = cv2.VideoWriter(output_video, fourcc, target_fps, (width, height))
    
    # 비디오 프레임 읽어서 새로운 FPS로 저장
    while True:
        ret, frame = video_capture.read()
        if not ret:
            break
        out.write(frame)
    
    # 자원 해제
    video_capture.release()
    out.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    # Argument parsing
    parser = argparse.ArgumentParser(description="Convert video to a new FPS.")
    parser.add_argument("--input", "-i", required=True, help="Path to the input video file.")
    parser.add_argument("--output", "-o", required=True, help="Path to the output video file.")
    parser.add_argument("--fps", "-f", type=int, default=15, help="Target FPS for the output video (default: 15).")
    args = parser.parse_args()
    
    # 입력 및 출력 경로 설정
    input_video = args.input
    output_video = args.output
    target_fps = args.fps
    
    # 비디오 변환 함수 호출
    convert_video(input_video, output_video, target_fps)
=======
import cv2
import argparse

def convert_video(input_video, output_video, target_fps=15):
    # 입력 비디오 파일 열기
    video_capture = cv2.VideoCapture(input_video)
    
    # 입력 비디오의 프레임 정보 가져오기
    fps = video_capture.get(cv2.CAP_PROP_FPS)
    width = int(video_capture.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(video_capture.get(cv2.CAP_PROP_FRAME_HEIGHT))
    
    # 비디오 저장을 위한 설정
    fourcc = cv2.VideoWriter_fourcc(*'XVID')  # 비디오 코덱 설정
    out = cv2.VideoWriter(output_video, fourcc, target_fps, (width, height))
    
    # 비디오 프레임 읽어서 새로운 FPS로 저장
    while True:
        ret, frame = video_capture.read()
        if not ret:
            break
        out.write(frame)
    
    # 자원 해제
    video_capture.release()
    out.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    # Argument parsing
    parser = argparse.ArgumentParser(description="Convert video to a new FPS.")
    parser.add_argument("--input", "-i", required=True, help="Path to the input video file.")
    parser.add_argument("--output", "-o", required=True, help="Path to the output video file.")
    parser.add_argument("--fps", "-f", type=int, default=15, help="Target FPS for the output video (default: 15).")
    args = parser.parse_args()
    
    # 입력 및 출력 경로 설정
    input_video = args.input
    output_video = args.output
    target_fps = args.fps
    
    # 비디오 변환 함수 호출
    convert_video(input_video, output_video, target_fps)
>>>>>>> 76971c0462add79cbd2d9396a36aecfdf9cbd931
=======
import cv2
import argparse

def convert_video(input_video, output_video, target_fps=15):
    # 입력 비디오 파일 열기
    video_capture = cv2.VideoCapture(input_video)
    
    # 입력 비디오의 프레임 정보 가져오기
    fps = video_capture.get(cv2.CAP_PROP_FPS)
    width = int(video_capture.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(video_capture.get(cv2.CAP_PROP_FRAME_HEIGHT))
    
    # 비디오 저장을 위한 설정
    fourcc = cv2.VideoWriter_fourcc(*'XVID')  # 비디오 코덱 설정
    out = cv2.VideoWriter(output_video, fourcc, target_fps, (width, height))
    
    # 비디오 프레임 읽어서 새로운 FPS로 저장
    while True:
        ret, frame = video_capture.read()
        if not ret:
            break
        out.write(frame)
    
    # 자원 해제
    video_capture.release()
    out.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    # Argument parsing
    parser = argparse.ArgumentParser(description="Convert video to a new FPS.")
    parser.add_argument("--input", "-i", required=True, help="Path to the input video file.")
    parser.add_argument("--output", "-o", required=True, help="Path to the output video file.")
    parser.add_argument("--fps", "-f", type=int, default=15, help="Target FPS for the output video (default: 15).")
    args = parser.parse_args()
    
    # 입력 및 출력 경로 설정
    input_video = args.input
    output_video = args.output
    target_fps = args.fps
    
    # 비디오 변환 함수 호출
    convert_video(input_video, output_video, target_fps)
>>>>>>> 76971c0462add79cbd2d9396a36aecfdf9cbd931
