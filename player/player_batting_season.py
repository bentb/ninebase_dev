#!/usr/bin/env python
# coding: utf-8

import streamlit as st
from nbconvert import PythonExporter

def batting_page():
    st.write('This is the batting page.')

    # Load the Jupyter notebook file
    notebook_filename = 'data_analyze/player_batting_season.ipynb'
    with open(notebook_filename, 'r') as f:
        notebook_content = f.read()

    # Convert the notebook content to executable Python code
    exporter = PythonExporter()
    python_code, _ = exporter.from_notebook_node(notebook_content)

    # Display the code using Streamlit's code block
    st.code(python_code, language='python')


