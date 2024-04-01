<!-- PROJECT LOGO -->
<br/>
<div align="center">
  <a href="https://github.com/othneildrew/Best-README-Template">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">"Recovery Cam"</h3>

  <p align="center">
    <br/>
    가상 검증을 통한 AI Segmentation & Inpainting 기반 자율주행 차량 카메라 센서 데이터 복원 시스템
    <br/><br/>
    <a href="https://github.com/othneildrew/Best-README-Template"><strong>Explore the docs »</strong></a>
    <br/>
    <br/>
    <a href="https://github.com/othneildrew/Best-README-Template">View Demo</a>
    ·
    <a href="https://github.com/othneildrew/Best-README-Template/issues/new?labels=bug&template=bug-report---.md">Report Bug</a>
    ·
    <a href="https://github.com/othneildrew/Best-README-Template/issues/new?labels=enhancement&template=feature-request---.md">Request Feature</a>
  </p>
</div>

<!-- About the Project -->
## 프로젝트 소개

![Project_Introduction](https://github.com/kookmin-sw/capstone-2024-29/assets/97654622/1397c9a7-98cb-4fab-8706-0e6018c46e49)

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

<p align="center">
  <img src="https://github.com/kookmin-sw/capstone-2024-29/assets/97654622/48c32b29-ca28-4bfe-9213-a5df6927f210" alt="dSPACE" /><br/><br/>
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


![dSPACE_Solution](https://github.com/kookmin-sw/capstone-2024-29/assets/97654622/100ef413-47d7-4e48-a54a-596b949c328d)

<br/>

## Abstract
<div style="text-align:justify;">
Ensuring high reliability and robustness of camera sensors is paramount in the realm of autonomous driving, where these sensors serve as the equivalent of human eyes. Contamination of camera sensors can lead to critical safety hazards, particularly in systems reliant on lane recognition such as Lane Keeping Assist (LKA), Lane Following Assist (LFA), and Highway Driving Assist (HDA). Current solutions predominantly focus on hardware-based approaches, including deactivating autonomous functions, utilizing built-in cleaning systems, and implementing rotating camera covers with wipers. However, these methods have limitations in providing comprehensive and effective mitigation strategies. In response to this challenge, this project proposes a novel software solution named 'Recovery Cam' to address camera lens contamination issues. By minimizing changes to vehicle design and architecture while ensuring robust camera perception performance, Recovery Cam aims to prevent accidents and enhance the safety of autonomous driving systems.  
</div>

 <br/> <br/> <br/>
## 3. 소개 영상

👉🏻[2024_29팀_소개 영상](https://youtube.com)

 <br/> <br/> <br/>

## 4. Recovery Cam 팀 소개

|<img src="https://github.com/kookmin-sw/capstone-2024-29/assets/97654622/e8d07cc9-80ee-41e2-9152-038c0d73b6cf" height="150">|<img src="https://github.com/kookmin-sw/capstone-2024-29/assets/65781023/94bf2f8a-c24d-4538-ba19-afc724c3c7c1" height="150">|<img src="https://github.com/kookmin-sw/capstone-2024-29/assets/97654622/ab84878d-7918-4142-9459-4be2bd115280" height="150">|<img src="https://github.com/kookmin-sw/capstone-2024-29/assets/97654622/b2506c95-6af7-4f58-8341-f0b971e69455" height="150">|<img src="https://github.com/kookmin-sw/capstone-2024-29/assets/97654622/34a2a60c-2ddf-40ac-a3e4-6f5c35e28871" height="150">|
| :---: | :---: | :---: | :---: | :---: |
| **조규현** | **박준석** | **변준형** | **오준호** | **이세현** |
| ********1669 | ********1271 | ********1606 | ********1626 | ********3043 |





 <br/> 


## 5. 사용법
 ```
$ python main.py
 ```
 <br/> <br/> <br/>
 
## 6. 기타
<img src="https://github.com/kookmin-sw/capstone-2024-29/assets/65781023/5eb56ff1-17da-41ac-9fa6-2bd0bb894fc3" style="width: 100%; max-width: 700px;" alt="Description">

<img src="https://github.com/kookmin-sw/capstone-2024-29/assets/65781023/9824ee5c-d9fd-458d-8c88-4647b0535502" style="width: 100%; max-width: 700px;" alt="Description">


