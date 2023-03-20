import streamlit as st
import plost
from src.data import get_data

POSSIBLE_DISPLAY_VALUES = [
    "Life Ladder", "Log GDP per capita", "Social support", "Healthy life expectancy at birth",
    "Freedom to make life choices", "Generosity", "Perceptions of corruption",
    "Positive affect", "Negative affect", "Confidence in national government"
]


def main():
    st.title("World Happiness Report 2005-2021 | Kaggle")

    df = get_data()

    with st.expander("Data source"):
        st.write("https://www.kaggle.com/datasets/jahaidulislam/world-happiness-report-2005-2021")

    with st.expander("Display full pandas DataFrame"):
        st.dataframe(df)

    st.write("---")

    query_2021 = df.query("Year == 2021")

    plost.bar_chart(
        query_2021.nlargest(20, columns="Life Ladder"),
        title="20 countries with highest 'Life Ladder' ranking in 2021.",
        bar="Country name",
        value="Life Ladder",
        direction="horizontal",
    )

    plost.bar_chart(
        query_2021.nlargest(20, columns="Confidence in national government"),
        title="20 countries with HIGHEST confidence in national government (2021).",
        bar="Country name",
        value="Confidence in national government",
        direction="horizontal",
    )

    plost.bar_chart(
        query_2021.nsmallest(10, columns="Confidence in national government"),
        title="10 countries with LOWEST confidence in national government (2021).",
        bar="Country name",
        value="Confidence in national government",
        direction="horizontal",
    )

    left_column, right_column = st.columns(2)
    with left_column:
        country = st.selectbox("Select country", options=df['Country name'].unique())

    with right_column:
        display_value = st.selectbox("Select value to display",
                                     options=POSSIBLE_DISPLAY_VALUES)

    country_df = df.loc[df['Country name'] == country].set_index('Year')
    st.subheader(f"{country} {display_value} ({country_df.index[0]} - {country_df.index[-1]})")
    st.bar_chart(country_df, y=display_value)


if __name__ == "__main__":
    main()
