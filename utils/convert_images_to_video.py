import cv2
import os
import argparse

def images_to_video(image_folder, video_name, fps):
    images = [img for img in os.listdir(image_folder) if img.endswith(".png")]
    images.sort()
    frame = cv2.imread(os.path.join(image_folder, images[0]))
    height, width, layers = frame.shape

    video = cv2.VideoWriter(video_name, cv2.VideoWriter_fourcc(*'mp4v'), fps, (width,height))

    for image in images:
        video.write(cv2.imread(os.path.join(image_folder, image)))

    cv2.destroyAllWindows()
    video.release()

if __name__ == "__main__":
    # Argument parsing
    parser = argparse.ArgumentParser(description="Convert images to a video.")
    parser.add_argument("--input", "-i", required=True, help="Path to the input image folder.")
    parser.add_argument("--output", "-o", required=True, help="Path to the output video file.")
    parser.add_argument("--fps", "-f", type=int, default=15, help="FPS of the output video (default: 15).")
    args = parser.parse_args()

    # 입력 및 출력 경로 설정
    image_folder = args.input
    video_name = args.output
    fps = args.fps
    
    # 이미지를 비디오로 변환하는 함수 호출
    images_to_video(image_folder, video_name, fps)
