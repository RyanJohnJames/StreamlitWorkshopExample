import streamlit as st
import pandas as pd

st.set_page_config(page_title="Get Recommendations", layout="wide", page_icon="🎯")
if "movies_df" not in st.session_state:
    st.error("Movie data not found! Please return to the home page.")
    st.page_link("pages/05_PagesHome.py", label="Return to Home", icon="🏠")
    st.stop()
movies_df = st.session_state.movies_df
genres = st.session_state.genres


def recommend_movies(genre=None, min_rating=None, min_year=None):
    filtered_df = movies_df.copy()
    if genre:
        filtered_df = filtered_df[filtered_df["Genre"] == genre]
    if min_rating:
        filtered_df = filtered_df[filtered_df["Rating"] >= min_rating]
    if min_year:
        filtered_df = filtered_df[filtered_df["Year"] >= min_year]
    return filtered_df.sort_values(by="Rating", ascending=False).head(10)
st.title("Get Personalized Recommendations")
st.subheader("What kind of movies do you like?")
fav_genre = st.selectbox("Favorite Genre", genres)
min_rating = st.slider("Minimum Rating", 1.0, 10.0, 7.0, 0.5)
recent_only = st.checkbox("Only movies from 2015 and later")
min_year = 2015 if recent_only else None
if st.button("Generate Recommendations"):
    recommendations = recommend_movies(genre=fav_genre, min_rating=min_rating, min_year=min_year)
    st.subheader("Your Recommendations")
    for i, (_, movie) in enumerate(recommendations.iterrows(), 1):
        st.write(f"{i}. **{movie['Title']}** ({movie['Year']}) - Rating: {movie['Rating']}/10")


# Navigation bar
st.sidebar.page_link("pages/05_PagesHome.py", label="Home", icon="🏠")
st.sidebar.page_link("pages/05_PagesBrowse.py", label="Browse Movies", icon="🔍")
st.sidebar.page_link("pages/05_PagesRecommend.py", label="Get Recommendations", icon="🎯", help="You are here")
st.sidebar.page_link("pages/05_PagesAnalytics.py", label="Movie Analytics", icon="📊")