import streamlit as st
import pickle
import pandas as pd
import numpy as np

st.set_page_config(
page_title="Book Recommendation System",
page_icon="📚",
layout="wide"
)

st.title("📚 Book Recommendation System")

# Load Popular Books

popular_df = pickle.load(open('popular.pkl', 'rb'))

st.subheader("Top Recommended Books")
st.dataframe(popular_df.head(10))

# Load Pivot File

pt = pickle.load(open('pivot.pkl', 'rb'))

# Load Similarity Matrix

similarity_scores = pickle.load(open('similarity.pkl', 'rb'))

st.write("Pivot Shape:", pt.shape)
st.write("Similarity Shape:", similarity_scores.shape)

# Recommendation Function

def recommend(book_name):

```
index = list(pt.index).index(book_name)

similar_items = sorted(
    list(enumerate(similarity_scores[index])),
    key=lambda x: x[1],
    reverse=True
)[1:6]

recommendations = []

for i in similar_items:
    recommendations.append(pt.index[i[0]])

return recommendations
```

# Recommendation Section

st.header("📚 Get Book Recommendations")

selected_book = st.selectbox(
"Choose a Book",
pt.index.values
)

if st.button("🔍 Recommend Books"):

```
recommendations = recommend(selected_book)

st.subheader("Recommended Books")

for book in recommendations:
    st.write("📖", book)
```
