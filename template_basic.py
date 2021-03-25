# A basic template for a Streamlit app. Check out docs.streamlit.io for more ideas.
import streamlit as st
import numpy as np
import pandas as pd

# Set to wide mode, add page title, change layout centering, or add a favicon
st.set_page_config(page_title="Streamlit Template: Basic", page_icon="🎈")

# Load your data, decorating with @st.cache to cache data for performance
@st.cache
def get_data():
    data = pd.DataFrame(
        np.random.randn(20, 3),
        columns=['a', 'b', 'c'])
    return data

data = get_data()

# Set a title for your app
st.title("Streamlit Template: Basic")

# Add some explainer text so users know how and why to use your app and what the widgets control
st.sidebar.subheader("Explainer text")
st.sidebar.write("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor.")

# Add widgets. Sidebar is one option for laying out your widgets.
st.sidebar.multiselect("Choose data", ["a", "b", "c"])
st.sidebar.slider("Select value",1,100)
st.sidebar.radio("Pick an option", ["option1", "option2", "option3"])

# Lay out your data and visualizations. We will use 2 columns. You should pick whichever column layout works best.
col1, col2 = st.beta_columns(2)

with col1:
    st.subheader("The chart")
    st.line_chart(data)

with col2:
    st.subheader("The data")
    st.write(data)

# Use expanders for extra data, charts, or explanations
with st.beta_expander("See more information"):
    st.write("Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo. Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit, sed quia consequuntur magni dolores eos qui ratione voluptatem sequi nesciunt. Neque porro quisquam est, qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit, sed quia non numquam eius modi tempora incidunt ut labore et dolore magnam aliquam quaerat voluptatem. Ut enim ad minima veniam, quis nostrum exercitationem ullam corporis suscipit laboriosam, nisi ut aliquid ex ea commodi consequatur? Quis autem vel eum iure reprehenderit qui in ea voluptate velit esse quam nihil molestiae consequatur, vel illum qui dolorem eum fugiat quo voluptas nulla pariatur?")
