import streamlit as st

st.set_page_config(page_title="Streamlit Templates")

title_col1, title_col2 = st.beta_columns(2)
with title_col1:
    st.title("Streamlit Templates")

with title_col2:
    # Add some explainer text so users know how and why to use your app and what the widgets control
    st.write("")
    st.write("")
    st.write("""
        &nbsp;&nbsp; Quickly get started with some app layouts.
        #
    """)

TEMPLATES = [
    "basic",
    "wide",
    "big_chart",
    "complex_menu",
]

THEMES = [
    "light",
    "dark",
    "green",
    "blue",
]
GITHUB_OWNER_TEMPLATE = "kellyamanda"
GITHUB_OWNER = "streamlit"

border_color = "lightgrey"

cols_templates = st.beta_columns(4)
for col, template in zip(cols_templates, TEMPLATES):

    # Get repo name for this theme (to link to correct deployed app)-
    repo = "templates"

    col.markdown(
        f'<p align=center><a href="https://apps.streamlitusercontent.com/{GITHUB_OWNER_TEMPLATE}/templates/main/template_{template}.py/+/"><img style="border: 1px solid {border_color}" alt="{template}" src="https://raw.githubusercontent.com/{GITHUB_OWNER_TEMPLATE}/templates/main/thumbnails/{template}.png" width=150></a></p>',
        unsafe_allow_html=True,
    )
    if template in ["basic", "wide"]:
        template_descriptor = template.capitalize()
    elif template == "big_chart":
        template_descriptor = "Big chart"
    elif template == "complex_menu":
        template_descriptor = "Complex menu"

    col.write(f"<p align=center>{template_descriptor}</p>", unsafe_allow_html=True)

st.write("")
cols = st.beta_columns(4)
for col, theme in zip(cols, THEMES):

    # Get repo name for this theme (to link to correct deployed app)-
    if theme == "light":
        repo = "theming-showcase"
    else:
        repo = f"theming-showcase-{theme}"

    col.markdown(
        f'<p align=center><a href="https://apps.streamlitusercontent.com/{GITHUB_OWNER}/{repo}/main/streamlit_app.py/+/"><img style="border: 1px solid {border_color}" alt="{theme}" src="https://raw.githubusercontent.com/{GITHUB_OWNER}/theming-showcase/main/thumbnails/{theme}.png" width=150></a></p>',
        unsafe_allow_html=True,
    )
    if theme in ["light", "dark"]:
        theme_descriptor = theme.capitalize() + " theme"
    else:
        theme_descriptor = "Custom " + theme + " theme"
    col.write(f"<p align=center>{theme_descriptor}</p>", unsafe_allow_html=True)

st.write("""
    ##
    &nbsp;Looking for more inspiration? Check out the [Streamlit Gallery](https://streamlit.io/gallery) to browse dozens of real user apps.
    """)
