import streamlit as st
from streamlit_webrtc import VideoProcessorBase, RTCConfiguration, WebRtcMode, webrtc_streamer
import cv2
import mediapipe as mp
import time
    


st.title('Dancing Game')

# 사이드바 생성
st.sidebar.title('사이드바')
st.sidebar.subheader('Select Video')

app_mode = st.sidebar.selectbox(
    'Video',
    ['Ditto1','Ditto2']
)

col1, col2 = st.columns(2)
run_yn = st.checkbox("실행하기", key='run')
# -------------- Webcam PoseDetection -------------

# VIDEO_PATH = './sample/Ditto_video.mp4'
cap = cv2.VideoCapture(0)
stframe = st.empty()


# -------------- PoseDetection -------------
mpPose = mp.solutions.pose
pose = mpPose.Pose()
mpDraw = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles

st.video("./sample/video/yt_newjeans_ditto1.mp4")

with col1 :
    while run_yn :
        success, img = cap.read()
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        results = pose.process(imgRGB)
        if results.pose_landmarks:
            mpDraw.draw_landmarks(
                img,
                results.pose_landmarks,
                mpPose.POSE_CONNECTIONS,
                landmark_drawing_spec=mp_drawing_styles.get_default_pose_landmarks_style())
            # for id, lm in enumerate(results.pose_landmarks.landmark):
            #     h, w,c = img.shape
            #     cx, cy = int(lm.x*w), int(lm.y*h)
            #     cv2.circle(img, (cx, cy), 5, (255,0,0), cv2.FILLED)
            landmarks = str(results.pose_landmarks.landmark[0].x)
            cv2.putText(img, landmarks, (100, 100), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 3, lineType=cv2.LINE_AA)
        cv2.imshow('MediaPipe Pose', cv2.flip(img, 1))
        img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
        #cv2.imshow("Image", img)
        stframe.image(img)

        if run_yn == False:
            break
            
    cv2.waitKey(1)
    cap.release()




