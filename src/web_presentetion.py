import streamlit as st
import pandas as pd
from data_pipeline import df 
from functions import compare_countries, regime_periods, rank_economies

# Page config
st.set_page_config(page_title="MacroLens", layout="wide")

# Load data
@st.cache_data
def load_data():
    return df
  

df = load_data()

# Sidebar navigation
section = st.sidebar.radio("Navigate", ["Country View", "Regional View", "World View"])

if section == "Country View":
    b=st.button('Rank economis')
    if b  :
        st.write(rank_economies(df))

elif section == "Regional View":
    pass

elif section == "World View":
    pass



# st.dataframe(df)

