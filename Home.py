import streamlit as st
import base64
import plotly.graph_objects as go
import streamlit.components.v1 as components

# MAIN
def main():
    st.set_page_config(
        page_title='Portfolio - Eniko Kakas' ,
        page_icon='👽',   
        layout="wide",
        initial_sidebar_state="expanded",
        )
    
    with open("./styles/main.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


    # Profile image
    with open("./images/pic.jpg", "rb") as img_file:
        img = "data:image/jpg;base64," + base64.b64encode(img_file.read()).decode()
    
    #social icons
    social_icons = {
        # Platform: [URL, Icon]
        "LinkedIn": ["https://www.linkedin.com/in/eniko-kakas/", "https://cdn-icons-png.flaticon.com/512/174/174857.png"],
        "GitHub": ["https://github.com/kakaseniko", "https://icon-library.com/images/github-icon-white/github-icon-white-6.jpg"],
        "Email" : ["mailto:kakas.eniko@gmail.com", "https://cdn-icons-png.flaticon.com/512/281/281769.png"],
    }
    social_icons_html = [f"<a href='{social_icons[platform][0]}' target='_blank' style='margin-right: 10px;'><img class='social-icon' src='{social_icons[platform][1]}'' alt='{platform}''></a>" for platform in social_icons]
    
    #CV
    with open("images/Resume.pdf", "rb") as pdf_file:
        pdf_bytes = pdf_file.read()
    
    b64_pdf = base64.b64encode(pdf_bytes).decode('utf-8')
    download_link = f'<a href="data:application/pdf;base64,{b64_pdf}" download="Resume.pdf"><button>📄 Download my CV</button></a>'

    st.write(f"""
            <h1 style=" margin-bottom:1rem;">Welcome! I'm Eniko Kakas.</h1>
            <div class="container">
                <div class="profile">
                    <div class="profile-frame">
                        <div class="circle">
                            <div class="img-frame">
                                <img class="bd" src="{img}" alt="Eniko Kakas">
                            </div>
                        </div>
                        <h2 style="margin-left: 1rem;">Software & AI Engineer 👩‍💻</h2>
                        <div style="display: flex; justify-content: center; margin-bottom: 20px;">
                        {''.join(social_icons_html)}
                        </div>
                    </div>
                </div>
                <div class="about-me" >
                    <div>
                        <h1>About Me</h1>
                        </br>
                    </div>
                    <div style="margin-left: 1rem; margin-top:1rem;">
                        <p style="font-size: 18px;">I am  junior Software and AI engineer with a BSc degree from Fontys ICT. I am also a Recreation Manager, a ski instructor, 
                        a hair dresser, and a (boulder) route setter...
                        a true generalist, versatile and adventurous with a passion for learning and exploring new paths.</br></br>
                        I believe my talent lies in the intersection of creativity, analytical thinking, and problem solving/ tackling challenging tasks. However, it took me some time 
                        to realize this and find a field where I can utilize all of the above.</br></br>
                        During obtaining my first Bsc degree in Recreation Management, my creative and problem solving skills were challenged but did not have a lot of room for analytical thinking.
                        I really enjoyed my courses, especially their wide range of topics from sports and movement, through health, to outdoor activities. However, eventually I had to realize that 
                        the continuous, intensive human interaction is overwhelming for me and had to find a different path.</br></br>  
                        I decided to focus on something creative and took a hairdressing course 💇‍♀️. I loved working with my hands and creating something beautiful. I also liked that 
                        my work brought joy into people's lives. However, soon the tasks of a hairdresser were not challenging enough intellectually, and I was looking for yet another 
                        path.</br></br>
                        I started taking some online courses. First about sustainability, then about programming. That was when I realized that coding is much more interesting than I thought 
                        and that I might even have a feeling for it. Soon I enrolled to Fontys ICT and started my journey in the world of IT.</br></br>
                        I was surprised by how much I enjoyed the program. The high focus on practice based learning really suited me, and I loved being able to turn my ideas into something 
                        tangible. </br></br>
                        Meanwhile, I had a side job as a route setter in a boulder gym. This was one of my first jobs where I found fulfillment. The way you have to come up with ideas/ 
                        challenges for others, while puzzling climbing holds together like they were Lego, in combination with thinking about movements and body positions is so exciting and 
                        inspiring for me. I always feel like a kid in a candy store when I am setting routes. I am still passionate about it today and want to pursue this side job until 
                        my body lets me.</br></br>
                        How I advanced further in my studies I found the same excitement and passion in programming as in route setting. They both seem to lend in this sweet spot between 
                        creativity, analyses, and problem solving where I feel inspired and driven. I also just adore the IT community with all its support, corkiness, and sense of humor 🪿. 
                        I feel like I have a place among these people. I love coming up with ideas for new projects (the more challenging, the better) and find a way to realize them. 
                        I also love how you can solve a problem in many different ways leaving room for creativity and playfulness. But my absolute favorite is how each project is connected 
                        to a different field and teaches you something that often has nothing to do with IT. From the various projects throughout my studies I learnt about HR management,
                        education, the funeral industry, restaurant reservations, <a href="/Laravel_es_magico_🦄" target="_self">holistic body treatments</a>, <a href="/Japanese_Knotweed_Detection_🌱" target="_self">invasive plant species</a> and so on. 
                        And these were only the projects that were 
                        given to me. Next to these, I had my own assignments where I always choose to tackle problems I encountered through my hobbies (like a <a href="/Surf_Tracker_🏄" target="_self">surf forecasting app</a>,
                        or a <a href="Climbing_Shoes_Fitter_🧗" target="_self">climbing shoes selector tool</a>). 
                        How awesome is that?! 
                        Learning while solving problems in fields that people connect to. It feels like I can have actual impact and reach people and society through IT.</br></br> 
                        So this is me in my versatile and adventures world, striving for a balanced life where my hobbies, work, and personal growth are all given equal importance, and a job that values my diverse interests and recognizes the importance of personal development.
                        My ultimate goal is to be in a position that encourages my curiosity and thirst for knowledge, ensuring I continue to grow and contribute in my unique way.</p>
                    </div>
                </div>
                <div class="extra-info" >
                    <div class="profile-frame" style="margin-top:0px;">
                        <p style="font-size: 18px;">If you want to know more ask the <a href="/Chatbot" target="_self" class="chatbot-link">Chatbot 🤖</a>  or: </p>
                        {download_link}
                        </br>
                        <p style="font-size: 18px;">👈 And don't forget to check out my projects on the left.</p>
                    </div>
                </div>
            </div>
        """, 
        unsafe_allow_html=True)

if __name__ == '__main__':
    main()