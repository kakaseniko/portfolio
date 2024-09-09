import streamlit as st

st.header("Log wave conditions during your surf session")
st.write(f"""
    <div>
         <p>loerm ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.</p>
    </div>
    """, 
    unsafe_allow_html=True)
video_file = open("./images/SurfTrackerDemo.webm", "rb")
video_bytes = video_file.read()

st.video(video_bytes, autoplay=True, loop=True)