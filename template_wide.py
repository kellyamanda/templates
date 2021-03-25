# A wide mode template for a Streamlit app. Check out docs.streamlit.io for more ideas.
import streamlit as st
import numpy as np
import pandas as pd

# Set to wide mode, add page title, change sidebar default, or add a favicon
st.set_page_config(page_title="Streamlit Template: Wide Mode", layout="wide")

# Load your data, decorating with @st.cache to cache data for performance
@st.cache
def get_data():
    data = pd.DataFrame(
        np.random.randn(20, 3),
        columns=['a', 'b', 'c'])
    return data

data = get_data()

# Set a title for your app
st.title("Streamlit Template: Wide Mode")

# Add some explainer text so users know how and why to use your app and what the widgets control
st.write("Explainer text about something. Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor.")

# Lay out your widgets in a grid
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

# Lay out the results
st.header("A header about the results")
st.write("Explainer text about the results. Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor.")


# Lay out your data and visualizations.
st.area_chart(data)

# We will use 3 columns. You should pick whichever column layout works best.
col1, col2, col3 = st.beta_columns(3)

with col1:
    st.bar_chart(data)

with col2:
    st.line_chart(data)

with col3:
    st.write(data)

# Use expanders for extra data, charts, or explanations
with st.beta_expander("See more information"):
    st.write("Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo. Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit, sed quia consequuntur magni dolores eos qui ratione voluptatem sequi nesciunt. Neque porro quisquam est, qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit, sed quia non numquam eius modi tempora incidunt ut labore et dolore magnam aliquam quaerat voluptatem. Ut enim ad minima veniam, quis nostrum exercitationem ullam corporis suscipit laboriosam, nisi ut aliquid ex ea commodi consequatur? Quis autem vel eum iure reprehenderit qui in ea voluptate velit esse quam nihil molestiae consequatur, vel illum qui dolorem eum fugiat quo voluptas nulla pariatur?")
