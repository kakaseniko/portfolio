import streamlit as st
st.set_page_config(page_title="Laravel es magico", page_icon="🦄", layout="centered")
st.header("Create anything with Laravel 🦄")

st.write("""...because Laravel is magical! 🪄 This sentence summarizes my internship on Gran Canaria 🏝️ where I spent a half year as a full-stack developer.</br></br>
         During the ICT study program at Fontys students are required to do two internships, one at the beginning of the third year and one during graduation. Fontys also
          encourages students to go abroad for a semester if they can. I thought I would seize the opportunity and go for an internship abroad. The plan: find a company at a 
         destination where I can surf 🏄‍♀️. (Cause why would it be enough to learn programming? I needed to pick up a new hobby too...). </br></br>
         This idea kicked off a new adventure for me. I was super lucky and found a company called Calima Solutions on Gran Canaria that offered Digital Opportunities internships for
          Erasmus students. I applied and two months later I was working in an office with an ocean view. </br></br> 
         """, unsafe_allow_html=True)
st.image("./images/6.jpg", caption="Office at Calima Solutions", width=400)

st.write("""My job was to implement functionalities in a full-stack application made for an upcoming health resort. This project was the one that thought me about Angular, 
         Ionic, Laravel, Filament, and Tailwind. Next to that, it also thought me soft skills as I was part of the development team, participated in daily stand ups, 
         code reviews, and of course some unforgettable team outings. The picture below gives a small impression about the application I was working on, but it does not 
         cover the whole system.""", unsafe_allow_html=True)
st.image("./images/3.png", caption="Admin panel made with Filament", use_column_width=True)
st.write("""
         The project was big and many developers worked on it for a while by the time I got there, consequently I had to work with legacy code and spend some time on 
         bug fixes and code refactoring. This gave me an opportunity to learn to work with different code quality tools (like Enlightn and PHPStan) and of course to 
         complain a lot to my supervisor 😜. 
         </br></br>
         At the end, all the efforts paid off and I left the company with a system that was easier to maintain, performed better, had less security vulnerabilities, and 
         had a documentation available for future developers.
         </br></br>
         The semester ended with a successful project and tearful goodbyes.
         Looking back I realized that that half year did not only extended my IT knowledge but also thought me how to adapt to a new living situation, it allowed me to explore a different culture, and gave me 
         the opportunity to learn a little bit of Spanish, lots of surfing, and make new friends for life. It was an entire adventure which made me grow as a person and 
         for which I will be grateful for my whole life.""", unsafe_allow_html=True)
st.image("./images/7.jpg", caption="Christmas presentation at Calima Solutions", use_column_width=True)
st.image("./images/8.jpg", caption="Team outing on a catamaran", use_column_width=True)
st.image("./images/9.JPG", caption="Surfing in Gran Canaria", use_column_width=True)


