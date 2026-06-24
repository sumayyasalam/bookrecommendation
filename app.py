import streamlit as st
import pickle
import pandas as pd

st.set_page_config(
page_title="Book Recommendation System",
page_icon="📚",
layout="wide"
)

st.markdown("""

<style>
.title{
text-align:center;
font-size:50px;
font-weight:bold;
color:#1f4e79;
}
.subtitle{
text-align:center;
font-size:20px;
color:gray;
}
</style>

""", unsafe_allow_html=True)

st.markdown("<p class='title'>📚 Book Recommendation System</p>",
unsafe_allow_html=True)

st.markdown("<p class='subtitle'>AI Powered Book Recommendation Engine</p>",
unsafe_allow_html=True)

popular_df = pickle.load(open('popular.pkl','rb'))

st.subheader("Top Recommended Books")

st.write(popular_df.head())
