import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="Widgets", page_icon="🔧", layout="centered")

st.title("Some of the widgets you can use")

st.header("Persistant state")
with st.echo():
    if 'counter' not in st.session_state:
        st.session_state.counter = 0
    col1, col2 = st.columns(2)
    with col1:
        if st.button(":arrow_left:"):
            st.session_state.counter += 1
    with col2:
        if st.button(":arrow_right:"):
            st.session_state.counter -= 1
    st.write("Count", st.session_state.counter)


st.divider()

st.header("Callbacks")
with st.echo():
    def on_value_change():
        st.session_state.message = (
            f"Selected: {st.session_state.selection} "
        )
    st.selectbox(
        "Pick a number",
        [1, 2 ,3],
        key="selection",
        on_change=on_value_change # calls the function 
    )
    if 'message' in st.session_state:
        st.write(st.session_state.message)
