import streamlit as st
import pandas as pd

# setup code, can ignore
st.set_page_config(page_title="Browse Movies", layout="wide", page_icon="🔍")
if "movies_df" not in st.session_state:
    st.error("Movie data not found! Please return to the home page.")
    st.page_link("pages/05_PagesHome.py", label="Return to Home", icon="🏠")
    st.stop()
movies_df = st.session_state.movies_df
genres = st.session_state.genres
years = st.session_state.years



st.title("Browse Movies")
col1, col2, col3 = st.columns(3)
with col1:
    genre_filter = st.selectbox("Genre", ["All"] + sorted(genres))
with col2:
    min_year_filter = st.number_input("Minimum Year", min_value=min(years), max_value=max(years), value=2010)
with col3:
    min_rating_filter = st.slider("Minimum Rating", 1.0, 10.0, 6.0, 0.5)
filtered_movies = movies_df.copy()
if genre_filter != "All":
    filtered_movies = filtered_movies[filtered_movies["Genre"] == genre_filter]
filtered_movies = filtered_movies[
    (filtered_movies["Year"] >= min_year_filter) & 
    (filtered_movies["Rating"] >= min_rating_filter)
]
st.write(f"Found {len(filtered_movies)} movies matching your criteria")
st.dataframe(filtered_movies)


# Navigation bar
st.sidebar.page_link("pages/05_PagesHome.py", label="Home", icon="🏠")
st.sidebar.page_link("pages/05_PagesBrowse.py", label="Browse Movies", icon="🔍", help="You are here")
st.sidebar.page_link("pages/05_PagesRecommend.py", label="Get Recommendations", icon="🎯")
st.sidebar.page_link("pages/05_PagesAnalytics.py", label="Movie Analytics", icon="📊")