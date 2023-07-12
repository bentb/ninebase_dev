#!/usr/bin/env python
# coding: utf-8
#data_analyze/player_batting_season.ipynb

import streamlit as st
from nbformat import read
from nbconvert import MarkdownExporter

def batting_page():
    st.write('This is the batting page.')

    # Load the Jupyter notebook file
    notebook_filename = 'data_analyze/player_batting_season.ipynb'  # Replace with the actual file path
    with open(notebook_filename, 'r') as f:
        notebook_content = read(f, 4)  # Specify the nbformat version (e.g., 4)

    # Convert the notebook content to Markdown
    exporter = MarkdownExporter()
    markdown_content, _ = exporter.from_notebook_node(notebook_content)

    # Display the rendered notebook content
    st.markdown(markdown_content)

try:
    batting_page()
except Exception as e:
    st.error(f"An error occurred: {e}")

