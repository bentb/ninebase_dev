#!/usr/bin/env python
# coding: utf-8

# # ninebase Home Page

# In[2]:


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


# In[3]:


from st_pages import show_pages_from_config, add_page_title

# Either this or add_indentation() MUST be called on each page in your
# app to add indentation in the sidebar
add_page_title("")

show_pages_from_config()


# In[5]:


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


# In[6]:


add_logo()


# In[7]:


import streamlit as st
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


# In[8]:





# In[9]:


st.markdown("")
st.markdown("")
st.markdown("")


# In[10]:


from PIL import Image

header_img = Image.open('assets/cards_at_mets.jpg')


# In[ ]:


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




