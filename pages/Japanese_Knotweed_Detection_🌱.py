import streamlit as st

st.set_page_config(page_title="Japanese Knotweed Detection", page_icon="🌱", layout="centered")
st.header("Detect Japanese Knotweed along the roads 🌱")



st.write("""This project was the one I graduated with from Fontys with cum laude 🥲. It was provided by and executed for <a href="https://www.ecogoggle.nl/" target="_blank">EcoGoggle</a>, 
         a company that works with technology to monitor nature. The goal was to prove that street view images can be used to identify plants (in this case the Japanese knotweed)
         automatically with computer vision.""", unsafe_allow_html=True)
st.image("./images/4.png", caption="Japanese Knotweed along the road.", use_column_width=True)
st.write("""I especially enjoyed working on this project because the domain/ cause is close to my heart, I really like and value nature and I find it important to 
         take action to protect it and to improve its current state. It was fulfilling to apply my knowledge for a cause that I believe in. I feel like this was the 
         perfect assignment that marks the end of my studies. </br></br>
         The process included data labeling (about 10.000 images was enough to condition myself to spot Japanese knotweed everywhere I go 🫠), testing different model 
         tasks (classification, object detection, and segmentation), and building a prototype application.""", unsafe_allow_html=True)
st.image("./images/5.png", caption="Prototype to display Japanese knotweed locations.", use_column_width=True)
st.write("""The image above shows the final outcome, a prototype that can be used to analyze a whole folder, find the images with Japanese knotweed, and display their 
         location on a map. The marked dots on the map are clickable and they show the image on which the knotweed was detected. </br></br>
         Since the project was a success, the company is planning to continue it and extend the model to be able to recognize multiple plant species and 
         use the solution to measure biodiversity along the roads.""", unsafe_allow_html=True)