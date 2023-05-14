import streamlit as st
from streamlit_webrtc import VideoProcessorBase, RTCConfiguration, WebRtcMode, webrtc_streamer
import cv2
import mediapipe as mp
import time
import sim_metrics
import base64
from streamlit_player import st_player
import av
    
st.title('Dancing Game')

# 사이드바 생성
st.sidebar.title('사이드바')
st.sidebar.subheader('Select Video')

id = st.sidebar.selectbox(
    'Video',
    ['yt_newjeans_ditto1','yt_newjeans_ditto2']
)

col1, col2 = st.columns(2)
run_yn = st.checkbox("실행하기", key='run',value=False)
# -------------- Webcam PoseDetection -------------

# VIDEO_PATH = './sample/Ditto_video.mp4'
cap = cv2.VideoCapture(0)
stframe = st.empty()
origframe=st.empty()
fps = cap.get(cv2.CAP_PROP_FPS)

# -------------- PoseDetection -------------
mpPose = mp.solutions.pose
pose = mpPose.Pose()
mpDraw = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles

# def prev_video(id):
#     MOVE_VECTOR = sim_metrics.get_video_keypoint(id)

# with st.spinner():
#     prev_video(id)

options={ "playing": run_yn}

# st_player("https://www.youtube.com/watch?v=LlBG2ipO6ZU",**options, key="soundcloud_player")

k=0
# origframe.write('aaa')
# prev_time = 0
# FPS = 30
# # orig = cv2.VideoCapture("./sample/video/yt_newjeans_ditto1.mp4")

if run_yn:
    # st.video("./sample/video/yt_newjeans_ditto1.mp4")
    st_player("https://www.youtube.com/watch?v=LlBG2ipO6ZU",**options, key="soundcloud_player")

with col2:
    while run_yn :
        success, img = cap.read()
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        if(k % fps == 0): #앞서 불러온 fps 값을 사용하여 1초마다 추출
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
                print(k,landmarks)
                cv2.putText(img, landmarks, (100, 100), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 3, lineType=cv2.LINE_AA)

        # cv2.imshow('MediaPipe Pose', cv2.flip(img, 1))
        img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
        #cv2.imshow("Image", img)
        stframe.image(img)

        # print(cap.get(cv2.CAP_PROP_FPS),cap.get(cv2.CAP_PROP_POS_FRAMES))
        k+=1
        if run_yn == False:
            break
    cv2.waitKey(1)
    cap.release()

    # prev_time = 0
    # FPS = 30
    # orig = cv2.VideoCapture("./sample/video/yt_newjeans_ditto1.mp4")

    #     ret,frame = orig.read()
    #     current_time = time.time() - prev_time

    #     if (ret is True) and (current_time > 1./ FPS) :
    #         frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
    #         origframe.image(frame)




