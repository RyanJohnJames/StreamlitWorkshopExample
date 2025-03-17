# TODO: heavily comment this version of the code for a guided project
# TODO: make this shorter somehow
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Page config
st.set_page_config(page_title="Movie Recommendation App", layout="wide")

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

# Convert to DataFrame
movies_df = pd.DataFrame(data)

# Helper function for recommending movies
def recommend_movies(genre=None, min_rating=None, min_year=None):
    filtered_df = movies_df.copy()
    
    if genre:
        filtered_df = filtered_df[filtered_df["Genre"] == genre]
    
    if min_rating:
        filtered_df = filtered_df[filtered_df["Rating"] >= min_rating]
        
    if min_year:
        filtered_df = filtered_df[filtered_df["Year"] >= min_year]
    
    return filtered_df.sort_values(by="Rating", ascending=False).head(10)

# Sidebar navigation (currently just text)
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Browse Movies", "Get Recommendations", "Analytics"])

# Home page
if page == "Home":
    st.title("🎬 Movie Recommendation App")
    st.write("Welcome to the Movie Recommendation App! Use the sidebar to navigate.")
    
    # Show some stats
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Movies", len(movies_df))
    col2.metric("Genres", len(movies_df["Genre"].unique()))
    col3.metric("Average Rating", f"{movies_df['Rating'].mean():.1f}/10")
    
    # Show random featured movie
    st.subheader("Featured Movie")
    featured = movies_df.sample(1).iloc[0]
    st.write(f"**{featured['Title']}** ({featured['Year']}) - {featured['Genre']}")
    st.write(f"Rating: {featured['Rating']}/10")
    
    # Preview of all movies
    with st.expander("Preview All Movies"):
        st.dataframe(movies_df.head(10))

# Browse Movies page
elif page == "Browse Movies":
    st.title("Browse Movies")
    
    # Filters
    col1, col2, col3 = st.columns(3)
    with col1:
        genre_filter = st.selectbox("Genre", ["All"] + sorted(genres))
    with col2:
        min_year_filter = st.number_input("Minimum Year", min_value=min(years), max_value=max(years), value=2010)
    with col3:
        min_rating_filter = st.slider("Minimum Rating", 1.0, 10.0, 6.0, 0.5)
    
    # Apply filters
    filtered_movies = movies_df.copy()
    if genre_filter != "All":
        filtered_movies = filtered_movies[filtered_movies["Genre"] == genre_filter]
    filtered_movies = filtered_movies[
        (filtered_movies["Year"] >= min_year_filter) & 
        (filtered_movies["Rating"] >= min_rating_filter)
    ]
    
    # Show filtered movies
    st.write(f"Found {len(filtered_movies)} movies matching your criteria")
    st.dataframe(filtered_movies)

# Recommendations page
elif page == "Get Recommendations":
    st.title("Get Personalized Recommendations")
    
    # User preferences
    st.subheader("What kind of movies do you like?")
    fav_genre = st.selectbox("Favorite Genre", genres)
    min_rating = st.slider("Minimum Rating", 1.0, 10.0, 7.0, 0.5)
    recent_only = st.checkbox("Only movies from 2015 and later")
    
    min_year = 2015 if recent_only else None
    
    # Generate recommendations
    if st.button("Generate Recommendations"):
        recommendations = recommend_movies(genre=fav_genre, min_rating=min_rating, min_year=min_year)
        
        st.subheader("Your Recommendations")
        for i, (_, movie) in enumerate(recommendations.iterrows(), 1):
            st.write(f"{i}. **{movie['Title']}** ({movie['Year']}) - Rating: {movie['Rating']}/10")

# Analytics page
elif page == "Analytics":
    st.title("Movie Analytics")
    
    # Simple analytics
    st.subheader("Ratings Distribution")
    fig, ax = plt.subplots(figsize=(10, 5))
    sns.histplot(data=movies_df, x="Rating", bins=18, kde=True, ax=ax)
    st.pyplot(fig)
    
    st.subheader("Movies by Genre")
    genre_counts = movies_df["Genre"].value_counts().reset_index()
    genre_counts.columns = ["Genre", "Count"]
    
    fig, ax = plt.subplots(figsize=(10, 5))
    sns.barplot(data=genre_counts, x="Genre", y="Count", ax=ax)
    plt.xticks(rotation=45)
    st.pyplot(fig)
    
    st.subheader("Average Rating by Genre")
    avg_ratings = movies_df.groupby("Genre")["Rating"].mean().reset_index()
    
    fig, ax = plt.subplots(figsize=(10, 5))
    sns.barplot(data=avg_ratings, x="Genre", y="Rating", ax=ax)
    plt.xticks(rotation=45)
    st.pyplot(fig)