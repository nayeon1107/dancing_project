import numpy as np
import natsort
from glob import glob
import json
import cv2
import time

MOVE_PARTS=[
            ['nose','Middle'],
            
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

def check_sim(test1,test2):
    score_avg = []
    i=0
    for move1,move2 in zip(test1,test2):
        cosine_sim= cosine_similarity(move1.flatten(),move2.flatten())
        score=cosine_sim
        eud = np.sqrt(2*(1-cosine_sim))
        score=100-(100*eud/2)

        # if score >=90 :
        #     g = 5
        # elif score >= 70 :
        #     g = 4
        # elif score >= 50:
        #     g = 3
        # elif score >= 20:
        #     g = 2
        # else :
        #     g= 1

        score_avg.append(score) 
        
        # part1 = MOVE_PARTS[i][0]
        # part2 = MOVE_PARTS[i][1]
        # print(f"{part1:10s} → {part2:>10s}",end=' ')
        # print(' | score : ',score.round(3))
        # print(' ')
        
        i+=1

    return score_avg

        
def get_video_keypoint(id):
    LABEL_PATH = './static/dancingLabel/'+id
    LABEL_LIST=natsort.natsorted(glob(LABEL_PATH+'/*.json'))
    MOVE_VECTOR={}

    for file in LABEL_LIST:
        f = open(file)
        data = json.load(f)
        data['Middle']=[(data['LShoulder'][0]+data['RShoulder'][0])/2,(data['LShoulder'][1]+data['RShoulder'][1])/2,(data['LShoulder'][2]+data['RShoulder'][2])/2]
        file_vec=[]
        for part in MOVE_PARTS:
            st_point=data[part[0]][:2] #x,y #유사도 측정 성능 향상을 위해 z삭제
            end_point=data[part[1]][:2] #x,y #z 삭제
            vec=[ep-sp for sp, ep in zip(st_point, end_point)]
            vec=vec/np.linalg.norm(vec)
            
            file_vec.append(vec)
        
        frame_time=int(data['frame_time']/1000)
        MOVE_VECTOR[frame_time]=file_vec

    return MOVE_VECTOR

def get_cam_movevector(key_dict):
    file_vec=[]
    for part in MOVE_PARTS:
        st_point=key_dict[part[0]][:2] 
        end_point=key_dict[part[1]][:]
        vec=[ep-sp for sp, ep in zip(st_point, end_point)]
        vec=vec/np.linalg.norm(vec)
        
        file_vec.append(vec)
        
    return file_vec


        