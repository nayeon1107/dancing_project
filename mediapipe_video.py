import cv2
import mediapipe as mp
import numpy as np
from glob import glob
import natsort
import os
import json
import getKeypoint

mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_pose = mp.solutions.pose

id = 'yt_newjeans_ditto1'
VIDEO_PATH = 'sample/video/'+id+'.mp4'

SAVE_PATH = 'sample/dancingLabel/'+id
if not os.path.exists(SAVE_PATH):
    os.mkdir(SAVE_PATH)
    print(SAVE_PATH, '폴더 생성 완료')

# video 불러오기 및 video 설정 저장
cap = cv2.VideoCapture(VIDEO_PATH)

video_inform = {
    'width' : int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),
    'height' : int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)),
    'fps' : cap.get(cv2.CAP_PROP_FPS),
    'frame_count' : int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
}

print(video_inform)

with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
    i=0
    while cap.isOpened():
        success, frame = cap.read()

        if not success : 
            print('카메라 미확인') 
            break
        
        # GET Frame Info
        frame.flags.writeable = False
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = pose.process(frame)
        
        frame_time=cap.get(cv2.CAP_PROP_POS_MSEC)
        frame_num=cap.get(cv2.CAP_PROP_POS_FRAMES)

        # Extract Pose Landmarks
        results = pose.process(frame)
        if not results.pose_landmarks:
            continue

        # Save Pose Keypoints
        keypoints = getKeypoint.get_keypoints(results.pose_landmarks.landmark, mp_pose,frame_time,frame_num)

        with open(SAVE_PATH+f'/{i}.json', "w") as f:
            json.dump(keypoints, f, indent='\t')
            
        i+=1
        
        if i%100==0:
            print(i)
        #'q'누르면 캠 꺼짐
        if cv2.waitKey(10) & 0xFF == ord("q"):
            break
        
    cap.release()
    cv2.destroyAllWindows()