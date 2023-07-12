#!/usr/bin/env python
# coding: utf-8
#data_analyze/player_batting_season.ipynb

import streamlit as st
from nbformat import reads
from nbconvert import HTMLExporter

def batting_page():
    st.write('This is the batting page.')

    # Load the Jupyter notebook file
    notebook_filename = 'data_analyze/player_batting_season.ipynb'  # Replace with the actual file path
    with open(notebook_filename, 'r') as f:
        notebook_content = f.read()

    # Parse the notebook content
    notebook_node = reads(notebook_content, as_version=4)

    # Convert the notebook content to HTML
    exporter = HTMLExporter()
    html_content, _ = exporter.from_notebook_node(notebook_node)

    # Display the rendered notebook content
    st.components.v1.html(html_content, width=800, height=600)

try:
    batting_page()
except Exception as e:
    st.error(f"An error occurred: {e}")

