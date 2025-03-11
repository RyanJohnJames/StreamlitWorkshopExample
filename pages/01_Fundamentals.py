import streamlit as st
import pandas as pd
import numpy as np


st.set_page_config(page_title="Fundementals", page_icon="🧱", layout="centered")

st.title("All of Streamlit Fundementals")

st.header("The power of st.write()")

st.subheader("What can st.write() do")

with st.echo():
    st.write("Hello, *world!* :fire:")
    st.write(12345)
    st.write(pd.DataFrame({
        'First column' : [1, 2, 3, 4 ],
        'Second column': [10, 20, 30, 40]
    }))

st.subheader("4 levels of write:")

with st.echo():
    st.title("title!")
    st.header("Header")
    st.subheader("subheader :)")
    st.write("Normal text :>")

    
st.divider()

st.header("st.metric()")

with st.echo():
    st.metric("Conversion Rate", "3.2%", "+0.8%")

st.divider()

st.header("st.image, audio and video")

with st.echo():
    st.image("images/feixiao.jpeg", 
             "Feixiao from the hit game Honkai Star Rail.", 300)
    
    st.write("Rick Astley - Never Gonna Give You Up")
    st.audio("images/never.mp3", loop=True)

    st.write("Spinning Herta")
    st.video("images/herta.mp4", loop=True, autoplay=True)