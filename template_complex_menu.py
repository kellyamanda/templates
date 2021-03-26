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
st.title("Streamlit Template: Complex Menu")

# Put your widgets in an expander and then in that lay out your widgets in a grid

# with st.beta_expander("View controls", expanded=True):
widget_col1, widget_col2, widget_col3, widget_col4 = st.beta_columns(4)

with widget_col1:
    with st.beta_expander("🔢 Data controls", expanded=True):
        st.number_input("Select number", 1,10)
        st.slider("Select value",1,100)


with widget_col2:
    with st.beta_expander("🔤 Text controls", expanded=True):
        st.multiselect("Choose text", ["apple", "banana", "cherry"])
        st.text_input("Add text")

with widget_col3:
    with st.beta_expander("*️⃣ Time controls", expanded=True):
        st.date_input("Select date")
        st.time_input("Pick a time")

with widget_col4:
    with st.beta_expander("🔄 Settings", expanded=True):
        st.selectbox("Choose options", ("Option A", "Option B", "Option C"))
        st.radio("Select one", ("Default", "Advanced"))
