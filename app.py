import streamlit as st
import pickle
import pandas as pd
import numpy as np

# Page Configuration
st.set_page_config(
    page_title="Book Recommendation System",
    page_icon="📚",
    layout="wide"
)

st.title("📚 Book Recommendation System")

# Load Files
import pickle
import streamlit as st

files = [
    "popular.pkl",
    "pivot.pkl",
    "similarity.pkl",
    "books_small.pkl"
]

for file in files:
    try:
        with open(file, "rb") as f:
            obj = pickle.load(f)
        st.success(f"{file} loaded successfully")
    except Exception as e:
        st.error(f"{file} ERROR: {e}")
# Display Popular Books
st.header("⭐ Top Recommended Books")

try:
    st.dataframe(popular_df.head(10))
except:
    st.write(popular_df)

# Debug Information
with st.expander("Dataset Information"):
    st.write("Pivot Table Shape:", pt.shape)
    st.write("Similarity Matrix Shape:", similarity_scores.shape)
    st.write("Number of Books:", len(pt.index))

# Recommendation Function
def recommend(book_name):
    try:
        if book_name not in pt.index:
            return []

        index = np.where(pt.index == book_name)[0][0]

        similar_items = sorted(
            list(enumerate(similarity_scores[index])),
            key=lambda x: x[1],
            reverse=True
        )[1:6]

        recommendations = []

        for i in similar_items:
            recommendations.append(pt.index[i[0]])

        return recommendations

    except Exception as e:
        st.error(f"Recommendation Error: {e}")
        return []

# Recommendation Section
st.header("📖 Get Book Recommendations")

selected_book = st.selectbox(
    "Choose a Book",
    pt.index.values
)

if st.button("🔍 Recommend Books"):

    recommendations = recommend(selected_book)

    if recommendations:
        st.subheader("Recommended Books")

        for i, book in enumerate(recommendations, start=1):
            st.write(f"{i}. 📚 {book}")

    else:
        st.warning("No recommendations found for the selected book.")
