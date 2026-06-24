import streamlit as st
import pickle
import pandas as pd
st.write("App Started")

popular_df = pickle.load(open('popular.pkl','rb'))

st.write("File Loaded Successfully")

st.write(type(popular_df))

st.write(popular_df.head())
