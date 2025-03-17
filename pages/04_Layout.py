# TODO: heavily comment this version of the code for a guided project
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

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

# Show dataset
st.header("Movie Dataset")
st.write(df)

# Filter controls
st.header("Filters")
selected_genres = st.multiselect("Select genres:", options=genres, default=genres)
min_year, max_year = st.slider("Year range:", min_value=min(years), max_value=max(years), value=(min(years), max(years)))
min_rating = st.slider("Minimum rating:", min_value=1.0, max_value=10.0, value=1.0, step=0.1)

# Filter the data
filtered_df = df[
    (df["Genre"].isin(selected_genres)) &
    (df["Year"] >= min_year) & (df["Year"] <= max_year) &
    (df["Rating"] >= min_rating)
]

# Show filtered data
st.header("Filtered Dataset")
st.write(filtered_df)

# Display basic statistics
st.header("Dataset Statistics")
st.write(filtered_df.describe())

# Genre Analysis
st.header("Genre Analysis")
genre_counts = filtered_df["Genre"].value_counts().reset_index()
genre_counts.columns = ["Genre", "Count"]

fig1, ax1 = plt.subplots(figsize=(10, 6))
sns.barplot(data=genre_counts, x="Genre", y="Count", ax=ax1)
ax1.set_title("Number of Movies by Genre")
ax1.set_xlabel("Genre")
ax1.set_ylabel("Count")
plt.xticks(rotation=45)
st.pyplot(fig1)

# Year vs. Ratings Scatter Plot
st.header("Year vs. Ratings")
fig2, ax2 = plt.subplots(figsize=(10, 6))
sns.scatterplot(data=filtered_df, x="Year", y="Rating", hue="Genre", size="Revenue (millions)", 
                sizes=(20, 200), alpha=0.7, ax=ax2)
ax2.set_title("Movie Ratings by Year and Genre")
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
st.pyplot(fig2)

# Budget vs. Revenue Analysis
st.header("Budget vs. Revenue")
fig3, ax3 = plt.subplots(figsize=(10, 6))
sns.scatterplot(data=filtered_df, x="Budget (millions)", y="Revenue (millions)", 
                hue="Genre", size="Rating", sizes=(20, 200), alpha=0.7, ax=ax3)
ax3.set_title("Budget vs. Revenue by Genre and Rating")
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
st.pyplot(fig3)

# Top Rated Movies
st.header("Top Rated Movies")
top_movies = filtered_df.sort_values(by="Rating", ascending=False).head(10)
st.write(top_movies[["Title", "Genre", "Year", "Rating"]])

# Most Profitable Movies
st.header("Most Profitable Movies")
profitable_movies = filtered_df.sort_values(by="Profit (millions)", ascending=False).head(10)
st.write(profitable_movies[["Title", "Genre", "Year", "Budget (millions)", "Revenue (millions)", "Profit (millions)"]])

# Average Rating by Genre
st.header("Average Rating by Genre")
avg_rating = filtered_df.groupby("Genre")["Rating"].mean().reset_index()
fig4, ax4 = plt.subplots(figsize=(10, 6))
sns.barplot(data=avg_rating, x="Genre", y="Rating", ax=ax4)
ax4.set_title("Average Rating by Genre")
ax4.set_xlabel("Genre")
ax4.set_ylabel("Average Rating")
plt.xticks(rotation=45)
st.pyplot(fig4)

# Runtime distribution
st.header("Runtime Distribution")
fig5, ax5 = plt.subplots(figsize=(10, 6))
sns.histplot(data=filtered_df, x="Runtime (min)", bins=20, kde=True, ax=ax5)
ax5.set_title("Distribution of Movie Runtimes")
ax5.set_xlabel("Runtime (minutes)")
ax5.set_ylabel("Count")
st.pyplot(fig5)