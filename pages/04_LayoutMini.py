import streamlit as st
import pandas as pd
import numpy as np


st.set_page_config(page_title="Layout", page_icon="🖥", layout="centered")

st.title("Examples of layouts you can use")

st.header("st.columns()")
with st.echo():
    col1, col2 = st.columns(2)
    with col1:
        st.header("Fei xiao")
        st.image("images/feixiao.jpeg")
    with col2:
        st.header("Kali")
        st.image('images/redmist.jpg',"bait used to be believeabl- IS THAT THE RED MIST??",300)

st.divider()

st.header("st.container()")
with st.echo():
    with st.container():
        st.write(":green[I'm inside the container!]")
        st.bar_chart(np.random.randn(50,3))

st.write(":red[I'm not inside the container!]")

st.divider()


st.header("st.expender()")

with st.echo():
    with st.expander("See explanation"):
        st.write("""
    One day, after dinner, while my younger sister and I were lounging about in Mr. Gopher Wood's yard, we spotted a fledgling Charmony Dove all on its own. 
    That baby bird was tiny, it didn't even have all of its feathers, and it couldn't sing. When we found it, it was already on its last breath, having fallen into a shrub — probably abandoned by its parents. 
    We decided to build a nest for it right there and then. However, thinking back, that winter was unusually cold, with fierce winds at night in the yard, not to mention the many poisonous bugs and wild beasts in the vicinity... 
    It was clear that if we left the fledgling in the yard, it stood no chance of surviving until spring. 
    So, I suggested we take it inside, place it on the shelf by the window, and asked the adults to fashion a cage for it. 
    We decided that when it regained its strength enough to spread its wings, we would release it back into the wild. 
    The tragic part — something that we'd never considered — was that this bird's fate had already been determined long before this moment... 
    Its destiny was determined by our momentary whim. Now, I pass the power of choice to you all. 
    Faced with this situation, what choice would you make? Stick to the original plan, and build a nest with soft net where the Charmony Dove fell? 
    Or build a cage for it, and feed it, giving it the utmost care from within the warmth of a home? I eagerly await your answer. 
    """)

st.divider()

st.header("st.popover()")

with st.echo():
    with st.popover("Open me"):
        st.image("images/changli.jpeg", "changli for the hit game Wuthering Waves", 300)

st.divider()

st.header("st.tabs()")

with st.echo():
    tab1, tab2, tab3 = st.tabs(["Changli", "Fei Xiao", "Kali"])
    with tab1:
        st.header("Changli")
        st.image("images/changli.jpeg", width=200)
    with tab2:
        st.header("Fei Xiao")
        st.image("images/feixiao.jpeg", width=200)
    with tab3:
        st.header("IS THAT THE RED MIST???")
        st.image("images/redmist.jpg", width=300)

st.divider()

