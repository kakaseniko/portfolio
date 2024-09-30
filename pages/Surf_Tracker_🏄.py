import streamlit as st

st.set_page_config(page_title="Surf Tracker", page_icon="🌊", layout="centered")
st.header("Log wave conditions during your surf session 🏄")

video_url = "https://youtu.be/dFDPbkbcdhA"

st.video(video_url, autoplay=True, loop=True)
st.write(f"""
         <p>
         The video above is a demo from a project I began with during my studies. It started out as a machine learning assignment in my specialization semester where I learnt the basics of working with data and AI.
         In that period, everyone could come up with a challenge for themselves and since I enjoy combining my hobbies with my projects, I decided to tackle a problem in the surfing world.
        </br></br>
         The idea was to create a surf forecasting app that is more reliable and easier to interpret than the current ones. As a beginner surfer at the time,
         I found it overwhelming to look at surf forecasts and trying to make sense of them so I had two things in mind: 1. I have to do my homework and learn about waves, 
         2. I want to find a way to make the forecasts more user-friendly.</br></br>
         During my specialization semester I tried to address the problem with machine learning, using wave data and some physics formulas to categorize them.
         At the end, I did get some interesting results out of it but I had to realize that I needed a different approach to reach my goal. Nevertheless, I really enjoyed the process
         and I became confident about reading surf forecasts and understanding waves.</br>
         </p>
    """, 
    unsafe_allow_html=True)
st.image("./images/1.png", caption="Categorizing breaking waves based on wave height, wave period and coastal steepness.", use_column_width=True)

st.write(""" 
          <p>
        A half year later, I was busy with my 'Advanced software engineering' semester where once again I could choose a project for myself. The project had to be
         an enterprise level software that uses micro services, so I have seen an opportunity to come back to my surf forecasting challenge and try to solve the problem from a different angle.
        </br></br>
        This time I wanted to base the surf conditions categorization on user feedback instead of physics formulas. And for that I needed an app. An app which surfers can use to log their surf sessions and rate the conditions. 
        An app that can collect data and train a machine learning model. An app that can help me pass the semester.
        </br></br>
        Without getting into too much technical details, I can say that a prototype was born and I passed the semester.🎉 I built a web-application (the one on the video) with an Ionic and Angular front-end,
         and a Django microservices back-end. I learnt how to use a message broker, orchestrate services with Docker, deploy with Kubernetes, and automate testing and deployment on GitHub.
          However, I did not get to the machine learning part this time, but hoping to finish it one day. </br></br>
         For anybody who wants to know more technical details, the code is available on <a href="https://github.com/kakaseniko/SurfTracker">GitHub</a>.
         </p> 
""", unsafe_allow_html=True)

