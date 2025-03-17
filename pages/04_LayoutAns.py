import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Page configuration
st.set_page_config(
    page_title="Movie Ratings Analysis Dashboard",
    layout="wide"
)

# Set page title
st.title("Movie Ratings Analysis Dashboard")

# Create sample movie dataset
np.random.seed(42)
n_movies = 100
genres = ["Action", "Comedy", "Drama", "Sci-Fi", "Horror", "Romance", "Animation"]
years = list(range(2000, 2023))

data = {
    "Title": [f"Movie {i}" for i in range(1, n_movies+1)],
    "Genre": np.random.choice(genres, n_movies),
    "Year": np.random.choice(years, n_movies),
    "Budget (millions)": np.random.uniform(1, 200, n_movies).round(2),
    "Revenue (millions)": np.random.uniform(1, 500, n_movies).round(2),
    "Rating": np.random.uniform(1, 10, n_movies).round(1),
    "Runtime (min)": np.random.randint(75, 210, n_movies)
}

# Convert to DataFrame
df = pd.DataFrame(data)
df["Profit (millions)"] = df["Revenue (millions)"] - df["Budget (millions)"]

# ----- SIDEBAR FILTERS -----
st.sidebar.header("Filters")
selected_genres = st.sidebar.multiselect("Select genres:", options=genres, default=genres)
min_year, max_year = st.sidebar.slider("Year range:", min_value=min(years), max_value=max(years), value=(min(years), max(years)))
min_rating = st.sidebar.slider("Minimum rating:", min_value=1.0, max_value=10.0, value=1.0, step=0.1)

# Add a sidebar divider and information
st.sidebar.markdown("---")
with st.sidebar.expander("About This Dashboard"):
    st.write("""
    This dashboard analyzes a dataset of movie ratings across different genres. 
    Use the filters above to explore different subsets of the data.
    """)

# Filter the data
filtered_df = df[
    (df["Genre"].isin(selected_genres)) &
    (df["Year"] >= min_year) & (df["Year"] <= max_year) &
    (df["Rating"] >= min_rating)
]

# Show filter summary 
st.sidebar.markdown("---")
st.sidebar.write(f"Showing {len(filtered_df)} out of {len(df)} movies")

# Download button for filtered data
csv = filtered_df.to_csv(index=False).encode('utf-8')
st.sidebar.download_button(
    label="Download Filtered Data",
    data=csv,
    file_name="filtered_movies.csv",
    mime="text/csv",
)

# ----- MAIN CONTENT AREA -----
# Create tabs for better organization
tab1, tab2, tab3 = st.tabs(["Overview", "Visualizations", "Top Movies"])

# TAB 1: Overview
with tab1:
    # Summary metrics in columns
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Total Movies", len(filtered_df))
    with col2:
        st.metric("Average Rating", f"{filtered_df['Rating'].mean():.1f}")
    with col3:
        st.metric("Average Budget", f"${filtered_df['Budget (millions)'].mean():.1f}M")
    with col4:
        st.metric("Average Revenue", f"${filtered_df['Revenue (millions)'].mean():.1f}M")
    
    # Dataset in an expander
    with st.expander("View Dataset", expanded=True):
        st.dataframe(filtered_df, use_container_width=True)
    
    # Statistics in an expander
    with st.expander("Dataset Statistics"):
        st.dataframe(filtered_df.describe(), use_container_width=True)

# TAB 2: Visualizations
with tab2:
    # First row of visualizations
    st.subheader("Movie Distribution")
    col1, col2 = st.columns(2)
    
    with col1:
        # Genre Analysis
        genre_counts = filtered_df["Genre"].value_counts().reset_index()
        genre_counts.columns = ["Genre", "Count"]

        fig1, ax1 = plt.subplots(figsize=(10, 6))
        sns.barplot(data=genre_counts, x="Genre", y="Count", ax=ax1)
        ax1.set_title("Number of Movies by Genre")
        ax1.set_xlabel("Genre")
        ax1.set_ylabel("Count")
        plt.xticks(rotation=45)
        st.pyplot(fig1)
    
    with col2:
        # Average Rating by Genre
        avg_rating = filtered_df.groupby("Genre")["Rating"].mean().reset_index()
        fig4, ax4 = plt.subplots(figsize=(10, 6))
        sns.barplot(data=avg_rating, x="Genre", y="Rating", ax=ax4)
        ax4.set_title("Average Rating by Genre")
        ax4.set_xlabel("Genre")
        ax4.set_ylabel("Average Rating")
        plt.xticks(rotation=45)
        st.pyplot(fig4)
    
    # Second row of visualizations
    st.subheader("Movie Trends")
    col1, col2 = st.columns(2)
    
    with col1:
        # Year vs. Ratings Scatter Plot
        fig2, ax2 = plt.subplots(figsize=(10, 6))
        sns.scatterplot(data=filtered_df, x="Year", y="Rating", hue="Genre", size="Revenue (millions)", 
                        sizes=(20, 200), alpha=0.7, ax=ax2)
        ax2.set_title("Movie Ratings by Year and Genre")
        plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
        st.pyplot(fig2)
    
    with col2:
        # Runtime distribution
        fig5, ax5 = plt.subplots(figsize=(10, 6))
        sns.histplot(data=filtered_df, x="Runtime (min)", bins=20, kde=True, ax=ax5)
        ax5.set_title("Distribution of Movie Runtimes")
        ax5.set_xlabel("Runtime (minutes)")
        ax5.set_ylabel("Count")
        st.pyplot(fig5)
    
    # Third visualization - full width
    st.subheader("Budget vs. Revenue Analysis")
    fig3, ax3 = plt.subplots(figsize=(12, 7))
    sns.scatterplot(data=filtered_df, x="Budget (millions)", y="Revenue (millions)", 
                    hue="Genre", size="Rating", sizes=(20, 200), alpha=0.7, ax=ax3)
    ax3.set_title("Budget vs. Revenue by Genre and Rating")
    ax3.axline([0, 0], [1, 1], color='red', linestyle='--', alpha=0.7, label='Break-even line')
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    st.pyplot(fig3)

# TAB 3: Top Movies
with tab3:
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Top Rated Movies")
        top_movies = filtered_df.sort_values(by="Rating", ascending=False).head(10)
        st.dataframe(top_movies[["Title", "Genre", "Year", "Rating"]], use_container_width=True)
        
        # Visualize top ratings
        fig6, ax6 = plt.subplots(figsize=(10, 6))
        sns.barplot(data=top_movies, x="Rating", y="Title", ax=ax6)
        ax6.set_title("Top 10 Movies by Rating")
        st.pyplot(fig6)
    
    with col2:
        st.subheader("Most Profitable Movies")
        profitable_movies = filtered_df.sort_values(by="Profit (millions)", ascending=False).head(10)
        st.dataframe(profitable_movies[["Title", "Genre", "Year", "Budget (millions)", "Revenue (millions)", "Profit (millions)"]], use_container_width=True)
        
        # Visualize top profits
        fig7, ax7 = plt.subplots(figsize=(10, 6))
        sns.barplot(data=profitable_movies, x="Profit (millions)", y="Title", ax=ax7)
        ax7.set_title("Top 10 Movies by Profit")
        st.pyplot(fig7)