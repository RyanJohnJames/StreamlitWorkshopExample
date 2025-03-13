import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="Widgets", page_icon="🔧", layout="centered")

st.title("Some of the widgets you can use")


st.header("st.text_input()")
with st.echo():
    title = st.text_input("Daily goal", "take a shower")
    st.write(f"your goal for today is to {title}!")

st.subheader("using st.date_input() & st.time_input()")

with st.echo():
    import datetime

    st.title("Time Machine :alarm_clock:")
    st.subheader("Travel to the past or the future!")
    d = st.date_input("Date to travel to:", datetime.date(2025, 2, 18))
    t = st.time_input("Time to travel to:", datetime.time(23,59))
    st.write("Travel to", d , "at", t)

st.divider()

st.header("Combing widgets (usiing slider + multiselect)")

with st.echo():
    df = pd.DataFrame({
    'name' : ['John', 'Jane', 'Bob'],
    'age' : [25, 30, 35],
    'city' : ['NY', 'SF', 'LA']
    })
    min_age = st.slider("Minimum age", 0, 100, 0)
    cities = st.multiselect("Select cities", df['city'].unique())
    filtered_df = df[df['age'] >= min_age]
    if cities:
        filtered_df = filtered_df[filtered_df['city'].isin(cities)]
        st.write(filtered_df)



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
