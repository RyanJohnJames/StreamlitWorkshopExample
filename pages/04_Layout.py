import streamlit as st
import pandas as pd
import numpy as np
from streamlit_lottie import st_lottie

st.set_page_config(page_title="Layout", page_icon="🖥", layout="centered")

st.title("Examples of layouts you can use")

st.header("st.text_input()")
with st.echo():
    title = st.text_input("Daily goal", "take a shower")
    st.write(f"your goal for today is to {title}!")

st.divider()



st.header("Adding lottie animations")
with st.echo(): 
    st_lottie("https://assets5.lottiefiles.com/packages/lf20_fcfjwiyb.json")
st.divider()