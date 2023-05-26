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
- **Frontend**

<img src="https://img.shields.io/badge/django-3776AB?style=for-the-badge&logo=django&logoColor=white"> <img src="https://img.shields.io/badge/Javascript-FF4B4B?style=for-the-badge&logo=Javascript&logoColor=white">

- **Backend**
<img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=Python&logoColor=white"> 

# 📚 파일 구조

# 🏆 점수 도출 방법

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
