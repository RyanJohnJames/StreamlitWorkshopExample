import streamlit as st
import datetime
from streamlit_lottie import st_lottie
st.title("Welcome to my wonderful about me! :fire:")

st.image("images/tofu.png", "Hello there! I'm tofu.boi", 300)

st.write("Hi there! I'm RyanJohnJames or tofu.boi, I love playing gacha games and watching anime!")

st_lottie("https://assets5.lottiefiles.com/packages/lf20_fcfjwiyb.json")


st.header("using a simpple text input")
input = st.text_input("What is your name?")

if input:
    st.write(f"Hello {input}")

