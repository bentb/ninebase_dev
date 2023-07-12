#!/usr/bin/env python
# coding: utf-8
#data_analyze/player_batting_season.ipynb

import streamlit as st
from nbformat import reads
from nbconvert import NotebookNode
from streamlit_ace import st_ace

def batting_page():
    st.write('This is the batting page.')

    # Load the Jupyter notebook file
    notebook_filename = 'data_analyze/player_batting_season.ipynb'  # Replace with the actual file path
    with open(notebook_filename, 'r') as f:
        notebook_content = f.read()

    # Parse the notebook content
    notebook_node = reads(notebook_content, as_version=4)

    # Display the notebook content with code cells and outputs
    for cell in notebook_node['cells']:
        if cell['cell_type'] == 'code':

