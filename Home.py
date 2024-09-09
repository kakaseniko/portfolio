import streamlit as st
import base64

# MAIN
def main():
    st.set_page_config(
        page_title='Portfolio - Eniko Kakas' ,
        page_icon='',   
        layout="wide",
        initial_sidebar_state="expanded")
    
    with open("./styles/main.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    
    st.write(f"""
             <h1 style="text-align:center; margin-bottom:1rem; margin-left:1rem;">Welcome! I'm Eniko Kakas.</h1>
             """, unsafe_allow_html=True)


    # Profile image
    with open("./images/pic.jpg", "rb") as img_file:
        img = "data:image/jpg;base64," + base64.b64encode(img_file.read()).decode()
    
    social_icons = {
        # Platform: [URL, Icon]
        "LinkedIn": ["https://www.linkedin.com/in/eniko-kakas/", "https://cdn-icons-png.flaticon.com/512/174/174857.png"],
        "GitHub": ["https://github.com/kakaseniko", "https://icon-library.com/images/github-icon-white/github-icon-white-6.jpg"],
        "Email" : ["mailto:kakas.eniko@gmail.com", "https://cdn-icons-png.flaticon.com/512/281/281769.png"],
    }

    social_icons_html = [f"<a href='{social_icons[platform][0]}' target='_blank' style='margin-right: 10px;'><img class='social-icon' src='{social_icons[platform][1]}'' alt='{platform}''></a>" for platform in social_icons]

    st.write(f"""
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
        """, 
        unsafe_allow_html=True)

    st.write(f"""
             <div class="section-title">
                <h1 style="padding:0;">About me</h1>
             </div>
             """,
             unsafe_allow_html=True)

    st.write("I am a Software engineer...")
    with open("./images/Resume.pdf", "rb") as pdf_file:
        pdf_bytes = pdf_file.read()

    st.download_button(
        label="📄 Download my CV",
        data=pdf_bytes,
        file_name="Resume.pdf",
        mime="application/pdf",
    )
    st.subheader("Jack of all trades")
    st.write("software, recreation manager, setter, dancer, a whole lot of hobbies")

    st.write("Ask the chatbot if you want to know more...")
    st.write("Check out my projects...")

    st.write(f"""
             <div class="section-title" id="contact" style="position:absolute; right: 0;">
                <h1 style="padding: 0; text-align: end;">Contact me</h1>
             </div>
             """, unsafe_allow_html=True)

if __name__ == '__main__':
    main()