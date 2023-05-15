import numpy as np
import natsort
from glob import glob
import json
import cv2
import time

MOVE_PARTS=[['nose','Middle'],
            
            ['LShoulder','RShoulder'],
            ['LElbow','LShoulder'],
            ['LWrist','LElbow'],
            ['RElbow','RShoulder'],
            ['RWrist','RElbow'],

            ['LHip','RHip'],
            ['LKnee','LHip'],
            ['LAnkle','LKnee'],
            ['RKnee','RHip'],
            ['RAnkle','RKnee']]

def cosine_similarity(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * (np.linalg.norm(b)))

def get_video_keypoint(id):
    LABEL_PATH = './static/dancingLabel/'+id
    LABEL_LIST=natsort.natsorted(glob(LABEL_PATH+'/*.json'))
    MOVE_VECTOR={}

    print(len(LABEL_LIST))

    for file in LABEL_LIST:
        f = open(file)
        data = json.load(f)
        data['Middle']=[(data['LShoulder'][0]+data['RShoulder'][0])/2,(data['LShoulder'][1]+data['RShoulder'][1])/2,(data['LShoulder'][2]+data['RShoulder'][2])/2]
        file_vec=[]
        for part in MOVE_PARTS:
            st_point=data[part[0]][:3] #x,y #유사도 측정 성능 향상을 위해 z삭제
            end_point=data[part[1]][:3] #x,y #z 삭제
            vec=[ep-sp for sp, ep in zip(st_point, end_point)]
            vec=vec/np.linalg.norm(vec)
            
            file_vec.append(vec)
        
        frame_time=int(data['frame_time']/100)
        MOVE_VECTOR[frame_time]=file_vec

    return MOVE_VECTOR

def get_cam_movevector(key_dict):
    for data in key_dict:
        data['Middle']=[(data['LShoulder'][0]+data['RShoulder'][0])/2,(data['LShoulder'][1]+data['RShoulder'][1])/2,(data['LShoulder'][2]+data['RShoulder'][2])/2]
        file_vec=[]
        for part in MOVE_PARTS:
            st_point=data[part[0]][:3] #x,y #유사도 측정 성능 향상을 위해 z삭제
            end_point=data[part[1]][:3] #x,y #z 삭제
            vec=[ep-sp for sp, ep in zip(st_point, end_point)]
            vec=vec/np.linalg.norm(vec)
            
            file_vec.append(vec)
        
        return file_vec


        