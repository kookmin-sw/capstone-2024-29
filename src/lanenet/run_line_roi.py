#!/usr/bin/python3
# -*- encoding: utf-8 -*-

import os
import cv2
import torch
import numpy as np
from Lanenet.model2 import Lanenet
from utils.evaluation import process_instance_embedding

device = 'cuda' if torch.cuda.is_available() else 'cpu'

def load_model(model_path):
    LaneNet_model = Lanenet(2, 4)  # Lanenet 모델 초기화 (2개의 클래스, 4개의 인스턴스 임베딩 채널)
    LaneNet_model.load_state_dict(torch.load(model_path, map_location=torch.device(device)))  # 학습된 모델 가중치 불러오기
    LaneNet_model.to(device)  # 모델을 GPU로 옮김 (가능한 경우)
    LaneNet_model.eval()  # 모델을 평가 모드로 설정
    return LaneNet_model

def preprocess(image):
    resized_image = cv2.resize(image, dsize=(512, 288), interpolation=cv2.INTER_LINEAR)  # 이미지 크기 조정
    normalized_image = resized_image / 127.5 - 1.0  # 이미지 정규화
    transposed_image = np.transpose(normalized_image, (2, 0, 1))  # 이미지 축 변환 (H, W, C) -> (C, H, W)
    return torch.tensor(transposed_image, dtype=torch.float).to(device)  # 이미지를 텐서로 변환하고 디바이스로 보냄

def inference(model, image):
    org_shape = image.shape  # 원본 이미지의 크기 저장
    input_tensor = preprocess(image).unsqueeze(0)  # 이미지 전처리 및 배치 차원 추가

    with torch.no_grad():  # 그래디언트 계산 비활성화
        binary_final_logits, instance_embedding = model(input_tensor)  # Lanenet 모델 실행

    binary_final_logits, instance_embedding = binary_final_logits.to('cpu'), instance_embedding.to('cpu')  # 결과를 CPU로 이동
    binary_img = torch.argmax(binary_final_logits, dim=1).squeeze().numpy()  # 이진 분할 결과 계산
    binary_img[0:40, :] = 0  # (0~40행)을 무시 - 불필요한 영역 제거

    rbg_emb, cluster_result = process_instance_embedding(instance_embedding, binary_img, distance=1.5, lane_num=2)  # 인스턴스 임베딩 처리
    rbg_emb = cv2.resize(rbg_emb, dsize=(org_shape[1], org_shape[0]), interpolation=cv2.INTER_LINEAR)  # 원본 크기로 변경

    a = 0.3
    frame = a * image[..., ::-1] / 255 + (1 - a) * rbg_emb  # 원본 이미지와 검출 결과 오버레이
    frame = np.rint(frame * 255).astype(np.uint8)  # 이미지를 정수형으로 변환

    return frame

def main():
    model_path = './TUSIMPLE/Lanenet_output/lanenet_epoch_39_batch_8_AUG.model'  # 학습된 모델 경로
    LaneNet_model = load_model(model_path)  # Lanenet 모델 불러오기

    video_path = './input.mp4'  # 입력 비디오 경로
    video_capture = cv2.VideoCapture(video_path)  # 비디오 캡처 객체 생성

    while video_capture.isOpened():  # 비디오 프레임 반복
        ret, frame = video_capture.read()  # 프레임 읽기

        if ret:
            processed_frame = inference(LaneNet_model, frame)  # Lanenet을 사용하여 차선 검출
            cv2.imshow('Processed Frame', processed_frame)  # 처리된 프레임 출력

            if cv2.waitKey(1) & 0xFF == ord('q'):  # 'q' 키를 누르면 종료
                break
        else:
            break

    video_capture.release()  # 비디오 캡처 객체 해제
    cv2.destroyAllWindows()  # 모든 창 닫기

if __name__ == "__main__":
    main()