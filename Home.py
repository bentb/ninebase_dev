#!/usr/bin/env python
# coding: utf-8

# # ninebase Home Page

# In[1]:


import streamlit as st
st.set_page_config(
    page_title="ninebase",
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


### Menu Structure


# In[ ]:


# Import the page modules
from player.batting import batting_page
#from player.pitching import pitching_page
#from player.fielding import fielding_page
#from references.data_dictionary import data_dictionary_page
#from references.box_plots import box_plots_page


# In[2]:


# Define the sections
st.sidebar.title('Player')
st.sidebar.button('Batting', on_click=batting_page)
st.sidebar.button('Pitching', on_click=pitching_page)
#st.sidebar.button('Fielding', on_click=fielding_page)

#st.sidebar.title('References')
#st.sidebar.button('Data Dictionary', on_click=data_dictionary_page)
#st.sidebar.button('Box Plots', on_click=box_plots_page)


# In[ ]:





# In[ ]:


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


# In[ ]:


add_logo()


# In[ ]:


from datetime import datetime

def countdown_to_playoffs():
    # Get the current date
    now = datetime.now().date()

    # Set the target date as October 3rd
    target_date = datetime(now.year, 10, 3).date()

    # Calculate the remaining days
    remaining_days = (target_date - now).days

    # Customize the countdown style
    countdown_style = f"<p style='text-align: right; color: #164f5e; font-size: 18px; padding: 0; margin: 0;'>Days until playoffs: <span style='font-size: 32px;'>{remaining_days}</span></p>"

    # Display the countdown
    st.markdown(countdown_style, unsafe_allow_html=True)


# st.markdown(
#     """
#     <style>
#         body {
#             display: flex;
#             flex-direction: row;
#             justify-content: center;
#             align-items: flex-start;
#             height: 100vh;
#             margin: 0;
#         }
# 
#         .title {
#             font-size: 46px;
#             font-weight: bold;
#             margin-bottom: 6px;
#             font-family: Lato, sans-serif;
#             color: #164f5e;
#         }
# 
#         .description {
#             font-size: 24px;
#             margin-bottom: 5px;
#             font-family: Lato, sans-serif;
#         }
#     </style>
#     """,
#     unsafe_allow_html=True
# )

# In[9]:


st.markdown("")
st.markdown("")
st.markdown("")


# In[10]:


from PIL import Image

header_img = Image.open('assets/cards_at_mets.jpg')


# In[11]:


col1, col2, col3 = st.columns([2, 6, 2])

with col1:
    st.write("#")

with col2:
    col2_content = st.container()
    with col2_content:
        st.image('assets/cards_at_mets.jpg')
        st.divider()

with col3:
    st.write("#")


# In[ ]:





# In[ ]:





# In[ ]:




