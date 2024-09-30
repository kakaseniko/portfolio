import streamlit as st

st.set_page_config(page_title="Staff Organizer", page_icon="🗓️", layout="centered")
st.header("Create schedules for your staff members 🗓️")
st.write("""My very first full stack project, also the most overwhelming one. I still cannot believe how much you can learn within a couple of months if you are 
         being pushed a little. Just to have an idea: in the beginning of the assignment I only knew a little bit of JavaScript and some basic OOD principles that I 
         mostly used in C#, by the end I had a working (not pretty but working) front-end with React, a back-end API with Java and SpringBoot, a chat functionality in 
         place that uses web sockets, 80% unit test coverage, end-to-end tests with Cypress, quality control with SonarCube, all tests part of a CI/CD pipeline where Docker is used for orchestration,
          and a whole bunch of functionalities including a log in system. On top of that I learnt to work Agile and deliver in 3 week sprints, write a project plan, 
         write user stories, and maintain a project backlog.</br></br>
         The video below is a small impression of the app 
         I built during the process. It is a staff management system that allows users to create and manage schedules and lets staff members to communicate via chat. By now I am 
         not particularly satisfied with the application but I am definitely proud that I managed to learn all these fundamental skills within such a short period.""", unsafe_allow_html=True)

url="https://youtu.be/2tdLxDeZ_DI"

st.video(url, autoplay=True, loop=True)