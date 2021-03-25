# This template is a layout for a tutorial or explainer style app that is explaining a concept. Check out docs.streamlit.io for more ideas.
import streamlit as st
import numpy as np
import pandas as pd

# Set to wide mode, add page title, change layout centering, or add a favicon
st.set_page_config(page_title="Streamlit Template: Explainer")

# Load the data you will use in your , decorating with @st.cache to cache data for performance
@st.cache
def get_data():
    data = pd.DataFrame(
        np.random.randn(20, 5),
        columns=['a', 'b', 'c', 'd', 'e'])
    return data

data = get_data()

# Set a title for your app and a short explanation
st.title("Streamlit Template: Explainer")
st.write("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor. ")

# If you want, add an image or chart to start off the app
image = "https://images.unsplash.com/photo-1607370883617-9720ac853cc4?ixlib=rb-1.2.1&ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&auto=format&fit=crop&w=2550&q=80"
st.image(image)


# Use subheaders to break up the sections
st.subheader("Section numero uno")
st.write("""
    Ed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam,
    eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo. Nemo enim ipsam
    voluptatem quia voluptas sit aspernatur aut odit aut fugit, sed quia consequuntur magni dolores eos qui ratione
    voluptatem sequi nesciunt. Neque porro quisquam est, qui dolorem ipsum quia dolor sit amet, consectetur, adipisci
    velit, sed quia non numquam eius modi tempora incidunt ut labore et dolore magnam aliquam quaerat voluptatem. Ut
    enim ad minima veniam, quis nostrum exercitationem ullam corporis suscipit laboriosam, nisi ut aliquid ex ea
    commodi consequatur? Quis autem vel eum iure reprehenderit qui in ea voluptate velit esse quam nihil molestiae
    consequatur, vel illum qui dolorem eum fugiat quo voluptas nulla pariatur?
""")

# Add in data, charts, and widgets that let your viewers interact with the charts and data
st.subheader("An example of a chart")
st.write("Words explaining what to do with the chart and how to use the widget to learn something")
st.slider("A slider",1,100)
st.line_chart(data)

st.subheader("More examples of things")
st.write("""
    Ed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam,
    eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo. Nemo enim ipsam
    voluptatem quia voluptas sit aspernatur aut odit aut fugit.
    """)

# You can use columns add text or widgets alongside images, charts, or data to better lay things out
col1, col2 = st.beta_columns((1,2)) # By default columns have equal width, but you can adjust the width of the columns by specify in parenthesis the proportional width you want

with col1:
    st.write("""
        An explanation of the data and what it means. Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do
        eiusmod tempor. Ut enim ad minima veniam, quis nostrum exercitationem ullam corporis suscipit laboriosam,
        nisi ut aliquid ex ea commodi consequatur.
        """)
with col2:
    st.write(data)
