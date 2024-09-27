import streamlit as st
import base64

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
                        <p style="font-size: 18px;">By my latest professional title I am a Software Engineer but that is not enough to describe me
                        ... because I am a true generalist, versatile and adventurous with a passion for learning and exploring new paths.</br></br>
                        I started out as a Recreation Manager, then became a hairdresser, finally ending up in IT. Within IT I am embracing variety too, from data preparation, through model training, to application development and deployment.</br></br>
                        Outside of work I can be found lost in one of my passions: climbing, surfing, dancing, or just being outdoors in the woods or on a campsite.</br></br>
                        I strive for a balanced life where my hobbies, work, and personal growth are all given equal importance, aiming for a work-life balance that values my diverse interests and recognizes the importance of personal development.
                            My ultimate goal is to find a position that encourages my curiosity and thirst for knowledge, ensuring I continue to grow and contribute in my unique way.</p>
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