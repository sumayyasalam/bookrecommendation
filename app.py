import streamlit as st
import pickle
import pandas as pd
import numpy as np

st.title("📚 Book Recommendation System")

# Load Popular Books
popular_df = pickle.load(open('popular.pkl','rb'))

st.subheader("Top Recommended Books")
st.dataframe(popular_df.head(10))

# Load Pivot File
pt = pickle.load(open('pivot.pkl','rb'))

st.write("Pivot Shape:")
st.write(pt.shape)

# Load Similarity File
st.header("📚 Get Book Recommendations")

selected_book = st.selectbox(
    "Choose a Book",
    pt.index.values
)

def recommend(book_name):

    index = np.where(
        pt.index == book_name
    )[0][0]

    similar_items = sorted(
        list(
            enumerate(
                similarity_scores[index]
            )
        ),
        key=lambda x: x[1],
        reverse=True
    )[1:6]

    recommendations = []

    for i in similar_items:
        recommendations.append(
            pt.index[i[0]]
        )

    return recommendations

if st.button("Recommend"):

    recommendations = recommend(
        selected_book
    )

    st.subheader(
        "Recommended Books"
    )

    for book in recommendations:
        st.write("📖", book)


