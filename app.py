import streamlit as st
import pickle
import pandas as pd
st.write("App Started")

popular_df = pickle.load(open('popular.pkl','rb'))

st.subheader("Top Recommended Books")

st.dataframe(popular_df.head(10))
st.write("Pivot Shape:", pt.shape)

st.write("Similarity Shape:")
st.write(similarity_scores.shape)
pt = pickle.load(open('pivot.pkl','rb'))

similarity_scores = pickle.load(open('similarity.pkl','rb'))
