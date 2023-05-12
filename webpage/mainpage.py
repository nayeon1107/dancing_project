import streamlit as st
import cv2



col1, col2= st.columns(2)

with col1:
   st.header("연습할 안무 영상")

with col2:
    st.title("내 영상")
    run = st.checkbox('Open camera')
    FRAME_WINDOW = st.image([])
    camera = cv2.VideoCapture(0)

    while run:
        _, frame = camera.read()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        FRAME_WINDOW.image(frame)
    else:
        st.write('Stopped')
