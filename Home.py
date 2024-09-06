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
    
    st.title("Welcome! I'm Eniko Kakas")


    #st.image("./images/pic.jpg", width=400)
        # Profile image
    with open("./images/pic.jpg", "rb") as img_file:
        img = "data:image/jpg;base64," + base64.b64encode(img_file.read()).decode()

    st.write(f"""
        <div class="container">
            <div class="box">
                <div class="shape">
                    <div class="bd">
                        <img src="{img}" alt="Enric Domingo">
                    </div>
                </div>
            </div>
        </div>
        """, 
        unsafe_allow_html=True)
    st.write(f"""<div class="subtitle" style="text-align: center;">Software & AI Engineer</div>""", unsafe_allow_html=True)

    st.subheader("Software & AI Engineer")

    st.title("About me")

    st.write("I am a Software engineer...")

    with open("./images/Resume.pdf", "rb") as pdf_file:
        pdf_bytes = pdf_file.read()

    st.download_button(
        label="📄 Download my CV",
        data=pdf_bytes,
        file_name="Resume.pdf",
        mime="application/pdf",
    )
    st.write("Ask the chatbot if you want to know more...")
    st.write("Check out my projects...")

    #with open("./images/Resume.pdf","rb") as f:
    #    base64_pdf = base64.b64encode(f.read()).decode('utf-8')
    #    pdf_display = F'<iframe src="data:application/pdf;base64,{base64_pdf}" width="1000mm" height="1000mm" type="application/pdf"></iframe>'
    #    st.markdown(pdf_display, unsafe_allow_html=True)
    st.title("Contact me")


if __name__ == '__main__':
    main()