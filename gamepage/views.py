from django.shortcuts import render
from django.views.decorators import gzip
from django.http import StreamingHttpResponse, HttpResponse

import cv2
import threading
import mediapipe as mp
import os

# -------------- PoseDetection -------------
mpPose = mp.solutions.pose
pose = mpPose.Pose()
mpDraw = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles

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
            imgRGB = cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGB)
            results = pose.process(imgRGB)
            landmarks = str(results.pose_landmarks.landmark[0].x)
            # print(landmarks)
            # getKeypoint(self.frame)

class choreoVideo(object):
    def __init__(self):
        self.cam = cv2.VideoCapture('./sample/video/yt_newjeans_ditto1.mp4')
        (self.success, self.frame) = self.cam.read()
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
            # print(self.cam.get(cv2.CAP_PROP_POS_FRAMES))


# -------------- Basic Cam -------------
def home(request):
    context = {}
    return render(request, "gamePage/home.html", context)

def gen(camera):
    while True:
        frame = camera.get_frame()
        yield(b'--frame\r\n'
              b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
        
@gzip.gzip_page
def detectme(request):
    try:
        cam = mediapipeCam()
        return StreamingHttpResponse(gen(cam), content_type="multipart/x-mixed-replace;boundary=frame")
    except:  # This is bad! replace it with proper handling
        print("에러입니다...")
        pass

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
     