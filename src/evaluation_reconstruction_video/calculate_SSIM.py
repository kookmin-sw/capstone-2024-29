import cv2
import numpy as np
from skimage.metrics import structural_similarity as ssim
import argparse

def calculate_video_ssim(video_file1, video_file2):
    cap1 = cv2.VideoCapture(video_file1)
    cap2 = cv2.VideoCapture(video_file2)
    
    # Check if the videos are opened successfully
    if not (cap1.isOpened() and cap2.isOpened()):
        print("Error: One or both video files could not be opened.")
        return
    
    ssim_values = []
    while True:
        ret1, frame1 = cap1.read()
        ret2, frame2 = cap2.read()
        
        # If either of the videos reaches the end, break the loop
        if not (ret1 and ret2):
            break
        
        # Convert frames to grayscale
        gray1 = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
        gray2 = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)
        
        # Calculate SSIM for the current frame pair
        score, _ = ssim(gray1, gray2, full=True)
        ssim_values.append(score)
        print("Frame SSIM: ", score)
    
    # Calculate the average SSIM score
    avg_ssim = np.mean(ssim_values)
    print("Average SSIM between the two videos:", avg_ssim)
    
    # Release video capture objects
    cap1.release()
    cap2.release()

if __name__ == "__main__":
    # Argument parsing
    parser = argparse.ArgumentParser(description="Calculate SSIM between two videos.")
    parser.add_argument("--video1", "-v1", required=True, help="Path to the first input video file.")
    parser.add_argument("--video2", "-v2", required=True, help="Path to the second input video file.")
    args = parser.parse_args()

    # 입력 비디오 파일 경로 설정
    video_file1 = args.video1
    video_file2 = args.video2
    
    # 비디오 간 SSIM 계산 함수 호출
    calculate_video_ssim(video_file1, video_file2)
