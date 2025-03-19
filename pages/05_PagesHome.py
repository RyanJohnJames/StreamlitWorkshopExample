import streamlit as st
import pandas as pd
import numpy as np

# Page config
st.set_page_config(page_title="Movie App - Home", layout="wide", page_icon="🎬")

# Initialize session state to store our movie data
if "movies_df" not in st.session_state:
    # Create sample movie dataset
    np.random.seed(42)
    n_movies = 100
    genres = ["Action", "Comedy", "Drama", "Sci-Fi", "Horror", "Romance", "Animation"]
    years = list(range(2000, 2023))

    data = {
        "Title": [f"Movie {i}" for i in range(1, n_movies+1)],
        "Genre": np.random.choice(genres, n_movies),
        "Year": np.random.choice(years, n_movies),
        "Rating": np.random.uniform(1, 10, n_movies).round(1),
        "Director": [f"Director {i}" for i in range(1, 101)],
        "Popularity": np.random.uniform(1, 100, n_movies).round(1),
    }

    # Convert to DataFrame and store in session state
    st.session_state.movies_df = pd.DataFrame(data)
    st.session_state.genres = genres
    st.session_state.years = years

# Get data from session state
movies_df = st.session_state.movies_df

st.title("🎬 Movie Recommendation App")
st.write("Welcome to the Movie Recommendation App! Use the sidebar to navigate.")
col1, col2, col3 = st.columns(3)
col1.metric("Total Movies", len(movies_df))
col2.metric("Genres", len(movies_df["Genre"].unique()))
col3.metric("Average Rating", f"{movies_df['Rating'].mean():.1f}/10")
st.subheader("Featured Movie")
featured = movies_df.sample(1).iloc[0]
st.write(f"**{featured['Title']}** ({featured['Year']}) - {featured['Genre']}")
st.write(f"Rating: {featured['Rating']}/10")
with st.expander("Preview All Movies"):
    st.dataframe(movies_df.head(10))

# add page links to the sidebar
st.sidebar.page_link("pages/05_PagesHome.py", label="Home", icon="🏠")
st.sidebar.page_link("pages/05_PagesBrowse.py", label="Browse Movies", icon="🔍", help="You are here")
st.sidebar.page_link("pages/05_PagesRecommend.py", label="Get Recommendations", icon="🎯")
st.sidebar.page_link("pages/05_PagesAnalytics.py", label="Movie Analytics", icon="📊")