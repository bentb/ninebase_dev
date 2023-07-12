#!/usr/bin/env python
# coding: utf-8
#data_analyze/player_batting_season.ipynb

import streamlit as st
import json
from nbformat import reads, NotebookNode

def batting_page():
    st.write('This is the batting page.')

    # Load the Jupyter notebook file
    notebook_filename = 'data_analyze/player_batting_season.ipynb'  # Replace with the actual file path
    with open(notebook_filename, 'r') as f:
        notebook_content = json.load(f)

    st.write(notebook_content)  # Print the notebook content

try:
    batting_page()
except Exception as e:
    st.error(f"An error occurred: {e}")

