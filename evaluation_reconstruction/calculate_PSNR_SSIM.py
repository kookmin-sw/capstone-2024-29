import cv2
import numpy as np
from skimage.metrics import structural_similarity as ssim
import argparse

def calculate_video_metrics(video_file1, video_file2, output_file):
    cap1 = cv2.VideoCapture(video_file1)
    cap2 = cv2.VideoCapture(video_file2)
    
    # Check if the videos are opened successfully
    if not (cap1.isOpened() and cap2.isOpened()):
        print("Error: One or both video files could not be opened.")
        return
    
    psnr_values = []
    ssim_values = []
    with open(output_file, 'w') as f:
        while True:
            ret1, frame1 = cap1.read()
            ret2, frame2 = cap2.read()
            
            # If either of the videos reaches the end, break the loop
            if not (ret1 and ret2):
                break
            
            # Convert frames to YUV color space (to calculate PSNR accurately)
            frame1_yuv = cv2.cvtColor(frame1, cv2.COLOR_BGR2YUV)
            frame2_yuv = cv2.cvtColor(frame2, cv2.COLOR_BGR2YUV)
            
            # Convert frames to grayscale
            gray1 = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
            gray2 = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)
            
            # Compute PSNR for the current frame pair
            mse = np.mean((frame1_yuv - frame2_yuv) ** 2)
            if mse == 0:
                psnr = float('inf')
            else:
                max_pixel = 255.0
                psnr = 20 * np.log10(max_pixel / np.sqrt(mse))
            psnr_values.append(psnr)
            
            # Calculate SSIM for the current frame pair
            score, _ = ssim(gray1, gray2, full=True)
            ssim_values.append(score)
            
            
            print(f"Frame PSNR: {psnr}, SSIM: {score}\n")
            
            # Write PSNR and SSIM values to the output file
            f.write(f"Frame PSNR: {psnr}, SSIM: {score}\n")
        
        # Calculate the average PSNR score
        avg_psnr = np.mean(psnr_values)
        avg_ssim = np.mean(ssim_values)
        max_psnr = np.max(psnr_values)
        min_psnr = np.min(psnr_values)
        max_ssim = np.max(ssim_values)
        min_ssim = np.min(ssim_values)
        
        # Write average, maximum, and minimum PSNR and SSIM values to the output file
        
        f.write(f"\n=========== PSNR ===========\n")
        f.write(f"Average: {avg_psnr}\n")
        f.write(f"Maximum: {max_psnr}\n")
        f.write(f"Minimum: {min_psnr}\n")
        f.write(f"============================\n")
        
        f.write(f"\n=========== SSIM ===========\n")
        f.write(f"Average: {avg_ssim}\n")
        f.write(f"Maximum: {max_ssim}\n")
        f.write(f"Minimum: {min_ssim}\n")
        f.write(f"============================\n")
        
        print("Average PSNR between the two videos:", avg_psnr)
        print("Maximum PSNR between the two videos:", max_psnr)
        print("Minimum PSNR between the two videos:", min_psnr)
        
        print("Average SSIM between the two videos:", avg_ssim)
        print("Maximum SSIM between the two videos:", max_ssim)
        print("Minimum SSIM between the two videos:", min_ssim)
    
    # Release video capture objects
    cap1.release()
    cap2.release()

if __name__ == "__main__":
    # Argument parsing
    parser = argparse.ArgumentParser(description="Calculate PSNR and SSIM between two videos.")
    parser.add_argument("--video1", "-v1", required=True, help="Path to the first input video file.")
    parser.add_argument("--video2", "-v2", required=True, help="Path to the second input video file.")
    parser.add_argument("--output", "-o", required=True, help="Path to the output text file.")
    args = parser.parse_args()

    # Input video file paths
    video_file1 = args.video1
    video_file2 = args.video2
    output_file = args.output
    
    # Call function to calculate video metrics and write to file
    calculate_video_metrics(video_file1, video_file2, output_file)
