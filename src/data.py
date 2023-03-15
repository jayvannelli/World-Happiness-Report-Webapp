import streamlit as st
import pandas as pd


@st.cache_data
def get_data() -> pd.DataFrame:
    df = pd.read_csv("data/WorldHappinessReport2005-2021.csv")
    return df
