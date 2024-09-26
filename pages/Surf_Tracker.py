import streamlit as st

st.header("Log wave conditions during your surf session 🏄")
st.write(f"""
    <div>
         <p>
         The video below is a demo from a hobby project I started during my studies.
         The idea of the project was to create a surf forcasting app that is more realiable and easier to interpret than the current ones.
         In theory, this could be achieved by allowing users to log their surf sessions and rate the conditions, 
         and later use this data to train a machine learning model to predict the surf conditions.
         The prototype is a simple web app where the front-end was built with Ionic and Angular, and the back-end with Django.
         </p>
         <p>
         At the moment the app only lives in a GitHub respository, but I hope to finish and launch it one day.
         </p> 
    </div>
    """, 
    unsafe_allow_html=True)
video_file = open("./images/SurfTrackerDemo.webm", "rb")
video_bytes = video_file.read()

st.video(video_bytes, autoplay=True, loop=True)