import streamlit as st

video_file = open("./images/SurfTrackerDemo.webm", "rb")
video_bytes = video_file.read()

st.video(video_bytes, autoplay=True, loop=True)