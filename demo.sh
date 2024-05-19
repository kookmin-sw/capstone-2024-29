#!/bin/bash

# 기본값 설정
video_name=""

# 옵션을 파싱합니다.
while [[ "$#" -gt 0 ]]; do
    case $1 in
        --video_name) video_name="$2"; shift ;;
        *) echo "Unknown parameter passed: $1"; exit 1 ;;
    esac
    shift
done

# 옵션이 제공되었는지 확인합니다.
if [ -z "$video_name" ]; then
    echo "Usage: $0 --video_name <name>"
    exit 1
fi

python ./utils/resize_videos.py --video_name "$video_name"

# Python 스크립트를 실행하면서 인자로 전달합니다.
python ./segmentation/segmentation_binary_masking.py --video_name "$video_name"

python ./image_inpainting/predict.py model.path=$(pwd)/image_inpainting/trained_model indir=$(pwd)/tmp/tmp_LaMa_test_images/ outdir=$(pwd)/tmp/

python ./lane_detection/lane_detection.py

TMP_DIR="./tmp"
rm -rf ${TMP_DIR}