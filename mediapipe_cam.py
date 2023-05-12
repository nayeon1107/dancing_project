import cv2
import mediapipe as mp
import numpy as np
import os
import json
import time
from sklearn.metrics.pairwise import cosine_similarity

mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_pose = mp.solutions.pose

# # # 이미지 파일의 경우 이것을 사용하세요.:
# IMAGE_FILES = []
# BG_COLOR = (192, 192, 192)  # 회색
# with mp_pose.Pose(
#         static_image_mode=False,
#         model_complexity=2,
#         enable_segmentation=True,
#         min_detection_confidence=0.5) as pose:
#     for idx, file in enumerate(IMAGE_FILES):
#         image = cv2.imread(file)
#         image_height, image_width, _ = image.shape
#         # 처리 전 BGR 이미지를 RGB로 변환합니다.
#         results = pose.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

#         if not results.pose_landmarks:
#             continue
#         print(
#             f'Nose coordinates: ('
#             f'{results.pose_landmarks.landmark[mp_pose.PoseLandmark.NOSE].x * image_width}, '
#             f'{results.pose_landmarks.landmark[mp_pose.PoseLandmark.NOSE].y * image_height})'
#         )

#         annotated_image = image.copy()
#         # 이미지를 분할합니다.
#         # 경계 주변의 분할을 개선하려면 "image"가 있는
#         # "results.segmentation_mask"에 공동 양방향 필터를 적용하는 것이 좋습니다.
#         condition = np.stack((results.segmentation_mask,) * 3, axis=-1) > 0.1
#         bg_image = np.zeros(image.shape, dtype=np.uint8)
#         bg_image[:] = BG_COLOR
#         annotated_image = np.where(condition, annotated_image, bg_image)
#         # 이미지 위에 포즈 랜드마크를 그립니다.
#         mp_drawing.draw_landmarks(
#             annotated_image,
#             results.pose_landmarks,
#             mp_pose.POSE_CONNECTIONS,
#             landmark_drawing_spec=mp_drawing_styles.get_default_pose_landmarks_style())
#         cv2.imwrite('./iam' +
#                     str(idx) + '.mp4', annotated_image)
#         # 포즈 월드 랜드마크를 그립니다.
#         mp_drawing.plot_landmarks(
#             results.pose_world_landmarks, mp_pose.POSE_CONNECTIONS)
        
#         print(results.pose_landmarks.landmark[11].x, results.pose_landmarks.landmark[12].x)

# # 웹캠, 영상 파일의 경우 이것을 사용하세요.:

path = './video_ditto'
file_list = os.listdir(path)
file_idx = 0


cap = cv2.VideoCapture(0)

order = 0
with mp_pose.Pose(
        min_detection_confidence=0.5,
        min_tracking_confidence=0.5) as pose:
    start = time.time()
    while cap.isOpened():
        success, image = cap.read()
        if not success:
            print("카메라를 찾을 수 없습니다.")
            # 동영상을 불러올 경우는 'continue' 대신 'break'를 사용합니다.
            continue

        # 필요에 따라 성능 향상을 위해 이미지 작성을 불가능함으로 기본 설정합니다.
        image.flags.writeable = False
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        results = pose.process(image)

        # 포즈 주석을 이미지 위에 그립니다.
        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        mp_drawing.draw_landmarks(
            image,
            results.pose_landmarks,
            mp_pose.POSE_CONNECTIONS,
            landmark_drawing_spec=mp_drawing_styles.get_default_pose_landmarks_style())
        
        # 보기 편하게 이미지를 좌우 반전합니다.
        cv2.imshow('MediaPipe Pose', cv2.flip(image, 1))

        # json 파일 열기
        with open(path+"/"+file_list[file_idx], "r", encoding="utf8") as f:
            file_idx += 1
            contents = f.read()
            json_data = json.loads(contents)['pose_keypoints'][11:29]
            json_data = np.reshape(np.array(json_data),(-1,4))
            points_matrix = np.delete(np.delete(json_data,3,axis=1),2,axis=1)
            order += 1
            if order % 20 == 0 :
                vectors = np.array([[results.pose_landmarks.landmark[i].x-results.pose_landmarks.landmark[0].x, results.pose_landmarks.landmark[i].y-results.pose_landmarks.landmark[0].y] for i in range(len(results.pose_landmarks.landmark[11:29]))])
                cosine_sim = cosine_similarity(vectors, points_matrix)
                node_sim = np.diagonal(cosine_sim)
                if np.mean(node_sim) > 0.9 :
                    print("SUCCESS", np.mean(node_sim))
                else :
                    print("TRY AGAIN", np.mean(node_sim))
                #     cv2.putText(image, 'success', (100, 100), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 3, lineType=cv2.LINE_AA)
                # else :
                #     cv2.putText(image, 'Try Again', (100, 100), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 3, lineType=cv2.LINE_AA)
                # print("cam : ", "{:.5f}".format(results.pose_landmarks.landmark[11].x), "{:.5f}".format(results.pose_landmarks.landmark[12].x))
                # if len(points_matrix) != 0 :
                #     print("video : ", points_matrix[0][0], points_matrix[1][0])
 
        # # 임시로 23 - 24 번째 좌표 (양어깨) 출력

        # print("{:.3f}".format(time.time() - start), "초")
        # print("{:.5f}".format(results.pose_landmarks.landmark[11].x), "{:.5f}".format(results.pose_landmarks.landmark[12].x))
        # print(points_matrix)
        # print("{:.5f}".format(points_matrix[2][1]))
    


        
        

        # ESC 누르면 종료
        if cv2.waitKey(5) & 0xFF == 27:
            break
        
cap.release()
cv2.destroyAllWindows() #모든 윈도우 창 닫음