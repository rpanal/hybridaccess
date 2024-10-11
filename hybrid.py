import streamlit as st
import pandas as pd
import pyodbc as msacc
#from st_aggrid import AgGrid, JsCode
from PIL import Image

#import cv2
client = OpenAI(
  organization='sk-_CR01dhBq9pZV4_j-4X8C-Y65P1747FF3yQwlN6umST3BlbkFJDvt5HxdRNhO6picD8zhcfRM92FUMsKoPhxqV_Ee_IA',
  project='$CCLPIHYBRID',
)

cnn_string = (r"Driver=(Microsoft Access driver (*.mdb, *.accdb));")
st.title("Restie")




col1, col2, col3 , col4 = st.columns([1,2,3,4])
col1.markdown ("Welcome to my Application")
col1.markdown ("Just for Samples")


col3.markdown("Just for Samples 3")
upload_soundfile = col4.file_uploader("Upload Audio File")

uploaded_photo = col3.file_uploader("upload a photo")                                                                                      
camera_photo = col2.camera_input("upload a photo from Camera",)
st.write("""# My first appn Hello *world!*""")

myname = col3.text_input("Enter your name")
col3.markdown (myname)

col4.markdown("")

if uploaded_photo is not None and camera_photo is not None:
    st.image(uploaded_photo,"My Image",300) 
    st.sidebar.image (camera_photo,caption = "Me",width = 100,clamp=True,output_format ="auto")
    st.sidebar.image (uploaded_photo)

st.form("Restie",border=True)

img = Image.open("./agentpics./user.png")
newimage = st.image(img,width=30)
st.sidebar.button("Reset", type="primary")


if st.sidebar.button("Say hello"):
    
    st.write("Why hello there")
else:
    st.write("Hello")


