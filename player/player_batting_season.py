#!/usr/bin/env python
# coding: utf-8

import streamlit as st
import json
from nbformat import reads, NotebookNode

def batting_page():
    st.write('This is the batting page.')

    # Load the Jupyter notebook file
    notebook_filename = 'path/to/player_batting_season.ipynb'  # Replace with the actual file path
    with open(notebook_filename, 'r') as f:
        notebook_content = json.load(f)

    # Extract code cells from the notebook content
    code_cells = [
        cell.source
        for cell in notebook_content['cells']
        if cell.cell_type == 'code'
    ]

    # Display the code cells
    for code_cell in code_cells:
        st.code(code_cell, language='python')
