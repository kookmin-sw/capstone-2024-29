#!/usr/bin/python3
# -*- encoding: utf-8 -*-

import os
import cv2
import torch
import numpy as np
from datetime import datetime
from Lanenet.model2 import Lanenet
from utils.evaluation import process_instance_embedding
import shutil

device = 'cuda' if torch.cuda.is_available() else 'cpu'

def load_model(model_path):
    LaneNet_model = Lanenet(2, 4)
    LaneNet_model.load_state_dict(torch.load(model_path, map_location=torch.device(device)))
    LaneNet_model.to(device)
    LaneNet_model.eval()
    return LaneNet_model

def preprocess(image):
    resized_image = cv2.resize(image, dsize=(512, 288), interpolation=cv2.INTER_LINEAR)
    normalized_image = resized_image / 127.5 - 1.0
    transposed_image = np.transpose(normalized_image, (2, 0, 1))
    return torch.tensor(transposed_image, dtype=torch.float).to(device)

def inference(model, image):
    org_shape = image.shape
    input_tensor = preprocess(image).unsqueeze(0)
    with torch.no_grad():
        binary_final_logits, instance_embedding = model(input_tensor)
    binary_final_logits, instance_embedding = binary_final_logits.to('cpu'), instance_embedding.to('cpu')
    binary_img = torch.argmax(binary_final_logits, dim=1).squeeze().numpy()
    binary_img[0:35, :] = 0  # (0~35행)을 무시
    rbg_emb, cluster_result = process_instance_embedding(instance_embedding, binary_img, distance=1.5, lane_num=2)
    rbg_emb = cv2.resize(rbg_emb, dsize=(org_shape[1], org_shape[0]), interpolation=cv2.INTER_LINEAR)
    a = 0.5
    frame = a * image[..., ::-1] / 255 + (1 - a) * rbg_emb
    frame = np.rint(frame * 255).astype(np.uint8)
    return frame

def main():
    model_path = './lane_detection/model/lanenet_epoch_39_batch_8_AUG.model'
    LaneNet_model = load_model(model_path)

    video_path = './tmp/inpainting.mp4'
    video_capture = cv2.VideoCapture(video_path)

    # 출력 비디오 설정
    fps = video_capture.get(cv2.CAP_PROP_FPS)
    width = int(video_capture.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(video_capture.get(cv2.CAP_PROP_FRAME_HEIGHT))
    processed_output_path = './tmp/lanenet_dection.mp4'
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    video_writer = cv2.VideoWriter(processed_output_path, fourcc, fps, (width, height))

    while video_capture.isOpened():
        ret, frame = video_capture.read()
        if ret:
            processed_frame = inference(LaneNet_model, frame)
            video_writer.write(processed_frame)
            cv2.imshow('Processed Frame', processed_frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            break

    video_capture.release()
    video_writer.release()
    cv2.destroyAllWindows()

    current_time = datetime.now().strftime('%Y%m%d_%H%M%S')
    output_dir = f'./demo_outputs/{current_time}'
    os.makedirs(output_dir, exist_ok=True)

    tmp_dir = './tmp'
    for file_name in os.listdir(tmp_dir):
        if file_name.endswith('.mp4'):
            shutil.copy(os.path.join(tmp_dir, file_name), os.path.join(output_dir, file_name))

    #shutil.move(processed_output_path, os.path.join(output_dir, 'lanenet_detection_video.mp4'))

if __name__ == "__main__":
    main()