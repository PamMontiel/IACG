import streamlit as st
from PIL import Image
import random 
import glob 

# Load the photos 
def load_images():
  image_list = []
  for filename in glob.glob('main/IACG/male/*.png'):
    image_list.append(filename)
  return image_list

def load_images_girls():
  image_list_girls = []
  for filename in glob.glob('main/IACG/female/*.png'):
    image_list_girls.append(filename)
  return image_list_girls

# Load list from state 
if 'image_list' not in st.session_state: 
  image_list = load_images()
  st.session_state['image_list'] = image_list
else: 
  image_list = st.session_state['image_list']

if 'image_list_girls' not in st.session_state: 
  image_list_girls = load_images_girls()
  st.session_state['image_list_girls'] = image_list_girls
else: 
  image_list_girls = st.session_state['image_list_girls']

# Make the page itself 

st.title("Infinite Anime Character Generator")

st.markdown(""" <style> .font {
    font-size:35px ; font-family: 'Calibri';  color: #BE7488;} 
    </style> """, unsafe_allow_html=True)
st.markdown('<p class="font">Infinite Characters!</p>', unsafe_allow_html=True)

st.caption("The IACG is a tool that generate characters with IA. You can generate male and female anime-like characters. Every character is unique! And they can be used for games and more!")

def get_face(image_list):
  if len(image_list) < 1: 
    image_list = load_images() 
    #st.session_state['image_list'] = image_list

  new_face = random.choice(image_list)
  image = Image.open(new_face)

  image_list.remove(new_face) 
  st.image(image, caption="")

def get_face_girl(image_list_girls):
  if len(image_list_girls) < 1: 
    image_list_girls = load_images_girls() 
    #st.session_state['image_list_girls'] = image_list_girls

  new_face_girl = random.choice(image_list_girls)
  image = Image.open(new_face_girl)

  image_list_girls.remove(new_face_girl) 
  st.image(image, caption="")

col1, col2 = st.columns(2)
with col1:
    st.header("BOYS ")
    st.button("Get character!", key=None, help=None, on_click=get_face(image_list), args=None, kwargs=None)

with col2:
    st.header("GIRLS")
    st.button("Get character! ", key=None, help=None, on_click=get_face_girl(image_list_girls), args=None, kwargs=None)

