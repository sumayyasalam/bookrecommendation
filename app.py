import streamlit as st
import pickle
import pandas as pd

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
similarity_scores = pickle.load(open('similarity.pkl','rb'))

st.write("Similarity Shape:")
st.write(similarity_scores.shape)
