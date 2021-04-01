# A wide mode template for a Streamlit app. Check out docs.streamlit.io for more ideas.
import streamlit as st
import numpy as np
import pandas as pd
import altair as alt

# Set to wide mode, add page title, change layout centering, or add a favicon
st.set_page_config(page_title="Streamlit Template: Big Chart", layout="wide")

# Load your data, decorating your function with @st.cache to cache data for performance
@st.cache
def get_data():
    data = pd.DataFrame(
        np.random.randn(50, 4),
        columns=['a', 'b', 'c', 'd'])
    return data

data = get_data()

# Set a title for your app
title_col1, title_col2 = st.beta_columns(2)
with title_col1:
    st.title("Streamlit Template: Big Chart!")

with title_col2:
    # Add some explainer text so users know how and why to use your app and what the widgets control
    st.write("")
    st.write("")
    st.write("""

    Explainer text about something. Lorem ipsum dolor sit amet, consectetur adipiscing.
    """)

# Put your widgets in an expander and then in that lay out your widgets in a grid
with st.beta_expander("Adjust chart values"):
    widget_col1, widget_col2, widget_col3 = st.beta_columns(3)

    with widget_col1:
        st.multiselect("Choose data", ["a", "b", "c"])
        st.slider("Select value",1,100)

    with widget_col2:
        st.number_input("Select number", 1,10)
        st.text_input("Add text")

    with widget_col3:
        st.date_input("Select date")
        st.time_input("Pick a time")


# Lay out your data and visualizations.

# We will use 3 columns. You should pick whichever column layout works best.
col1, col2 = st.beta_columns((2,1))

with col1:
    st.area_chart(data, height=610)

with col2:
    st.line_chart(data)
    st.bar_chart(data)
