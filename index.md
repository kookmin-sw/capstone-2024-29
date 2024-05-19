<!-- PROJECT LOGO -->
<br/>
<div align="center">
  <a href="https://github.com/othneildrew/Best-README-Template">
    <img src="https://github.com/kookmin-sw/capstone-2024-29/assets/97654622/1b1202a7-e86f-4116-9f8b-4f1a655590b1" alt="Logo" width="200">
  </a>
  <p align="center">
    <h3>가상 검증을 통한 AI Segmentation & Inpainting 기반</h3>
    <h3>자율주행 차량 카메라 센서 데이터 복원 시스템</h3>
    <a href="https://github.com/kookmin-sw/capstone-2024-29/"><strong>Github Project»</strong></a>
    <br/>
    <br/>
    <a href="https://drive.google.com/file/d/1BzG9TZCIlh8-AR9lcQLL_JFlLFJuQi7q/view?usp=sharing"><strong>[최종 보고서]</strong></a>
    ·
    <a href="https://drive.google.com/file/d/10aN_GWOGEg3s0kv2hkrTJInUGjD0v7Mm/view?usp=sharing"><strong>[최종 발표자료]</strong></a>
    ·
    <a href="https://drive.google.com/drive/folders/1JG_uZ_8SscJbndWIRyrJjG9popEl_f5N?usp=sharing"><strong>[Datasets]</strong></a>
    .
    <a href="https://drive.google.com/drive/folders/10rTSopBSLmt1ZVPomukQiAclbBFIBYo1?usp=sharing"><strong>[Inpainting Weights]</strong></a>
    <br/>
  </p>
</div>

<!-- About the Project -->
## 프로젝트 소개
<img src="https://github.com/kookmin-sw/capstone-2024-29/assets/97654622/2c3e94ab-1eb5-450b-a658-a9560aaf3222" width="640" />

자율주행 차량에 사용되는 여러 센서 중 카메라 센서는 ‘인간의 눈’ 역할을 담당하는 만큼 높은 신뢰성과 강인성이 중요합니다.

실제로 LKA(Lane Keeping Assist), LFA(Lane Following Assist) 그리고 HDA(Highway Driving Assist) 등 차선 인식 기반 ADAS 사용 중 카메라 센서에 오염이 발생할 경우 차량 제어에 이상이 생겨 치명적인 사고로 발생할 가능성이 있습니다.

카메라 센서 오염과 관련하여 현재 시장에 나와 있는, 혹은 관련 연구가 진행되고 있는 솔루션은 크게 세 가지입니다.
* 자율주행 기능 비활성화하기. 그러나, 근본적인 해결책이 될 수 없습니다.
* Built-in 팝업 노즐을 활용하여 물 세척하기. 그러나, 날씨에 따라 오히려 얼룩(Water Spot)이 발생할 수 있습니다.
* 카메라 커버 글래스를 회전시켜 고정된 와이퍼로 오염물질 제거하기. 그러나, 아직 실제 양산으로 이어지지 않았습니다.

이처럼 하드웨어 기반의 솔루션을 중점으로 개발이 진행되고 있는 현 시장의 상황을 바탕으로 본 팀은 카메라 렌즈 오염 문제를 소프트웨어적인 솔루션으로 해결하는 ‘Recovery Cam’을 제안합니다.

이를 통해 차량 설계 및 디자인 변경 최소화는 물론, 자율주행 차량의 강건한 카메라 인지 성능을 보장하여 인명사고를 예방하길 기대합니다.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<br/>

### 산학 협력 기업: dSPACE Korea


<img src="https://github.com/kookmin-sw/capstone-2024-29/assets/97654622/48c32b29-ca28-4bfe-9213-a5df6927f210" alt="dSPACE"  width="640"/><br/><br/>
<p align="center">
  "자율주행차 개발을 위한 시뮬레이션 및 검증 솔루션을 제공하는 선도적인 글로벌 기업"
</p>

<br/>

dSPACE는 소프트웨어(SIL) 및 하드웨어(HIL) 기반의 시뮬레이션을 통해 복잡한 시스템의 효율적인 개발과 신뢰할 수 있는 검증 프로세스를 제공합니다. 

글로벌 모빌리티 시장을 이끄는 혁신 기업으로서, 자율주행, e-mobility 및 디지털화를 위한 툴체인을 제공하여 자동차 산업의 역동적인 전환을 지원합니다. 

dSPACE는 독일 파더보른에 본사를 두고 있으며, 전 세계적으로 1,800명 이상의 직원을 두고 있습니다. 

미국, 영국, 프랑스, 크로아티아, 일본, 중국 그리고 한국에 지사를 두고 있으며, 글로벌 지원을 위해 전 세계에 dSPACE를 대표하는 공급 업체를 두고 있습니다. 

<br/>

본 프로젝트에 사용된 dSPACE사의 솔루션은 다음 세 가지입니다.
* ModelDesk: 매개변수화 및 시뮬레이션을 위한 그래픽 사용자 인터페이스
* Aurelion: ADAS/AD용 사실적인 실시간 센서 시뮬레이션
* RTMaps: 데이터 기록 및 재생, 멀티센서 인지 알고리즘 개발을 위한 프레임워크

<img src="https://github.com/kookmin-sw/capstone-2024-29/assets/97654622/100ef413-47d7-4e48-a54a-596b949c328d" width="640" />

<br/>

## Abstract
Ensuring high reliability and robustness of camera sensors is paramount in the realm of autonomous driving, where these sensors serve as the equivalent of human eyes. Contamination of camera sensors can lead to critical safety hazards, particularly in systems reliant on lane recognition such as Lane Keeping Assist (LKA), Lane Following Assist (LFA), and Highway Driving Assist (HDA). Current solutions predominantly focus on hardware-based approaches, including deactivating autonomous functions, utilizing built-in cleaning systems, and implementing rotating camera covers with wipers. However, these methods have limitations in providing comprehensive and effective mitigation strategies. In response to this challenge, this project proposes a novel software solution named 'Recovery Cam' to address camera lens contamination issues. By minimizing changes to vehicle design and architecture while ensuring robust camera perception performance, Recovery Cam aims to prevent accidents and enhance the safety of autonomous driving systems.  

<br/>

## 소개 영상
<a href="https://youtu.be/9Sv_1WKCnC4?feature=shared" target="_blank">
  <img src="https://github.com/kookmin-sw/capstone-2024-29/assets/84698896/801477b1-18f7-475b-85c5-9c4b0f6ba504" width="640">
</a>

<br/>

## Recovery Cam 팀 소개

|<img src="https://github.com/kookmin-sw/capstone-2024-29/assets/97654622/e8d07cc9-80ee-41e2-9152-038c0d73b6cf" height="150">|<img src="https://github.com/kookmin-sw/capstone-2024-29/assets/65781023/94bf2f8a-c24d-4538-ba19-afc724c3c7c1" height="150">|<img src="https://github.com/kookmin-sw/capstone-2024-29/assets/97654622/ab84878d-7918-4142-9459-4be2bd115280" height="150">|<img src="https://github.com/kookmin-sw/capstone-2024-29/assets/97654622/b2506c95-6af7-4f58-8341-f0b971e69455" height="150">|<img src="https://github.com/kookmin-sw/capstone-2024-29/assets/97654622/34a2a60c-2ddf-40ac-a3e4-6f5c35e28871" height="150">|
| :---: | :---: | :---: | :---: | :---: |
| **조규현** | **박준석** | **변준형** | **오준호** | **이세현** |
| ****1669 | ****1271 | ****1606 | ****1626 | ****3043 |

<br />

## 사용법
1. Clone Repo
 ```
git clone https://github.com/kookmin-sw/capstone-2024-29.git
 ```
<br/>
2. Create Conda Environment and Install Dependencies 
 ```
# create new anaconda env
conda create -n recovery_cam python=3.8 -y
conda activate recovery_cam
# install python dependencies
pip3 install -r requirements.txt
 ```
* CUDA >= 9.2
* PyTorch >= 1.7.1
* Torchvision >= 0.8.2
* Other required packages in requirements.txt
<br/>
3. Download Inpainting ckpt file
 ```
# Download Inpainting ckpt file
# Download trained_model from https://drive.google.com/drive/folders/10rTSopBSLmt1ZVPomukQiAclbBFIBYo1?usp=sharing

# Move the trained_model folder into the /image_inpainting folder.
# ./image_inpainting/trained_model
 ```
</br>
4. Quick test
 ```
bash ./demo.sh --video_name {your video file name}.mp4

#You can check the results in the ./demo_outputs folder.
 ```

</br> 
 
## 기타
<div align="center">
  <p align="center">
    <a href="https://kookmin-sw.github.io/capstone-2024-29/"><strong>Github Page »</strong></a>
    <br/>
    <br/>
    <a href="https://drive.google.com/file/d/1BzG9TZCIlh8-AR9lcQLL_JFlLFJuQi7q/view?usp=sharing"><strong>[최종 보고서]</strong></a>
    ·
    <a href="https://drive.google.com/file/d/10aN_GWOGEg3s0kv2hkrTJInUGjD0v7Mm/view?usp=sharing"><strong>[최종 발표자료]</strong></a>
    ·
    <a href="https://drive.google.com/drive/folders/1JG_uZ_8SscJbndWIRyrJjG9popEl_f5N?usp=sharing"><strong>[Datasets]</strong></a>
    .
    <a href="https://drive.google.com/drive/folders/10rTSopBSLmt1ZVPomukQiAclbBFIBYo1?usp=sharing"><strong>[Inpainting Weights]</strong></a>
    <br/>
  </p>
</div>



