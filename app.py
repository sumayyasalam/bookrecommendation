import streamlit as st
import pickle
import numpy as np

st.set_page_config(
    page_title="Book Recommendation System",
    page_icon="📚",
    layout="wide"
)

st.markdown("""
<style>
.main {background-color: #f7f9fc;}
.big-title {
    font-size: 48px;
    font-weight: 800;
    color: #243447;
    text-align: center;
}
.subtitle {
    font-size: 20px;
    color: #6c757d;
    text-align: center;
}
.card {
    background-color: white;
    padding: 22px;
    border-radius: 18px;
    box-shadow: 0 4px 14px rgba(0,0,0,0.08);
    margin-bottom: 18px;
}
.book-title {
    font-size: 18px;
    font-weight: 700;
    color: #1f4e79;
}
.small-text {
    font-size: 14px;
    color: #6c757d;
}
</style>
""", unsafe_allow_html=True)

st.markdown("<div class='big-title'>📚 Book Recommendation System</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>AI-powered book suggestions using collaborative filtering</div>", unsafe_allow_html=True)
st.write("---")

try:
    popular_df = pickle.load(open("popular.pkl", "rb"))
    pt = pickle.load(open("pivot.pkl", "rb"))
    similarity_scores = pickle.load(open("similarity.pkl", "rb"))
    books = pickle.load(open("books_small.pkl", "rb"))
except Exception as e:
    st.error(f"Error loading files: {e}")
    st.stop()

def recommend(book_name):
    try:
        index = np.where(pt.index == book_name)[0][0]
        similar_books = sorted(
            list(enumerate(similarity_scores[index])),
            key=lambda x: x[1],
            reverse=True
        )[1:6]
        return [pt.index[i[0]] for i in similar_books]
    except Exception as e:
        st.error(f"Recommendation Error: {e}")
        return []

tab1, tab2 = st.tabs(["🏆 Popular Books", "🔍 Recommend Books"])

with tab1:
    st.header("⭐ Top Recommended Books")

    for i, row in popular_df.head(10).iterrows():
        book_name = row["Book-Title"] if "Book-Title" in popular_df.columns else i
        rating = row["avg_rating"] if "avg_rating" in popular_df.columns else "N/A"
        count = row["num_rating"] if "num_rating" in popular_df.columns else "N/A"

        st.markdown(f"""
        <div class="card">
            <div class="book-title">📖 {book_name}</div>
            <div class="small-text">⭐ Average Rating: {rating}</div>
            <div class="small-text">👥 Number of Ratings: {count}</div>
        </div>
        """, unsafe_allow_html=True)

with tab2:
    st.header("📖 Find Similar Books")

    selected_book = st.selectbox(
        "Select a book you like",
        pt.index.values
    )

    if st.button("🔍 Recommend Books", use_container_width=True):
        recommended_books = recommend(selected_book)

        if recommended_books:
            st.subheader("Books You May Like")

            cols = st.columns(5)

            for idx, book in enumerate(recommended_books):
                with cols[idx]:
                    st.markdown(f"""
                    <div class="card">
                        <div class="book-title">📚 {book}</div>
                        <div class="small-text">Recommended based on similar user preferences</div>
                    </div>
                    """, unsafe_allow_html=True)
        else:
            st.warning("No recommendations found.")

with st.expander("📊 Dataset Information"):
    st.write("Popular Books Shape:", getattr(popular_df, "shape", "N/A"))
    st.write("Pivot Table Shape:", pt.shape)
    st.write("Similarity Matrix Shape:", similarity_scores.shape)
