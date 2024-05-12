import cv2
import numpy as np
import argparse

def calculate_video_psnr(video_file1, video_file2):
    cap1 = cv2.VideoCapture(video_file1)
    cap2 = cv2.VideoCapture(video_file2)
    
    # Check if the videos are opened successfully
    if not (cap1.isOpened() and cap2.isOpened()):
        print("Error: One or both video files could not be opened.")
        return
    
    psnr_values = []
    while True:
        ret1, frame1 = cap1.read()
        ret2, frame2 = cap2.read()
        
        # If either of the videos reaches the end, break the loop
        if not (ret1 and ret2):
            break
        
        # Convert frames to YUV color space (to calculate PSNR accurately)
        frame1_yuv = cv2.cvtColor(frame1, cv2.COLOR_BGR2YUV)
        frame2_yuv = cv2.cvtColor(frame2, cv2.COLOR_BGR2YUV)
        
        # Compute PSNR for the current frame pair
        mse = np.mean((frame1_yuv - frame2_yuv) ** 2)
        if mse == 0:
            psnr = float('inf')
        else:
            max_pixel = 255.0
            psnr = 20 * np.log10(max_pixel / np.sqrt(mse))
        psnr_values.append(psnr)
        print("Frame PSNR: ", psnr)
    
    # Calculate the average PSNR score
    avg_psnr = np.mean(psnr_values)
    print("Average PSNR between the two videos:", avg_psnr)
    
    # Release video capture objects
    cap1.release()
    cap2.release()

if __name__ == "__main__":
    # Argument parsing
    parser = argparse.ArgumentParser(description="Calculate PSNR between two videos.")
    parser.add_argument("--video1", "-v1", required=True, help="Path to the first input video file.")
    parser.add_argument("--video2", "-v2", required=True, help="Path to the second input video file.")
    args = parser.parse_args()

    # 입력 비디오 파일 경로 설정
    video_file1 = args.video1
    video_file2 = args.video2
    
    # 비디오 간 PSNR 계산 함수 호출
    calculate_video_psnr(video_file1, video_file2)
