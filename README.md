# 💃 dancing_project 🕺

Mediapipe model을 기반으로 안무 영상 속 Dancer의 동작과 User의 동작 간 유사도를 실시간으로 측정하여 점수를 도출하는 Dancing Game 

# 💡 아이디어 도출배경

- 현존하는 댄싱 게임 '저스트 댄스'는 해외 곡은 다수 존재하나 케이팝은 소수이며 연 1회씩 신곡이 업데이트
- 안무를 혼자 연습하기 어렵고 내 모습과 영상을 실시간으로 비교할 수 있는 서비스가 필요

  **▶ 위 서비스가 구현된다면, 댄스분야에서도 노래방과 같은 서비스를 제공할 수 있다는 가능성으로부터 착안**

# ⭐ 모델
#### **Mediapipe**

- 구글에서 제공하는 AI 프레임워크
- 인체를 대상으로 하는 인식에 대한 다양한 형태의 기능과 모델제공
- openpose, 와 비교 결과 Webcom 연결 시 Mediapipe의 속도가 더 우수하여 채택

# 🖥 기술 스택
<img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=Python&logoColor=white"> <img src="https://img.shields.io/badge/django-3776AB?style=for-the-badge&logo=django&logoColor=white"> <img src="https://img.shields.io/badge/Javascript-FF4B4B?style=for-the-badge&logo=Javascript&logoColor=white">

# 📚 파일 구조
- templates

home.html -- 메인페이지

stgame.html -- 게임페이지

rank.html -- 점수페이지

- functions


get_keypoint.py -- 관절 추정 기능

sim_metrics.py -- 유사도 측정 기능

view.py -- 주요 기능



# 🏆 점수 도출 방법
![동작벡터](https://github.com/nayeon1107/dancing_project/assets/95599133/f7ab17e6-86d3-4328-99dc-eb1c4b78fc13)
- 추정된 포인트를 비교에 용이한 벡터 형식 동작 데이터로 변환
  - mediapipe 로 도출되는 keypoint 중 13개 사용
  
    ㄴ nose, left_shoulder, left_elbow, left_wrist,right_shoulder, right_elbow, right_wrist,left_hip, left_knee, left_ankle, right_hip, right_knee, right_ankle
  - keypoint를 연결하여 핵심 동작 벡터 변환 
  
    ㄴ 머리 : ['nose','Middle’], 어깨 : ['LShoulder','RShoulder’], 엉덩이 : ['LHip','RHip'], 왼상체1: ['LElbow','LShoulder’], 오른상체1 : ['RElbow','RShoulder’], 왼상체2 :[ 'LWrist','LElbow’], 오른상체2 : ['RWrist','RElbow'], 왼하체1 : ['LKnee','LHip'], 오른하체1 : ['RKnee','RHip’], 왼하체2 : ['LAnkle','LKnee'], 오른하체2 :['RAnkle','RKnee']
- 동일 부위의 두 벡터 간 각도차를 스코어로 정량화하기 위하여 L2 정규화, 코사인 유사도와 유클리드 거리 공식 사용 후 점수화
![정량화](https://github.com/nayeon1107/dancing_project/assets/95599133/f7f5a185-e694-4307-904d-719fcb5ff5aa)


# 개발 개요
- **인원** : 2명
- **기간**
  - ver 1 : 2023.05.11 ~ 2023.05.17


패키지 다운로드
```python
pip install requirements.txt
```

웹페이지 실행
```python
python manage.py runserver
```
