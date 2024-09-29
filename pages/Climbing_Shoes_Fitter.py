import streamlit as st
import os
#os.environ['PYOPENGL_PLATFORM'] = 'osmesa'
import cv2
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from skimage.io import imread, imsave
import tensorflow as tf
import pandas as pd
import helpers

@st.cache_data
def load_shoes():
    shoesdf = pd.read_csv('./data/climbingshoesdata.csv')
    return shoesdf

st.header("Take a picture of your foot to find out which climbing shoes fit you best 🧗")
st.write(""" Probably this project is the one I am most excited about. It allows users to take a picture of their foot,
         then two different AI models work together to determine which climbing shoes fit them best. The choice is based on the shape and the width of the foot, 
         and the selection is made from a dataset containing 14 different climbing shoes. </br></br>
         It is a perfect example of how I combine my hobbies with school projects. This time I had to create a prototype for my 'Advanced AI' semester that showcases how 
         real world problems can be solved with AI. The problem I tried to tackle was the difficulty of finding the right climbing shoes. There are many different models available 
         from many different brands and the overwhelming number of choices can be difficult to navigate, especially for beginners. I found a guide online that included a diagram
         of climbing shoes and feet types, and I thought it would be interesting to try to "automate" this guide.</br></br>
""", unsafe_allow_html=True)

st.image("./images/2.jpg", caption="Climbing shoes by foot shapes. source: https://www.climbingshoereview.com/how-to-choose-climbing-shoes/", use_column_width=True)
st.write("""
            The process was both interesting and fun. As all machine learning projects, it started with gathering data. Since I needed a rather unusual dataset (pictures of feet),
         I found lots of entertainment in this beginning phase. I was lucky to come by a dataset on Kaggle that contained the necessary images for training one of the models,
         however I had to be creative to obtain data for the other model. I ended up using my network of climbers who were happy to help me out with this climbing related project,
         and allowed me to take a picture of their foot (no matter how bizarre this request was). I assured them that the data is anonymous and will never leave my computer,
         then we cracked some tasteless jokes about OnlyFeet accounts. </br></br>
         Once I had enough data, the next step was to figure out how the width and the shape can be determined from an image. The shape was quiet straight forward, I knew I needed a classification model,
         however I did not calculate with the odd task of labeling hundreds of feet images. But eventually I got there and my first model was trained. Then I moved on to
         determining the width. First, I tried without AI by using images where the feet are on an A4 paper and make calculations based on the paper size. This approach was fine
         but not very accurate, and it required the user to have an A4 paper with them which I did not find very practical. Then it struck me that I do not need the actual size
         in cm to determine the width, I just need the width and height ratio. And what can be a better way to get that than a bounding box?! So I went on to embedding an object detection model 
         into the application and voilà, the solution was there. </br></br>
         I really enjoyed this project from beginning to end. I learnt to think practically and creatively about AI based solutions, and just like almost every time I work with data,
         I got to discover and gain some knowledge about a new field, this time about feet and climbing shoes. </br></br>
         Below you can try out the prototype and experience the power of two AI models working together. It is important to know though that it is just a proof of concept, 
         the solution is not perfect and has its limitations. However, it is suitable for showcasing that the climbing shoes selection process can be automated.
         (Don't worry I do not store any of the images you take, they are only used for the prediction.)
         """,
         unsafe_allow_html=True)
#APP
img_file_buffer = st.camera_input("Take a picture")

if img_file_buffer is not None:
    #take image
    bytes_data = img_file_buffer.getvalue()
    cv2_img = cv2.imdecode(np.frombuffer(bytes_data, np.uint8), cv2.IMREAD_COLOR)
    cv2.imwrite('captured.jpeg', cv2_img)

    #find bounding box
    image_path = './captured.jpeg'
    results = helpers.get_bounding_boxes(image_path)

    if len(results) == 0:
        st.error("No foot detected")
        st.stop()

    fig, ax = plt.subplots(1)
    image = Image.open(image_path) 
    ax.imshow(image)
    box_coordinates = results.xyxy.cpu().numpy()
    min_area = float('inf')
    min_box = None
    for box in box_coordinates:
        x_min, y_min, x_max, y_max = box[:4]
        area = (x_max - x_min) * (y_max - y_min)

    # Check if the current bounding box has a smaller area than the minimum
    if area < min_area:
        min_area = area
        min_box = box

    # Plot the bounding boxes
    if min_box is not None:
        x_min, y_min, x_max, y_max = box[:4]
        rect = patches.Rectangle((x_min, y_min), x_max - x_min, y_max - y_min, linewidth=2, edgecolor='r', facecolor='none')
        ax.add_patch(rect)
    st.pyplot(fig)

    #get foot width
    boxw = box[2] - box[0]
    boxh = box[3] - box[1]
    if boxw > boxh:
        boxw = box[3] - box[1]
        boxh = box[2] - box[0] 
    footWidth = helpers.calculateWidthCategory(boxh, boxw)

    #process image
    img = imread(image_path)
    clusteredImage = helpers.kMeans_cluster(img)
    st.image(clusteredImage, caption='Clustered Image', use_column_width=True)

    edgedImg = helpers.edgeDetection(clusteredImage)
    #st.image(edgedImg, caption='Edged Image', use_column_width=True)
    imsave('edged.jpg', edgedImg)

    footshape = helpers.predict_foot_shape('./edged.jpg')

    #get shoes
    shoesdf = load_shoes()
    shoes = shoesdf.query(f'{footshape} == 1 & {footWidth} == 1')
    st.write(footshape, footWidth)
    #st.table(shoes)

    helpers.display_results(shoes)




