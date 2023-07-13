#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# sources:
# docs.streamlit.io/library/get-started

# # Introduction

# In[80]:


# Import Libraries
import numpy as np
import pandas as pd

pd.set_option("display.precision", 2)
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.float_format', lambda x: '%.5f' % x)
from pandas.api.types import (
    is_categorical_dtype,
    is_datetime64_any_dtype,
    is_numeric_dtype,
    is_object_dtype,
)

import plotly.figure_factory as ff


# ## Streamlit

# In[81]:


import streamlit as st


# In[82]:


st.set_page_config(
    page_title="Player Batting",
    page_icon="⚾",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Report a bug': 'https://www.extremelycoolapp.com/help',
        'Get help': "https://www.extremelycoolapp.com/bug",
        'About': "# This is a header. This is an *extremely* cool app!"
    }
)


# In[ ]:


### trying st-pages


# In[1]:





# In[ ]:





# In[ ]:





# In[83]:


def add_logo():
    st.markdown(
        """
        <style>
            [data-testid="stSidebarNav"] {
                background-image: url(https://i.imgur.com/sLSMBYJ.png);
                background-repeat: no-repeat;
                padding-top: 40px;
                background-position: 20px 20px;
            }
            [data-testid="stSidebarNav"]::before {
                content: "Navigation Menu";
                margin-left: 20px;
                margin-top: 20px;
                font-size: 26px;
                position: relative;
                top: 100px;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )


# In[84]:


add_logo()


# ## Load Data

# In[6]:


# Format for GitHub
df = pd.read_csv('data_storage/player_batting_season.csv')

# Format for Jupyter Notebook
#df = pd.read_csv('C:/Users/b7tbu/NINEBASE/ninebase/data_storage/player_batting_season.csv')


# In[85]:


df.head()


# In[86]:


import plotly.express as px
import statsmodels.api as sm


# ### Row 1 - Plot 1 (outdated)

# fig_1 = px.scatter(
#     df.query("Season==2023"),
#     title="Hard%+ vs. BABIP+",
#     x = "Hard%+",
#     y = "BABIP+",
#     hover_name = "Name",
#     log_x = True,
#     trendline = "ols",
#     size_max = 60,
#     height = 750,
#     width = 750,
# )

# ### Row 1 - Tab 1

# In[87]:


fig_11 = px.box(
    df.query("Season==2023"),
    y = "wRC+",
    points="all",
    hover_name = "Name",
    height = 500,
    width = 500,
)

fig_11.update_traces(marker=dict(color="#7284cc"))

fig_11.update_layout(
    title=dict(text="wRC+", font=dict(size=22), automargin=True, yref='paper'),
    title_font_color="#164f5e",
    yaxis=dict(title=""),
    xaxis=dict(title="")
)


# In[88]:


fig_12 = px.box(
    df.query("Season==2023"),
    y = "Bat",
    points="all",
    hover_name = "Name",
    height = 500,
    width = 500,
)

fig_12.update_traces(marker=dict(color="#7284cc"))

fig_12.update_layout(
    title=dict(text="Batting WAR", font=dict(size=22), automargin=True, yref='paper'),
    title_font_color="#164f5e",
    yaxis=dict(title=""),
    xaxis=dict(title="")
)


# In[89]:


fig_13 = px.box(
    df.query("Season==2023"),
    y = "Pos",
    points="all",
    hover_name = "Name",
    height = 500,
    width = 500,
)

fig_13.update_traces(marker=dict(color="#7284cc"))

fig_13.update_layout(
    title=dict(text="Positon Batting WAR", font=dict(size=22), automargin=True, yref='paper'),
    title_font_color="#164f5e",
    yaxis=dict(title=""),
    xaxis=dict(title="")
)


# ### Row 1 - Tab 2

# In[90]:


fig_21 = px.box(
    df.query("Season==2023"),
    y = "Soft%+",
    points="all",
    hover_name = "Name",
    height = 500,
    width = 500,
)

fig_21.update_traces(marker=dict(color="#7284cc"))

fig_21.update_layout(
    title=dict(text="Soft Hit%+", font=dict(size=22), automargin=True, yref='paper'),
    title_font_color="#164f5e",
    yaxis=dict(title=""),
    xaxis=dict(title="")
)


# In[91]:


fig_22 = px.box(
    df.query("Season==2023"),
    y = "Hard%+",
    points="all",
    hover_name = "Name",
    height = 500,
    width = 500,
)

fig_22.update_traces(marker=dict(color="#7284cc"))

fig_22.update_layout(
    title=dict(text="Hard Hit%+", font=dict(size=22), automargin=True, yref='paper'),
    title_font_color="#164f5e",
    yaxis=dict(title=""),
    xaxis=dict(title="")
)


# In[92]:


fig_23 = px.box(
    df.query("Season==2023"),
    y = "HR",
    points="all",
    hover_name = "Name",
    height = 500,
    width = 500,
)

fig_23.update_traces(marker=dict(color="#7284cc"))

fig_23.update_layout(
    title=dict(text="Home Runs", font=dict(size=22), automargin=True, yref='paper'),
    title_font_color="#164f5e",
    yaxis=dict(title=""),
    xaxis=dict(title="")
)


# ### Row 1 - Tab 3

# In[93]:


fig_31 = px.box(
    df.query("Season==2023"),
    y = "Contact%",
    points="all",
    hover_name = "Name",
    height = 500,
    width = 500,
)

fig_31.update_traces(marker=dict(color="#7284cc"))

fig_31.update_layout(
    title=dict(text="Contact%", font=dict(size=22), automargin=True, yref='paper'),
    title_font_color="#164f5e",
    yaxis=dict(title=""),
    xaxis=dict(title="")
)


# In[94]:


fig_32 = px.box(
    df.query("Season==2023"),
    y = "Z-Contact%",
    points="all",
    hover_name = "Name",
    height = 500,
    width = 500,
)

fig_32.update_traces(marker=dict(color="#7284cc"))

fig_32.update_layout(
    title=dict(text="In-Zone Contact%", font=dict(size=22), automargin=True, yref='paper'),
    title_font_color="#164f5e",
    yaxis=dict(title=""),
    xaxis=dict(title="")
)


# In[95]:


fig_33 = px.box(
    df.query("Season==2023"),
    y = "O-Contact%",
    points="all",
    hover_name = "Name",
    height = 500,
    width = 500,
)

fig_33.update_traces(marker=dict(color="#7284cc"))

fig_33.update_layout(
    title=dict(text="Out-Zone Contact%", font=dict(size=22), automargin=True, yref='paper'),
    title_font_color="#164f5e",
    yaxis=dict(title=""),
    xaxis=dict(title="")
)


# ### Row 1 - Tab 4

# In[96]:


fig_41 = px.box(
    df.query("Season==2023"),
    y = "BB%+",
    points="all",
    hover_name = "Name",
    height = 500,
    width = 500,
)

fig_41.update_traces(marker=dict(color="#7284cc"))

fig_41.update_layout(
    title=dict(text="Walk%+", font=dict(size=22), automargin=True, yref='paper'),
    title_font_color="#164f5e",
    yaxis=dict(title=""),
    xaxis=dict(title="")
)


# In[97]:


fig_42 = px.box(
    df.query("Season==2023"),
    y = "K%+",
    points="all",
    hover_name = "Name",
    height = 500,
    width = 500,
)

fig_42.update_traces(marker=dict(color="#7284cc"))

fig_42.update_layout(
    title=dict(text="Strikeout%+", font=dict(size=22), automargin=True, yref='paper'),
    title_font_color="#164f5e",
    yaxis=dict(title=""),
    xaxis=dict(title="")
)


# In[98]:


fig_43 = px.box(
    df.query("Season==2023"),
    y = "O-Swing%",
    points="all",
    hover_name = "Name",
    height = 500,
    width = 500,
)

fig_43.update_traces(marker=dict(color="#7284cc"))

fig_43.update_layout(
    title=dict(text="Out-Zone Swing%", font=dict(size=22), automargin=True, yref='paper'),
    title_font_color="#164f5e",
    yaxis=dict(title=""),
    xaxis=dict(title="")
)


# ### Row 1 - Tab 5

# In[99]:


fig_51 = px.box(
    df.query("Season==2023"),
    y = "Pull%+",
    points="all",
    hover_name = "Name",
    height = 500,
    width = 500,
)

fig_51.update_traces(marker=dict(color="#7284cc"))

fig_51.update_layout(
    title=dict(text="Pull%+", font=dict(size=22), automargin=True, yref='paper'),
    title_font_color="#164f5e",
    yaxis=dict(title=""),
    xaxis=dict(title="")
)


# In[100]:


fig_52 = px.box(
    df.query("Season==2023"),
    y = "Cent%+",
    points="all",
    hover_name = "Name",
    height = 500,
    width = 500,
)

fig_52.update_traces(marker=dict(color="#7284cc"))

fig_52.update_layout(
    title=dict(text="Center%+", font=dict(size=22), automargin=True, yref='paper'),
    title_font_color="#164f5e",
    yaxis=dict(title=""),
    xaxis=dict(title="")
)


# In[101]:


fig_53 = px.box(
    df.query("Season==2023"),
    y = "Oppo%+",
    points="all",
    hover_name = "Name",
    height = 500,
    width = 500,
)

fig_53.update_traces(marker=dict(color="#7284cc"))

fig_53.update_layout(
    title=dict(text="Oppo%+", font=dict(size=22), automargin=True, yref='paper'),
    title_font_color="#164f5e",
    yaxis=dict(title=""),
    xaxis=dict(title="")
)


# ### Row 1 - Print

# In[102]:


# Title
st.markdown('<span style="font-family: Lato, sans-serif; font-size: 28px; color: #2f4858; font-weight: bold;">Hitting Specialties</span>', unsafe_allow_html=True)

# Create the tabs
tabs = st.tabs(["Overall", "Power", "Contact", "Plate Discipline", "Pull/Oppo"])

# Display the charts within the tabs
with tabs[0]:
    col1, col2, col3 = st.columns(3)
    col1.plotly_chart(fig_11, theme="streamlit", use_container_width=False)
    col2.plotly_chart(fig_12, theme="streamlit", use_container_width=False)
    col3.plotly_chart(fig_13, theme="streamlit", use_container_width=False)

with tabs[1]:
    col4, col5, col6 = st.columns(3)
    col4.plotly_chart(fig_21, theme="streamlit", use_container_width=False)
    col5.plotly_chart(fig_22, theme="streamlit", use_container_width=False)
    col6.plotly_chart(fig_23, theme="streamlit", use_container_width=False)

with tabs[2]:
    col7, col8, col9 = st.columns(3)
    col7.plotly_chart(fig_31, theme="streamlit", use_container_width=False)
    col8.plotly_chart(fig_32, theme="streamlit", use_container_width=False)
    col9.plotly_chart(fig_33, theme="streamlit", use_container_width=False)
    
with tabs[3]:
    col10, col11, col12 = st.columns(3)
    col10.plotly_chart(fig_41, theme="streamlit", use_container_width=False)
    col11.plotly_chart(fig_42, theme="streamlit", use_container_width=False)
    col12.plotly_chart(fig_43, theme="streamlit", use_container_width=False)
    
with tabs[4]:
    col13, col14, col15 = st.columns(3)
    col13.plotly_chart(fig_51, theme="streamlit", use_container_width=False)
    col14.plotly_chart(fig_52, theme="streamlit", use_container_width=False)
    col15.plotly_chart(fig_53, theme="streamlit", use_container_width=False)


# ## Row 2

# ### Raw Data

# In[103]:


from st_aggrid import AgGrid, GridOptionsBuilder, DataReturnMode, JsCode


# In[104]:


# Builds a gridOptions dictionary using a GridOptionsBuilder instance.
builder = GridOptionsBuilder.from_dataframe(df)

# Configs
builder.configure_side_bar(filters_panel=True, columns_panel=True)

# Column Grouping
column_defs = [
    {
        "headerName": "Player",
        "field": "Name",
        "headerClass": "column-header",
        "width": 150,
        "pinned": "left",
        "enableRowGroup": True,  # Enable row grouping on the "Name" column
        "enableValue": False,  # Disable column aggregation for the "Name" column
    },
    {
        "headerName": "Player Details",
        "children": [
            {
                "field": "Team",
                "headerName": "Team",
                "width": 150,
                "enableRowGroup": True,  # Enable row grouping on the "Team" column
                "enableValue": False,  # Disable column aggregation for the "Team" column
            },
            {"field": "Age", "headerName": "Age", "width": 150, "enableValue": True},
            {"field": "AB", "headerName": "At Bats", "width": 150, "enableValue": True},
        ],
    },
    {
        "headerName": "Batting Summary",
        "children": [
            {"field": "wRC+", "headerName": "wRC+", "sort": "desc", "width": 150, "enableValue": True},
            {"field": "Bat", "headerName": "Batting WAR", "width": 150, "enableValue": True},
            {"field": "Pos", "headerName": "Pos Batting WAR", "width": 150, "enableValue": True},
        ],
    },
    {
        "headerName": "Power",
        "children": [
            {"field": "Soft%+", "headerName": "Soft Hit%+", "width": 150, "enableValue": True},
            {"field": "Med%+", "headerName": "Med Hit%+", "width": 150, "enableValue": True},
            {"field": "Hard%+", "headerName": "Hard Hit%+", "width": 150, "enableValue": True},
            {"field": "HR", "headerName": "Home Runs", "width": 150, "enableValue": True},
        ],
    },
    {
        "headerName": "Contact",
        "children": [
            {"field": "Contact%", "headerName": "Contact%", "width": 150, "enableValue": True},
            {"field": "Z-Contact%", "headerName": "In-Zone Contact%", "width": 150, "enableValue": True},
            {"field": "O-Contact%", "headerName": "Out-Zone Contact%", "width": 150, "enableValue": True},
            {"field": "BABIP+", "headerName": "BABIP+", "width": 150, "enableValue": True},
        ],
    },
    {
        "headerName": "Plate Discipline",
        "children": [
            {"field": "BB%+", "headerName": "Walk%+", "width": 150, "enableValue": True},
            {"field": "K%+", "headerName": "Strikeout%+", "width": 150, "enableValue": True},
            {"field": "Swing%", "headerName": "Swing%", "width": 150, "enableValue": True},
            {"field": "Z-Swing%", "headerName": "In-Zone Swing%", "width": 150, "enableValue": True},
            {"field": "O-Swing%", "headerName": "Out-Zone Swing%", "width": 150, "enableValue": True},
        ],
    },
    {
        "headerName": "Pull/Oppo",
        "children": [
            {"field": "Pull%+", "headerName": "Pull%+", "width": 150, "enableValue": True},
            {"field": "Cent%+", "headerName": "Cent%+", "width": 150, "enableValue": True},
            {"field": "Oppo%+", "headerName": "Oppo%+", "width": 150, "enableValue": True},
        ],
    },
]


# Merge columnDefs with existing column definitions
grid_options = {"columnDefs": column_defs}

# Launch
go = grid_options

col1, col2 = st.columns([98, 2])

with col1:
    st.write('<div style="display: flex; align-items: baseline;"><span style="font-family: Lato, sans-serif; font-size: 28px; font-weight: bold; color: #2f4858; margin-right: auto;">Browse Data</span><span>Default Sort: wRC+</span></div>', unsafe_allow_html=True)
    grid_response = AgGrid(
        df,
        gridOptions=go,
        theme="streamlit",
        height=600
    )

with col2:
    st.subheader("")


# In[105]:


# Import Asset
from PIL import Image
header_img = Image.open('assets/stevens_bat.jpg')

# Print as Columns
st.markdown("")
img_col1, img_col2, img_col3 = st.columns([20,60,20])

with img_col1:
    pass

with img_col2:
    st.image('assets/cards_at_mets.jpg')

with img_col3:
    pass


# In[ ]:





# ### Playground

# In[78]:


st.subheader("⛔ NO ENTRY ⛔ ...construction in progress 🏗️...")


# In[ ]:


import streamlit as st
from st_aggrid import AgGrid, GridOptionsBuilder

# ...

# Column Grouping
column_defs = [        
    {
        "headerName": "",
        "children": [
            {"field": "Name", "headerName": "Player", "pinned": 'left'},
        ],
        "headerClass": "player-group"  # CSS class for the Player group
    },
    {
        "headerName": "Player Details",
        "children": [
            {"field": "Team"},
            {"field": "Age"},
            {"field": "AB", "headerName": "At Bats"},
        ],
        "headerClass": "details-group"  # CSS class for the Player Details group
    },
    # ...
]

# Merge columnDefs with existing column definitions
grid_options = {"columnDefs": column_defs}

# CSS styles
st.markdown("""
<style>
.ag-header-group-player-group {
    background-color: #FF0000;  /* Red color for Player group */
}

.ag-header-group-details-group {
    background-color: #00FF00;  /* Green color for Player Details group */
}

/* Add more styles for other groups as needed */
</style>
""", unsafe_allow_html=True)

# Launch
go = grid_options

col1, col2 = st.columns([0.75, 0.25])

with col1:
    st.subheader("Browse Data")
    grid_response = AgGrid(
        df,
        gridOptions=go,
        theme="streamlit",
        height=600
    )

with col2:
    st.subheader("")


# In[ ]:





# In[ ]:




