import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Page config
st.set_page_config(page_title="Movie Analytics", layout="wide", page_icon="📊")

# Check if we have our movies data in session state
if "movies_df" not in st.session_state:
    st.error("Movie data not found! Please return to the home page.")
    st.page_link("pages/05_PagesHome.py", label="Return to Home", icon="🏠")
    st.stop()

# Get data from session state
movies_df = st.session_state.movies_df

# Navigation bar
st.sidebar.page_link("pages/05_PagesHome.py", label="Home", icon="🏠")
st.sidebar.page_link("pages/05_PagesBrowse.py", label="Browse Movies", icon="🔍")
st.sidebar.page_link("pages/05_PagesRecommend.py", label="Get Recommendations", icon="🎯")
st.sidebar.page_link("pages/05_PagesAnalytics.py", label="Movie Analytics", icon="📊", help="You are here")

# Main content
st.title("📊 Movie Analytics")

tab1, tab2 = st.tabs(["Ratings Analysis", "Genre Analysis"])

with tab1:
    # Simple analytics for ratings
    st.subheader("Ratings Distribution")
    fig, ax = plt.subplots(figsize=(10, 5))
    sns.histplot(data=movies_df, x="Rating", bins=18, kde=True, ax=ax)
    st.pyplot(fig)
    
    # Ratings over time
    st.subheader("Average Rating by Year")
    yearly_ratings = movies_df.groupby("Year")["Rating"].mean().reset_index()
    fig, ax = plt.subplots(figsize=(10, 5))
    sns.lineplot(data=yearly_ratings, x="Year", y="Rating", marker="o", ax=ax)
    st.pyplot(fig)

with tab2:
    # Analytics for genres
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