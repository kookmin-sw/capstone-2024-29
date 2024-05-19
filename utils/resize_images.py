import cv2
import os
import argparse

# Function to resize a single image
def resize_image(image_path, output_path, width=512, height=288):
    # Read the image
    image = cv2.imread(image_path)
    # Resize the image
    resized_image = cv2.resize(image, (width, height))
    # Write the resized image to the output path
    cv2.imwrite(output_path, resized_image)

# Function to resize all PNG files in a directory
def resize_images_in_directory(input_dir, output_dir, width=512, height=288):
    # Create the output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    # List all files in the input directory
    files = os.listdir(input_dir)
    # Iterate through each file
    for i, file in enumerate(files):
        # Check if the file is a PNG file
        if file.endswith(".png"):
            # Construct the input and output paths
            input_path = os.path.join(input_dir, file)
            output_path = os.path.join(output_dir, file)
            # Resize the image
            resize_image(input_path, output_path, width, height)
            
            print(i, "is done")

if __name__ == "__main__":
    # Argument parsing
    parser = argparse.ArgumentParser(description="Resize images in a directory.")
    parser.add_argument("--input", "-i", required=True, help="Path to the input directory containing images.")
    parser.add_argument("--output", "-o", required=True, help="Path to the output directory where resized images will be saved.")
    parser.add_argument("--width", "-w", type=int, default=512, help="Width of the resized images (default: 512).")
    parser.add_argument("--height", "-H", type=int, default=288, help="Height of the resized images (default: 288).")
    args = parser.parse_args()

    # 입력 및 출력 경로 설정
    input_directory = args.input
    output_directory = args.output
    width = args.width
    height = args.height
    
    # 이미지 리사이징 함수 호출
    resize_images_in_directory(input_directory, output_directory, width, height)
