# A wide mode template for a Streamlit app. Check out docs.streamlit.io for more ideas.
import streamlit as st
import numpy as np
import pandas as pd
import altair as alt
from vega_datasets import data

# Set to wide mode, add page title, change layout centering, or add a favicon
st.set_page_config(page_title="Streamlit Dark and Wide", layout="wide")

source = data.unemployment_across_industries.url

# Load your data, decorating your function with @st.cache to cache data for performance
@st.cache
def get_data():
    data = pd.DataFrame(
        np.random.randn(50, 4),
        columns=['cohort1', 'cohort2', 'cohort3', 'cohort4'])
    return data

# def get_UN_data():
#     AWS_BUCKET_URL = "https://streamlit-demo-data.s3-us-west-2.amazonaws.com"
#     df = pd.read_csv(AWS_BUCKET_URL + "/agri.csv.gz")
#     return df.set_index("Region")
#
# df = get_UN_data()
# df2 = df.T
#
# df3 = df2[['Poland', 'Turkey', 'Germany', 'Brazil']].copy()
#
# df3 = df3.rename(columns={'Poland':'04.2021', 'Turkey':'01.2021','Germany':'03.2021','Brazil':'02.2021'})
# df4 = df3.T
# df4 = df4[['1961','1965','1969','1972','1978','1982','1984','1985','1991']]
# df4 = df4.rename(columns={'1961':'cohort1','1965':'cohort2','1969':'cohort3','1972':'cohort4','1978':'cohort5','1982':'cohort6','1984':'cohort7','1985':'cohort8','1991':'cohort9'})
# data = get_data()
# data2 = pd.DataFrame(
#     np.random.randn(15, 3),
#     columns=['January', 'February', 'March'])
data3 = pd.DataFrame(
    np.array([["1jfidihs_3", "cohort1", "-.127"], ["1ei4i3i2_2", "cohort1", ".422"], ["2aisud0q_2", "cohort1", ".371"],["2hbaiid2_3", "cohort1", ".137"], ["1dkithss0_2", "cohort1", ".021"], ["3askdif9_1", "cohort2", ".211"]]),
                   columns=['user_id', 'cohort', 'corr'])

c = alt.Chart(source).mark_area().encode(
    alt.X('yearmonth(date):T',
        axis=alt.Axis(format='%Y', domain=False, tickSize=0)
    ),
    alt.Y('sum(count):Q', stack='center', axis=None),
    alt.Color('series:N',legend=None,
        scale=alt.Scale(scheme='category20b')
    )
).properties(height=610, width=700)

# Compute x^2 + y^2 across a 2D grid
nps, use_rate = np.meshgrid(range(-5, 5), range(0, 10))
churn_risk = nps ** 2 + use_rate ** 2

# Convert this grid to columnar data expected by Altair
source = pd.DataFrame({'nps': nps.ravel(),
                     'use_rate': use_rate.ravel(),
                     'churn_risk': churn_risk.ravel()})

d = alt.Chart(source).mark_rect().encode(
    x='nps:O',
    y='use_rate:O',
    color='churn_risk:Q'
).properties(width=400)

# Set a title for your app
title_col1, title_col2, title_col3 = st.beta_columns((.1,1,.6))

with title_col1:
    st.write("####")
    st.image("thumbnails/logoexample.png", width=52)

with title_col2:
    st.title("Generate Cohort Experiments")

with title_col3:
    st.write("""
    ##
    Run predictive modeling on various cohorts and return lists of user_ids.
    """)

# Put your widgets in an expander and then in that lay out your widgets in a grid
with st.beta_expander("Adjust chart values"):
    widget_col1, widget_col2, widget_col3 = st.beta_columns(3)

    with widget_col1:
        st.multiselect("Choose data set", ["a", "b", "c"])
        st.slider("Select rate",1,100)

    with widget_col2:
        st.number_input("Select product category", 1,10)
        st.radio("Select one", ("Default", "Advanced"))

    with widget_col3:
        st.date_input("Select end date")
        st.button("Generate Experiments")

st.write("#")

# Lay out your data and visualizations.

# We will use 3 columns. You should pick whichever column layout works best.
col1, col2 = st.beta_columns((2,1))

with col1:
    st.altair_chart(c)

with col2:
    st.altair_chart(d)
    st.table(data3)
