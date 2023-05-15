#!/opt/local/bin/python
# -*- coding: utf-8 -*-
import cv2
import numpy as np
import mediapipe as mp
import os
import json
from sklearn.metrics.pairwise import cosine_similarity

mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_pose = mp.solutions.pose

mp_drawing_ = mp.solutions.drawing_utils
mp_drawing_styles_ = mp.solutions.drawing_styles
mp_pose_ = mp.solutions.pose


CAM_ID = 0
VIDEO_PATH = './sample/video/ditto1_video.mp4'



#검정색 이미지를 생성 
#h : 높이
#w : 넓이
#d : 깊이 (1 : gray, 3: bgr)
def create_image(h, w, d):
    image = np.zeros((h, w,  d), np.uint8)
    color = tuple(reversed((0,0,0)))
    image[:] = color
    return image



#검정색 이미지를 생성 단 배율로 더 크게
#hcout : 높이 배수(2: 세로로 2배)
#wcount : 넓이 배수 (2: 가로로 2배)
def create_image_multiple(h, w, d, hcout, wcount):
    image = np.zeros((h*hcout, w*wcount,  d), np.uint8)
    color = tuple(reversed((0,0,0)))
    image[:] = color
    return image



#통이미지 하나에 원하는 위치로 복사(표시) 
#dst : create_image_multiple 함수에서 만든 통 이미지
#src : 복사할 이미지
#h : 높이
#w : 넓이
#d : 깊이
#col : 행 위치(0부터 시작)
#row : 열 위치(0부터 시작) 
def showMultiImage(dst, src, h, w, d, col, row):
    # 3 color
    if  d==3:
        dst[(col*h):(col*h)+h, (row*w):(row*w)+w] = src[0:h, 0:w]
    # 1 color
    elif d==1:
        dst[(col*h):(col*h)+h, (row*w):(row*w)+w, 0] = src[0:h, 0:w]
        dst[(col*h):(col*h)+h, (row*w):(row*w)+w, 1] = src[0:h, 0:w]
        dst[(col*h):(col*h)+h, (row*w):(row*w)+w, 2] = src[0:h, 0:w]



##### 코드 시작 ####
cap = cv2.VideoCapture(CAM_ID) #카메라 생성
cap2 = cv2.VideoCapture('./sample/video/ditto1_video.mp4')

if cap.isOpened() == False: #카메라 생성 확인
    print ('Can\'t open the CAM(%d)' % (CAM_ID))
    exit()

#윈도우 생성 및 사이즈 변경
cv2.namedWindow('multiView')

with mp_pose.Pose(
        min_detection_confidence=0.5,
        min_tracking_confidence=0.5) as pose:
    while(True):
        #카메라에서 이미지 얻기
        ret, frame = cap.read()
        ret2, frame2 = cap2.read()

        # 이미지 사이즈
        height = frame.shape[0]
        width = frame.shape[1]
        depth = frame.shape[2]


        frame2.flags.writeable = True
        frame2 = cv2.cvtColor(frame2, cv2.COLOR_RGB2BGR)
        frame2.flags.writeable = False
        frame2 = cv2.cvtColor(frame2, cv2.COLOR_BGR2RGB)
        results2 = pose.process(frame2)

        # 웹캠 송출 처리
        frame.flags.writeable = False
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = pose.process(frame)

        # 포즈 주석을 이미지 위에 그립니다.
        frame.flags.writeable = True
        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
        mp_drawing.draw_landmarks(
            frame,
            results.pose_landmarks,
            mp_pose.POSE_CONNECTIONS,
            landmark_drawing_spec=mp_drawing_styles.get_default_pose_landmarks_style())


        # ------ 동영상에도 같이 적용 ------ #
        # frame2.flags.writeable = False
        # frame2 = cv2.cvtColor(frame2, cv2.COLOR_BGR2RGB)
        # results2 = pose.process(frame2)

        if (results2.pose_landmarks != None) and (results.pose_landmarks != None) :
            text = f"{results.pose_landmarks.landmark[0]}, {results2.pose_landmarks.landmark[0]}"
            cv2.putText(frame2, text, (100, 100), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1, lineType=cv2.LINE_AA)
            

        # # 포즈 주석을 이미지 위에 그립니다.
        # frame2.flags.writeable = True
        # frame2 = cv2.cvtColor(frame2, cv2.COLOR_RGB2BGR)
        # mp_drawing_.draw_landmarks(
        #     frame2,
        #     results2.pose_landmarks,
        #     mp_pose_.POSE_CONNECTIONS,
        #     landmark_drawing_spec=mp_drawing_styles_.get_default_pose_landmarks_style())

        # 화면에 표시할 이미지 만들기 ( 2 x 2 )
        dstimage = create_image_multiple(height, width, depth, 1, 2)

        # 원하는 위치에 복사
        #왼쪽 위에 표시(0,0)
        showMultiImage(dstimage, frame, height, width, depth, 0, 0)
        #오른쪽 위에 표시(0,1)
        showMultiImage(dstimage, frame2, height, width, depth, 0, 1)


        # 화면 표시
        cv2.imshow('multiView',dstimage)

        #1ms 동안 키입력 대기 ESC키 눌리면 종료
        if cv2.waitKey(1) == 27:
            break;

#윈도우 종료
cap.release()
cv2.destroyWindow('multiView')