import streamlit as st
import pickle
import numpy as np

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="Book Recommendation System",
    page_icon="📚",
    layout="wide"
)

st.title("📚 Book Recommendation System")

# -----------------------------
# Load Files
# -----------------------------
try:
    popular_df = pickle.load(open("popular.pkl", "rb"))
    pt = pickle.load(open("pivot.pkl", "rb"))
    similarity_scores = pickle.load(open("similarity.pkl", "rb"))
    books = pickle.load(open("books_small.pkl", "rb"))

except Exception as e:
    st.error(f"Error loading files: {e}")
    st.stop()

# -----------------------------
# Popular Books Section
# -----------------------------
st.header("⭐ Top Recommended Books")

try:
    st.dataframe(popular_df.head(10))
except Exception:
    st.write(popular_df)

# -----------------------------
# Recommendation Function
# -----------------------------
def recommend(book_name):

    try:
        index = np.where(pt.index == book_name)[0][0]

        similar_books = sorted(
            list(enumerate(similarity_scores[index])),
            key=lambda x: x[1],
            reverse=True
        )[1:6]

        recommendations = []

        for i in similar_books:
            recommendations.append(pt.index[i[0]])

        return recommendations

    except Exception as e:
        st.error(f"Recommendation Error: {e}")
        return []

# -----------------------------
# Recommendation UI
# -----------------------------
st.header("📖 Get Book Recommendations")

selected_book = st.selectbox(
    "Select a Book",
    pt.index.values
)

if st.button("Recommend"):

    recommended_books = recommend(selected_book)

    if len(recommended_books) > 0:

        st.subheader("Books You May Like")

        for book in recommended_books:
            st.write("📚", book)

    else:
        st.warning("No recommendations found.")

# -----------------------------
# Debug Information
# -----------------------------
with st.expander("Dataset Information"):
    st.write("Popular Books Shape:", getattr(popular_df, "shape", "N/A"))
    st.write("Pivot Table Shape:", pt.shape)
    st.write("Similarity Matrix Shape:", similarity_scores.shape)
