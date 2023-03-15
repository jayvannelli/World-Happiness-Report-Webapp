import streamlit as st
from src.data import get_data


def main():
    st.title("World Happiness Report 2005-2021 | Kaggle")

    df = get_data()
    st.dataframe(df)


if __name__ == "__main__":
    main()
