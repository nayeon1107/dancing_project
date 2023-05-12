
def get_keypoints(landmarks, mp_pose,frame_time,frame_num):
        #kp center
        nose = [
            landmarks[mp_pose.PoseLandmark.NOSE.value].x,
            landmarks[mp_pose.PoseLandmark.NOSE.value].y,
            landmarks[mp_pose.PoseLandmark.NOSE.value].z,
            landmarks[mp_pose.PoseLandmark.NOSE.value].visibility,
        ]

        #left upper
        left_shoulder = [
            landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].x,
            landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].y,
            landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].z,
            landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].visibility,
        ]
        left_elbow = [
            landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].x,
            landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].y,
            landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].z,
            landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].visibility,
        ]
        left_wrist = [
            landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].x,
            landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].y,
            landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].z,
            landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].visibility,
        ]
        #right upper
        right_shoulder = [
            landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].x,
            landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].y,
            landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].z,
            landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].visibility,
        ]
        right_elbow = [
            landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value].x,
            landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value].y,
            landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value].z,
            landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value].visibility,
        ]
        right_wrist = [
            landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value].x,
            landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value].y,
            landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value].z,
            landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value].visibility,
        ]

        #left lower
        left_hip = [
            landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].x,
            landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].y,
            landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].z,
            landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].visibility,
        ]
        left_knee = [
            landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value].x,
            landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value].y,
            landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value].z,
            landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value].visibility,
        ]
        left_ankle = [
            landmarks[mp_pose.PoseLandmark.LEFT_ANKLE.value].x,
            landmarks[mp_pose.PoseLandmark.LEFT_ANKLE.value].y,
            landmarks[mp_pose.PoseLandmark.LEFT_ANKLE.value].z,
            landmarks[mp_pose.PoseLandmark.LEFT_ANKLE.value].visibility,
        ]

        #right lower
        right_hip = [
            landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value].x,
            landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value].y,
            landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value].z,
            landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value].visibility,
        ]
        right_knee = [
            landmarks[mp_pose.PoseLandmark.RIGHT_KNEE.value].x,
            landmarks[mp_pose.PoseLandmark.RIGHT_KNEE.value].y,
            landmarks[mp_pose.PoseLandmark.RIGHT_KNEE.value].z,
            landmarks[mp_pose.PoseLandmark.RIGHT_KNEE.value].visibility,
        ]
        right_ankle = [
            landmarks[mp_pose.PoseLandmark.RIGHT_ANKLE.value].x,
            landmarks[mp_pose.PoseLandmark.RIGHT_ANKLE.value].y,
            landmarks[mp_pose.PoseLandmark.RIGHT_ANKLE.value].z,
            landmarks[mp_pose.PoseLandmark.RIGHT_ANKLE.value].visibility,
        ]

        return {
            'nose' : nose,
            'LShoulder' : left_shoulder,
            'LElbow' : left_elbow,
            'LWrist' : left_wrist,
            'RShoulder' : right_shoulder,
            'RElbow' : right_elbow,
            'RWrist' : right_wrist,
            'LHip':left_hip,
            'LKnee':left_knee,
            'LAnkle':left_ankle,
            'RHip':right_hip,
            'RKnee':right_knee,
            'RAnkle':right_ankle,
            'frame_time':frame_time,
            'frame_num':frame_num
        }
        