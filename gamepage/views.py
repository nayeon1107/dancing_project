from django.shortcuts import render
from django.views.decorators import gzip
from django.http import StreamingHttpResponse, JsonResponse, HttpResponse

from . import sim_metrics, getKeypoint
import cv2
import threading
import mediapipe as mp
import json
import numpy as np

# -------------- PoseDetection -------------
mpPose = mp.solutions.pose
pose = mpPose.Pose()
mpDraw = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles

id = 'yt_newjeans_ditto1'

def prev_video(id):
    MOVE_VECTOR = sim_metrics.get_video_keypoint(id)
    print(len(MOVE_VECTOR))
    return MOVE_VECTOR

MOVE_VECTOR = prev_video(id)
print(MOVE_VECTOR[5])

class mediapipeCam(object):
    def __init__(self):
        self.cam = cv2.VideoCapture(0)
        (self.grabbed, self.frame) = self.cam.read()
        threading.Thread(target=self.update, args=()).start()

    def __del__(self):
        self.cam.release()

    def get_frame(self):
        image = self.frame
        _, jpeg = cv2.imencode('.jpg', image)
        return jpeg.tobytes()
    
    def update(self):
        while True:
            (self.grabbed, self.frame) = self.cam.read()
            # print(self.getKeypoint(self.frame))

    def PoseProcess(self):
        imgRGB = cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGB)
        results = pose.process(imgRGB)
        if results.pose_landmarks:
            mpDraw.draw_landmarks(
                self.frame,
                results.pose_landmarks,
                mpPose.POSE_CONNECTIONS,
                landmark_drawing_spec=mp_drawing_styles.get_default_pose_landmarks_style())

        return results
        
# -------------- Basic Cam -------------
def home(request):
    context = {}
    return render(request, "gamepage/home.html", context)

def gen(camera):
    while True:
        frame = camera.get_frame()
        yield(b'--frame\r\n'
              b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

cam = mediapipeCam()

@gzip.gzip_page
def detectme(request):
    # pong(request)
    try:
        return StreamingHttpResponse(gen(cam), content_type="multipart/x-mixed-replace;boundary=frame")
    except:  # This is bad! replace it with proper handling
        print("에러입니다...")
        pass

def check_sim(request):
    jsonObject = json.loads(request.body)
    frame_time=jsonObject.get('ctime')

    results = cam.PoseProcess()
    key_dict=getKeypoint.get_keypoints(results.pose_landmarks.landmark,mpPose)
    key_dict['Middle']=[(key_dict['LShoulder'][0]+key_dict['RShoulder'][0])/2,(key_dict['LShoulder'][1]+key_dict['RShoulder'][1])/2,(key_dict['LShoulder'][2]+key_dict['RShoulder'][2])/2]
    MY_MOVE=sim_metrics.get_cam_movevector(key_dict)
    score=sim_metrics.check_sim(MY_MOVE,MOVE_VECTOR[frame_time])

    return render(request, "gamepage/home.html", {'score':score[0]})


# def origvideo(request):
#     try:
#         cap = choreoVideo()
#         return StreamingHttpResponse(gen(cap), content_type="multipart/x-mixed-replace;boundary=frame")
#     except:  # This is bad! replace it with proper handling
#         print("에러입니다...")
#         pass

# def origvideo(request):
#     extra_path = "./sample/video/yt_newjeans_ditto1.mp4"
#     response = HttpResponse(mimetype='video/mp4')
#     response['Accept-Ranges'] = 'bytes'
#     response['X-Accel-Redirect'] = 'yt_newjeans'
     