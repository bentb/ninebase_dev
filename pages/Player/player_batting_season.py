{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "adc17684",
   "metadata": {},
   "source": [
    "sources:\n",
    "docs.streamlit.io/library/get-started"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "47dd150c",
   "metadata": {},
   "source": [
    "# Introduction"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 80,
   "id": "2f035944",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Import Libraries\n",
    "import numpy as np\n",
    "import pandas as pd\n",
    "\n",
    "pd.set_option(\"display.precision\", 2)\n",
    "pd.set_option('display.max_rows', None)\n",
    "pd.set_option('display.max_columns', None)\n",
    "pd.set_option('display.float_format', lambda x: '%.5f' % x)\n",
    "from pandas.api.types import (\n",
    "    is_categorical_dtype,\n",
    "    is_datetime64_any_dtype,\n",
    "    is_numeric_dtype,\n",
    "    is_object_dtype,\n",
    ")\n",
    "\n",
    "import plotly.figure_factory as ff"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "f0b15390",
   "metadata": {},
   "source": [
    "## Streamlit"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 81,
   "id": "44929fa4",
   "metadata": {},
   "outputs": [],
   "source": [
    "import streamlit as st"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 82,
   "id": "078c4e1b",
   "metadata": {},
   "outputs": [],
   "source": [
    "st.set_page_config(\n",
    "    page_title=\"Player Batting\",\n",
    "    page_icon=\"⚾\",\n",
    "    layout=\"wide\",\n",
    "    initial_sidebar_state=\"expanded\",\n",
    "    menu_items={\n",
    "        'Report a bug': 'https://www.extremelycoolapp.com/help',\n",
    "        'Get help': \"https://www.extremelycoolapp.com/bug\",\n",
    "        'About': \"# This is a header. This is an *extremely* cool app!\"\n",
    "    }\n",
    ")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 83,
   "id": "b94f7696",
   "metadata": {},
   "outputs": [],
   "source": [
    "def add_logo():\n",
    "    st.markdown(\n",
    "        \"\"\"\n",
    "        <style>\n",
    "            [data-testid=\"stSidebarNav\"] {\n",
    "                background-image: url(https://i.imgur.com/sLSMBYJ.png);\n",
    "                background-repeat: no-repeat;\n",
    "                padding-top: 40px;\n",
    "                background-position: 20px 20px;\n",
    "            }\n",
    "            [data-testid=\"stSidebarNav\"]::before {\n",
    "                content: \"Navigation Menu\";\n",
    "                margin-left: 20px;\n",
    "                margin-top: 20px;\n",
    "                font-size: 26px;\n",
    "                position: relative;\n",
    "                top: 100px;\n",
    "            }\n",
    "        </style>\n",
    "        \"\"\",\n",
    "        unsafe_allow_html=True,\n",
    "    )"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 84,
   "id": "3fbe1638",
   "metadata": {},
   "outputs": [],
   "source": [
    "add_logo()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "72eb6105",
   "metadata": {},
   "source": [
    "## Load Data"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "ba1672fc",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Format for GitHub\n",
    "df = pd.read_csv('data_storage/player_batting_season.csv')\n",
    "\n",
    "# Format for Jupyter Notebook\n",
    "#df = pd.read_csv('C:/Users/b7tbu/NINEBASE/ninebase/data_storage/player_batting_season.csv')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 85,
   "id": "19b215a4",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>IDfg</th>\n",
       "      <th>Season</th>\n",
       "      <th>Name</th>\n",
       "      <th>Team</th>\n",
       "      <th>Age</th>\n",
       "      <th>G</th>\n",
       "      <th>AB</th>\n",
       "      <th>PA</th>\n",
       "      <th>H</th>\n",
       "      <th>1B</th>\n",
       "      <th>2B</th>\n",
       "      <th>3B</th>\n",
       "      <th>HR</th>\n",
       "      <th>R</th>\n",
       "      <th>RBI</th>\n",
       "      <th>BB</th>\n",
       "      <th>IBB</th>\n",
       "      <th>SO</th>\n",
       "      <th>HBP</th>\n",
       "      <th>SF</th>\n",
       "      <th>SH</th>\n",
       "      <th>GDP</th>\n",
       "      <th>SB</th>\n",
       "      <th>CS</th>\n",
       "      <th>AVG</th>\n",
       "      <th>GB</th>\n",
       "      <th>FB</th>\n",
       "      <th>LD</th>\n",
       "      <th>IFFB</th>\n",
       "      <th>Pitches</th>\n",
       "      <th>Balls</th>\n",
       "      <th>Strikes</th>\n",
       "      <th>IFH</th>\n",
       "      <th>BU</th>\n",
       "      <th>BUH</th>\n",
       "      <th>BB%</th>\n",
       "      <th>K%</th>\n",
       "      <th>BB/K</th>\n",
       "      <th>OBP</th>\n",
       "      <th>SLG</th>\n",
       "      <th>OPS</th>\n",
       "      <th>ISO</th>\n",
       "      <th>BABIP</th>\n",
       "      <th>GB/FB</th>\n",
       "      <th>LD%</th>\n",
       "      <th>GB%</th>\n",
       "      <th>FB%</th>\n",
       "      <th>IFFB%</th>\n",
       "      <th>HR/FB</th>\n",
       "      <th>IFH%</th>\n",
       "      <th>BUH%</th>\n",
       "      <th>wOBA</th>\n",
       "      <th>wRAA</th>\n",
       "      <th>wRC</th>\n",
       "      <th>Bat</th>\n",
       "      <th>Fld</th>\n",
       "      <th>Rep</th>\n",
       "      <th>Pos</th>\n",
       "      <th>RAR</th>\n",
       "      <th>WAR</th>\n",
       "      <th>Dol</th>\n",
       "      <th>Spd</th>\n",
       "      <th>wRC+</th>\n",
       "      <th>WPA</th>\n",
       "      <th>-WPA</th>\n",
       "      <th>+WPA</th>\n",
       "      <th>RE24</th>\n",
       "      <th>REW</th>\n",
       "      <th>pLI</th>\n",
       "      <th>phLI</th>\n",
       "      <th>PH</th>\n",
       "      <th>WPA/LI</th>\n",
       "      <th>Clutch</th>\n",
       "      <th>FB% (Pitch)</th>\n",
       "      <th>FBv</th>\n",
       "      <th>SL%</th>\n",
       "      <th>SLv</th>\n",
       "      <th>CT%</th>\n",
       "      <th>CTv</th>\n",
       "      <th>CB%</th>\n",
       "      <th>CBv</th>\n",
       "      <th>CH%</th>\n",
       "      <th>CHv</th>\n",
       "      <th>SF%</th>\n",
       "      <th>SFv</th>\n",
       "      <th>KN%</th>\n",
       "      <th>KNv</th>\n",
       "      <th>XX%</th>\n",
       "      <th>PO%</th>\n",
       "      <th>wFB</th>\n",
       "      <th>wSL</th>\n",
       "      <th>wCT</th>\n",
       "      <th>wCB</th>\n",
       "      <th>wCH</th>\n",
       "      <th>wSF</th>\n",
       "      <th>wKN</th>\n",
       "      <th>wFB/C</th>\n",
       "      <th>wSL/C</th>\n",
       "      <th>wCT/C</th>\n",
       "      <th>wCB/C</th>\n",
       "      <th>wCH/C</th>\n",
       "      <th>wSF/C</th>\n",
       "      <th>wKN/C</th>\n",
       "      <th>O-Swing%</th>\n",
       "      <th>Z-Swing%</th>\n",
       "      <th>Swing%</th>\n",
       "      <th>O-Contact%</th>\n",
       "      <th>Z-Contact%</th>\n",
       "      <th>Contact%</th>\n",
       "      <th>Zone%</th>\n",
       "      <th>F-Strike%</th>\n",
       "      <th>SwStr%</th>\n",
       "      <th>BsR</th>\n",
       "      <th>FA% (sc)</th>\n",
       "      <th>FT% (sc)</th>\n",
       "      <th>FC% (sc)</th>\n",
       "      <th>FS% (sc)</th>\n",
       "      <th>FO% (sc)</th>\n",
       "      <th>SI% (sc)</th>\n",
       "      <th>SL% (sc)</th>\n",
       "      <th>CU% (sc)</th>\n",
       "      <th>KC% (sc)</th>\n",
       "      <th>EP% (sc)</th>\n",
       "      <th>CH% (sc)</th>\n",
       "      <th>SC% (sc)</th>\n",
       "      <th>KN% (sc)</th>\n",
       "      <th>UN% (sc)</th>\n",
       "      <th>vFA (sc)</th>\n",
       "      <th>vFT (sc)</th>\n",
       "      <th>vFC (sc)</th>\n",
       "      <th>vFS (sc)</th>\n",
       "      <th>vFO (sc)</th>\n",
       "      <th>vSI (sc)</th>\n",
       "      <th>vSL (sc)</th>\n",
       "      <th>vCU (sc)</th>\n",
       "      <th>vKC (sc)</th>\n",
       "      <th>vEP (sc)</th>\n",
       "      <th>vCH (sc)</th>\n",
       "      <th>vSC (sc)</th>\n",
       "      <th>vKN (sc)</th>\n",
       "      <th>FA-X (sc)</th>\n",
       "      <th>FT-X (sc)</th>\n",
       "      <th>FC-X (sc)</th>\n",
       "      <th>FS-X (sc)</th>\n",
       "      <th>FO-X (sc)</th>\n",
       "      <th>SI-X (sc)</th>\n",
       "      <th>SL-X (sc)</th>\n",
       "      <th>CU-X (sc)</th>\n",
       "      <th>KC-X (sc)</th>\n",
       "      <th>EP-X (sc)</th>\n",
       "      <th>CH-X (sc)</th>\n",
       "      <th>SC-X (sc)</th>\n",
       "      <th>KN-X (sc)</th>\n",
       "      <th>FA-Z (sc)</th>\n",
       "      <th>FT-Z (sc)</th>\n",
       "      <th>FC-Z (sc)</th>\n",
       "      <th>FS-Z (sc)</th>\n",
       "      <th>FO-Z (sc)</th>\n",
       "      <th>SI-Z (sc)</th>\n",
       "      <th>SL-Z (sc)</th>\n",
       "      <th>CU-Z (sc)</th>\n",
       "      <th>KC-Z (sc)</th>\n",
       "      <th>EP-Z (sc)</th>\n",
       "      <th>CH-Z (sc)</th>\n",
       "      <th>SC-Z (sc)</th>\n",
       "      <th>KN-Z (sc)</th>\n",
       "      <th>wFA (sc)</th>\n",
       "      <th>wFT (sc)</th>\n",
       "      <th>wFC (sc)</th>\n",
       "      <th>wFS (sc)</th>\n",
       "      <th>wFO (sc)</th>\n",
       "      <th>wSI (sc)</th>\n",
       "      <th>wSL (sc)</th>\n",
       "      <th>wCU (sc)</th>\n",
       "      <th>wKC (sc)</th>\n",
       "      <th>wEP (sc)</th>\n",
       "      <th>wCH (sc)</th>\n",
       "      <th>wSC (sc)</th>\n",
       "      <th>wKN (sc)</th>\n",
       "      <th>wFA/C (sc)</th>\n",
       "      <th>wFT/C (sc)</th>\n",
       "      <th>wFC/C (sc)</th>\n",
       "      <th>wFS/C (sc)</th>\n",
       "      <th>wFO/C (sc)</th>\n",
       "      <th>wSI/C (sc)</th>\n",
       "      <th>wSL/C (sc)</th>\n",
       "      <th>wCU/C (sc)</th>\n",
       "      <th>wKC/C (sc)</th>\n",
       "      <th>wEP/C (sc)</th>\n",
       "      <th>wCH/C (sc)</th>\n",
       "      <th>wSC/C (sc)</th>\n",
       "      <th>wKN/C (sc)</th>\n",
       "      <th>O-Swing% (sc)</th>\n",
       "      <th>Z-Swing% (sc)</th>\n",
       "      <th>Swing% (sc)</th>\n",
       "      <th>O-Contact% (sc)</th>\n",
       "      <th>Z-Contact% (sc)</th>\n",
       "      <th>Contact% (sc)</th>\n",
       "      <th>Zone% (sc)</th>\n",
       "      <th>Pace</th>\n",
       "      <th>Def</th>\n",
       "      <th>wSB</th>\n",
       "      <th>UBR</th>\n",
       "      <th>Age Rng</th>\n",
       "      <th>Off</th>\n",
       "      <th>Lg</th>\n",
       "      <th>wGDP</th>\n",
       "      <th>Pull%</th>\n",
       "      <th>Cent%</th>\n",
       "      <th>Oppo%</th>\n",
       "      <th>Soft%</th>\n",
       "      <th>Med%</th>\n",
       "      <th>Hard%</th>\n",
       "      <th>TTO%</th>\n",
       "      <th>CH% (pi)</th>\n",
       "      <th>CS% (pi)</th>\n",
       "      <th>CU% (pi)</th>\n",
       "      <th>FA% (pi)</th>\n",
       "      <th>FC% (pi)</th>\n",
       "      <th>FS% (pi)</th>\n",
       "      <th>KN% (pi)</th>\n",
       "      <th>SB% (pi)</th>\n",
       "      <th>SI% (pi)</th>\n",
       "      <th>SL% (pi)</th>\n",
       "      <th>XX% (pi)</th>\n",
       "      <th>vCH (pi)</th>\n",
       "      <th>vCS (pi)</th>\n",
       "      <th>vCU (pi)</th>\n",
       "      <th>vFA (pi)</th>\n",
       "      <th>vFC (pi)</th>\n",
       "      <th>vFS (pi)</th>\n",
       "      <th>vKN (pi)</th>\n",
       "      <th>vSB (pi)</th>\n",
       "      <th>vSI (pi)</th>\n",
       "      <th>vSL (pi)</th>\n",
       "      <th>vXX (pi)</th>\n",
       "      <th>CH-X (pi)</th>\n",
       "      <th>CS-X (pi)</th>\n",
       "      <th>CU-X (pi)</th>\n",
       "      <th>FA-X (pi)</th>\n",
       "      <th>FC-X (pi)</th>\n",
       "      <th>FS-X (pi)</th>\n",
       "      <th>KN-X (pi)</th>\n",
       "      <th>SB-X (pi)</th>\n",
       "      <th>SI-X (pi)</th>\n",
       "      <th>SL-X (pi)</th>\n",
       "      <th>XX-X (pi)</th>\n",
       "      <th>CH-Z (pi)</th>\n",
       "      <th>CS-Z (pi)</th>\n",
       "      <th>CU-Z (pi)</th>\n",
       "      <th>FA-Z (pi)</th>\n",
       "      <th>FC-Z (pi)</th>\n",
       "      <th>FS-Z (pi)</th>\n",
       "      <th>KN-Z (pi)</th>\n",
       "      <th>SB-Z (pi)</th>\n",
       "      <th>SI-Z (pi)</th>\n",
       "      <th>SL-Z (pi)</th>\n",
       "      <th>XX-Z (pi)</th>\n",
       "      <th>wCH (pi)</th>\n",
       "      <th>wCS (pi)</th>\n",
       "      <th>wCU (pi)</th>\n",
       "      <th>wFA (pi)</th>\n",
       "      <th>wFC (pi)</th>\n",
       "      <th>wFS (pi)</th>\n",
       "      <th>wKN (pi)</th>\n",
       "      <th>wSB (pi)</th>\n",
       "      <th>wSI (pi)</th>\n",
       "      <th>wSL (pi)</th>\n",
       "      <th>wXX (pi)</th>\n",
       "      <th>wCH/C (pi)</th>\n",
       "      <th>wCS/C (pi)</th>\n",
       "      <th>wCU/C (pi)</th>\n",
       "      <th>wFA/C (pi)</th>\n",
       "      <th>wFC/C (pi)</th>\n",
       "      <th>wFS/C (pi)</th>\n",
       "      <th>wKN/C (pi)</th>\n",
       "      <th>wSB/C (pi)</th>\n",
       "      <th>wSI/C (pi)</th>\n",
       "      <th>wSL/C (pi)</th>\n",
       "      <th>wXX/C (pi)</th>\n",
       "      <th>O-Swing% (pi)</th>\n",
       "      <th>Z-Swing% (pi)</th>\n",
       "      <th>Swing% (pi)</th>\n",
       "      <th>O-Contact% (pi)</th>\n",
       "      <th>Z-Contact% (pi)</th>\n",
       "      <th>Contact% (pi)</th>\n",
       "      <th>Zone% (pi)</th>\n",
       "      <th>Pace (pi)</th>\n",
       "      <th>FRM</th>\n",
       "      <th>AVG+</th>\n",
       "      <th>BB%+</th>\n",
       "      <th>K%+</th>\n",
       "      <th>OBP+</th>\n",
       "      <th>SLG+</th>\n",
       "      <th>ISO+</th>\n",
       "      <th>BABIP+</th>\n",
       "      <th>LD+%</th>\n",
       "      <th>GB%+</th>\n",
       "      <th>FB%+</th>\n",
       "      <th>HR/FB%+</th>\n",
       "      <th>Pull%+</th>\n",
       "      <th>Cent%+</th>\n",
       "      <th>Oppo%+</th>\n",
       "      <th>Soft%+</th>\n",
       "      <th>Med%+</th>\n",
       "      <th>Hard%+</th>\n",
       "      <th>EV</th>\n",
       "      <th>LA</th>\n",
       "      <th>Barrels</th>\n",
       "      <th>Barrel%</th>\n",
       "      <th>maxEV</th>\n",
       "      <th>HardHit</th>\n",
       "      <th>HardHit%</th>\n",
       "      <th>Events</th>\n",
       "      <th>CStr%</th>\n",
       "      <th>CSW%</th>\n",
       "      <th>xBA</th>\n",
       "      <th>xSLG</th>\n",
       "      <th>xwOBA</th>\n",
       "      <th>L-WAR</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>18401</td>\n",
       "      <td>2023</td>\n",
       "      <td>Ronald Acuna Jr.</td>\n",
       "      <td>ATL</td>\n",
       "      <td>25</td>\n",
       "      <td>86</td>\n",
       "      <td>347</td>\n",
       "      <td>396</td>\n",
       "      <td>117</td>\n",
       "      <td>71</td>\n",
       "      <td>24</td>\n",
       "      <td>1</td>\n",
       "      <td>21</td>\n",
       "      <td>78</td>\n",
       "      <td>54</td>\n",
       "      <td>43</td>\n",
       "      <td>2</td>\n",
       "      <td>49</td>\n",
       "      <td>4</td>\n",
       "      <td>2</td>\n",
       "      <td>0</td>\n",
       "      <td>7</td>\n",
       "      <td>41</td>\n",
       "      <td>7</td>\n",
       "      <td>0.33700</td>\n",
       "      <td>150</td>\n",
       "      <td>91</td>\n",
       "      <td>59</td>\n",
       "      <td>6</td>\n",
       "      <td>1528</td>\n",
       "      <td>617</td>\n",
       "      <td>911</td>\n",
       "      <td>16</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0.10900</td>\n",
       "      <td>0.12400</td>\n",
       "      <td>0.88000</td>\n",
       "      <td>0.41400</td>\n",
       "      <td>0.59400</td>\n",
       "      <td>1.00800</td>\n",
       "      <td>0.25600</td>\n",
       "      <td>0.34400</td>\n",
       "      <td>0.01650</td>\n",
       "      <td>0.19700</td>\n",
       "      <td>0.50000</td>\n",
       "      <td>0.30300</td>\n",
       "      <td>0.06600</td>\n",
       "      <td>0.23100</td>\n",
       "      <td>0.10700</td>\n",
       "      <td>0.00000</td>\n",
       "      <td>0.42700</td>\n",
       "      <td>35.50000</td>\n",
       "      <td>83</td>\n",
       "      <td>33.50000</td>\n",
       "      <td>0.30000</td>\n",
       "      <td>12.20000</td>\n",
       "      <td>-3.90000</td>\n",
       "      <td>48.70000</td>\n",
       "      <td>4.90000</td>\n",
       "      <td>$39.0</td>\n",
       "      <td>6.80000</td>\n",
       "      <td>168</td>\n",
       "      <td>3.67000</td>\n",
       "      <td>-5.24000</td>\n",
       "      <td>8.91000</td>\n",
       "      <td>42.05000</td>\n",
       "      <td>4.33000</td>\n",
       "      <td>0.90000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>0</td>\n",
       "      <td>3.65000</td>\n",
       "      <td>0.43000</td>\n",
       "      <td>0.50100</td>\n",
       "      <td>93.70000</td>\n",
       "      <td>0.23200</td>\n",
       "      <td>85.10000</td>\n",
       "      <td>0.06200</td>\n",
       "      <td>89.30000</td>\n",
       "      <td>0.08200</td>\n",
       "      <td>80.00000</td>\n",
       "      <td>0.09600</td>\n",
       "      <td>85.40000</td>\n",
       "      <td>0.02700</td>\n",
       "      <td>85.00000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>0.00800</td>\n",
       "      <td>NaN</td>\n",
       "      <td>17.40000</td>\n",
       "      <td>11.30000</td>\n",
       "      <td>1.00000</td>\n",
       "      <td>6.40000</td>\n",
       "      <td>-0.90000</td>\n",
       "      <td>2.30000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>2.28000</td>\n",
       "      <td>3.20000</td>\n",
       "      <td>1.09000</td>\n",
       "      <td>5.09000</td>\n",
       "      <td>-0.61000</td>\n",
       "      <td>5.73000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>0.26700</td>\n",
       "      <td>0.72100</td>\n",
       "      <td>0.45600</td>\n",
       "      <td>0.72700</td>\n",
       "      <td>0.87100</td>\n",
       "      <td>0.82200</td>\n",
       "      <td>0.41600</td>\n",
       "      <td>0.58300</td>\n",
       "      <td>0.08100</td>\n",
       "      <td>5.40000</td>\n",
       "      <td>0.30400</td>\n",
       "      <td>NaN</td>\n",
       "      <td>0.06100</td>\n",
       "      <td>0.02300</td>\n",
       "      <td>0.00200</td>\n",
       "      <td>0.19100</td>\n",
       "      <td>0.23300</td>\n",
       "      <td>0.06100</td>\n",
       "      <td>0.02200</td>\n",
       "      <td>0.00300</td>\n",
       "      <td>0.09800</td>\n",
       "      <td>0.00100</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>94.00000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>89.40000</td>\n",
       "      <td>84.70000</td>\n",
       "      <td>81.40000</td>\n",
       "      <td>94.10000</td>\n",
       "      <td>85.10000</td>\n",
       "      <td>79.10000</td>\n",
       "      <td>81.90000</td>\n",
       "      <td>54.20000</td>\n",
       "      <td>85.60000</td>\n",
       "      <td>81.30000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>-2.30000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>0.50000</td>\n",
       "      <td>-4.90000</td>\n",
       "      <td>-6.10000</td>\n",
       "      <td>-7.00000</td>\n",
       "      <td>1.90000</td>\n",
       "      <td>1.70000</td>\n",
       "      <td>3.30000</td>\n",
       "      <td>-3.90000</td>\n",
       "      <td>-1.60000</td>\n",
       "      <td>-7.00000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>9.10000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>5.00000</td>\n",
       "      <td>1.80000</td>\n",
       "      <td>-0.20000</td>\n",
       "      <td>5.20000</td>\n",
       "      <td>1.30000</td>\n",
       "      <td>-5.50000</td>\n",
       "      <td>-5.50000</td>\n",
       "      <td>6.90000</td>\n",
       "      <td>3.80000</td>\n",
       "      <td>-2.60000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>12.90000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>0.50000</td>\n",
       "      <td>1.90000</td>\n",
       "      <td>0.00000</td>\n",
       "      <td>4.00000</td>\n",
       "      <td>9.40000</td>\n",
       "      <td>5.50000</td>\n",
       "      <td>0.50000</td>\n",
       "      <td>0.40000</td>\n",
       "      <td>-0.40000</td>\n",
       "      <td>0.10000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>2.78000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>0.57000</td>\n",
       "      <td>5.45000</td>\n",
       "      <td>0.29000</td>\n",
       "      <td>1.37000</td>\n",
       "      <td>2.64000</td>\n",
       "      <td>5.94000</td>\n",
       "      <td>1.37000</td>\n",
       "      <td>10.70000</td>\n",
       "      <td>-0.30000</td>\n",
       "      <td>4.27000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>0.23100</td>\n",
       "      <td>0.67800</td>\n",
       "      <td>0.45700</td>\n",
       "      <td>0.66100</td>\n",
       "      <td>0.87300</td>\n",
       "      <td>0.82000</td>\n",
       "      <td>0.50600</td>\n",
       "      <td>18.10000</td>\n",
       "      <td>-3.60000</td>\n",
       "      <td>4.40000</td>\n",
       "      <td>1.70000</td>\n",
       "      <td>25 - 25</td>\n",
       "      <td>38.90000</td>\n",
       "      <td>1.20000</td>\n",
       "      <td>-0.70000</td>\n",
       "      <td>0.45700</td>\n",
       "      <td>0.33300</td>\n",
       "      <td>0.21000</td>\n",
       "      <td>0.10000</td>\n",
       "      <td>0.46000</td>\n",
       "      <td>0.44000</td>\n",
       "      <td>0.28500</td>\n",
       "      <td>0.09900</td>\n",
       "      <td>NaN</td>\n",
       "      <td>0.08100</td>\n",
       "      <td>0.29700</td>\n",
       "      <td>0.06100</td>\n",
       "      <td>0.02700</td>\n",
       "      <td>NaN</td>\n",
       "      <td>0.00100</td>\n",
       "      <td>0.19800</td>\n",
       "      <td>0.23700</td>\n",
       "      <td>NaN</td>\n",
       "      <td>85.40000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>79.60000</td>\n",
       "      <td>94.10000</td>\n",
       "      <td>89.60000</td>\n",
       "      <td>84.80000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>81.90000</td>\n",
       "      <td>94.40000</td>\n",
       "      <td>85.30000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>-1.50000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>2.90000</td>\n",
       "      <td>-1.90000</td>\n",
       "      <td>0.70000</td>\n",
       "      <td>-4.70000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>-6.60000</td>\n",
       "      <td>-6.80000</td>\n",
       "      <td>2.30000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>2.50000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>-7.30000</td>\n",
       "      <td>8.20000</td>\n",
       "      <td>3.90000</td>\n",
       "      <td>0.50000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>-4.10000</td>\n",
       "      <td>4.20000</td>\n",
       "      <td>0.10000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>-0.30000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>4.10000</td>\n",
       "      <td>12.80000</td>\n",
       "      <td>0.90000</td>\n",
       "      <td>2.00000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>0.10000</td>\n",
       "      <td>3.90000</td>\n",
       "      <td>10.50000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>-0.20000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>3.34000</td>\n",
       "      <td>2.87000</td>\n",
       "      <td>0.96000</td>\n",
       "      <td>4.97000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>4.27000</td>\n",
       "      <td>1.31000</td>\n",
       "      <td>2.93000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>0.22600</td>\n",
       "      <td>0.67500</td>\n",
       "      <td>0.45600</td>\n",
       "      <td>0.65100</td>\n",
       "      <td>0.87700</td>\n",
       "      <td>0.82200</td>\n",
       "      <td>0.51200</td>\n",
       "      <td>18.10000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>134</td>\n",
       "      <td>122</td>\n",
       "      <td>55</td>\n",
       "      <td>128</td>\n",
       "      <td>143</td>\n",
       "      <td>157</td>\n",
       "      <td>114</td>\n",
       "      <td>0.97000</td>\n",
       "      <td>116</td>\n",
       "      <td>82</td>\n",
       "      <td>184</td>\n",
       "      <td>112</td>\n",
       "      <td>97</td>\n",
       "      <td>85</td>\n",
       "      <td>64</td>\n",
       "      <td>89</td>\n",
       "      <td>135</td>\n",
       "      <td>94.90000</td>\n",
       "      <td>7.80000</td>\n",
       "      <td>47</td>\n",
       "      <td>0.15700</td>\n",
       "      <td>116.70000</td>\n",
       "      <td>165</td>\n",
       "      <td>0.55000</td>\n",
       "      <td>300</td>\n",
       "      <td>0.14000</td>\n",
       "      <td>0.22100</td>\n",
       "      <td>0.35400</td>\n",
       "      <td>0.65900</td>\n",
       "      <td>0.46100</td>\n",
       "      <td>4.80000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>19755</td>\n",
       "      <td>2023</td>\n",
       "      <td>Shohei Ohtani</td>\n",
       "      <td>LAA</td>\n",
       "      <td>28</td>\n",
       "      <td>87</td>\n",
       "      <td>334</td>\n",
       "      <td>389</td>\n",
       "      <td>99</td>\n",
       "      <td>48</td>\n",
       "      <td>15</td>\n",
       "      <td>5</td>\n",
       "      <td>31</td>\n",
       "      <td>61</td>\n",
       "      <td>68</td>\n",
       "      <td>47</td>\n",
       "      <td>4</td>\n",
       "      <td>86</td>\n",
       "      <td>1</td>\n",
       "      <td>2</td>\n",
       "      <td>0</td>\n",
       "      <td>7</td>\n",
       "      <td>11</td>\n",
       "      <td>4</td>\n",
       "      <td>0.29600</td>\n",
       "      <td>110</td>\n",
       "      <td>102</td>\n",
       "      <td>38</td>\n",
       "      <td>6</td>\n",
       "      <td>1541</td>\n",
       "      <td>604</td>\n",
       "      <td>937</td>\n",
       "      <td>7</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0.12100</td>\n",
       "      <td>0.22100</td>\n",
       "      <td>0.55000</td>\n",
       "      <td>0.38300</td>\n",
       "      <td>0.65000</td>\n",
       "      <td>1.03300</td>\n",
       "      <td>0.35300</td>\n",
       "      <td>0.31100</td>\n",
       "      <td>0.01080</td>\n",
       "      <td>0.15200</td>\n",
       "      <td>0.44000</td>\n",
       "      <td>0.40800</td>\n",
       "      <td>0.05900</td>\n",
       "      <td>0.30400</td>\n",
       "      <td>0.06400</td>\n",
       "      <td>0.00000</td>\n",
       "      <td>0.42700</td>\n",
       "      <td>34.90000</td>\n",
       "      <td>82</td>\n",
       "      <td>35.20000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>12.00000</td>\n",
       "      <td>-9.40000</td>\n",
       "      <td>39.50000</td>\n",
       "      <td>4.00000</td>\n",
       "      <td>$31.7</td>\n",
       "      <td>6.20000</td>\n",
       "      <td>177</td>\n",
       "      <td>2.92000</td>\n",
       "      <td>-6.26000</td>\n",
       "      <td>9.18000</td>\n",
       "      <td>36.48000</td>\n",
       "      <td>3.81000</td>\n",
       "      <td>1.03000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>0</td>\n",
       "      <td>3.71000</td>\n",
       "      <td>-0.88000</td>\n",
       "      <td>0.40600</td>\n",
       "      <td>94.50000</td>\n",
       "      <td>0.21700</td>\n",
       "      <td>84.60000</td>\n",
       "      <td>0.10800</td>\n",
       "      <td>89.70000</td>\n",
       "      <td>0.08600</td>\n",
       "      <td>80.30000</td>\n",
       "      <td>0.14100</td>\n",
       "      <td>86.20000</td>\n",
       "      <td>0.04200</td>\n",
       "      <td>87.50000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>0.01400</td>\n",
       "      <td>NaN</td>\n",
       "      <td>12.90000</td>\n",
       "      <td>6.90000</td>\n",
       "      <td>3.50000</td>\n",
       "      <td>4.50000</td>\n",
       "      <td>5.00000</td>\n",
       "      <td>1.20000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>2.07000</td>\n",
       "      <td>2.08000</td>\n",
       "      <td>2.12000</td>\n",
       "      <td>3.43000</td>\n",
       "      <td>2.28000</td>\n",
       "      <td>1.80000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>0.33300</td>\n",
       "      <td>0.69200</td>\n",
       "      <td>0.47600</td>\n",
       "      <td>0.60200</td>\n",
       "      <td>0.79600</td>\n",
       "      <td>0.71400</td>\n",
       "      <td>0.39600</td>\n",
       "      <td>0.58400</td>\n",
       "      <td>0.13600</td>\n",
       "      <td>0.60000</td>\n",
       "      <td>0.30400</td>\n",
       "      <td>NaN</td>\n",
       "      <td>0.11100</td>\n",
       "      <td>0.04300</td>\n",
       "      <td>NaN</td>\n",
       "      <td>0.09700</td>\n",
       "      <td>0.21700</td>\n",
       "      <td>0.06800</td>\n",
       "      <td>0.02000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>0.14000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>94.70000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>89.90000</td>\n",
       "      <td>87.20000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>93.70000</td>\n",
       "      <td>84.80000</td>\n",
       "      <td>79.60000</td>\n",
       "      <td>81.00000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>86.20000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>-2.00000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>0.30000</td>\n",
       "      <td>-7.20000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>-1.20000</td>\n",
       "      <td>0.70000</td>\n",
       "      <td>3.90000</td>\n",
       "      <td>2.90000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>-7.50000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>9.40000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>4.10000</td>\n",
       "      <td>2.00000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>5.10000</td>\n",
       "      <td>1.20000</td>\n",
       "      <td>-5.90000</td>\n",
       "      <td>-3.60000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>4.20000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>8.20000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>2.60000</td>\n",
       "      <td>1.90000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>4.70000</td>\n",
       "      <td>7.80000</td>\n",
       "      <td>4.30000</td>\n",
       "      <td>-0.10000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>4.20000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>1.75000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>1.52000</td>\n",
       "      <td>2.95000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>3.18000</td>\n",
       "      <td>2.35000</td>\n",
       "      <td>4.16000</td>\n",
       "      <td>-0.22000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>1.94000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>0.29800</td>\n",
       "      <td>0.68500</td>\n",
       "      <td>0.47900</td>\n",
       "      <td>0.52900</td>\n",
       "      <td>0.80700</td>\n",
       "      <td>0.71400</td>\n",
       "      <td>0.46700</td>\n",
       "      <td>18.70000</td>\n",
       "      <td>-9.40000</td>\n",
       "      <td>-0.20000</td>\n",
       "      <td>0.50000</td>\n",
       "      <td>28 - 28</td>\n",
       "      <td>35.80000</td>\n",
       "      <td>1.10000</td>\n",
       "      <td>0.30000</td>\n",
       "      <td>0.39600</td>\n",
       "      <td>0.35600</td>\n",
       "      <td>0.24800</td>\n",
       "      <td>0.10000</td>\n",
       "      <td>0.50000</td>\n",
       "      <td>0.40000</td>\n",
       "      <td>0.42200</td>\n",
       "      <td>0.14000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>0.08300</td>\n",
       "      <td>0.29400</td>\n",
       "      <td>0.10000</td>\n",
       "      <td>0.04200</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>0.10200</td>\n",
       "      <td>0.24000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>86.30000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>80.10000</td>\n",
       "      <td>94.60000</td>\n",
       "      <td>90.70000</td>\n",
       "      <td>87.00000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>94.10000</td>\n",
       "      <td>84.70000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>-7.30000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>3.50000</td>\n",
       "      <td>-1.70000</td>\n",
       "      <td>1.20000</td>\n",
       "      <td>-6.70000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>-1.80000</td>\n",
       "      <td>0.60000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>2.80000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>-7.20000</td>\n",
       "      <td>8.50000</td>\n",
       "      <td>3.90000</td>\n",
       "      <td>0.70000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>4.10000</td>\n",
       "      <td>-0.40000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>4.10000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>4.50000</td>\n",
       "      <td>6.50000</td>\n",
       "      <td>1.90000</td>\n",
       "      <td>1.50000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>5.40000</td>\n",
       "      <td>7.90000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>1.92000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>3.53000</td>\n",
       "      <td>1.44000</td>\n",
       "      <td>1.21000</td>\n",
       "      <td>2.36000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>3.45000</td>\n",
       "      <td>2.15000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>0.29700</td>\n",
       "      <td>0.67900</td>\n",
       "      <td>0.47900</td>\n",
       "      <td>0.51900</td>\n",
       "      <td>0.80800</td>\n",
       "      <td>0.71400</td>\n",
       "      <td>0.47500</td>\n",
       "      <td>18.70000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>121</td>\n",
       "      <td>144</td>\n",
       "      <td>97</td>\n",
       "      <td>121</td>\n",
       "      <td>160</td>\n",
       "      <td>220</td>\n",
       "      <td>105</td>\n",
       "      <td>0.76000</td>\n",
       "      <td>104</td>\n",
       "      <td>108</td>\n",
       "      <td>252</td>\n",
       "      <td>97</td>\n",
       "      <td>103</td>\n",
       "      <td>102</td>\n",
       "      <td>65</td>\n",
       "      <td>95</td>\n",
       "      <td>124</td>\n",
       "      <td>93.70000</td>\n",
       "      <td>13.10000</td>\n",
       "      <td>46</td>\n",
       "      <td>0.18000</td>\n",
       "      <td>117.10000</td>\n",
       "      <td>130</td>\n",
       "      <td>0.51000</td>\n",
       "      <td>255</td>\n",
       "      <td>0.13000</td>\n",
       "      <td>0.26500</td>\n",
       "      <td>0.29100</td>\n",
       "      <td>0.64100</td>\n",
       "      <td>0.42600</td>\n",
       "      <td>4.00000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>13611</td>\n",
       "      <td>2023</td>\n",
       "      <td>Mookie Betts</td>\n",
       "      <td>LAD</td>\n",
       "      <td>30</td>\n",
       "      <td>84</td>\n",
       "      <td>325</td>\n",
       "      <td>386</td>\n",
       "      <td>88</td>\n",
       "      <td>42</td>\n",
       "      <td>22</td>\n",
       "      <td>1</td>\n",
       "      <td>23</td>\n",
       "      <td>68</td>\n",
       "      <td>57</td>\n",
       "      <td>52</td>\n",
       "      <td>0</td>\n",
       "      <td>64</td>\n",
       "      <td>4</td>\n",
       "      <td>5</td>\n",
       "      <td>0</td>\n",
       "      <td>4</td>\n",
       "      <td>7</td>\n",
       "      <td>2</td>\n",
       "      <td>0.27100</td>\n",
       "      <td>79</td>\n",
       "      <td>130</td>\n",
       "      <td>57</td>\n",
       "      <td>12</td>\n",
       "      <td>1482</td>\n",
       "      <td>620</td>\n",
       "      <td>862</td>\n",
       "      <td>5</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0.13500</td>\n",
       "      <td>0.16600</td>\n",
       "      <td>0.81000</td>\n",
       "      <td>0.37300</td>\n",
       "      <td>0.55700</td>\n",
       "      <td>0.93000</td>\n",
       "      <td>0.28600</td>\n",
       "      <td>0.26700</td>\n",
       "      <td>0.00610</td>\n",
       "      <td>0.21400</td>\n",
       "      <td>0.29700</td>\n",
       "      <td>0.48900</td>\n",
       "      <td>0.09200</td>\n",
       "      <td>0.17700</td>\n",
       "      <td>0.06300</td>\n",
       "      <td>0.00000</td>\n",
       "      <td>0.39300</td>\n",
       "      <td>23.80000</td>\n",
       "      <td>71</td>\n",
       "      <td>23.80000</td>\n",
       "      <td>0.30000</td>\n",
       "      <td>11.90000</td>\n",
       "      <td>-1.70000</td>\n",
       "      <td>38.10000</td>\n",
       "      <td>3.80000</td>\n",
       "      <td>$30.6</td>\n",
       "      <td>4.90000</td>\n",
       "      <td>150</td>\n",
       "      <td>2.73000</td>\n",
       "      <td>-5.84000</td>\n",
       "      <td>8.56000</td>\n",
       "      <td>28.67000</td>\n",
       "      <td>2.91000</td>\n",
       "      <td>0.97000</td>\n",
       "      <td>1.14000</td>\n",
       "      <td>1</td>\n",
       "      <td>2.89000</td>\n",
       "      <td>-0.07000</td>\n",
       "      <td>0.53500</td>\n",
       "      <td>94.00000</td>\n",
       "      <td>0.23100</td>\n",
       "      <td>84.80000</td>\n",
       "      <td>0.08100</td>\n",
       "      <td>88.50000</td>\n",
       "      <td>0.07100</td>\n",
       "      <td>79.90000</td>\n",
       "      <td>0.06500</td>\n",
       "      <td>86.20000</td>\n",
       "      <td>0.01800</td>\n",
       "      <td>89.20000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>0.00300</td>\n",
       "      <td>NaN</td>\n",
       "      <td>16.30000</td>\n",
       "      <td>6.80000</td>\n",
       "      <td>-0.20000</td>\n",
       "      <td>2.40000</td>\n",
       "      <td>1.80000</td>\n",
       "      <td>-0.70000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>2.06000</td>\n",
       "      <td>1.99000</td>\n",
       "      <td>-0.21000</td>\n",
       "      <td>2.33000</td>\n",
       "      <td>1.82000</td>\n",
       "      <td>-2.72000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>0.19400</td>\n",
       "      <td>0.63300</td>\n",
       "      <td>0.38200</td>\n",
       "      <td>0.60400</td>\n",
       "      <td>0.93500</td>\n",
       "      <td>0.83900</td>\n",
       "      <td>0.42800</td>\n",
       "      <td>0.56200</td>\n",
       "      <td>0.06100</td>\n",
       "      <td>2.60000</td>\n",
       "      <td>0.32000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>0.09600</td>\n",
       "      <td>0.02000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>0.20900</td>\n",
       "      <td>0.22000</td>\n",
       "      <td>0.04800</td>\n",
       "      <td>0.02200</td>\n",
       "      <td>NaN</td>\n",
       "      <td>0.06400</td>\n",
       "      <td>0.00100</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>94.20000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>88.70000</td>\n",
       "      <td>89.60000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>93.40000</td>\n",
       "      <td>84.50000</td>\n",
       "      <td>79.60000</td>\n",
       "      <td>80.60000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>86.00000</td>\n",
       "      <td>79.90000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>-2.60000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>0.50000</td>\n",
       "      <td>-6.80000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>-4.70000</td>\n",
       "      <td>2.60000</td>\n",
       "      <td>0.90000</td>\n",
       "      <td>3.60000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>-1.90000</td>\n",
       "      <td>-6.20000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>9.20000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>4.20000</td>\n",
       "      <td>2.60000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>5.00000</td>\n",
       "      <td>1.30000</td>\n",
       "      <td>-4.30000</td>\n",
       "      <td>-4.60000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>3.50000</td>\n",
       "      <td>-0.30000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>7.10000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>-1.00000</td>\n",
       "      <td>0.50000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>9.60000</td>\n",
       "      <td>8.10000</td>\n",
       "      <td>-0.20000</td>\n",
       "      <td>2.20000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>0.10000</td>\n",
       "      <td>-0.20000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>1.50000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>-0.69000</td>\n",
       "      <td>1.67000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>3.09000</td>\n",
       "      <td>2.49000</td>\n",
       "      <td>-0.24000</td>\n",
       "      <td>6.62000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>0.10000</td>\n",
       "      <td>-15.92000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>0.17600</td>\n",
       "      <td>0.59300</td>\n",
       "      <td>0.38200</td>\n",
       "      <td>0.52700</td>\n",
       "      <td>0.93500</td>\n",
       "      <td>0.84000</td>\n",
       "      <td>0.49400</td>\n",
       "      <td>17.70000</td>\n",
       "      <td>-1.40000</td>\n",
       "      <td>-0.20000</td>\n",
       "      <td>2.50000</td>\n",
       "      <td>30 - 30</td>\n",
       "      <td>26.50000</td>\n",
       "      <td>1.10000</td>\n",
       "      <td>0.30000</td>\n",
       "      <td>0.47700</td>\n",
       "      <td>0.35300</td>\n",
       "      <td>0.16900</td>\n",
       "      <td>0.09800</td>\n",
       "      <td>0.46600</td>\n",
       "      <td>0.43600</td>\n",
       "      <td>0.36000</td>\n",
       "      <td>0.06300</td>\n",
       "      <td>NaN</td>\n",
       "      <td>0.06500</td>\n",
       "      <td>0.31800</td>\n",
       "      <td>0.08900</td>\n",
       "      <td>0.01700</td>\n",
       "      <td>NaN</td>\n",
       "      <td>0.00100</td>\n",
       "      <td>0.21400</td>\n",
       "      <td>0.23400</td>\n",
       "      <td>NaN</td>\n",
       "      <td>86.10000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>79.90000</td>\n",
       "      <td>94.40000</td>\n",
       "      <td>88.90000</td>\n",
       "      <td>88.30000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>80.10000</td>\n",
       "      <td>93.50000</td>\n",
       "      <td>84.70000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>-1.60000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>2.80000</td>\n",
       "      <td>-2.10000</td>\n",
       "      <td>0.80000</td>\n",
       "      <td>-6.10000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>-5.30000</td>\n",
       "      <td>-4.50000</td>\n",
       "      <td>3.20000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>2.30000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>-6.30000</td>\n",
       "      <td>8.20000</td>\n",
       "      <td>3.60000</td>\n",
       "      <td>1.30000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>-2.30000</td>\n",
       "      <td>3.90000</td>\n",
       "      <td>0.10000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>-0.20000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>2.20000</td>\n",
       "      <td>7.40000</td>\n",
       "      <td>-1.00000</td>\n",
       "      <td>0.30000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>-0.20000</td>\n",
       "      <td>10.30000</td>\n",
       "      <td>7.80000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>-0.25000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>2.29000</td>\n",
       "      <td>1.58000</td>\n",
       "      <td>-0.78000</td>\n",
       "      <td>1.07000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>-15.92000</td>\n",
       "      <td>3.26000</td>\n",
       "      <td>2.26000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>0.17200</td>\n",
       "      <td>0.59200</td>\n",
       "      <td>0.38100</td>\n",
       "      <td>0.54300</td>\n",
       "      <td>0.93100</td>\n",
       "      <td>0.84300</td>\n",
       "      <td>0.49800</td>\n",
       "      <td>17.70000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>108</td>\n",
       "      <td>152</td>\n",
       "      <td>74</td>\n",
       "      <td>115</td>\n",
       "      <td>134</td>\n",
       "      <td>176</td>\n",
       "      <td>89</td>\n",
       "      <td>1.06000</td>\n",
       "      <td>69</td>\n",
       "      <td>133</td>\n",
       "      <td>141</td>\n",
       "      <td>117</td>\n",
       "      <td>102</td>\n",
       "      <td>69</td>\n",
       "      <td>63</td>\n",
       "      <td>90</td>\n",
       "      <td>134</td>\n",
       "      <td>92.40000</td>\n",
       "      <td>19.60000</td>\n",
       "      <td>32</td>\n",
       "      <td>0.12000</td>\n",
       "      <td>110.10000</td>\n",
       "      <td>129</td>\n",
       "      <td>0.48500</td>\n",
       "      <td>266</td>\n",
       "      <td>0.20000</td>\n",
       "      <td>0.26100</td>\n",
       "      <td>0.28000</td>\n",
       "      <td>0.55700</td>\n",
       "      <td>0.40300</td>\n",
       "      <td>3.80000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>23667</td>\n",
       "      <td>2023</td>\n",
       "      <td>Wander Franco</td>\n",
       "      <td>TBR</td>\n",
       "      <td>22</td>\n",
       "      <td>83</td>\n",
       "      <td>331</td>\n",
       "      <td>366</td>\n",
       "      <td>94</td>\n",
       "      <td>59</td>\n",
       "      <td>21</td>\n",
       "      <td>4</td>\n",
       "      <td>10</td>\n",
       "      <td>47</td>\n",
       "      <td>43</td>\n",
       "      <td>29</td>\n",
       "      <td>2</td>\n",
       "      <td>49</td>\n",
       "      <td>2</td>\n",
       "      <td>4</td>\n",
       "      <td>0</td>\n",
       "      <td>12</td>\n",
       "      <td>28</td>\n",
       "      <td>8</td>\n",
       "      <td>0.28400</td>\n",
       "      <td>138</td>\n",
       "      <td>79</td>\n",
       "      <td>69</td>\n",
       "      <td>8</td>\n",
       "      <td>1419</td>\n",
       "      <td>526</td>\n",
       "      <td>893</td>\n",
       "      <td>7</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0.07900</td>\n",
       "      <td>0.13400</td>\n",
       "      <td>0.59000</td>\n",
       "      <td>0.34200</td>\n",
       "      <td>0.46200</td>\n",
       "      <td>0.80400</td>\n",
       "      <td>0.17800</td>\n",
       "      <td>0.30400</td>\n",
       "      <td>0.01750</td>\n",
       "      <td>0.24100</td>\n",
       "      <td>0.48300</td>\n",
       "      <td>0.27600</td>\n",
       "      <td>0.10100</td>\n",
       "      <td>0.12700</td>\n",
       "      <td>0.05100</td>\n",
       "      <td>0.00000</td>\n",
       "      <td>0.34400</td>\n",
       "      <td>7.70000</td>\n",
       "      <td>52</td>\n",
       "      <td>11.00000</td>\n",
       "      <td>9.20000</td>\n",
       "      <td>11.30000</td>\n",
       "      <td>3.50000</td>\n",
       "      <td>38.00000</td>\n",
       "      <td>3.80000</td>\n",
       "      <td>$30.5</td>\n",
       "      <td>7.20000</td>\n",
       "      <td>125</td>\n",
       "      <td>0.59000</td>\n",
       "      <td>-5.56000</td>\n",
       "      <td>6.15000</td>\n",
       "      <td>13.35000</td>\n",
       "      <td>1.49000</td>\n",
       "      <td>0.89000</td>\n",
       "      <td>1.46000</td>\n",
       "      <td>2</td>\n",
       "      <td>1.37000</td>\n",
       "      <td>-0.70000</td>\n",
       "      <td>0.41200</td>\n",
       "      <td>93.80000</td>\n",
       "      <td>0.17400</td>\n",
       "      <td>84.50000</td>\n",
       "      <td>0.09100</td>\n",
       "      <td>89.30000</td>\n",
       "      <td>0.09300</td>\n",
       "      <td>80.50000</td>\n",
       "      <td>0.19900</td>\n",
       "      <td>85.70000</td>\n",
       "      <td>0.03100</td>\n",
       "      <td>87.30000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>0.00800</td>\n",
       "      <td>NaN</td>\n",
       "      <td>11.00000</td>\n",
       "      <td>5.10000</td>\n",
       "      <td>-1.50000</td>\n",
       "      <td>-2.00000</td>\n",
       "      <td>-0.90000</td>\n",
       "      <td>-2.20000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>1.89000</td>\n",
       "      <td>2.07000</td>\n",
       "      <td>-1.17000</td>\n",
       "      <td>-1.54000</td>\n",
       "      <td>-0.30000</td>\n",
       "      <td>-4.97000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>0.29300</td>\n",
       "      <td>0.63900</td>\n",
       "      <td>0.44600</td>\n",
       "      <td>0.80100</td>\n",
       "      <td>0.92000</td>\n",
       "      <td>0.87700</td>\n",
       "      <td>0.44400</td>\n",
       "      <td>0.63400</td>\n",
       "      <td>0.05500</td>\n",
       "      <td>2.00000</td>\n",
       "      <td>0.28700</td>\n",
       "      <td>NaN</td>\n",
       "      <td>0.09300</td>\n",
       "      <td>0.02500</td>\n",
       "      <td>0.00400</td>\n",
       "      <td>0.12600</td>\n",
       "      <td>0.16700</td>\n",
       "      <td>0.07600</td>\n",
       "      <td>0.02200</td>\n",
       "      <td>NaN</td>\n",
       "      <td>0.20100</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>93.80000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>89.20000</td>\n",
       "      <td>87.10000</td>\n",
       "      <td>85.20000</td>\n",
       "      <td>93.60000</td>\n",
       "      <td>84.40000</td>\n",
       "      <td>79.90000</td>\n",
       "      <td>82.80000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>85.70000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>-2.50000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>0.60000</td>\n",
       "      <td>-7.50000</td>\n",
       "      <td>-6.50000</td>\n",
       "      <td>-4.50000</td>\n",
       "      <td>2.60000</td>\n",
       "      <td>2.30000</td>\n",
       "      <td>3.00000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>-5.90000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>9.60000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>5.20000</td>\n",
       "      <td>2.30000</td>\n",
       "      <td>1.50000</td>\n",
       "      <td>5.30000</td>\n",
       "      <td>0.90000</td>\n",
       "      <td>-5.20000</td>\n",
       "      <td>-5.80000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>3.60000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>9.40000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>-0.10000</td>\n",
       "      <td>-1.80000</td>\n",
       "      <td>-0.10000</td>\n",
       "      <td>1.50000</td>\n",
       "      <td>2.00000</td>\n",
       "      <td>-0.50000</td>\n",
       "      <td>0.00000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>-1.30000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>2.32000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>-0.10000</td>\n",
       "      <td>-5.12000</td>\n",
       "      <td>-2.12000</td>\n",
       "      <td>0.84000</td>\n",
       "      <td>0.86000</td>\n",
       "      <td>-0.46000</td>\n",
       "      <td>-0.11000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>-0.46000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>0.25600</td>\n",
       "      <td>0.61300</td>\n",
       "      <td>0.44500</td>\n",
       "      <td>0.74700</td>\n",
       "      <td>0.92200</td>\n",
       "      <td>0.87500</td>\n",
       "      <td>0.53100</td>\n",
       "      <td>18.80000</td>\n",
       "      <td>12.70000</td>\n",
       "      <td>1.60000</td>\n",
       "      <td>0.70000</td>\n",
       "      <td>22 - 22</td>\n",
       "      <td>13.00000</td>\n",
       "      <td>1.00000</td>\n",
       "      <td>-0.30000</td>\n",
       "      <td>0.41600</td>\n",
       "      <td>0.35000</td>\n",
       "      <td>0.23400</td>\n",
       "      <td>0.14000</td>\n",
       "      <td>0.51000</td>\n",
       "      <td>0.35000</td>\n",
       "      <td>0.24000</td>\n",
       "      <td>0.20400</td>\n",
       "      <td>NaN</td>\n",
       "      <td>0.08300</td>\n",
       "      <td>0.28700</td>\n",
       "      <td>0.09300</td>\n",
       "      <td>0.02600</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>0.12100</td>\n",
       "      <td>0.18500</td>\n",
       "      <td>NaN</td>\n",
       "      <td>86.00000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>80.60000</td>\n",
       "      <td>94.10000</td>\n",
       "      <td>89.70000</td>\n",
       "      <td>87.00000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>93.80000</td>\n",
       "      <td>84.50000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>-5.60000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>3.40000</td>\n",
       "      <td>-2.30000</td>\n",
       "      <td>1.00000</td>\n",
       "      <td>-6.90000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>-4.20000</td>\n",
       "      <td>2.80000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>2.10000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>-7.80000</td>\n",
       "      <td>8.60000</td>\n",
       "      <td>4.20000</td>\n",
       "      <td>1.10000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>4.00000</td>\n",
       "      <td>-0.50000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>-2.00000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>-1.20000</td>\n",
       "      <td>9.10000</td>\n",
       "      <td>-0.40000</td>\n",
       "      <td>-1.30000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>1.40000</td>\n",
       "      <td>3.30000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>-0.69000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>-1.04000</td>\n",
       "      <td>2.24000</td>\n",
       "      <td>-0.30000</td>\n",
       "      <td>-3.63000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>0.84000</td>\n",
       "      <td>1.26000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>0.25600</td>\n",
       "      <td>0.60900</td>\n",
       "      <td>0.44500</td>\n",
       "      <td>0.76300</td>\n",
       "      <td>0.91600</td>\n",
       "      <td>0.87500</td>\n",
       "      <td>0.53500</td>\n",
       "      <td>18.80000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>116</td>\n",
       "      <td>95</td>\n",
       "      <td>59</td>\n",
       "      <td>108</td>\n",
       "      <td>114</td>\n",
       "      <td>111</td>\n",
       "      <td>103</td>\n",
       "      <td>1.20000</td>\n",
       "      <td>115</td>\n",
       "      <td>73</td>\n",
       "      <td>105</td>\n",
       "      <td>102</td>\n",
       "      <td>101</td>\n",
       "      <td>96</td>\n",
       "      <td>91</td>\n",
       "      <td>97</td>\n",
       "      <td>109</td>\n",
       "      <td>88.90000</td>\n",
       "      <td>8.30000</td>\n",
       "      <td>18</td>\n",
       "      <td>0.06300</td>\n",
       "      <td>111.00000</td>\n",
       "      <td>112</td>\n",
       "      <td>0.39200</td>\n",
       "      <td>286</td>\n",
       "      <td>0.18200</td>\n",
       "      <td>0.23700</td>\n",
       "      <td>0.29200</td>\n",
       "      <td>0.45100</td>\n",
       "      <td>0.34900</td>\n",
       "      <td>3.10000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>25878</td>\n",
       "      <td>2023</td>\n",
       "      <td>Corbin Carroll</td>\n",
       "      <td>ARI</td>\n",
       "      <td>22</td>\n",
       "      <td>83</td>\n",
       "      <td>297</td>\n",
       "      <td>335</td>\n",
       "      <td>86</td>\n",
       "      <td>45</td>\n",
       "      <td>20</td>\n",
       "      <td>3</td>\n",
       "      <td>18</td>\n",
       "      <td>61</td>\n",
       "      <td>46</td>\n",
       "      <td>30</td>\n",
       "      <td>1</td>\n",
       "      <td>66</td>\n",
       "      <td>6</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>3</td>\n",
       "      <td>24</td>\n",
       "      <td>2</td>\n",
       "      <td>0.29000</td>\n",
       "      <td>105</td>\n",
       "      <td>85</td>\n",
       "      <td>38</td>\n",
       "      <td>9</td>\n",
       "      <td>1293</td>\n",
       "      <td>487</td>\n",
       "      <td>806</td>\n",
       "      <td>6</td>\n",
       "      <td>5</td>\n",
       "      <td>2</td>\n",
       "      <td>0.09000</td>\n",
       "      <td>0.19700</td>\n",
       "      <td>0.45000</td>\n",
       "      <td>0.36500</td>\n",
       "      <td>0.55900</td>\n",
       "      <td>0.92400</td>\n",
       "      <td>0.26900</td>\n",
       "      <td>0.31800</td>\n",
       "      <td>0.01240</td>\n",
       "      <td>0.16700</td>\n",
       "      <td>0.46100</td>\n",
       "      <td>0.37300</td>\n",
       "      <td>0.10600</td>\n",
       "      <td>0.21200</td>\n",
       "      <td>0.05700</td>\n",
       "      <td>0.40000</td>\n",
       "      <td>0.39200</td>\n",
       "      <td>20.30000</td>\n",
       "      <td>61</td>\n",
       "      <td>18.80000</td>\n",
       "      <td>0.70000</td>\n",
       "      <td>10.40000</td>\n",
       "      <td>-2.60000</td>\n",
       "      <td>36.50000</td>\n",
       "      <td>3.70000</td>\n",
       "      <td>$29.3</td>\n",
       "      <td>8.30000</td>\n",
       "      <td>145</td>\n",
       "      <td>2.81000</td>\n",
       "      <td>-4.71000</td>\n",
       "      <td>7.52000</td>\n",
       "      <td>26.36000</td>\n",
       "      <td>2.75000</td>\n",
       "      <td>0.98000</td>\n",
       "      <td>1.30000</td>\n",
       "      <td>3</td>\n",
       "      <td>2.64000</td>\n",
       "      <td>0.24000</td>\n",
       "      <td>0.46300</td>\n",
       "      <td>94.00000</td>\n",
       "      <td>0.21300</td>\n",
       "      <td>83.80000</td>\n",
       "      <td>0.10000</td>\n",
       "      <td>90.60000</td>\n",
       "      <td>0.10000</td>\n",
       "      <td>80.20000</td>\n",
       "      <td>0.10100</td>\n",
       "      <td>86.60000</td>\n",
       "      <td>0.02400</td>\n",
       "      <td>86.20000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>0.00400</td>\n",
       "      <td>NaN</td>\n",
       "      <td>20.40000</td>\n",
       "      <td>3.70000</td>\n",
       "      <td>-3.00000</td>\n",
       "      <td>-0.20000</td>\n",
       "      <td>-1.20000</td>\n",
       "      <td>1.10000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>3.41000</td>\n",
       "      <td>1.36000</td>\n",
       "      <td>-2.30000</td>\n",
       "      <td>-0.14000</td>\n",
       "      <td>-0.90000</td>\n",
       "      <td>3.41000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>0.29200</td>\n",
       "      <td>0.67100</td>\n",
       "      <td>0.44800</td>\n",
       "      <td>0.73000</td>\n",
       "      <td>0.86300</td>\n",
       "      <td>0.81200</td>\n",
       "      <td>0.41200</td>\n",
       "      <td>0.53400</td>\n",
       "      <td>0.08400</td>\n",
       "      <td>8.30000</td>\n",
       "      <td>0.31100</td>\n",
       "      <td>NaN</td>\n",
       "      <td>0.08700</td>\n",
       "      <td>0.01900</td>\n",
       "      <td>0.00400</td>\n",
       "      <td>0.15300</td>\n",
       "      <td>0.21900</td>\n",
       "      <td>0.08900</td>\n",
       "      <td>0.01800</td>\n",
       "      <td>NaN</td>\n",
       "      <td>0.09800</td>\n",
       "      <td>0.00200</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>94.30000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>90.60000</td>\n",
       "      <td>87.40000</td>\n",
       "      <td>85.30000</td>\n",
       "      <td>93.30000</td>\n",
       "      <td>84.30000</td>\n",
       "      <td>79.80000</td>\n",
       "      <td>80.10000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>86.30000</td>\n",
       "      <td>82.30000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>-2.60000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>0.20000</td>\n",
       "      <td>-7.10000</td>\n",
       "      <td>-4.90000</td>\n",
       "      <td>-3.20000</td>\n",
       "      <td>1.20000</td>\n",
       "      <td>3.80000</td>\n",
       "      <td>5.00000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>-6.80000</td>\n",
       "      <td>-8.90000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>9.10000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>5.20000</td>\n",
       "      <td>2.30000</td>\n",
       "      <td>0.90000</td>\n",
       "      <td>4.30000</td>\n",
       "      <td>1.30000</td>\n",
       "      <td>-4.70000</td>\n",
       "      <td>-5.70000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>3.50000</td>\n",
       "      <td>-0.40000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>10.10000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>-2.40000</td>\n",
       "      <td>0.40000</td>\n",
       "      <td>-0.10000</td>\n",
       "      <td>10.10000</td>\n",
       "      <td>2.80000</td>\n",
       "      <td>-0.80000</td>\n",
       "      <td>0.60000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>-1.50000</td>\n",
       "      <td>1.30000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>2.51000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>-2.13000</td>\n",
       "      <td>1.77000</td>\n",
       "      <td>-1.81000</td>\n",
       "      <td>5.11000</td>\n",
       "      <td>1.00000</td>\n",
       "      <td>-0.67000</td>\n",
       "      <td>2.80000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>-1.15000</td>\n",
       "      <td>62.60000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>0.27700</td>\n",
       "      <td>0.62600</td>\n",
       "      <td>0.44800</td>\n",
       "      <td>0.69200</td>\n",
       "      <td>0.86900</td>\n",
       "      <td>0.81300</td>\n",
       "      <td>0.49100</td>\n",
       "      <td>18.40000</td>\n",
       "      <td>-1.90000</td>\n",
       "      <td>3.40000</td>\n",
       "      <td>3.80000</td>\n",
       "      <td>22 - 22</td>\n",
       "      <td>27.10000</td>\n",
       "      <td>1.00000</td>\n",
       "      <td>1.10000</td>\n",
       "      <td>0.43800</td>\n",
       "      <td>0.30500</td>\n",
       "      <td>0.25800</td>\n",
       "      <td>0.12000</td>\n",
       "      <td>0.55400</td>\n",
       "      <td>0.32600</td>\n",
       "      <td>0.34000</td>\n",
       "      <td>0.09100</td>\n",
       "      <td>0.00100</td>\n",
       "      <td>0.09500</td>\n",
       "      <td>0.31000</td>\n",
       "      <td>0.09500</td>\n",
       "      <td>0.02900</td>\n",
       "      <td>NaN</td>\n",
       "      <td>0.00200</td>\n",
       "      <td>0.14600</td>\n",
       "      <td>0.23000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>86.20000</td>\n",
       "      <td>77.40000</td>\n",
       "      <td>80.00000</td>\n",
       "      <td>94.30000</td>\n",
       "      <td>90.80000</td>\n",
       "      <td>87.30000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>82.80000</td>\n",
       "      <td>93.50000</td>\n",
       "      <td>84.10000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>-6.80000</td>\n",
       "      <td>7.00000</td>\n",
       "      <td>5.20000</td>\n",
       "      <td>-2.20000</td>\n",
       "      <td>0.80000</td>\n",
       "      <td>-5.90000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>-8.30000</td>\n",
       "      <td>-3.20000</td>\n",
       "      <td>1.20000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>2.10000</td>\n",
       "      <td>-10.50000</td>\n",
       "      <td>-6.90000</td>\n",
       "      <td>8.10000</td>\n",
       "      <td>4.40000</td>\n",
       "      <td>1.20000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>-2.40000</td>\n",
       "      <td>3.10000</td>\n",
       "      <td>0.00000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>-1.20000</td>\n",
       "      <td>0.00000</td>\n",
       "      <td>0.00000</td>\n",
       "      <td>10.80000</td>\n",
       "      <td>-2.40000</td>\n",
       "      <td>-0.10000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>1.30000</td>\n",
       "      <td>8.90000</td>\n",
       "      <td>3.20000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>-1.00000</td>\n",
       "      <td>3.61000</td>\n",
       "      <td>0.04000</td>\n",
       "      <td>2.71000</td>\n",
       "      <td>-1.96000</td>\n",
       "      <td>-0.19000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>62.60000</td>\n",
       "      <td>4.71000</td>\n",
       "      <td>1.09000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>0.27700</td>\n",
       "      <td>0.62500</td>\n",
       "      <td>0.44800</td>\n",
       "      <td>0.69800</td>\n",
       "      <td>0.86600</td>\n",
       "      <td>0.81300</td>\n",
       "      <td>0.49100</td>\n",
       "      <td>18.40000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>115</td>\n",
       "      <td>101</td>\n",
       "      <td>88</td>\n",
       "      <td>113</td>\n",
       "      <td>135</td>\n",
       "      <td>165</td>\n",
       "      <td>106</td>\n",
       "      <td>0.82000</td>\n",
       "      <td>107</td>\n",
       "      <td>101</td>\n",
       "      <td>169</td>\n",
       "      <td>107</td>\n",
       "      <td>88</td>\n",
       "      <td>105</td>\n",
       "      <td>77</td>\n",
       "      <td>107</td>\n",
       "      <td>100</td>\n",
       "      <td>90.70000</td>\n",
       "      <td>11.80000</td>\n",
       "      <td>22</td>\n",
       "      <td>0.09400</td>\n",
       "      <td>113.80000</td>\n",
       "      <td>101</td>\n",
       "      <td>0.43300</td>\n",
       "      <td>233</td>\n",
       "      <td>0.17500</td>\n",
       "      <td>0.25900</td>\n",
       "      <td>0.26100</td>\n",
       "      <td>0.45300</td>\n",
       "      <td>0.34700</td>\n",
       "      <td>3.50000</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "    IDfg  Season              Name Team  Age   G   AB   PA    H  1B  2B  3B  \\\n",
       "0  18401    2023  Ronald Acuna Jr.  ATL   25  86  347  396  117  71  24   1   \n",
       "1  19755    2023     Shohei Ohtani  LAA   28  87  334  389   99  48  15   5   \n",
       "2  13611    2023      Mookie Betts  LAD   30  84  325  386   88  42  22   1   \n",
       "3  23667    2023     Wander Franco  TBR   22  83  331  366   94  59  21   4   \n",
       "4  25878    2023    Corbin Carroll  ARI   22  83  297  335   86  45  20   3   \n",
       "\n",
       "   HR   R  RBI  BB  IBB  SO  HBP  SF  SH  GDP  SB  CS     AVG   GB   FB  LD  \\\n",
       "0  21  78   54  43    2  49    4   2   0    7  41   7 0.33700  150   91  59   \n",
       "1  31  61   68  47    4  86    1   2   0    7  11   4 0.29600  110  102  38   \n",
       "2  23  68   57  52    0  64    4   5   0    4   7   2 0.27100   79  130  57   \n",
       "3  10  47   43  29    2  49    2   4   0   12  28   8 0.28400  138   79  69   \n",
       "4  18  61   46  30    1  66    6   1   1    3  24   2 0.29000  105   85  38   \n",
       "\n",
       "   IFFB  Pitches  Balls  Strikes  IFH  BU  BUH     BB%      K%    BB/K  \\\n",
       "0     6     1528    617      911   16   0    0 0.10900 0.12400 0.88000   \n",
       "1     6     1541    604      937    7   0    0 0.12100 0.22100 0.55000   \n",
       "2    12     1482    620      862    5   0    0 0.13500 0.16600 0.81000   \n",
       "3     8     1419    526      893    7   0    0 0.07900 0.13400 0.59000   \n",
       "4     9     1293    487      806    6   5    2 0.09000 0.19700 0.45000   \n",
       "\n",
       "      OBP     SLG     OPS     ISO   BABIP   GB/FB     LD%     GB%     FB%  \\\n",
       "0 0.41400 0.59400 1.00800 0.25600 0.34400 0.01650 0.19700 0.50000 0.30300   \n",
       "1 0.38300 0.65000 1.03300 0.35300 0.31100 0.01080 0.15200 0.44000 0.40800   \n",
       "2 0.37300 0.55700 0.93000 0.28600 0.26700 0.00610 0.21400 0.29700 0.48900   \n",
       "3 0.34200 0.46200 0.80400 0.17800 0.30400 0.01750 0.24100 0.48300 0.27600   \n",
       "4 0.36500 0.55900 0.92400 0.26900 0.31800 0.01240 0.16700 0.46100 0.37300   \n",
       "\n",
       "    IFFB%   HR/FB    IFH%    BUH%    wOBA     wRAA  wRC      Bat     Fld  \\\n",
       "0 0.06600 0.23100 0.10700 0.00000 0.42700 35.50000   83 33.50000 0.30000   \n",
       "1 0.05900 0.30400 0.06400 0.00000 0.42700 34.90000   82 35.20000     NaN   \n",
       "2 0.09200 0.17700 0.06300 0.00000 0.39300 23.80000   71 23.80000 0.30000   \n",
       "3 0.10100 0.12700 0.05100 0.00000 0.34400  7.70000   52 11.00000 9.20000   \n",
       "4 0.10600 0.21200 0.05700 0.40000 0.39200 20.30000   61 18.80000 0.70000   \n",
       "\n",
       "       Rep      Pos      RAR     WAR    Dol     Spd  wRC+     WPA     -WPA  \\\n",
       "0 12.20000 -3.90000 48.70000 4.90000  $39.0 6.80000   168 3.67000 -5.24000   \n",
       "1 12.00000 -9.40000 39.50000 4.00000  $31.7 6.20000   177 2.92000 -6.26000   \n",
       "2 11.90000 -1.70000 38.10000 3.80000  $30.6 4.90000   150 2.73000 -5.84000   \n",
       "3 11.30000  3.50000 38.00000 3.80000  $30.5 7.20000   125 0.59000 -5.56000   \n",
       "4 10.40000 -2.60000 36.50000 3.70000  $29.3 8.30000   145 2.81000 -4.71000   \n",
       "\n",
       "     +WPA     RE24     REW     pLI    phLI  PH  WPA/LI   Clutch  FB% (Pitch)  \\\n",
       "0 8.91000 42.05000 4.33000 0.90000     NaN   0 3.65000  0.43000      0.50100   \n",
       "1 9.18000 36.48000 3.81000 1.03000     NaN   0 3.71000 -0.88000      0.40600   \n",
       "2 8.56000 28.67000 2.91000 0.97000 1.14000   1 2.89000 -0.07000      0.53500   \n",
       "3 6.15000 13.35000 1.49000 0.89000 1.46000   2 1.37000 -0.70000      0.41200   \n",
       "4 7.52000 26.36000 2.75000 0.98000 1.30000   3 2.64000  0.24000      0.46300   \n",
       "\n",
       "       FBv     SL%      SLv     CT%      CTv     CB%      CBv     CH%  \\\n",
       "0 93.70000 0.23200 85.10000 0.06200 89.30000 0.08200 80.00000 0.09600   \n",
       "1 94.50000 0.21700 84.60000 0.10800 89.70000 0.08600 80.30000 0.14100   \n",
       "2 94.00000 0.23100 84.80000 0.08100 88.50000 0.07100 79.90000 0.06500   \n",
       "3 93.80000 0.17400 84.50000 0.09100 89.30000 0.09300 80.50000 0.19900   \n",
       "4 94.00000 0.21300 83.80000 0.10000 90.60000 0.10000 80.20000 0.10100   \n",
       "\n",
       "       CHv     SF%      SFv  KN%  KNv     XX%  PO%      wFB      wSL      wCT  \\\n",
       "0 85.40000 0.02700 85.00000  NaN  NaN 0.00800  NaN 17.40000 11.30000  1.00000   \n",
       "1 86.20000 0.04200 87.50000  NaN  NaN 0.01400  NaN 12.90000  6.90000  3.50000   \n",
       "2 86.20000 0.01800 89.20000  NaN  NaN 0.00300  NaN 16.30000  6.80000 -0.20000   \n",
       "3 85.70000 0.03100 87.30000  NaN  NaN 0.00800  NaN 11.00000  5.10000 -1.50000   \n",
       "4 86.60000 0.02400 86.20000  NaN  NaN 0.00400  NaN 20.40000  3.70000 -3.00000   \n",
       "\n",
       "       wCB      wCH      wSF  wKN   wFB/C   wSL/C    wCT/C    wCB/C    wCH/C  \\\n",
       "0  6.40000 -0.90000  2.30000  NaN 2.28000 3.20000  1.09000  5.09000 -0.61000   \n",
       "1  4.50000  5.00000  1.20000  NaN 2.07000 2.08000  2.12000  3.43000  2.28000   \n",
       "2  2.40000  1.80000 -0.70000  NaN 2.06000 1.99000 -0.21000  2.33000  1.82000   \n",
       "3 -2.00000 -0.90000 -2.20000  NaN 1.89000 2.07000 -1.17000 -1.54000 -0.30000   \n",
       "4 -0.20000 -1.20000  1.10000  NaN 3.41000 1.36000 -2.30000 -0.14000 -0.90000   \n",
       "\n",
       "     wSF/C  wKN/C  O-Swing%  Z-Swing%  Swing%  O-Contact%  Z-Contact%  \\\n",
       "0  5.73000    NaN   0.26700   0.72100 0.45600     0.72700     0.87100   \n",
       "1  1.80000    NaN   0.33300   0.69200 0.47600     0.60200     0.79600   \n",
       "2 -2.72000    NaN   0.19400   0.63300 0.38200     0.60400     0.93500   \n",
       "3 -4.97000    NaN   0.29300   0.63900 0.44600     0.80100     0.92000   \n",
       "4  3.41000    NaN   0.29200   0.67100 0.44800     0.73000     0.86300   \n",
       "\n",
       "   Contact%   Zone%  F-Strike%  SwStr%     BsR  FA% (sc)  FT% (sc)  FC% (sc)  \\\n",
       "0   0.82200 0.41600    0.58300 0.08100 5.40000   0.30400       NaN   0.06100   \n",
       "1   0.71400 0.39600    0.58400 0.13600 0.60000   0.30400       NaN   0.11100   \n",
       "2   0.83900 0.42800    0.56200 0.06100 2.60000   0.32000       NaN   0.09600   \n",
       "3   0.87700 0.44400    0.63400 0.05500 2.00000   0.28700       NaN   0.09300   \n",
       "4   0.81200 0.41200    0.53400 0.08400 8.30000   0.31100       NaN   0.08700   \n",
       "\n",
       "   FS% (sc)  FO% (sc)  SI% (sc)  SL% (sc)  CU% (sc)  KC% (sc)  EP% (sc)  \\\n",
       "0   0.02300   0.00200   0.19100   0.23300   0.06100   0.02200   0.00300   \n",
       "1   0.04300       NaN   0.09700   0.21700   0.06800   0.02000       NaN   \n",
       "2   0.02000       NaN   0.20900   0.22000   0.04800   0.02200       NaN   \n",
       "3   0.02500   0.00400   0.12600   0.16700   0.07600   0.02200       NaN   \n",
       "4   0.01900   0.00400   0.15300   0.21900   0.08900   0.01800       NaN   \n",
       "\n",
       "   CH% (sc)  SC% (sc)  KN% (sc)  UN% (sc)  vFA (sc)  vFT (sc)  vFC (sc)  \\\n",
       "0   0.09800   0.00100       NaN       NaN  94.00000       NaN  89.40000   \n",
       "1   0.14000       NaN       NaN       NaN  94.70000       NaN  89.90000   \n",
       "2   0.06400   0.00100       NaN       NaN  94.20000       NaN  88.70000   \n",
       "3   0.20100       NaN       NaN       NaN  93.80000       NaN  89.20000   \n",
       "4   0.09800   0.00200       NaN       NaN  94.30000       NaN  90.60000   \n",
       "\n",
       "   vFS (sc)  vFO (sc)  vSI (sc)  vSL (sc)  vCU (sc)  vKC (sc)  vEP (sc)  \\\n",
       "0  84.70000  81.40000  94.10000  85.10000  79.10000  81.90000  54.20000   \n",
       "1  87.20000       NaN  93.70000  84.80000  79.60000  81.00000       NaN   \n",
       "2  89.60000       NaN  93.40000  84.50000  79.60000  80.60000       NaN   \n",
       "3  87.10000  85.20000  93.60000  84.40000  79.90000  82.80000       NaN   \n",
       "4  87.40000  85.30000  93.30000  84.30000  79.80000  80.10000       NaN   \n",
       "\n",
       "   vCH (sc)  vSC (sc)  vKN (sc)  FA-X (sc)  FT-X (sc)  FC-X (sc)  FS-X (sc)  \\\n",
       "0  85.60000  81.30000       NaN   -2.30000        NaN    0.50000   -4.90000   \n",
       "1  86.20000       NaN       NaN   -2.00000        NaN    0.30000   -7.20000   \n",
       "2  86.00000  79.90000       NaN   -2.60000        NaN    0.50000   -6.80000   \n",
       "3  85.70000       NaN       NaN   -2.50000        NaN    0.60000   -7.50000   \n",
       "4  86.30000  82.30000       NaN   -2.60000        NaN    0.20000   -7.10000   \n",
       "\n",
       "   FO-X (sc)  SI-X (sc)  SL-X (sc)  CU-X (sc)  KC-X (sc)  EP-X (sc)  \\\n",
       "0   -6.10000   -7.00000    1.90000    1.70000    3.30000   -3.90000   \n",
       "1        NaN   -1.20000    0.70000    3.90000    2.90000        NaN   \n",
       "2        NaN   -4.70000    2.60000    0.90000    3.60000        NaN   \n",
       "3   -6.50000   -4.50000    2.60000    2.30000    3.00000        NaN   \n",
       "4   -4.90000   -3.20000    1.20000    3.80000    5.00000        NaN   \n",
       "\n",
       "   CH-X (sc)  SC-X (sc)  KN-X (sc)  FA-Z (sc)  FT-Z (sc)  FC-Z (sc)  \\\n",
       "0   -1.60000   -7.00000        NaN    9.10000        NaN    5.00000   \n",
       "1   -7.50000        NaN        NaN    9.40000        NaN    4.10000   \n",
       "2   -1.90000   -6.20000        NaN    9.20000        NaN    4.20000   \n",
       "3   -5.90000        NaN        NaN    9.60000        NaN    5.20000   \n",
       "4   -6.80000   -8.90000        NaN    9.10000        NaN    5.20000   \n",
       "\n",
       "   FS-Z (sc)  FO-Z (sc)  SI-Z (sc)  SL-Z (sc)  CU-Z (sc)  KC-Z (sc)  \\\n",
       "0    1.80000   -0.20000    5.20000    1.30000   -5.50000   -5.50000   \n",
       "1    2.00000        NaN    5.10000    1.20000   -5.90000   -3.60000   \n",
       "2    2.60000        NaN    5.00000    1.30000   -4.30000   -4.60000   \n",
       "3    2.30000    1.50000    5.30000    0.90000   -5.20000   -5.80000   \n",
       "4    2.30000    0.90000    4.30000    1.30000   -4.70000   -5.70000   \n",
       "\n",
       "   EP-Z (sc)  CH-Z (sc)  SC-Z (sc)  KN-Z (sc)  wFA (sc)  wFT (sc)  wFC (sc)  \\\n",
       "0    6.90000    3.80000   -2.60000        NaN  12.90000       NaN   0.50000   \n",
       "1        NaN    4.20000        NaN        NaN   8.20000       NaN   2.60000   \n",
       "2        NaN    3.50000   -0.30000        NaN   7.10000       NaN  -1.00000   \n",
       "3        NaN    3.60000        NaN        NaN   9.40000       NaN  -0.10000   \n",
       "4        NaN    3.50000   -0.40000        NaN  10.10000       NaN  -2.40000   \n",
       "\n",
       "   wFS (sc)  wFO (sc)  wSI (sc)  wSL (sc)  wCU (sc)  wKC (sc)  wEP (sc)  \\\n",
       "0   1.90000   0.00000   4.00000   9.40000   5.50000   0.50000   0.40000   \n",
       "1   1.90000       NaN   4.70000   7.80000   4.30000  -0.10000       NaN   \n",
       "2   0.50000       NaN   9.60000   8.10000  -0.20000   2.20000       NaN   \n",
       "3  -1.80000  -0.10000   1.50000   2.00000  -0.50000   0.00000       NaN   \n",
       "4   0.40000  -0.10000  10.10000   2.80000  -0.80000   0.60000       NaN   \n",
       "\n",
       "   wCH (sc)  wSC (sc)  wKN (sc)  wFA/C (sc)  wFT/C (sc)  wFC/C (sc)  \\\n",
       "0  -0.40000   0.10000       NaN     2.78000         NaN     0.57000   \n",
       "1   4.20000       NaN       NaN     1.75000         NaN     1.52000   \n",
       "2   0.10000  -0.20000       NaN     1.50000         NaN    -0.69000   \n",
       "3  -1.30000       NaN       NaN     2.32000         NaN    -0.10000   \n",
       "4  -1.50000   1.30000       NaN     2.51000         NaN    -2.13000   \n",
       "\n",
       "   wFS/C (sc)  wFO/C (sc)  wSI/C (sc)  wSL/C (sc)  wCU/C (sc)  wKC/C (sc)  \\\n",
       "0     5.45000     0.29000     1.37000     2.64000     5.94000     1.37000   \n",
       "1     2.95000         NaN     3.18000     2.35000     4.16000    -0.22000   \n",
       "2     1.67000         NaN     3.09000     2.49000    -0.24000     6.62000   \n",
       "3    -5.12000    -2.12000     0.84000     0.86000    -0.46000    -0.11000   \n",
       "4     1.77000    -1.81000     5.11000     1.00000    -0.67000     2.80000   \n",
       "\n",
       "   wEP/C (sc)  wCH/C (sc)  wSC/C (sc)  wKN/C (sc)  O-Swing% (sc)  \\\n",
       "0    10.70000    -0.30000     4.27000         NaN        0.23100   \n",
       "1         NaN     1.94000         NaN         NaN        0.29800   \n",
       "2         NaN     0.10000   -15.92000         NaN        0.17600   \n",
       "3         NaN    -0.46000         NaN         NaN        0.25600   \n",
       "4         NaN    -1.15000    62.60000         NaN        0.27700   \n",
       "\n",
       "   Z-Swing% (sc)  Swing% (sc)  O-Contact% (sc)  Z-Contact% (sc)  \\\n",
       "0        0.67800      0.45700          0.66100          0.87300   \n",
       "1        0.68500      0.47900          0.52900          0.80700   \n",
       "2        0.59300      0.38200          0.52700          0.93500   \n",
       "3        0.61300      0.44500          0.74700          0.92200   \n",
       "4        0.62600      0.44800          0.69200          0.86900   \n",
       "\n",
       "   Contact% (sc)  Zone% (sc)     Pace      Def      wSB     UBR  Age Rng  \\\n",
       "0        0.82000     0.50600 18.10000 -3.60000  4.40000 1.70000  25 - 25   \n",
       "1        0.71400     0.46700 18.70000 -9.40000 -0.20000 0.50000  28 - 28   \n",
       "2        0.84000     0.49400 17.70000 -1.40000 -0.20000 2.50000  30 - 30   \n",
       "3        0.87500     0.53100 18.80000 12.70000  1.60000 0.70000  22 - 22   \n",
       "4        0.81300     0.49100 18.40000 -1.90000  3.40000 3.80000  22 - 22   \n",
       "\n",
       "       Off      Lg     wGDP   Pull%   Cent%   Oppo%   Soft%    Med%   Hard%  \\\n",
       "0 38.90000 1.20000 -0.70000 0.45700 0.33300 0.21000 0.10000 0.46000 0.44000   \n",
       "1 35.80000 1.10000  0.30000 0.39600 0.35600 0.24800 0.10000 0.50000 0.40000   \n",
       "2 26.50000 1.10000  0.30000 0.47700 0.35300 0.16900 0.09800 0.46600 0.43600   \n",
       "3 13.00000 1.00000 -0.30000 0.41600 0.35000 0.23400 0.14000 0.51000 0.35000   \n",
       "4 27.10000 1.00000  1.10000 0.43800 0.30500 0.25800 0.12000 0.55400 0.32600   \n",
       "\n",
       "     TTO%  CH% (pi)  CS% (pi)  CU% (pi)  FA% (pi)  FC% (pi)  FS% (pi)  \\\n",
       "0 0.28500   0.09900       NaN   0.08100   0.29700   0.06100   0.02700   \n",
       "1 0.42200   0.14000       NaN   0.08300   0.29400   0.10000   0.04200   \n",
       "2 0.36000   0.06300       NaN   0.06500   0.31800   0.08900   0.01700   \n",
       "3 0.24000   0.20400       NaN   0.08300   0.28700   0.09300   0.02600   \n",
       "4 0.34000   0.09100   0.00100   0.09500   0.31000   0.09500   0.02900   \n",
       "\n",
       "   KN% (pi)  SB% (pi)  SI% (pi)  SL% (pi)  XX% (pi)  vCH (pi)  vCS (pi)  \\\n",
       "0       NaN   0.00100   0.19800   0.23700       NaN  85.40000       NaN   \n",
       "1       NaN       NaN   0.10200   0.24000       NaN  86.30000       NaN   \n",
       "2       NaN   0.00100   0.21400   0.23400       NaN  86.10000       NaN   \n",
       "3       NaN       NaN   0.12100   0.18500       NaN  86.00000       NaN   \n",
       "4       NaN   0.00200   0.14600   0.23000       NaN  86.20000  77.40000   \n",
       "\n",
       "   vCU (pi)  vFA (pi)  vFC (pi)  vFS (pi)  vKN (pi)  vSB (pi)  vSI (pi)  \\\n",
       "0  79.60000  94.10000  89.60000  84.80000       NaN  81.90000  94.40000   \n",
       "1  80.10000  94.60000  90.70000  87.00000       NaN       NaN  94.10000   \n",
       "2  79.90000  94.40000  88.90000  88.30000       NaN  80.10000  93.50000   \n",
       "3  80.60000  94.10000  89.70000  87.00000       NaN       NaN  93.80000   \n",
       "4  80.00000  94.30000  90.80000  87.30000       NaN  82.80000  93.50000   \n",
       "\n",
       "   vSL (pi)  vXX (pi)  CH-X (pi)  CS-X (pi)  CU-X (pi)  FA-X (pi)  FC-X (pi)  \\\n",
       "0  85.30000       NaN   -1.50000        NaN    2.90000   -1.90000    0.70000   \n",
       "1  84.70000       NaN   -7.30000        NaN    3.50000   -1.70000    1.20000   \n",
       "2  84.70000       NaN   -1.60000        NaN    2.80000   -2.10000    0.80000   \n",
       "3  84.50000       NaN   -5.60000        NaN    3.40000   -2.30000    1.00000   \n",
       "4  84.10000       NaN   -6.80000    7.00000    5.20000   -2.20000    0.80000   \n",
       "\n",
       "   FS-X (pi)  KN-X (pi)  SB-X (pi)  SI-X (pi)  SL-X (pi)  XX-X (pi)  \\\n",
       "0   -4.70000        NaN   -6.60000   -6.80000    2.30000        NaN   \n",
       "1   -6.70000        NaN        NaN   -1.80000    0.60000        NaN   \n",
       "2   -6.10000        NaN   -5.30000   -4.50000    3.20000        NaN   \n",
       "3   -6.90000        NaN        NaN   -4.20000    2.80000        NaN   \n",
       "4   -5.90000        NaN   -8.30000   -3.20000    1.20000        NaN   \n",
       "\n",
       "   CH-Z (pi)  CS-Z (pi)  CU-Z (pi)  FA-Z (pi)  FC-Z (pi)  FS-Z (pi)  \\\n",
       "0    2.50000        NaN   -7.30000    8.20000    3.90000    0.50000   \n",
       "1    2.80000        NaN   -7.20000    8.50000    3.90000    0.70000   \n",
       "2    2.30000        NaN   -6.30000    8.20000    3.60000    1.30000   \n",
       "3    2.10000        NaN   -7.80000    8.60000    4.20000    1.10000   \n",
       "4    2.10000  -10.50000   -6.90000    8.10000    4.40000    1.20000   \n",
       "\n",
       "   KN-Z (pi)  SB-Z (pi)  SI-Z (pi)  SL-Z (pi)  XX-Z (pi)  wCH (pi)  wCS (pi)  \\\n",
       "0        NaN   -4.10000    4.20000    0.10000        NaN  -0.30000       NaN   \n",
       "1        NaN        NaN    4.10000   -0.40000        NaN   4.10000       NaN   \n",
       "2        NaN   -2.30000    3.90000    0.10000        NaN  -0.20000       NaN   \n",
       "3        NaN        NaN    4.00000   -0.50000        NaN  -2.00000       NaN   \n",
       "4        NaN   -2.40000    3.10000    0.00000        NaN  -1.20000   0.00000   \n",
       "\n",
       "   wCU (pi)  wFA (pi)  wFC (pi)  wFS (pi)  wKN (pi)  wSB (pi)  wSI (pi)  \\\n",
       "0   4.10000  12.80000   0.90000   2.00000       NaN   0.10000   3.90000   \n",
       "1   4.50000   6.50000   1.90000   1.50000       NaN       NaN   5.40000   \n",
       "2   2.20000   7.40000  -1.00000   0.30000       NaN  -0.20000  10.30000   \n",
       "3  -1.20000   9.10000  -0.40000  -1.30000       NaN       NaN   1.40000   \n",
       "4   0.00000  10.80000  -2.40000  -0.10000       NaN   1.30000   8.90000   \n",
       "\n",
       "   wSL (pi)  wXX (pi)  wCH/C (pi)  wCS/C (pi)  wCU/C (pi)  wFA/C (pi)  \\\n",
       "0  10.50000       NaN    -0.20000         NaN     3.34000     2.87000   \n",
       "1   7.90000       NaN     1.92000         NaN     3.53000     1.44000   \n",
       "2   7.80000       NaN    -0.25000         NaN     2.29000     1.58000   \n",
       "3   3.30000       NaN    -0.69000         NaN    -1.04000     2.24000   \n",
       "4   3.20000       NaN    -1.00000     3.61000     0.04000     2.71000   \n",
       "\n",
       "   wFC/C (pi)  wFS/C (pi)  wKN/C (pi)  wSB/C (pi)  wSI/C (pi)  wSL/C (pi)  \\\n",
       "0     0.96000     4.97000         NaN     4.27000     1.31000     2.93000   \n",
       "1     1.21000     2.36000         NaN         NaN     3.45000     2.15000   \n",
       "2    -0.78000     1.07000         NaN   -15.92000     3.26000     2.26000   \n",
       "3    -0.30000    -3.63000         NaN         NaN     0.84000     1.26000   \n",
       "4    -1.96000    -0.19000         NaN    62.60000     4.71000     1.09000   \n",
       "\n",
       "   wXX/C (pi)  O-Swing% (pi)  Z-Swing% (pi)  Swing% (pi)  O-Contact% (pi)  \\\n",
       "0         NaN        0.22600        0.67500      0.45600          0.65100   \n",
       "1         NaN        0.29700        0.67900      0.47900          0.51900   \n",
       "2         NaN        0.17200        0.59200      0.38100          0.54300   \n",
       "3         NaN        0.25600        0.60900      0.44500          0.76300   \n",
       "4         NaN        0.27700        0.62500      0.44800          0.69800   \n",
       "\n",
       "   Z-Contact% (pi)  Contact% (pi)  Zone% (pi)  Pace (pi)  FRM  AVG+  BB%+  \\\n",
       "0          0.87700        0.82200     0.51200   18.10000  NaN   134   122   \n",
       "1          0.80800        0.71400     0.47500   18.70000  NaN   121   144   \n",
       "2          0.93100        0.84300     0.49800   17.70000  NaN   108   152   \n",
       "3          0.91600        0.87500     0.53500   18.80000  NaN   116    95   \n",
       "4          0.86600        0.81300     0.49100   18.40000  NaN   115   101   \n",
       "\n",
       "   K%+  OBP+  SLG+  ISO+  BABIP+    LD+%  GB%+  FB%+  HR/FB%+  Pull%+  Cent%+  \\\n",
       "0   55   128   143   157     114 0.97000   116    82      184     112      97   \n",
       "1   97   121   160   220     105 0.76000   104   108      252      97     103   \n",
       "2   74   115   134   176      89 1.06000    69   133      141     117     102   \n",
       "3   59   108   114   111     103 1.20000   115    73      105     102     101   \n",
       "4   88   113   135   165     106 0.82000   107   101      169     107      88   \n",
       "\n",
       "   Oppo%+  Soft%+  Med%+  Hard%+       EV       LA  Barrels  Barrel%  \\\n",
       "0      85      64     89     135 94.90000  7.80000       47  0.15700   \n",
       "1     102      65     95     124 93.70000 13.10000       46  0.18000   \n",
       "2      69      63     90     134 92.40000 19.60000       32  0.12000   \n",
       "3      96      91     97     109 88.90000  8.30000       18  0.06300   \n",
       "4     105      77    107     100 90.70000 11.80000       22  0.09400   \n",
       "\n",
       "      maxEV  HardHit  HardHit%  Events   CStr%    CSW%     xBA    xSLG  \\\n",
       "0 116.70000      165   0.55000     300 0.14000 0.22100 0.35400 0.65900   \n",
       "1 117.10000      130   0.51000     255 0.13000 0.26500 0.29100 0.64100   \n",
       "2 110.10000      129   0.48500     266 0.20000 0.26100 0.28000 0.55700   \n",
       "3 111.00000      112   0.39200     286 0.18200 0.23700 0.29200 0.45100   \n",
       "4 113.80000      101   0.43300     233 0.17500 0.25900 0.26100 0.45300   \n",
       "\n",
       "    xwOBA   L-WAR  \n",
       "0 0.46100 4.80000  \n",
       "1 0.42600 4.00000  \n",
       "2 0.40300 3.80000  \n",
       "3 0.34900 3.10000  \n",
       "4 0.34700 3.50000  "
      ]
     },
     "execution_count": 85,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 86,
   "id": "03c1f54e",
   "metadata": {},
   "outputs": [],
   "source": [
    "import plotly.express as px\n",
    "import statsmodels.api as sm"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "8e1ce2bd",
   "metadata": {},
   "source": [
    "### Row 1 - Plot 1 (outdated)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "60cf56d2",
   "metadata": {},
   "source": [
    "fig_1 = px.scatter(\n",
    "    df.query(\"Season==2023\"),\n",
    "    title=\"Hard%+ vs. BABIP+\",\n",
    "    x = \"Hard%+\",\n",
    "    y = \"BABIP+\",\n",
    "    hover_name = \"Name\",\n",
    "    log_x = True,\n",
    "    trendline = \"ols\",\n",
    "    size_max = 60,\n",
    "    height = 750,\n",
    "    width = 750,\n",
    ")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "4abfe4a2",
   "metadata": {},
   "source": [
    "### Row 1 - Tab 1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 87,
   "id": "fb8ad184",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "application/vnd.plotly.v1+json": {
       "config": {
        "plotlyServerURL": "https://plot.ly"
       },
       "data": [
        {
         "alignmentgroup": "True",
         "boxpoints": "all",
         "hovertemplate": "<b>%{hovertext}</b><br><br>wRC+=%{y}<extra></extra>",
         "hovertext": [
          "Ronald Acuna Jr.",
          "Shohei Ohtani",
          "Mookie Betts",
          "Wander Franco",
          "Corbin Carroll",
          "Luis Robert",
          "Freddie Freeman",
          "Juan Soto",
          "Fernando Tatis Jr.",
          "Jose Ramirez",
          "Adolis Garcia",
          "Mike Trout",
          "Jonah Heim",
          "Marcus Semien",
          "Bo Bichette",
          "Christian Yelich",
          "Francisco Lindor",
          "Dansby Swanson",
          "Luis Arraez",
          "Will Smith",
          "Ha-seong Kim",
          "Randy Arozarena",
          "Paul Goldschmidt",
          "Matt Chapman",
          "Isaac Paredes",
          "Brandon Nimmo",
          "Jeimer Candelario",
          "Thairo Estrada",
          "Matt Olson",
          "Christian Walker",
          "Jack Suwinski",
          "Julio Rodriguez",
          "Yandy Diaz",
          "Kyle Tucker",
          "Josh Jung",
          "Ketel Marte",
          "Ozzie Albies",
          "William Contreras",
          "Xander Bogaerts",
          "Leody Taveras",
          "Adley Rutschman",
          "Nico Hoerner",
          "Lane Thomas",
          "Bobby Witt Jr.",
          "LaMonte Wade Jr.",
          "Austin Hays",
          "J.D. Davis",
          "Gunnar Henderson",
          "Alex Verdugo",
          "Nathaniel Lowe",
          "Jorge Soler",
          "Nolan Arenado",
          "Rafael Devers",
          "Austin Riley",
          "Brendan Donovan",
          "Bryson Stott",
          "Brandon Drury",
          "Brandon Marsh",
          "Ian Happ",
          "J.P. Crawford",
          "Alex Bregman",
          "Andres Gimenez",
          "Cal Raleigh",
          "Spencer Steer",
          "Nolan Gorman",
          "Ryan Noda",
          "Cedric Mullins II",
          "James Outman",
          "Nick Castellanos",
          "Pete Alonso",
          "Anthony Santander",
          "Ryan McMahon",
          "Zach McKinstry",
          "Trea Turner",
          "Anthony Volpe",
          "Masataka Yoshida",
          "Justin Turner",
          "Bryan Reynolds",
          "Manny Machado",
          "Whit Merrifield",
          "Jeremy Pena",
          "Josh Naylor",
          "Anthony Rizzo",
          "Jonathan India",
          "Jarred Kelenic",
          "George Springer",
          "Eugenio Suarez",
          "Joey Wiemer",
          "Andrew McCutchen",
          "Lourdes Gurriel Jr.",
          "Max Muncy",
          "Hunter Renfroe",
          "Mauricio Dubon",
          "Steven Kwan",
          "Tommy Edman",
          "Brent Rooker",
          "J.T. Realmuto",
          "Teoscar Hernandez",
          "Ezequiel Tovar",
          "Willson Contreras",
          "Carlos Correa",
          "Ke'Bryan Hayes",
          "Willy Adames",
          "Gleyber Torres",
          "Esteury Ruiz",
          "Marcell Ozuna",
          "Byron Buxton",
          "Andrew Benintendi",
          "Daulton Varsho",
          "J.D. Martinez",
          "Elias Diaz",
          "Ty France",
          "Taylor Ward",
          "Jeff McNeil",
          "Eddie Rosario",
          "Seiya Suzuki",
          "Carlos Santana",
          "Trent Grisham",
          "Vladimir Guerrero Jr.",
          "Michael Conforto",
          "Brian Anderson",
          "Jace Peterson",
          "Javier Baez",
          "Andrew Vaughn",
          "Alec Bohm",
          "Bryan De La Cruz",
          "Jake Cronenworth",
          "Salvador Perez",
          "CJ Abrams",
          "Spencer Torkelson",
          "Adam Frazier",
          "Miguel Vargas",
          "Amed Rosario",
          "Starling Marte",
          "Luis Garcia",
          "DJ LeMahieu",
          "Tyler Stephenson",
          "Kyle Schwarber",
          "Triston Casas",
          "Dominic Smith",
          "Shea Langeliers",
          "Josh Bell",
          "Myles Straw",
          "Joey Meneses",
          "Jose Abreu",
          "MJ Melendez",
          "Tim Anderson",
          "Rowdy Tellez",
          "Jurickson Profar",
          "Keibert Ruiz",
          "Enrique Hernandez"
         ],
         "legendgroup": "",
         "marker": {
          "color": "#7284cc"
         },
         "name": "",
         "notched": false,
         "offsetgroup": "",
         "orientation": "v",
         "showlegend": false,
         "type": "box",
         "x0": " ",
         "xaxis": "x",
         "y": [
          168,
          177,
          150,
          125,
          145,
          144,
          152,
          153,
          139,
          132,
          131,
          137,
          124,
          115,
          136,
          129,
          117,
          108,
          152,
          140,
          111,
          149,
          134,
          122,
          147,
          131,
          118,
          108,
          146,
          124,
          138,
          107,
          157,
          134,
          122,
          131,
          119,
          110,
          111,
          129,
          124,
          94,
          129,
          92,
          140,
          133,
          122,
          123,
          117,
          120,
          136,
          123,
          118,
          108,
          120,
          104,
          122,
          111,
          118,
          123,
          108,
          100,
          101,
          130,
          118,
          132,
          118,
          103,
          128,
          126,
          125,
          103,
          101,
          85,
          90,
          135,
          123,
          115,
          100,
          104,
          95,
          120,
          117,
          102,
          109,
          106,
          100,
          82,
          123,
          112,
          114,
          103,
          99,
          95,
          90,
          126,
          101,
          106,
          82,
          104,
          96,
          83,
          82,
          104,
          85,
          119,
          110,
          100,
          84,
          119,
          94,
          110,
          93,
          93,
          110,
          105,
          95,
          96,
          123,
          102,
          89,
          76,
          64,
          109,
          103,
          104,
          91,
          93,
          80,
          97,
          94,
          84,
          85,
          86,
          81,
          78,
          94,
          104,
          96,
          82,
          77,
          88,
          71,
          86,
          77,
          71,
          49,
          79,
          80,
          72,
          65
         ],
         "y0": " ",
         "yaxis": "y"
        }
       ],
       "layout": {
        "boxmode": "group",
        "height": 500,
        "legend": {
         "tracegroupgap": 0
        },
        "margin": {
         "t": 60
        },
        "template": {
         "data": {
          "candlestick": [
           {
            "decreasing": {
             "line": {
              "color": "#000033"
             }
            },
            "increasing": {
             "line": {
              "color": "#000032"
             }
            },
            "type": "candlestick"
           }
          ],
          "contour": [
           {
            "colorscale": [
             [
              0,
              "#000011"
             ],
             [
              0.1111111111111111,
              "#000012"
             ],
             [
              0.2222222222222222,
              "#000013"
             ],
             [
              0.3333333333333333,
              "#000014"
             ],
             [
              0.4444444444444444,
              "#000015"
             ],
             [
              0.5555555555555556,
              "#000016"
             ],
             [
              0.6666666666666666,
              "#000017"
             ],
             [
              0.7777777777777778,
              "#000018"
             ],
             [
              0.8888888888888888,
              "#000019"
             ],
             [
              1,
              "#000020"
             ]
            ],
            "type": "contour"
           }
          ],
          "contourcarpet": [
           {
            "colorscale": [
             [
              0,
              "#000011"
             ],
             [
              0.1111111111111111,
              "#000012"
             ],
             [
              0.2222222222222222,
              "#000013"
             ],
             [
              0.3333333333333333,
              "#000014"
             ],
             [
              0.4444444444444444,
              "#000015"
             ],
             [
              0.5555555555555556,
              "#000016"
             ],
             [
              0.6666666666666666,
              "#000017"
             ],
             [
              0.7777777777777778,
              "#000018"
             ],
             [
              0.8888888888888888,
              "#000019"
             ],
             [
              1,
              "#000020"
             ]
            ],
            "type": "contourcarpet"
           }
          ],
          "heatmap": [
           {
            "colorscale": [
             [
              0,
              "#000011"
             ],
             [
              0.1111111111111111,
              "#000012"
             ],
             [
              0.2222222222222222,
              "#000013"
             ],
             [
              0.3333333333333333,
              "#000014"
             ],
             [
              0.4444444444444444,
              "#000015"
             ],
             [
              0.5555555555555556,
              "#000016"
             ],
             [
              0.6666666666666666,
              "#000017"
             ],
             [
              0.7777777777777778,
              "#000018"
             ],
             [
              0.8888888888888888,
              "#000019"
             ],
             [
              1,
              "#000020"
             ]
            ],
            "type": "heatmap"
           }
          ],
          "histogram2d": [
           {
            "colorscale": [
             [
              0,
              "#000011"
             ],
             [
              0.1111111111111111,
              "#000012"
             ],
             [
              0.2222222222222222,
              "#000013"
             ],
             [
              0.3333333333333333,
              "#000014"
             ],
             [
              0.4444444444444444,
              "#000015"
             ],
             [
              0.5555555555555556,
              "#000016"
             ],
             [
              0.6666666666666666,
              "#000017"
             ],
             [
              0.7777777777777778,
              "#000018"
             ],
             [
              0.8888888888888888,
              "#000019"
             ],
             [
              1,
              "#000020"
             ]
            ],
            "type": "histogram2d"
           }
          ],
          "icicle": [
           {
            "textfont": {
             "color": "white"
            },
            "type": "icicle"
           }
          ],
          "sankey": [
           {
            "textfont": {
             "color": "#000036"
            },
            "type": "sankey"
           }
          ],
          "scatter": [
           {
            "marker": {
             "line": {
              "width": 0
             }
            },
            "type": "scatter"
           }
          ],
          "table": [
           {
            "cells": {
             "fill": {
              "color": "#000038"
             },
             "font": {
              "color": "#000037"
             },
             "line": {
              "color": "#000039"
             }
            },
            "header": {
             "fill": {
              "color": "#000040"
             },
             "font": {
              "color": "#000036"
             },
             "line": {
              "color": "#000039"
             }
            },
            "type": "table"
           }
          ],
          "waterfall": [
           {
            "connector": {
             "line": {
              "color": "#000036",
              "width": 2
             }
            },
            "decreasing": {
             "marker": {
              "color": "#000033"
             }
            },
            "increasing": {
             "marker": {
              "color": "#000032"
             }
            },
            "totals": {
             "marker": {
              "color": "#000034"
             }
            },
            "type": "waterfall"
           }
          ]
         },
         "layout": {
          "coloraxis": {
           "colorscale": [
            [
             0,
             "#000011"
            ],
            [
             0.1111111111111111,
             "#000012"
            ],
            [
             0.2222222222222222,
             "#000013"
            ],
            [
             0.3333333333333333,
             "#000014"
            ],
            [
             0.4444444444444444,
             "#000015"
            ],
            [
             0.5555555555555556,
             "#000016"
            ],
            [
             0.6666666666666666,
             "#000017"
            ],
            [
             0.7777777777777778,
             "#000018"
            ],
            [
             0.8888888888888888,
             "#000019"
            ],
            [
             1,
             "#000020"
            ]
           ]
          },
          "colorscale": {
           "diverging": [
            [
             0,
             "#000021"
            ],
            [
             0.1,
             "#000022"
            ],
            [
             0.2,
             "#000023"
            ],
            [
             0.3,
             "#000024"
            ],
            [
             0.4,
             "#000025"
            ],
            [
             0.5,
             "#000026"
            ],
            [
             0.6,
             "#000027"
            ],
            [
             0.7,
             "#000028"
            ],
            [
             0.8,
             "#000029"
            ],
            [
             0.9,
             "#000030"
            ],
            [
             1,
             "#000031"
            ]
           ],
           "sequential": [
            [
             0,
             "#000011"
            ],
            [
             0.1111111111111111,
             "#000012"
            ],
            [
             0.2222222222222222,
             "#000013"
            ],
            [
             0.3333333333333333,
             "#000014"
            ],
            [
             0.4444444444444444,
             "#000015"
            ],
            [
             0.5555555555555556,
             "#000016"
            ],
            [
             0.6666666666666666,
             "#000017"
            ],
            [
             0.7777777777777778,
             "#000018"
            ],
            [
             0.8888888888888888,
             "#000019"
            ],
            [
             1,
             "#000020"
            ]
           ],
           "sequentialminus": [
            [
             0,
             "#000011"
            ],
            [
             0.1111111111111111,
             "#000012"
            ],
            [
             0.2222222222222222,
             "#000013"
            ],
            [
             0.3333333333333333,
             "#000014"
            ],
            [
             0.4444444444444444,
             "#000015"
            ],
            [
             0.5555555555555556,
             "#000016"
            ],
            [
             0.6666666666666666,
             "#000017"
            ],
            [
             0.7777777777777778,
             "#000018"
            ],
            [
             0.8888888888888888,
             "#000019"
            ],
            [
             1,
             "#000020"
            ]
           ]
          },
          "colorway": [
           "#000001",
           "#000002",
           "#000003",
           "#000004",
           "#000005",
           "#000006",
           "#000007",
           "#000008",
           "#000009",
           "#000010"
          ]
         }
        },
        "title": {
         "automargin": true,
         "font": {
          "color": "#164f5e",
          "size": 22
         },
         "text": "wRC+",
         "yref": "paper"
        },
        "width": 500,
        "xaxis": {
         "anchor": "y",
         "domain": [
          0,
          1
         ],
         "title": {
          "text": ""
         }
        },
        "yaxis": {
         "anchor": "x",
         "domain": [
          0,
          1
         ],
         "title": {
          "text": ""
         }
        }
       }
      },
      "text/html": [
       "<div>                            <div id=\"b835a9a9-447c-43d2-a63d-548a78582184\" class=\"plotly-graph-div\" style=\"height:500px; width:500px;\"></div>            <script type=\"text/javascript\">                require([\"plotly\"], function(Plotly) {                    window.PLOTLYENV=window.PLOTLYENV || {};                                    if (document.getElementById(\"b835a9a9-447c-43d2-a63d-548a78582184\")) {                    Plotly.newPlot(                        \"b835a9a9-447c-43d2-a63d-548a78582184\",                        [{\"alignmentgroup\":\"True\",\"boxpoints\":\"all\",\"hovertemplate\":\"\\u003cb\\u003e%{hovertext}\\u003c\\u002fb\\u003e\\u003cbr\\u003e\\u003cbr\\u003ewRC+=%{y}\\u003cextra\\u003e\\u003c\\u002fextra\\u003e\",\"hovertext\":[\"Ronald Acuna Jr.\",\"Shohei Ohtani\",\"Mookie Betts\",\"Wander Franco\",\"Corbin Carroll\",\"Luis Robert\",\"Freddie Freeman\",\"Juan Soto\",\"Fernando Tatis Jr.\",\"Jose Ramirez\",\"Adolis Garcia\",\"Mike Trout\",\"Jonah Heim\",\"Marcus Semien\",\"Bo Bichette\",\"Christian Yelich\",\"Francisco Lindor\",\"Dansby Swanson\",\"Luis Arraez\",\"Will Smith\",\"Ha-seong Kim\",\"Randy Arozarena\",\"Paul Goldschmidt\",\"Matt Chapman\",\"Isaac Paredes\",\"Brandon Nimmo\",\"Jeimer Candelario\",\"Thairo Estrada\",\"Matt Olson\",\"Christian Walker\",\"Jack Suwinski\",\"Julio Rodriguez\",\"Yandy Diaz\",\"Kyle Tucker\",\"Josh Jung\",\"Ketel Marte\",\"Ozzie Albies\",\"William Contreras\",\"Xander Bogaerts\",\"Leody Taveras\",\"Adley Rutschman\",\"Nico Hoerner\",\"Lane Thomas\",\"Bobby Witt Jr.\",\"LaMonte Wade Jr.\",\"Austin Hays\",\"J.D. Davis\",\"Gunnar Henderson\",\"Alex Verdugo\",\"Nathaniel Lowe\",\"Jorge Soler\",\"Nolan Arenado\",\"Rafael Devers\",\"Austin Riley\",\"Brendan Donovan\",\"Bryson Stott\",\"Brandon Drury\",\"Brandon Marsh\",\"Ian Happ\",\"J.P. Crawford\",\"Alex Bregman\",\"Andres Gimenez\",\"Cal Raleigh\",\"Spencer Steer\",\"Nolan Gorman\",\"Ryan Noda\",\"Cedric Mullins II\",\"James Outman\",\"Nick Castellanos\",\"Pete Alonso\",\"Anthony Santander\",\"Ryan McMahon\",\"Zach McKinstry\",\"Trea Turner\",\"Anthony Volpe\",\"Masataka Yoshida\",\"Justin Turner\",\"Bryan Reynolds\",\"Manny Machado\",\"Whit Merrifield\",\"Jeremy Pena\",\"Josh Naylor\",\"Anthony Rizzo\",\"Jonathan India\",\"Jarred Kelenic\",\"George Springer\",\"Eugenio Suarez\",\"Joey Wiemer\",\"Andrew McCutchen\",\"Lourdes Gurriel Jr.\",\"Max Muncy\",\"Hunter Renfroe\",\"Mauricio Dubon\",\"Steven Kwan\",\"Tommy Edman\",\"Brent Rooker\",\"J.T. Realmuto\",\"Teoscar Hernandez\",\"Ezequiel Tovar\",\"Willson Contreras\",\"Carlos Correa\",\"Ke'Bryan Hayes\",\"Willy Adames\",\"Gleyber Torres\",\"Esteury Ruiz\",\"Marcell Ozuna\",\"Byron Buxton\",\"Andrew Benintendi\",\"Daulton Varsho\",\"J.D. Martinez\",\"Elias Diaz\",\"Ty France\",\"Taylor Ward\",\"Jeff McNeil\",\"Eddie Rosario\",\"Seiya Suzuki\",\"Carlos Santana\",\"Trent Grisham\",\"Vladimir Guerrero Jr.\",\"Michael Conforto\",\"Brian Anderson\",\"Jace Peterson\",\"Javier Baez\",\"Andrew Vaughn\",\"Alec Bohm\",\"Bryan De La Cruz\",\"Jake Cronenworth\",\"Salvador Perez\",\"CJ Abrams\",\"Spencer Torkelson\",\"Adam Frazier\",\"Miguel Vargas\",\"Amed Rosario\",\"Starling Marte\",\"Luis Garcia\",\"DJ LeMahieu\",\"Tyler Stephenson\",\"Kyle Schwarber\",\"Triston Casas\",\"Dominic Smith\",\"Shea Langeliers\",\"Josh Bell\",\"Myles Straw\",\"Joey Meneses\",\"Jose Abreu\",\"MJ Melendez\",\"Tim Anderson\",\"Rowdy Tellez\",\"Jurickson Profar\",\"Keibert Ruiz\",\"Enrique Hernandez\"],\"legendgroup\":\"\",\"marker\":{\"color\":\"#7284cc\"},\"name\":\"\",\"notched\":false,\"offsetgroup\":\"\",\"orientation\":\"v\",\"showlegend\":false,\"x0\":\" \",\"xaxis\":\"x\",\"y\":[168,177,150,125,145,144,152,153,139,132,131,137,124,115,136,129,117,108,152,140,111,149,134,122,147,131,118,108,146,124,138,107,157,134,122,131,119,110,111,129,124,94,129,92,140,133,122,123,117,120,136,123,118,108,120,104,122,111,118,123,108,100,101,130,118,132,118,103,128,126,125,103,101,85,90,135,123,115,100,104,95,120,117,102,109,106,100,82,123,112,114,103,99,95,90,126,101,106,82,104,96,83,82,104,85,119,110,100,84,119,94,110,93,93,110,105,95,96,123,102,89,76,64,109,103,104,91,93,80,97,94,84,85,86,81,78,94,104,96,82,77,88,71,86,77,71,49,79,80,72,65],\"y0\":\" \",\"yaxis\":\"y\",\"type\":\"box\"}],                        {\"template\":{\"data\":{\"candlestick\":[{\"decreasing\":{\"line\":{\"color\":\"#000033\"}},\"increasing\":{\"line\":{\"color\":\"#000032\"}},\"type\":\"candlestick\"}],\"contourcarpet\":[{\"colorscale\":[[0.0,\"#000011\"],[0.1111111111111111,\"#000012\"],[0.2222222222222222,\"#000013\"],[0.3333333333333333,\"#000014\"],[0.4444444444444444,\"#000015\"],[0.5555555555555556,\"#000016\"],[0.6666666666666666,\"#000017\"],[0.7777777777777778,\"#000018\"],[0.8888888888888888,\"#000019\"],[1.0,\"#000020\"]],\"type\":\"contourcarpet\"}],\"contour\":[{\"colorscale\":[[0.0,\"#000011\"],[0.1111111111111111,\"#000012\"],[0.2222222222222222,\"#000013\"],[0.3333333333333333,\"#000014\"],[0.4444444444444444,\"#000015\"],[0.5555555555555556,\"#000016\"],[0.6666666666666666,\"#000017\"],[0.7777777777777778,\"#000018\"],[0.8888888888888888,\"#000019\"],[1.0,\"#000020\"]],\"type\":\"contour\"}],\"heatmap\":[{\"colorscale\":[[0.0,\"#000011\"],[0.1111111111111111,\"#000012\"],[0.2222222222222222,\"#000013\"],[0.3333333333333333,\"#000014\"],[0.4444444444444444,\"#000015\"],[0.5555555555555556,\"#000016\"],[0.6666666666666666,\"#000017\"],[0.7777777777777778,\"#000018\"],[0.8888888888888888,\"#000019\"],[1.0,\"#000020\"]],\"type\":\"heatmap\"}],\"histogram2d\":[{\"colorscale\":[[0.0,\"#000011\"],[0.1111111111111111,\"#000012\"],[0.2222222222222222,\"#000013\"],[0.3333333333333333,\"#000014\"],[0.4444444444444444,\"#000015\"],[0.5555555555555556,\"#000016\"],[0.6666666666666666,\"#000017\"],[0.7777777777777778,\"#000018\"],[0.8888888888888888,\"#000019\"],[1.0,\"#000020\"]],\"type\":\"histogram2d\"}],\"icicle\":[{\"textfont\":{\"color\":\"white\"},\"type\":\"icicle\"}],\"sankey\":[{\"textfont\":{\"color\":\"#000036\"},\"type\":\"sankey\"}],\"scatter\":[{\"marker\":{\"line\":{\"width\":0}},\"type\":\"scatter\"}],\"table\":[{\"cells\":{\"fill\":{\"color\":\"#000038\"},\"font\":{\"color\":\"#000037\"},\"line\":{\"color\":\"#000039\"}},\"header\":{\"fill\":{\"color\":\"#000040\"},\"font\":{\"color\":\"#000036\"},\"line\":{\"color\":\"#000039\"}},\"type\":\"table\"}],\"waterfall\":[{\"connector\":{\"line\":{\"color\":\"#000036\",\"width\":2}},\"decreasing\":{\"marker\":{\"color\":\"#000033\"}},\"increasing\":{\"marker\":{\"color\":\"#000032\"}},\"totals\":{\"marker\":{\"color\":\"#000034\"}},\"type\":\"waterfall\"}]},\"layout\":{\"coloraxis\":{\"colorscale\":[[0.0,\"#000011\"],[0.1111111111111111,\"#000012\"],[0.2222222222222222,\"#000013\"],[0.3333333333333333,\"#000014\"],[0.4444444444444444,\"#000015\"],[0.5555555555555556,\"#000016\"],[0.6666666666666666,\"#000017\"],[0.7777777777777778,\"#000018\"],[0.8888888888888888,\"#000019\"],[1.0,\"#000020\"]]},\"colorscale\":{\"diverging\":[[0.0,\"#000021\"],[0.1,\"#000022\"],[0.2,\"#000023\"],[0.3,\"#000024\"],[0.4,\"#000025\"],[0.5,\"#000026\"],[0.6,\"#000027\"],[0.7,\"#000028\"],[0.8,\"#000029\"],[0.9,\"#000030\"],[1.0,\"#000031\"]],\"sequential\":[[0.0,\"#000011\"],[0.1111111111111111,\"#000012\"],[0.2222222222222222,\"#000013\"],[0.3333333333333333,\"#000014\"],[0.4444444444444444,\"#000015\"],[0.5555555555555556,\"#000016\"],[0.6666666666666666,\"#000017\"],[0.7777777777777778,\"#000018\"],[0.8888888888888888,\"#000019\"],[1.0,\"#000020\"]],\"sequentialminus\":[[0.0,\"#000011\"],[0.1111111111111111,\"#000012\"],[0.2222222222222222,\"#000013\"],[0.3333333333333333,\"#000014\"],[0.4444444444444444,\"#000015\"],[0.5555555555555556,\"#000016\"],[0.6666666666666666,\"#000017\"],[0.7777777777777778,\"#000018\"],[0.8888888888888888,\"#000019\"],[1.0,\"#000020\"]]},\"colorway\":[\"#000001\",\"#000002\",\"#000003\",\"#000004\",\"#000005\",\"#000006\",\"#000007\",\"#000008\",\"#000009\",\"#000010\"]}},\"xaxis\":{\"anchor\":\"y\",\"domain\":[0.0,1.0],\"title\":{\"text\":\"\"}},\"yaxis\":{\"anchor\":\"x\",\"domain\":[0.0,1.0],\"title\":{\"text\":\"\"}},\"legend\":{\"tracegroupgap\":0},\"margin\":{\"t\":60},\"boxmode\":\"group\",\"height\":500,\"width\":500,\"title\":{\"font\":{\"size\":22,\"color\":\"#164f5e\"},\"text\":\"wRC+\",\"automargin\":true,\"yref\":\"paper\"}},                        {\"responsive\": true}                    ).then(function(){\n",
       "                            \n",
       "var gd = document.getElementById('b835a9a9-447c-43d2-a63d-548a78582184');\n",
       "var x = new MutationObserver(function (mutations, observer) {{\n",
       "        var display = window.getComputedStyle(gd).display;\n",
       "        if (!display || display === 'none') {{\n",
       "            console.log([gd, 'removed!']);\n",
       "            Plotly.purge(gd);\n",
       "            observer.disconnect();\n",
       "        }}\n",
       "}});\n",
       "\n",
       "// Listen for the removal of the full notebook cells\n",
       "var notebookContainer = gd.closest('#notebook-container');\n",
       "if (notebookContainer) {{\n",
       "    x.observe(notebookContainer, {childList: true});\n",
       "}}\n",
       "\n",
       "// Listen for the clearing of the current output cell\n",
       "var outputEl = gd.closest('.output');\n",
       "if (outputEl) {{\n",
       "    x.observe(outputEl, {childList: true});\n",
       "}}\n",
       "\n",
       "                        })                };                });            </script>        </div>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "fig_11 = px.box(\n",
    "    df.query(\"Season==2023\"),\n",
    "    y = \"wRC+\",\n",
    "    points=\"all\",\n",
    "    hover_name = \"Name\",\n",
    "    height = 500,\n",
    "    width = 500,\n",
    ")\n",
    "\n",
    "fig_11.update_traces(marker=dict(color=\"#7284cc\"))\n",
    "\n",
    "fig_11.update_layout(\n",
    "    title=dict(text=\"wRC+\", font=dict(size=22), automargin=True, yref='paper'),\n",
    "    title_font_color=\"#164f5e\",\n",
    "    yaxis=dict(title=\"\"),\n",
    "    xaxis=dict(title=\"\")\n",
    ")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 88,
   "id": "1b0510b2",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "application/vnd.plotly.v1+json": {
       "config": {
        "plotlyServerURL": "https://plot.ly"
       },
       "data": [
        {
         "alignmentgroup": "True",
         "boxpoints": "all",
         "hovertemplate": "<b>%{hovertext}</b><br><br>Bat=%{y}<extra></extra>",
         "hovertext": [
          "Ronald Acuna Jr.",
          "Shohei Ohtani",
          "Mookie Betts",
          "Wander Franco",
          "Corbin Carroll",
          "Luis Robert",
          "Freddie Freeman",
          "Juan Soto",
          "Fernando Tatis Jr.",
          "Jose Ramirez",
          "Adolis Garcia",
          "Mike Trout",
          "Jonah Heim",
          "Marcus Semien",
          "Bo Bichette",
          "Christian Yelich",
          "Francisco Lindor",
          "Dansby Swanson",
          "Luis Arraez",
          "Will Smith",
          "Ha-seong Kim",
          "Randy Arozarena",
          "Paul Goldschmidt",
          "Matt Chapman",
          "Isaac Paredes",
          "Brandon Nimmo",
          "Jeimer Candelario",
          "Thairo Estrada",
          "Matt Olson",
          "Christian Walker",
          "Jack Suwinski",
          "Julio Rodriguez",
          "Yandy Diaz",
          "Kyle Tucker",
          "Josh Jung",
          "Ketel Marte",
          "Ozzie Albies",
          "William Contreras",
          "Xander Bogaerts",
          "Leody Taveras",
          "Adley Rutschman",
          "Nico Hoerner",
          "Lane Thomas",
          "Bobby Witt Jr.",
          "LaMonte Wade Jr.",
          "Austin Hays",
          "J.D. Davis",
          "Gunnar Henderson",
          "Alex Verdugo",
          "Nathaniel Lowe",
          "Jorge Soler",
          "Nolan Arenado",
          "Rafael Devers",
          "Austin Riley",
          "Brendan Donovan",
          "Bryson Stott",
          "Brandon Drury",
          "Brandon Marsh",
          "Ian Happ",
          "J.P. Crawford",
          "Alex Bregman",
          "Andres Gimenez",
          "Cal Raleigh",
          "Spencer Steer",
          "Nolan Gorman",
          "Ryan Noda",
          "Cedric Mullins II",
          "James Outman",
          "Nick Castellanos",
          "Pete Alonso",
          "Anthony Santander",
          "Ryan McMahon",
          "Zach McKinstry",
          "Trea Turner",
          "Anthony Volpe",
          "Masataka Yoshida",
          "Justin Turner",
          "Bryan Reynolds",
          "Manny Machado",
          "Whit Merrifield",
          "Jeremy Pena",
          "Josh Naylor",
          "Anthony Rizzo",
          "Jonathan India",
          "Jarred Kelenic",
          "George Springer",
          "Eugenio Suarez",
          "Joey Wiemer",
          "Andrew McCutchen",
          "Lourdes Gurriel Jr.",
          "Max Muncy",
          "Hunter Renfroe",
          "Mauricio Dubon",
          "Steven Kwan",
          "Tommy Edman",
          "Brent Rooker",
          "J.T. Realmuto",
          "Teoscar Hernandez",
          "Ezequiel Tovar",
          "Willson Contreras",
          "Carlos Correa",
          "Ke'Bryan Hayes",
          "Willy Adames",
          "Gleyber Torres",
          "Esteury Ruiz",
          "Marcell Ozuna",
          "Byron Buxton",
          "Andrew Benintendi",
          "Daulton Varsho",
          "J.D. Martinez",
          "Elias Diaz",
          "Ty France",
          "Taylor Ward",
          "Jeff McNeil",
          "Eddie Rosario",
          "Seiya Suzuki",
          "Carlos Santana",
          "Trent Grisham",
          "Vladimir Guerrero Jr.",
          "Michael Conforto",
          "Brian Anderson",
          "Jace Peterson",
          "Javier Baez",
          "Andrew Vaughn",
          "Alec Bohm",
          "Bryan De La Cruz",
          "Jake Cronenworth",
          "Salvador Perez",
          "CJ Abrams",
          "Spencer Torkelson",
          "Adam Frazier",
          "Miguel Vargas",
          "Amed Rosario",
          "Starling Marte",
          "Luis Garcia",
          "DJ LeMahieu",
          "Tyler Stephenson",
          "Kyle Schwarber",
          "Triston Casas",
          "Dominic Smith",
          "Shea Langeliers",
          "Josh Bell",
          "Myles Straw",
          "Joey Meneses",
          "Jose Abreu",
          "MJ Melendez",
          "Tim Anderson",
          "Rowdy Tellez",
          "Jurickson Profar",
          "Keibert Ruiz",
          "Enrique Hernandez"
         ],
         "legendgroup": "",
         "marker": {
          "color": "#7284cc"
         },
         "name": "",
         "notched": false,
         "offsetgroup": "",
         "orientation": "v",
         "showlegend": false,
         "type": "box",
         "x0": " ",
         "xaxis": "x",
         "y": [
          33.5,
          35.2,
          23.8,
          11,
          18.8,
          18.6,
          25.8,
          25,
          15.1,
          14.2,
          13.7,
          15.8,
          8.6,
          7.2,
          16.5,
          13.1,
          7.8,
          3.5,
          22.8,
          13.7,
          4.2,
          21.1,
          16,
          9.4,
          16.5,
          14.8,
          7.7,
          3.1,
          22.2,
          10.4,
          13.6,
          3,
          22.2,
          14.4,
          9.5,
          13.6,
          8.7,
          3.4,
          4.6,
          9.8,
          10.6,
          -2.8,
          13.5,
          -3.5,
          15.3,
          11.6,
          8.3,
          7.9,
          7.3,
          9.5,
          16,
          10,
          7.6,
          3.8,
          7.6,
          1.8,
          8.1,
          4,
          8,
          9.1,
          3.7,
          0,
          0.4,
          13.3,
          6.7,
          11.7,
          5.9,
          1.2,
          12.3,
          10.9,
          10.3,
          1.4,
          0.4,
          -7.2,
          -3.7,
          13.7,
          9.7,
          5.8,
          0.1,
          1.7,
          -1.8,
          7.3,
          7.1,
          1,
          3.7,
          2.8,
          0.2,
          -6.6,
          9,
          4.5,
          5.1,
          1.1,
          -0.3,
          -2.2,
          -3.7,
          8.9,
          0.3,
          2.4,
          -6.9,
          1.6,
          -1.6,
          -6.6,
          -7.5,
          1.9,
          -6.7,
          6.7,
          3.2,
          -0.2,
          -6.5,
          7.1,
          -2.3,
          4.4,
          -2.8,
          -3.1,
          3.6,
          1.7,
          -2.1,
          -1.6,
          10.1,
          0.6,
          -4.4,
          -8,
          -14.8,
          4,
          1.2,
          1.5,
          -4,
          -2.9,
          -7.2,
          -1.2,
          -2.2,
          -6,
          -6.4,
          -5.5,
          -8,
          -7.8,
          -2.7,
          1.8,
          -1.4,
          -7.5,
          -7.6,
          -4.7,
          -10.8,
          -6,
          -9.8,
          -11.5,
          -16.7,
          -7.5,
          -8.4,
          -10.3,
          -12.1
         ],
         "y0": " ",
         "yaxis": "y"
        }
       ],
       "layout": {
        "boxmode": "group",
        "height": 500,
        "legend": {
         "tracegroupgap": 0
        },
        "margin": {
         "t": 60
        },
        "template": {
         "data": {
          "candlestick": [
           {
            "decreasing": {
             "line": {
              "color": "#000033"
             }
            },
            "increasing": {
             "line": {
              "color": "#000032"
             }
            },
            "type": "candlestick"
           }
          ],
          "contour": [
           {
            "colorscale": [
             [
              0,
              "#000011"
             ],
             [
              0.1111111111111111,
              "#000012"
             ],
             [
              0.2222222222222222,
              "#000013"
             ],
             [
              0.3333333333333333,
              "#000014"
             ],
             [
              0.4444444444444444,
              "#000015"
             ],
             [
              0.5555555555555556,
              "#000016"
             ],
             [
              0.6666666666666666,
              "#000017"
             ],
             [
              0.7777777777777778,
              "#000018"
             ],
             [
              0.8888888888888888,
              "#000019"
             ],
             [
              1,
              "#000020"
             ]
            ],
            "type": "contour"
           }
          ],
          "contourcarpet": [
           {
            "colorscale": [
             [
              0,
              "#000011"
             ],
             [
              0.1111111111111111,
              "#000012"
             ],
             [
              0.2222222222222222,
              "#000013"
             ],
             [
              0.3333333333333333,
              "#000014"
             ],
             [
              0.4444444444444444,
              "#000015"
             ],
             [
              0.5555555555555556,
              "#000016"
             ],
             [
              0.6666666666666666,
              "#000017"
             ],
             [
              0.7777777777777778,
              "#000018"
             ],
             [
              0.8888888888888888,
              "#000019"
             ],
             [
              1,
              "#000020"
             ]
            ],
            "type": "contourcarpet"
           }
          ],
          "heatmap": [
           {
            "colorscale": [
             [
              0,
              "#000011"
             ],
             [
              0.1111111111111111,
              "#000012"
             ],
             [
              0.2222222222222222,
              "#000013"
             ],
             [
              0.3333333333333333,
              "#000014"
             ],
             [
              0.4444444444444444,
              "#000015"
             ],
             [
              0.5555555555555556,
              "#000016"
             ],
             [
              0.6666666666666666,
              "#000017"
             ],
             [
              0.7777777777777778,
              "#000018"
             ],
             [
              0.8888888888888888,
              "#000019"
             ],
             [
              1,
              "#000020"
             ]
            ],
            "type": "heatmap"
           }
          ],
          "histogram2d": [
           {
            "colorscale": [
             [
              0,
              "#000011"
             ],
             [
              0.1111111111111111,
              "#000012"
             ],
             [
              0.2222222222222222,
              "#000013"
             ],
             [
              0.3333333333333333,
              "#000014"
             ],
             [
              0.4444444444444444,
              "#000015"
             ],
             [
              0.5555555555555556,
              "#000016"
             ],
             [
              0.6666666666666666,
              "#000017"
             ],
             [
              0.7777777777777778,
              "#000018"
             ],
             [
              0.8888888888888888,
              "#000019"
             ],
             [
              1,
              "#000020"
             ]
            ],
            "type": "histogram2d"
           }
          ],
          "icicle": [
           {
            "textfont": {
             "color": "white"
            },
            "type": "icicle"
           }
          ],
          "sankey": [
           {
            "textfont": {
             "color": "#000036"
            },
            "type": "sankey"
           }
          ],
          "scatter": [
           {
            "marker": {
             "line": {
              "width": 0
             }
            },
            "type": "scatter"
           }
          ],
          "table": [
           {
            "cells": {
             "fill": {
              "color": "#000038"
             },
             "font": {
              "color": "#000037"
             },
             "line": {
              "color": "#000039"
             }
            },
            "header": {
             "fill": {
              "color": "#000040"
             },
             "font": {
              "color": "#000036"
             },
             "line": {
              "color": "#000039"
             }
            },
            "type": "table"
           }
          ],
          "waterfall": [
           {
            "connector": {
             "line": {
              "color": "#000036",
              "width": 2
             }
            },
            "decreasing": {
             "marker": {
              "color": "#000033"
             }
            },
            "increasing": {
             "marker": {
              "color": "#000032"
             }
            },
            "totals": {
             "marker": {
              "color": "#000034"
             }
            },
            "type": "waterfall"
           }
          ]
         },
         "layout": {
          "coloraxis": {
           "colorscale": [
            [
             0,
             "#000011"
            ],
            [
             0.1111111111111111,
             "#000012"
            ],
            [
             0.2222222222222222,
             "#000013"
            ],
            [
             0.3333333333333333,
             "#000014"
            ],
            [
             0.4444444444444444,
             "#000015"
            ],
            [
             0.5555555555555556,
             "#000016"
            ],
            [
             0.6666666666666666,
             "#000017"
            ],
            [
             0.7777777777777778,
             "#000018"
            ],
            [
             0.8888888888888888,
             "#000019"
            ],
            [
             1,
             "#000020"
            ]
           ]
          },
          "colorscale": {
           "diverging": [
            [
             0,
             "#000021"
            ],
            [
             0.1,
             "#000022"
            ],
            [
             0.2,
             "#000023"
            ],
            [
             0.3,
             "#000024"
            ],
            [
             0.4,
             "#000025"
            ],
            [
             0.5,
             "#000026"
            ],
            [
             0.6,
             "#000027"
            ],
            [
             0.7,
             "#000028"
            ],
            [
             0.8,
             "#000029"
            ],
            [
             0.9,
             "#000030"
            ],
            [
             1,
             "#000031"
            ]
           ],
           "sequential": [
            [
             0,
             "#000011"
            ],
            [
             0.1111111111111111,
             "#000012"
            ],
            [
             0.2222222222222222,
             "#000013"
            ],
            [
             0.3333333333333333,
             "#000014"
            ],
            [
             0.4444444444444444,
             "#000015"
            ],
            [
             0.5555555555555556,
             "#000016"
            ],
            [
             0.6666666666666666,
             "#000017"
            ],
            [
             0.7777777777777778,
             "#000018"
            ],
            [
             0.8888888888888888,
             "#000019"
            ],
            [
             1,
             "#000020"
            ]
           ],
           "sequentialminus": [
            [
             0,
             "#000011"
            ],
            [
             0.1111111111111111,
             "#000012"
            ],
            [
             0.2222222222222222,
             "#000013"
            ],
            [
             0.3333333333333333,
             "#000014"
            ],
            [
             0.4444444444444444,
             "#000015"
            ],
            [
             0.5555555555555556,
             "#000016"
            ],
            [
             0.6666666666666666,
             "#000017"
            ],
            [
             0.7777777777777778,
             "#000018"
            ],
            [
             0.8888888888888888,
             "#000019"
            ],
            [
             1,
             "#000020"
            ]
           ]
          },
          "colorway": [
           "#000001",
           "#000002",
           "#000003",
           "#000004",
           "#000005",
           "#000006",
           "#000007",
           "#000008",
           "#000009",
           "#000010"
          ]
         }
        },
        "title": {
         "automargin": true,
         "font": {
          "color": "#164f5e",
          "size": 22
         },
         "text": "Batting WAR",
         "yref": "paper"
        },
        "width": 500,
        "xaxis": {
         "anchor": "y",
         "domain": [
          0,
          1
         ],
         "title": {
          "text": ""
         }
        },
        "yaxis": {
         "anchor": "x",
         "domain": [
          0,
          1
         ],
         "title": {
          "text": ""
         }
        }
       }
      },
      "text/html": [
       "<div>                            <div id=\"a347e869-be52-49f1-8fbb-03c60e89f2b6\" class=\"plotly-graph-div\" style=\"height:500px; width:500px;\"></div>            <script type=\"text/javascript\">                require([\"plotly\"], function(Plotly) {                    window.PLOTLYENV=window.PLOTLYENV || {};                                    if (document.getElementById(\"a347e869-be52-49f1-8fbb-03c60e89f2b6\")) {                    Plotly.newPlot(                        \"a347e869-be52-49f1-8fbb-03c60e89f2b6\",                        [{\"alignmentgroup\":\"True\",\"boxpoints\":\"all\",\"hovertemplate\":\"\\u003cb\\u003e%{hovertext}\\u003c\\u002fb\\u003e\\u003cbr\\u003e\\u003cbr\\u003eBat=%{y}\\u003cextra\\u003e\\u003c\\u002fextra\\u003e\",\"hovertext\":[\"Ronald Acuna Jr.\",\"Shohei Ohtani\",\"Mookie Betts\",\"Wander Franco\",\"Corbin Carroll\",\"Luis Robert\",\"Freddie Freeman\",\"Juan Soto\",\"Fernando Tatis Jr.\",\"Jose Ramirez\",\"Adolis Garcia\",\"Mike Trout\",\"Jonah Heim\",\"Marcus Semien\",\"Bo Bichette\",\"Christian Yelich\",\"Francisco Lindor\",\"Dansby Swanson\",\"Luis Arraez\",\"Will Smith\",\"Ha-seong Kim\",\"Randy Arozarena\",\"Paul Goldschmidt\",\"Matt Chapman\",\"Isaac Paredes\",\"Brandon Nimmo\",\"Jeimer Candelario\",\"Thairo Estrada\",\"Matt Olson\",\"Christian Walker\",\"Jack Suwinski\",\"Julio Rodriguez\",\"Yandy Diaz\",\"Kyle Tucker\",\"Josh Jung\",\"Ketel Marte\",\"Ozzie Albies\",\"William Contreras\",\"Xander Bogaerts\",\"Leody Taveras\",\"Adley Rutschman\",\"Nico Hoerner\",\"Lane Thomas\",\"Bobby Witt Jr.\",\"LaMonte Wade Jr.\",\"Austin Hays\",\"J.D. Davis\",\"Gunnar Henderson\",\"Alex Verdugo\",\"Nathaniel Lowe\",\"Jorge Soler\",\"Nolan Arenado\",\"Rafael Devers\",\"Austin Riley\",\"Brendan Donovan\",\"Bryson Stott\",\"Brandon Drury\",\"Brandon Marsh\",\"Ian Happ\",\"J.P. Crawford\",\"Alex Bregman\",\"Andres Gimenez\",\"Cal Raleigh\",\"Spencer Steer\",\"Nolan Gorman\",\"Ryan Noda\",\"Cedric Mullins II\",\"James Outman\",\"Nick Castellanos\",\"Pete Alonso\",\"Anthony Santander\",\"Ryan McMahon\",\"Zach McKinstry\",\"Trea Turner\",\"Anthony Volpe\",\"Masataka Yoshida\",\"Justin Turner\",\"Bryan Reynolds\",\"Manny Machado\",\"Whit Merrifield\",\"Jeremy Pena\",\"Josh Naylor\",\"Anthony Rizzo\",\"Jonathan India\",\"Jarred Kelenic\",\"George Springer\",\"Eugenio Suarez\",\"Joey Wiemer\",\"Andrew McCutchen\",\"Lourdes Gurriel Jr.\",\"Max Muncy\",\"Hunter Renfroe\",\"Mauricio Dubon\",\"Steven Kwan\",\"Tommy Edman\",\"Brent Rooker\",\"J.T. Realmuto\",\"Teoscar Hernandez\",\"Ezequiel Tovar\",\"Willson Contreras\",\"Carlos Correa\",\"Ke'Bryan Hayes\",\"Willy Adames\",\"Gleyber Torres\",\"Esteury Ruiz\",\"Marcell Ozuna\",\"Byron Buxton\",\"Andrew Benintendi\",\"Daulton Varsho\",\"J.D. Martinez\",\"Elias Diaz\",\"Ty France\",\"Taylor Ward\",\"Jeff McNeil\",\"Eddie Rosario\",\"Seiya Suzuki\",\"Carlos Santana\",\"Trent Grisham\",\"Vladimir Guerrero Jr.\",\"Michael Conforto\",\"Brian Anderson\",\"Jace Peterson\",\"Javier Baez\",\"Andrew Vaughn\",\"Alec Bohm\",\"Bryan De La Cruz\",\"Jake Cronenworth\",\"Salvador Perez\",\"CJ Abrams\",\"Spencer Torkelson\",\"Adam Frazier\",\"Miguel Vargas\",\"Amed Rosario\",\"Starling Marte\",\"Luis Garcia\",\"DJ LeMahieu\",\"Tyler Stephenson\",\"Kyle Schwarber\",\"Triston Casas\",\"Dominic Smith\",\"Shea Langeliers\",\"Josh Bell\",\"Myles Straw\",\"Joey Meneses\",\"Jose Abreu\",\"MJ Melendez\",\"Tim Anderson\",\"Rowdy Tellez\",\"Jurickson Profar\",\"Keibert Ruiz\",\"Enrique Hernandez\"],\"legendgroup\":\"\",\"marker\":{\"color\":\"#7284cc\"},\"name\":\"\",\"notched\":false,\"offsetgroup\":\"\",\"orientation\":\"v\",\"showlegend\":false,\"x0\":\" \",\"xaxis\":\"x\",\"y\":[33.5,35.2,23.8,11.0,18.8,18.6,25.8,25.0,15.1,14.2,13.7,15.8,8.6,7.2,16.5,13.1,7.8,3.5,22.8,13.7,4.2,21.1,16.0,9.4,16.5,14.8,7.7,3.1,22.2,10.4,13.6,3.0,22.2,14.4,9.5,13.6,8.7,3.4,4.6,9.8,10.6,-2.8,13.5,-3.5,15.3,11.6,8.3,7.9,7.3,9.5,16.0,10.0,7.6,3.8,7.6,1.8,8.1,4.0,8.0,9.1,3.7,0.0,0.4,13.3,6.7,11.7,5.9,1.2,12.3,10.9,10.3,1.4,0.4,-7.2,-3.7,13.7,9.7,5.8,0.1,1.7,-1.8,7.3,7.1,1.0,3.7,2.8,0.2,-6.6,9.0,4.5,5.1,1.1,-0.3,-2.2,-3.7,8.9,0.3,2.4,-6.9,1.6,-1.6,-6.6,-7.5,1.9,-6.7,6.7,3.2,-0.2,-6.5,7.1,-2.3,4.4,-2.8,-3.1,3.6,1.7,-2.1,-1.6,10.1,0.6,-4.4,-8.0,-14.8,4.0,1.2,1.5,-4.0,-2.9,-7.2,-1.2,-2.2,-6.0,-6.4,-5.5,-8.0,-7.8,-2.7,1.8,-1.4,-7.5,-7.6,-4.7,-10.8,-6.0,-9.8,-11.5,-16.7,-7.5,-8.4,-10.3,-12.1],\"y0\":\" \",\"yaxis\":\"y\",\"type\":\"box\"}],                        {\"template\":{\"data\":{\"candlestick\":[{\"decreasing\":{\"line\":{\"color\":\"#000033\"}},\"increasing\":{\"line\":{\"color\":\"#000032\"}},\"type\":\"candlestick\"}],\"contourcarpet\":[{\"colorscale\":[[0.0,\"#000011\"],[0.1111111111111111,\"#000012\"],[0.2222222222222222,\"#000013\"],[0.3333333333333333,\"#000014\"],[0.4444444444444444,\"#000015\"],[0.5555555555555556,\"#000016\"],[0.6666666666666666,\"#000017\"],[0.7777777777777778,\"#000018\"],[0.8888888888888888,\"#000019\"],[1.0,\"#000020\"]],\"type\":\"contourcarpet\"}],\"contour\":[{\"colorscale\":[[0.0,\"#000011\"],[0.1111111111111111,\"#000012\"],[0.2222222222222222,\"#000013\"],[0.3333333333333333,\"#000014\"],[0.4444444444444444,\"#000015\"],[0.5555555555555556,\"#000016\"],[0.6666666666666666,\"#000017\"],[0.7777777777777778,\"#000018\"],[0.8888888888888888,\"#000019\"],[1.0,\"#000020\"]],\"type\":\"contour\"}],\"heatmap\":[{\"colorscale\":[[0.0,\"#000011\"],[0.1111111111111111,\"#000012\"],[0.2222222222222222,\"#000013\"],[0.3333333333333333,\"#000014\"],[0.4444444444444444,\"#000015\"],[0.5555555555555556,\"#000016\"],[0.6666666666666666,\"#000017\"],[0.7777777777777778,\"#000018\"],[0.8888888888888888,\"#000019\"],[1.0,\"#000020\"]],\"type\":\"heatmap\"}],\"histogram2d\":[{\"colorscale\":[[0.0,\"#000011\"],[0.1111111111111111,\"#000012\"],[0.2222222222222222,\"#000013\"],[0.3333333333333333,\"#000014\"],[0.4444444444444444,\"#000015\"],[0.5555555555555556,\"#000016\"],[0.6666666666666666,\"#000017\"],[0.7777777777777778,\"#000018\"],[0.8888888888888888,\"#000019\"],[1.0,\"#000020\"]],\"type\":\"histogram2d\"}],\"icicle\":[{\"textfont\":{\"color\":\"white\"},\"type\":\"icicle\"}],\"sankey\":[{\"textfont\":{\"color\":\"#000036\"},\"type\":\"sankey\"}],\"scatter\":[{\"marker\":{\"line\":{\"width\":0}},\"type\":\"scatter\"}],\"table\":[{\"cells\":{\"fill\":{\"color\":\"#000038\"},\"font\":{\"color\":\"#000037\"},\"line\":{\"color\":\"#000039\"}},\"header\":{\"fill\":{\"color\":\"#000040\"},\"font\":{\"color\":\"#000036\"},\"line\":{\"color\":\"#000039\"}},\"type\":\"table\"}],\"waterfall\":[{\"connector\":{\"line\":{\"color\":\"#000036\",\"width\":2}},\"decreasing\":{\"marker\":{\"color\":\"#000033\"}},\"increasing\":{\"marker\":{\"color\":\"#000032\"}},\"totals\":{\"marker\":{\"color\":\"#000034\"}},\"type\":\"waterfall\"}]},\"layout\":{\"coloraxis\":{\"colorscale\":[[0.0,\"#000011\"],[0.1111111111111111,\"#000012\"],[0.2222222222222222,\"#000013\"],[0.3333333333333333,\"#000014\"],[0.4444444444444444,\"#000015\"],[0.5555555555555556,\"#000016\"],[0.6666666666666666,\"#000017\"],[0.7777777777777778,\"#000018\"],[0.8888888888888888,\"#000019\"],[1.0,\"#000020\"]]},\"colorscale\":{\"diverging\":[[0.0,\"#000021\"],[0.1,\"#000022\"],[0.2,\"#000023\"],[0.3,\"#000024\"],[0.4,\"#000025\"],[0.5,\"#000026\"],[0.6,\"#000027\"],[0.7,\"#000028\"],[0.8,\"#000029\"],[0.9,\"#000030\"],[1.0,\"#000031\"]],\"sequential\":[[0.0,\"#000011\"],[0.1111111111111111,\"#000012\"],[0.2222222222222222,\"#000013\"],[0.3333333333333333,\"#000014\"],[0.4444444444444444,\"#000015\"],[0.5555555555555556,\"#000016\"],[0.6666666666666666,\"#000017\"],[0.7777777777777778,\"#000018\"],[0.8888888888888888,\"#000019\"],[1.0,\"#000020\"]],\"sequentialminus\":[[0.0,\"#000011\"],[0.1111111111111111,\"#000012\"],[0.2222222222222222,\"#000013\"],[0.3333333333333333,\"#000014\"],[0.4444444444444444,\"#000015\"],[0.5555555555555556,\"#000016\"],[0.6666666666666666,\"#000017\"],[0.7777777777777778,\"#000018\"],[0.8888888888888888,\"#000019\"],[1.0,\"#000020\"]]},\"colorway\":[\"#000001\",\"#000002\",\"#000003\",\"#000004\",\"#000005\",\"#000006\",\"#000007\",\"#000008\",\"#000009\",\"#000010\"]}},\"xaxis\":{\"anchor\":\"y\",\"domain\":[0.0,1.0],\"title\":{\"text\":\"\"}},\"yaxis\":{\"anchor\":\"x\",\"domain\":[0.0,1.0],\"title\":{\"text\":\"\"}},\"legend\":{\"tracegroupgap\":0},\"margin\":{\"t\":60},\"boxmode\":\"group\",\"height\":500,\"width\":500,\"title\":{\"font\":{\"size\":22,\"color\":\"#164f5e\"},\"text\":\"Batting WAR\",\"automargin\":true,\"yref\":\"paper\"}},                        {\"responsive\": true}                    ).then(function(){\n",
       "                            \n",
       "var gd = document.getElementById('a347e869-be52-49f1-8fbb-03c60e89f2b6');\n",
       "var x = new MutationObserver(function (mutations, observer) {{\n",
       "        var display = window.getComputedStyle(gd).display;\n",
       "        if (!display || display === 'none') {{\n",
       "            console.log([gd, 'removed!']);\n",
       "            Plotly.purge(gd);\n",
       "            observer.disconnect();\n",
       "        }}\n",
       "}});\n",
       "\n",
       "// Listen for the removal of the full notebook cells\n",
       "var notebookContainer = gd.closest('#notebook-container');\n",
       "if (notebookContainer) {{\n",
       "    x.observe(notebookContainer, {childList: true});\n",
       "}}\n",
       "\n",
       "// Listen for the clearing of the current output cell\n",
       "var outputEl = gd.closest('.output');\n",
       "if (outputEl) {{\n",
       "    x.observe(outputEl, {childList: true});\n",
       "}}\n",
       "\n",
       "                        })                };                });            </script>        </div>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "fig_12 = px.box(\n",
    "    df.query(\"Season==2023\"),\n",
    "    y = \"Bat\",\n",
    "    points=\"all\",\n",
    "    hover_name = \"Name\",\n",
    "    height = 500,\n",
    "    width = 500,\n",
    ")\n",
    "\n",
    "fig_12.update_traces(marker=dict(color=\"#7284cc\"))\n",
    "\n",
    "fig_12.update_layout(\n",
    "    title=dict(text=\"Batting WAR\", font=dict(size=22), automargin=True, yref='paper'),\n",
    "    title_font_color=\"#164f5e\",\n",
    "    yaxis=dict(title=\"\"),\n",
    "    xaxis=dict(title=\"\")\n",
    ")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 89,
   "id": "911a887a",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "application/vnd.plotly.v1+json": {
       "config": {
        "plotlyServerURL": "https://plot.ly"
       },
       "data": [
        {
         "alignmentgroup": "True",
         "boxpoints": "all",
         "hovertemplate": "<b>%{hovertext}</b><br><br>Pos=%{y}<extra></extra>",
         "hovertext": [
          "Ronald Acuna Jr.",
          "Shohei Ohtani",
          "Mookie Betts",
          "Wander Franco",
          "Corbin Carroll",
          "Luis Robert",
          "Freddie Freeman",
          "Juan Soto",
          "Fernando Tatis Jr.",
          "Jose Ramirez",
          "Adolis Garcia",
          "Mike Trout",
          "Jonah Heim",
          "Marcus Semien",
          "Bo Bichette",
          "Christian Yelich",
          "Francisco Lindor",
          "Dansby Swanson",
          "Luis Arraez",
          "Will Smith",
          "Ha-seong Kim",
          "Randy Arozarena",
          "Paul Goldschmidt",
          "Matt Chapman",
          "Isaac Paredes",
          "Brandon Nimmo",
          "Jeimer Candelario",
          "Thairo Estrada",
          "Matt Olson",
          "Christian Walker",
          "Jack Suwinski",
          "Julio Rodriguez",
          "Yandy Diaz",
          "Kyle Tucker",
          "Josh Jung",
          "Ketel Marte",
          "Ozzie Albies",
          "William Contreras",
          "Xander Bogaerts",
          "Leody Taveras",
          "Adley Rutschman",
          "Nico Hoerner",
          "Lane Thomas",
          "Bobby Witt Jr.",
          "LaMonte Wade Jr.",
          "Austin Hays",
          "J.D. Davis",
          "Gunnar Henderson",
          "Alex Verdugo",
          "Nathaniel Lowe",
          "Jorge Soler",
          "Nolan Arenado",
          "Rafael Devers",
          "Austin Riley",
          "Brendan Donovan",
          "Bryson Stott",
          "Brandon Drury",
          "Brandon Marsh",
          "Ian Happ",
          "J.P. Crawford",
          "Alex Bregman",
          "Andres Gimenez",
          "Cal Raleigh",
          "Spencer Steer",
          "Nolan Gorman",
          "Ryan Noda",
          "Cedric Mullins II",
          "James Outman",
          "Nick Castellanos",
          "Pete Alonso",
          "Anthony Santander",
          "Ryan McMahon",
          "Zach McKinstry",
          "Trea Turner",
          "Anthony Volpe",
          "Masataka Yoshida",
          "Justin Turner",
          "Bryan Reynolds",
          "Manny Machado",
          "Whit Merrifield",
          "Jeremy Pena",
          "Josh Naylor",
          "Anthony Rizzo",
          "Jonathan India",
          "Jarred Kelenic",
          "George Springer",
          "Eugenio Suarez",
          "Joey Wiemer",
          "Andrew McCutchen",
          "Lourdes Gurriel Jr.",
          "Max Muncy",
          "Hunter Renfroe",
          "Mauricio Dubon",
          "Steven Kwan",
          "Tommy Edman",
          "Brent Rooker",
          "J.T. Realmuto",
          "Teoscar Hernandez",
          "Ezequiel Tovar",
          "Willson Contreras",
          "Carlos Correa",
          "Ke'Bryan Hayes",
          "Willy Adames",
          "Gleyber Torres",
          "Esteury Ruiz",
          "Marcell Ozuna",
          "Byron Buxton",
          "Andrew Benintendi",
          "Daulton Varsho",
          "J.D. Martinez",
          "Elias Diaz",
          "Ty France",
          "Taylor Ward",
          "Jeff McNeil",
          "Eddie Rosario",
          "Seiya Suzuki",
          "Carlos Santana",
          "Trent Grisham",
          "Vladimir Guerrero Jr.",
          "Michael Conforto",
          "Brian Anderson",
          "Jace Peterson",
          "Javier Baez",
          "Andrew Vaughn",
          "Alec Bohm",
          "Bryan De La Cruz",
          "Jake Cronenworth",
          "Salvador Perez",
          "CJ Abrams",
          "Spencer Torkelson",
          "Adam Frazier",
          "Miguel Vargas",
          "Amed Rosario",
          "Starling Marte",
          "Luis Garcia",
          "DJ LeMahieu",
          "Tyler Stephenson",
          "Kyle Schwarber",
          "Triston Casas",
          "Dominic Smith",
          "Shea Langeliers",
          "Josh Bell",
          "Myles Straw",
          "Joey Meneses",
          "Jose Abreu",
          "MJ Melendez",
          "Tim Anderson",
          "Rowdy Tellez",
          "Jurickson Profar",
          "Keibert Ruiz",
          "Enrique Hernandez"
         ],
         "legendgroup": "",
         "marker": {
          "color": "#7284cc"
         },
         "name": "",
         "notched": false,
         "offsetgroup": "",
         "orientation": "v",
         "showlegend": false,
         "type": "box",
         "x0": " ",
         "xaxis": "x",
         "y": [
          -3.9,
          -9.4,
          -1.7,
          3.5,
          -2.6,
          1.3,
          -6.5,
          -3.9,
          -3,
          -0.2,
          -3.7,
          0.9,
          4.4,
          1.3,
          3.6,
          -4.1,
          3.7,
          3.7,
          0.9,
          3.7,
          1.5,
          -4.4,
          -6.6,
          1,
          0.4,
          0.9,
          1.2,
          1.1,
          -6.6,
          -6.4,
          0.2,
          0.9,
          -5.2,
          -4,
          1.3,
          0.8,
          1.3,
          3.1,
          3.1,
          1,
          2.5,
          1.2,
          -3.8,
          2.3,
          -4.8,
          -3.4,
          -0.5,
          0.8,
          -3.5,
          -6.5,
          -7.4,
          0.2,
          1.1,
          1.3,
          -1.6,
          1.2,
          -1.1,
          1.1,
          -3.9,
          3.6,
          1.2,
          1.2,
          3.8,
          -4.3,
          -2.2,
          -5.4,
          0.7,
          0.3,
          -4.1,
          -5.9,
          -5.4,
          1.2,
          -1,
          3.7,
          3.8,
          -5,
          -7.5,
          -3.3,
          0.7,
          -1,
          3.6,
          -6,
          -6.3,
          -0.3,
          -3.5,
          -4.3,
          0.9,
          0.5,
          -7.1,
          -5,
          0.7,
          -3.6,
          0.8,
          -3.9,
          1.7,
          -5.6,
          5.5,
          -4.7,
          3.6,
          2.1,
          3.4,
          1.1,
          3.2,
          0,
          1,
          -7.3,
          -7.1,
          -3.6,
          -2.2,
          -7.5,
          4.4,
          -6.1,
          -3.4,
          0.1,
          -3.8,
          -3.1,
          -6,
          1.2,
          -7,
          -3.5,
          -1.2,
          0.9,
          3.1,
          -6.6,
          -3,
          -3.6,
          -4.9,
          1.9,
          3.5,
          -6.5,
          0.6,
          0.8,
          3.2,
          -3.3,
          1.1,
          -0.4,
          -1.8,
          -5,
          -5.3,
          -6.2,
          4.2,
          -7.5,
          1.3,
          -8.4,
          -6.6,
          -2.7,
          2.6,
          -5.5,
          -3.7,
          4.7,
          2.7
         ],
         "y0": " ",
         "yaxis": "y"
        }
       ],
       "layout": {
        "boxmode": "group",
        "height": 500,
        "legend": {
         "tracegroupgap": 0
        },
        "margin": {
         "t": 60
        },
        "template": {
         "data": {
          "candlestick": [
           {
            "decreasing": {
             "line": {
              "color": "#000033"
             }
            },
            "increasing": {
             "line": {
              "color": "#000032"
             }
            },
            "type": "candlestick"
           }
          ],
          "contour": [
           {
            "colorscale": [
             [
              0,
              "#000011"
             ],
             [
              0.1111111111111111,
              "#000012"
             ],
             [
              0.2222222222222222,
              "#000013"
             ],
             [
              0.3333333333333333,
              "#000014"
             ],
             [
              0.4444444444444444,
              "#000015"
             ],
             [
              0.5555555555555556,
              "#000016"
             ],
             [
              0.6666666666666666,
              "#000017"
             ],
             [
              0.7777777777777778,
              "#000018"
             ],
             [
              0.8888888888888888,
              "#000019"
             ],
             [
              1,
              "#000020"
             ]
            ],
            "type": "contour"
           }
          ],
          "contourcarpet": [
           {
            "colorscale": [
             [
              0,
              "#000011"
             ],
             [
              0.1111111111111111,
              "#000012"
             ],
             [
              0.2222222222222222,
              "#000013"
             ],
             [
              0.3333333333333333,
              "#000014"
             ],
             [
              0.4444444444444444,
              "#000015"
             ],
             [
              0.5555555555555556,
              "#000016"
             ],
             [
              0.6666666666666666,
              "#000017"
             ],
             [
              0.7777777777777778,
              "#000018"
             ],
             [
              0.8888888888888888,
              "#000019"
             ],
             [
              1,
              "#000020"
             ]
            ],
            "type": "contourcarpet"
           }
          ],
          "heatmap": [
           {
            "colorscale": [
             [
              0,
              "#000011"
             ],
             [
              0.1111111111111111,
              "#000012"
             ],
             [
              0.2222222222222222,
              "#000013"
             ],
             [
              0.3333333333333333,
              "#000014"
             ],
             [
              0.4444444444444444,
              "#000015"
             ],
             [
              0.5555555555555556,
              "#000016"
             ],
             [
              0.6666666666666666,
              "#000017"
             ],
             [
              0.7777777777777778,
              "#000018"
             ],
             [
              0.8888888888888888,
              "#000019"
             ],
             [
              1,
              "#000020"
             ]
            ],
            "type": "heatmap"
           }
          ],
          "histogram2d": [
           {
            "colorscale": [
             [
              0,
              "#000011"
             ],
             [
              0.1111111111111111,
              "#000012"
             ],
             [
              0.2222222222222222,
              "#000013"
             ],
             [
              0.3333333333333333,
              "#000014"
             ],
             [
              0.4444444444444444,
              "#000015"
             ],
             [
              0.5555555555555556,
              "#000016"
             ],
             [
              0.6666666666666666,
              "#000017"
             ],
             [
              0.7777777777777778,
              "#000018"
             ],
             [
              0.8888888888888888,
              "#000019"
             ],
             [
              1,
              "#000020"
             ]
            ],
            "type": "histogram2d"
           }
          ],
          "icicle": [
           {
            "textfont": {
             "color": "white"
            },
            "type": "icicle"
           }
          ],
          "sankey": [
           {
            "textfont": {
             "color": "#000036"
            },
            "type": "sankey"
           }
          ],
          "scatter": [
           {
            "marker": {
             "line": {
              "width": 0
             }
            },
            "type": "scatter"
           }
          ],
          "table": [
           {
            "cells": {
             "fill": {
              "color": "#000038"
             },
             "font": {
              "color": "#000037"
             },
             "line": {
              "color": "#000039"
             }
            },
            "header": {
             "fill": {
              "color": "#000040"
             },
             "font": {
              "color": "#000036"
             },
             "line": {
              "color": "#000039"
             }
            },
            "type": "table"
           }
          ],
          "waterfall": [
           {
            "connector": {
             "line": {
              "color": "#000036",
              "width": 2
             }
            },
            "decreasing": {
             "marker": {
              "color": "#000033"
             }
            },
            "increasing": {
             "marker": {
              "color": "#000032"
             }
            },
            "totals": {
             "marker": {
              "color": "#000034"
             }
            },
            "type": "waterfall"
           }
          ]
         },
         "layout": {
          "coloraxis": {
           "colorscale": [
            [
             0,
             "#000011"
            ],
            [
             0.1111111111111111,
             "#000012"
            ],
            [
             0.2222222222222222,
             "#000013"
            ],
            [
             0.3333333333333333,
             "#000014"
            ],
            [
             0.4444444444444444,
             "#000015"
            ],
            [
             0.5555555555555556,
             "#000016"
            ],
            [
             0.6666666666666666,
             "#000017"
            ],
            [
             0.7777777777777778,
             "#000018"
            ],
            [
             0.8888888888888888,
             "#000019"
            ],
            [
             1,
             "#000020"
            ]
           ]
          },
          "colorscale": {
           "diverging": [
            [
             0,
             "#000021"
            ],
            [
             0.1,
             "#000022"
            ],
            [
             0.2,
             "#000023"
            ],
            [
             0.3,
             "#000024"
            ],
            [
             0.4,
             "#000025"
            ],
            [
             0.5,
             "#000026"
            ],
            [
             0.6,
             "#000027"
            ],
            [
             0.7,
             "#000028"
            ],
            [
             0.8,
             "#000029"
            ],
            [
             0.9,
             "#000030"
            ],
            [
             1,
             "#000031"
            ]
           ],
           "sequential": [
            [
             0,
             "#000011"
            ],
            [
             0.1111111111111111,
             "#000012"
            ],
            [
             0.2222222222222222,
             "#000013"
            ],
            [
             0.3333333333333333,
             "#000014"
            ],
            [
             0.4444444444444444,
             "#000015"
            ],
            [
             0.5555555555555556,
             "#000016"
            ],
            [
             0.6666666666666666,
             "#000017"
            ],
            [
             0.7777777777777778,
             "#000018"
            ],
            [
             0.8888888888888888,
             "#000019"
            ],
            [
             1,
             "#000020"
            ]
           ],
           "sequentialminus": [
            [
             0,
             "#000011"
            ],
            [
             0.1111111111111111,
             "#000012"
            ],
            [
             0.2222222222222222,
             "#000013"
            ],
            [
             0.3333333333333333,
             "#000014"
            ],
            [
             0.4444444444444444,
             "#000015"
            ],
            [
             0.5555555555555556,
             "#000016"
            ],
            [
             0.6666666666666666,
             "#000017"
            ],
            [
             0.7777777777777778,
             "#000018"
            ],
            [
             0.8888888888888888,
             "#000019"
            ],
            [
             1,
             "#000020"
            ]
           ]
          },
          "colorway": [
           "#000001",
           "#000002",
           "#000003",
           "#000004",
           "#000005",
           "#000006",
           "#000007",
           "#000008",
           "#000009",
           "#000010"
          ]
         }
        },
        "title": {
         "automargin": true,
         "font": {
          "color": "#164f5e",
          "size": 22
         },
         "text": "Positon Batting WAR",
         "yref": "paper"
        },
        "width": 500,
        "xaxis": {
         "anchor": "y",
         "domain": [
          0,
          1
         ],
         "title": {
          "text": ""
         }
        },
        "yaxis": {
         "anchor": "x",
         "domain": [
          0,
          1
         ],
         "title": {
          "text": ""
         }
        }
       }
      },
      "text/html": [
       "<div>                            <div id=\"80b7f94f-3b70-41c2-b67c-6b0daefc737d\" class=\"plotly-graph-div\" style=\"height:500px; width:500px;\"></div>            <script type=\"text/javascript\">                require([\"plotly\"], function(Plotly) {                    window.PLOTLYENV=window.PLOTLYENV || {};                                    if (document.getElementById(\"80b7f94f-3b70-41c2-b67c-6b0daefc737d\")) {                    Plotly.newPlot(                        \"80b7f94f-3b70-41c2-b67c-6b0daefc737d\",                        [{\"alignmentgroup\":\"True\",\"boxpoints\":\"all\",\"hovertemplate\":\"\\u003cb\\u003e%{hovertext}\\u003c\\u002fb\\u003e\\u003cbr\\u003e\\u003cbr\\u003ePos=%{y}\\u003cextra\\u003e\\u003c\\u002fextra\\u003e\",\"hovertext\":[\"Ronald Acuna Jr.\",\"Shohei Ohtani\",\"Mookie Betts\",\"Wander Franco\",\"Corbin Carroll\",\"Luis Robert\",\"Freddie Freeman\",\"Juan Soto\",\"Fernando Tatis Jr.\",\"Jose Ramirez\",\"Adolis Garcia\",\"Mike Trout\",\"Jonah Heim\",\"Marcus Semien\",\"Bo Bichette\",\"Christian Yelich\",\"Francisco Lindor\",\"Dansby Swanson\",\"Luis Arraez\",\"Will Smith\",\"Ha-seong Kim\",\"Randy Arozarena\",\"Paul Goldschmidt\",\"Matt Chapman\",\"Isaac Paredes\",\"Brandon Nimmo\",\"Jeimer Candelario\",\"Thairo Estrada\",\"Matt Olson\",\"Christian Walker\",\"Jack Suwinski\",\"Julio Rodriguez\",\"Yandy Diaz\",\"Kyle Tucker\",\"Josh Jung\",\"Ketel Marte\",\"Ozzie Albies\",\"William Contreras\",\"Xander Bogaerts\",\"Leody Taveras\",\"Adley Rutschman\",\"Nico Hoerner\",\"Lane Thomas\",\"Bobby Witt Jr.\",\"LaMonte Wade Jr.\",\"Austin Hays\",\"J.D. Davis\",\"Gunnar Henderson\",\"Alex Verdugo\",\"Nathaniel Lowe\",\"Jorge Soler\",\"Nolan Arenado\",\"Rafael Devers\",\"Austin Riley\",\"Brendan Donovan\",\"Bryson Stott\",\"Brandon Drury\",\"Brandon Marsh\",\"Ian Happ\",\"J.P. Crawford\",\"Alex Bregman\",\"Andres Gimenez\",\"Cal Raleigh\",\"Spencer Steer\",\"Nolan Gorman\",\"Ryan Noda\",\"Cedric Mullins II\",\"James Outman\",\"Nick Castellanos\",\"Pete Alonso\",\"Anthony Santander\",\"Ryan McMahon\",\"Zach McKinstry\",\"Trea Turner\",\"Anthony Volpe\",\"Masataka Yoshida\",\"Justin Turner\",\"Bryan Reynolds\",\"Manny Machado\",\"Whit Merrifield\",\"Jeremy Pena\",\"Josh Naylor\",\"Anthony Rizzo\",\"Jonathan India\",\"Jarred Kelenic\",\"George Springer\",\"Eugenio Suarez\",\"Joey Wiemer\",\"Andrew McCutchen\",\"Lourdes Gurriel Jr.\",\"Max Muncy\",\"Hunter Renfroe\",\"Mauricio Dubon\",\"Steven Kwan\",\"Tommy Edman\",\"Brent Rooker\",\"J.T. Realmuto\",\"Teoscar Hernandez\",\"Ezequiel Tovar\",\"Willson Contreras\",\"Carlos Correa\",\"Ke'Bryan Hayes\",\"Willy Adames\",\"Gleyber Torres\",\"Esteury Ruiz\",\"Marcell Ozuna\",\"Byron Buxton\",\"Andrew Benintendi\",\"Daulton Varsho\",\"J.D. Martinez\",\"Elias Diaz\",\"Ty France\",\"Taylor Ward\",\"Jeff McNeil\",\"Eddie Rosario\",\"Seiya Suzuki\",\"Carlos Santana\",\"Trent Grisham\",\"Vladimir Guerrero Jr.\",\"Michael Conforto\",\"Brian Anderson\",\"Jace Peterson\",\"Javier Baez\",\"Andrew Vaughn\",\"Alec Bohm\",\"Bryan De La Cruz\",\"Jake Cronenworth\",\"Salvador Perez\",\"CJ Abrams\",\"Spencer Torkelson\",\"Adam Frazier\",\"Miguel Vargas\",\"Amed Rosario\",\"Starling Marte\",\"Luis Garcia\",\"DJ LeMahieu\",\"Tyler Stephenson\",\"Kyle Schwarber\",\"Triston Casas\",\"Dominic Smith\",\"Shea Langeliers\",\"Josh Bell\",\"Myles Straw\",\"Joey Meneses\",\"Jose Abreu\",\"MJ Melendez\",\"Tim Anderson\",\"Rowdy Tellez\",\"Jurickson Profar\",\"Keibert Ruiz\",\"Enrique Hernandez\"],\"legendgroup\":\"\",\"marker\":{\"color\":\"#7284cc\"},\"name\":\"\",\"notched\":false,\"offsetgroup\":\"\",\"orientation\":\"v\",\"showlegend\":false,\"x0\":\" \",\"xaxis\":\"x\",\"y\":[-3.9,-9.4,-1.7,3.5,-2.6,1.3,-6.5,-3.9,-3.0,-0.2,-3.7,0.9,4.4,1.3,3.6,-4.1,3.7,3.7,0.9,3.7,1.5,-4.4,-6.6,1.0,0.4,0.9,1.2,1.1,-6.6,-6.4,0.2,0.9,-5.2,-4.0,1.3,0.8,1.3,3.1,3.1,1.0,2.5,1.2,-3.8,2.3,-4.8,-3.4,-0.5,0.8,-3.5,-6.5,-7.4,0.2,1.1,1.3,-1.6,1.2,-1.1,1.1,-3.9,3.6,1.2,1.2,3.8,-4.3,-2.2,-5.4,0.7,0.3,-4.1,-5.9,-5.4,1.2,-1.0,3.7,3.8,-5.0,-7.5,-3.3,0.7,-1.0,3.6,-6.0,-6.3,-0.3,-3.5,-4.3,0.9,0.5,-7.1,-5.0,0.7,-3.6,0.8,-3.9,1.7,-5.6,5.5,-4.7,3.6,2.1,3.4,1.1,3.2,0.0,1.0,-7.3,-7.1,-3.6,-2.2,-7.5,4.4,-6.1,-3.4,0.1,-3.8,-3.1,-6.0,1.2,-7.0,-3.5,-1.2,0.9,3.1,-6.6,-3.0,-3.6,-4.9,1.9,3.5,-6.5,0.6,0.8,3.2,-3.3,1.1,-0.4,-1.8,-5.0,-5.3,-6.2,4.2,-7.5,1.3,-8.4,-6.6,-2.7,2.6,-5.5,-3.7,4.7,2.7],\"y0\":\" \",\"yaxis\":\"y\",\"type\":\"box\"}],                        {\"template\":{\"data\":{\"candlestick\":[{\"decreasing\":{\"line\":{\"color\":\"#000033\"}},\"increasing\":{\"line\":{\"color\":\"#000032\"}},\"type\":\"candlestick\"}],\"contourcarpet\":[{\"colorscale\":[[0.0,\"#000011\"],[0.1111111111111111,\"#000012\"],[0.2222222222222222,\"#000013\"],[0.3333333333333333,\"#000014\"],[0.4444444444444444,\"#000015\"],[0.5555555555555556,\"#000016\"],[0.6666666666666666,\"#000017\"],[0.7777777777777778,\"#000018\"],[0.8888888888888888,\"#000019\"],[1.0,\"#000020\"]],\"type\":\"contourcarpet\"}],\"contour\":[{\"colorscale\":[[0.0,\"#000011\"],[0.1111111111111111,\"#000012\"],[0.2222222222222222,\"#000013\"],[0.3333333333333333,\"#000014\"],[0.4444444444444444,\"#000015\"],[0.5555555555555556,\"#000016\"],[0.6666666666666666,\"#000017\"],[0.7777777777777778,\"#000018\"],[0.8888888888888888,\"#000019\"],[1.0,\"#000020\"]],\"type\":\"contour\"}],\"heatmap\":[{\"colorscale\":[[0.0,\"#000011\"],[0.1111111111111111,\"#000012\"],[0.2222222222222222,\"#000013\"],[0.3333333333333333,\"#000014\"],[0.4444444444444444,\"#000015\"],[0.5555555555555556,\"#000016\"],[0.6666666666666666,\"#000017\"],[0.7777777777777778,\"#000018\"],[0.8888888888888888,\"#000019\"],[1.0,\"#000020\"]],\"type\":\"heatmap\"}],\"histogram2d\":[{\"colorscale\":[[0.0,\"#000011\"],[0.1111111111111111,\"#000012\"],[0.2222222222222222,\"#000013\"],[0.3333333333333333,\"#000014\"],[0.4444444444444444,\"#000015\"],[0.5555555555555556,\"#000016\"],[0.6666666666666666,\"#000017\"],[0.7777777777777778,\"#000018\"],[0.8888888888888888,\"#000019\"],[1.0,\"#000020\"]],\"type\":\"histogram2d\"}],\"icicle\":[{\"textfont\":{\"color\":\"white\"},\"type\":\"icicle\"}],\"sankey\":[{\"textfont\":{\"color\":\"#000036\"},\"type\":\"sankey\"}],\"scatter\":[{\"marker\":{\"line\":{\"width\":0}},\"type\":\"scatter\"}],\"table\":[{\"cells\":{\"fill\":{\"color\":\"#000038\"},\"font\":{\"color\":\"#000037\"},\"line\":{\"color\":\"#000039\"}},\"header\":{\"fill\":{\"color\":\"#000040\"},\"font\":{\"color\":\"#000036\"},\"line\":{\"color\":\"#000039\"}},\"type\":\"table\"}],\"waterfall\":[{\"connector\":{\"line\":{\"color\":\"#000036\",\"width\":2}},\"decreasing\":{\"marker\":{\"color\":\"#000033\"}},\"increasing\":{\"marker\":{\"color\":\"#000032\"}},\"totals\":{\"marker\":{\"color\":\"#000034\"}},\"type\":\"waterfall\"}]},\"layout\":{\"coloraxis\":{\"colorscale\":[[0.0,\"#000011\"],[0.1111111111111111,\"#000012\"],[0.2222222222222222,\"#000013\"],[0.3333333333333333,\"#000014\"],[0.4444444444444444,\"#000015\"],[0.5555555555555556,\"#000016\"],[0.6666666666666666,\"#000017\"],[0.7777777777777778,\"#000018\"],[0.8888888888888888,\"#000019\"],[1.0,\"#000020\"]]},\"colorscale\":{\"diverging\":[[0.0,\"#000021\"],[0.1,\"#000022\"],[0.2,\"#000023\"],[0.3,\"#000024\"],[0.4,\"#000025\"],[0.5,\"#000026\"],[0.6,\"#000027\"],[0.7,\"#000028\"],[0.8,\"#000029\"],[0.9,\"#000030\"],[1.0,\"#000031\"]],\"sequential\":[[0.0,\"#000011\"],[0.1111111111111111,\"#000012\"],[0.2222222222222222,\"#000013\"],[0.3333333333333333,\"#000014\"],[0.4444444444444444,\"#000015\"],[0.5555555555555556,\"#000016\"],[0.6666666666666666,\"#000017\"],[0.7777777777777778,\"#000018\"],[0.8888888888888888,\"#000019\"],[1.0,\"#000020\"]],\"sequentialminus\":[[0.0,\"#000011\"],[0.1111111111111111,\"#000012\"],[0.2222222222222222,\"#000013\"],[0.3333333333333333,\"#000014\"],[0.4444444444444444,\"#000015\"],[0.5555555555555556,\"#000016\"],[0.6666666666666666,\"#000017\"],[0.7777777777777778,\"#000018\"],[0.8888888888888888,\"#000019\"],[1.0,\"#000020\"]]},\"colorway\":[\"#000001\",\"#000002\",\"#000003\",\"#000004\",\"#000005\",\"#000006\",\"#000007\",\"#000008\",\"#000009\",\"#000010\"]}},\"xaxis\":{\"anchor\":\"y\",\"domain\":[0.0,1.0],\"title\":{\"text\":\"\"}},\"yaxis\":{\"anchor\":\"x\",\"domain\":[0.0,1.0],\"title\":{\"text\":\"\"}},\"legend\":{\"tracegroupgap\":0},\"margin\":{\"t\":60},\"boxmode\":\"group\",\"height\":500,\"width\":500,\"title\":{\"font\":{\"size\":22,\"color\":\"#164f5e\"},\"text\":\"Positon Batting WAR\",\"automargin\":true,\"yref\":\"paper\"}},                        {\"responsive\": true}                    ).then(function(){\n",
       "                            \n",
       "var gd = document.getElementById('80b7f94f-3b70-41c2-b67c-6b0daefc737d');\n",
       "var x = new MutationObserver(function (mutations, observer) {{\n",
       "        var display = window.getComputedStyle(gd).display;\n",
       "        if (!display || display === 'none') {{\n",
       "            console.log([gd, 'removed!']);\n",
       "            Plotly.purge(gd);\n",
       "            observer.disconnect();\n",
       "        }}\n",
       "}});\n",
       "\n",
       "// Listen for the removal of the full notebook cells\n",
       "var notebookContainer = gd.closest('#notebook-container');\n",
       "if (notebookContainer) {{\n",
       "    x.observe(notebookContainer, {childList: true});\n",
       "}}\n",
       "\n",
       "// Listen for the clearing of the current output cell\n",
       "var outputEl = gd.closest('.output');\n",
       "if (outputEl) {{\n",
       "    x.observe(outputEl, {childList: true});\n",
       "}}\n",
       "\n",
       "                        })                };                });            </script>        </div>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "fig_13 = px.box(\n",
    "    df.query(\"Season==2023\"),\n",
    "    y = \"Pos\",\n",
    "    points=\"all\",\n",
    "    hover_name = \"Name\",\n",
    "    height = 500,\n",
    "    width = 500,\n",
    ")\n",
    "\n",
    "fig_13.update_traces(marker=dict(color=\"#7284cc\"))\n",
    "\n",
    "fig_13.update_layout(\n",
    "    title=dict(text=\"Positon Batting WAR\", font=dict(size=22), automargin=True, yref='paper'),\n",
    "    title_font_color=\"#164f5e\",\n",
    "    yaxis=dict(title=\"\"),\n",
    "    xaxis=dict(title=\"\")\n",
    ")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "72ad313a",
   "metadata": {},
   "source": [
    "### Row 1 - Tab 2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 90,
   "id": "16906dae",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "application/vnd.plotly.v1+json": {
       "config": {
        "plotlyServerURL": "https://plot.ly"
       },
       "data": [
        {
         "alignmentgroup": "True",
         "boxpoints": "all",
         "hovertemplate": "<b>%{hovertext}</b><br><br>Soft%+=%{y}<extra></extra>",
         "hovertext": [
          "Ronald Acuna Jr.",
          "Shohei Ohtani",
          "Mookie Betts",
          "Wander Franco",
          "Corbin Carroll",
          "Luis Robert",
          "Freddie Freeman",
          "Juan Soto",
          "Fernando Tatis Jr.",
          "Jose Ramirez",
          "Adolis Garcia",
          "Mike Trout",
          "Jonah Heim",
          "Marcus Semien",
          "Bo Bichette",
          "Christian Yelich",
          "Francisco Lindor",
          "Dansby Swanson",
          "Luis Arraez",
          "Will Smith",
          "Ha-seong Kim",
          "Randy Arozarena",
          "Paul Goldschmidt",
          "Matt Chapman",
          "Isaac Paredes",
          "Brandon Nimmo",
          "Jeimer Candelario",
          "Thairo Estrada",
          "Matt Olson",
          "Christian Walker",
          "Jack Suwinski",
          "Julio Rodriguez",
          "Yandy Diaz",
          "Kyle Tucker",
          "Josh Jung",
          "Ketel Marte",
          "Ozzie Albies",
          "William Contreras",
          "Xander Bogaerts",
          "Leody Taveras",
          "Adley Rutschman",
          "Nico Hoerner",
          "Lane Thomas",
          "Bobby Witt Jr.",
          "LaMonte Wade Jr.",
          "Austin Hays",
          "J.D. Davis",
          "Gunnar Henderson",
          "Alex Verdugo",
          "Nathaniel Lowe",
          "Jorge Soler",
          "Nolan Arenado",
          "Rafael Devers",
          "Austin Riley",
          "Brendan Donovan",
          "Bryson Stott",
          "Brandon Drury",
          "Brandon Marsh",
          "Ian Happ",
          "J.P. Crawford",
          "Alex Bregman",
          "Andres Gimenez",
          "Cal Raleigh",
          "Spencer Steer",
          "Nolan Gorman",
          "Ryan Noda",
          "Cedric Mullins II",
          "James Outman",
          "Nick Castellanos",
          "Pete Alonso",
          "Anthony Santander",
          "Ryan McMahon",
          "Zach McKinstry",
          "Trea Turner",
          "Anthony Volpe",
          "Masataka Yoshida",
          "Justin Turner",
          "Bryan Reynolds",
          "Manny Machado",
          "Whit Merrifield",
          "Jeremy Pena",
          "Josh Naylor",
          "Anthony Rizzo",
          "Jonathan India",
          "Jarred Kelenic",
          "George Springer",
          "Eugenio Suarez",
          "Joey Wiemer",
          "Andrew McCutchen",
          "Lourdes Gurriel Jr.",
          "Max Muncy",
          "Hunter Renfroe",
          "Mauricio Dubon",
          "Steven Kwan",
          "Tommy Edman",
          "Brent Rooker",
          "J.T. Realmuto",
          "Teoscar Hernandez",
          "Ezequiel Tovar",
          "Willson Contreras",
          "Carlos Correa",
          "Ke'Bryan Hayes",
          "Willy Adames",
          "Gleyber Torres",
          "Esteury Ruiz",
          "Marcell Ozuna",
          "Byron Buxton",
          "Andrew Benintendi",
          "Daulton Varsho",
          "J.D. Martinez",
          "Elias Diaz",
          "Ty France",
          "Taylor Ward",
          "Jeff McNeil",
          "Eddie Rosario",
          "Seiya Suzuki",
          "Carlos Santana",
          "Trent Grisham",
          "Vladimir Guerrero Jr.",
          "Michael Conforto",
          "Brian Anderson",
          "Jace Peterson",
          "Javier Baez",
          "Andrew Vaughn",
          "Alec Bohm",
          "Bryan De La Cruz",
          "Jake Cronenworth",
          "Salvador Perez",
          "CJ Abrams",
          "Spencer Torkelson",
          "Adam Frazier",
          "Miguel Vargas",
          "Amed Rosario",
          "Starling Marte",
          "Luis Garcia",
          "DJ LeMahieu",
          "Tyler Stephenson",
          "Kyle Schwarber",
          "Triston Casas",
          "Dominic Smith",
          "Shea Langeliers",
          "Josh Bell",
          "Myles Straw",
          "Joey Meneses",
          "Jose Abreu",
          "MJ Melendez",
          "Tim Anderson",
          "Rowdy Tellez",
          "Jurickson Profar",
          "Keibert Ruiz",
          "Enrique Hernandez"
         ],
         "legendgroup": "",
         "marker": {
          "color": "#7284cc"
         },
         "name": "",
         "notched": false,
         "offsetgroup": "",
         "orientation": "v",
         "showlegend": false,
         "type": "box",
         "x0": " ",
         "xaxis": "x",
         "y": [
          64,
          65,
          63,
          91,
          77,
          133,
          66,
          109,
          83,
          117,
          69,
          96,
          101,
          94,
          77,
          90,
          82,
          80,
          70,
          94,
          102,
          86,
          72,
          83,
          109,
          99,
          103,
          108,
          80,
          112,
          114,
          97,
          55,
          67,
          47,
          83,
          69,
          104,
          104,
          84,
          103,
          130,
          129,
          110,
          101,
          86,
          74,
          66,
          120,
          107,
          92,
          121,
          81,
          90,
          79,
          69,
          98,
          39,
          111,
          105,
          101,
          149,
          145,
          92,
          89,
          84,
          107,
          126,
          81,
          103,
          132,
          51,
          91,
          115,
          81,
          148,
          70,
          72,
          101,
          91,
          87,
          104,
          85,
          96,
          76,
          102,
          86,
          105,
          74,
          112,
          93,
          114,
          105,
          96,
          109,
          76,
          98,
          108,
          89,
          88,
          112,
          53,
          126,
          81,
          137,
          87,
          125,
          80,
          139,
          57,
          110,
          123,
          63,
          116,
          82,
          97,
          127,
          90,
          85,
          112,
          124,
          122,
          94,
          86,
          104,
          57,
          115,
          101,
          142,
          93,
          93,
          130,
          101,
          91,
          105,
          104,
          87,
          103,
          97,
          105,
          152,
          103,
          109,
          119,
          126,
          52,
          83,
          121,
          125,
          116,
          124
         ],
         "y0": " ",
         "yaxis": "y"
        }
       ],
       "layout": {
        "boxmode": "group",
        "height": 500,
        "legend": {
         "tracegroupgap": 0
        },
        "margin": {
         "t": 60
        },
        "template": {
         "data": {
          "candlestick": [
           {
            "decreasing": {
             "line": {
              "color": "#000033"
             }
            },
            "increasing": {
             "line": {
              "color": "#000032"
             }
            },
            "type": "candlestick"
           }
          ],
          "contour": [
           {
            "colorscale": [
             [
              0,
              "#000011"
             ],
             [
              0.1111111111111111,
              "#000012"
             ],
             [
              0.2222222222222222,
              "#000013"
             ],
             [
              0.3333333333333333,
              "#000014"
             ],
             [
              0.4444444444444444,
              "#000015"
             ],
             [
              0.5555555555555556,
              "#000016"
             ],
             [
              0.6666666666666666,
              "#000017"
             ],
             [
              0.7777777777777778,
              "#000018"
             ],
             [
              0.8888888888888888,
              "#000019"
             ],
             [
              1,
              "#000020"
             ]
            ],
            "type": "contour"
           }
          ],
          "contourcarpet": [
           {
            "colorscale": [
             [
              0,
              "#000011"
             ],
             [
              0.1111111111111111,
              "#000012"
             ],
             [
              0.2222222222222222,
              "#000013"
             ],
             [
              0.3333333333333333,
              "#000014"
             ],
             [
              0.4444444444444444,
              "#000015"
             ],
             [
              0.5555555555555556,
              "#000016"
             ],
             [
              0.6666666666666666,
              "#000017"
             ],
             [
              0.7777777777777778,
              "#000018"
             ],
             [
              0.8888888888888888,
              "#000019"
             ],
             [
              1,
              "#000020"
             ]
            ],
            "type": "contourcarpet"
           }
          ],
          "heatmap": [
           {
            "colorscale": [
             [
              0,
              "#000011"
             ],
             [
              0.1111111111111111,
              "#000012"
             ],
             [
              0.2222222222222222,
              "#000013"
             ],
             [
              0.3333333333333333,
              "#000014"
             ],
             [
              0.4444444444444444,
              "#000015"
             ],
             [
              0.5555555555555556,
              "#000016"
             ],
             [
              0.6666666666666666,
              "#000017"
             ],
             [
              0.7777777777777778,
              "#000018"
             ],
             [
              0.8888888888888888,
              "#000019"
             ],
             [
              1,
              "#000020"
             ]
            ],
            "type": "heatmap"
           }
          ],
          "histogram2d": [
           {
            "colorscale": [
             [
              0,
              "#000011"
             ],
             [
              0.1111111111111111,
              "#000012"
             ],
             [
              0.2222222222222222,
              "#000013"
             ],
             [
              0.3333333333333333,
              "#000014"
             ],
             [
              0.4444444444444444,
              "#000015"
             ],
             [
              0.5555555555555556,
              "#000016"
             ],
             [
              0.6666666666666666,
              "#000017"
             ],
             [
              0.7777777777777778,
              "#000018"
             ],
             [
              0.8888888888888888,
              "#000019"
             ],
             [
              1,
              "#000020"
             ]
            ],
            "type": "histogram2d"
           }
          ],
          "icicle": [
           {
            "textfont": {
             "color": "white"
            },
            "type": "icicle"
           }
          ],
          "sankey": [
           {
            "textfont": {
             "color": "#000036"
            },
            "type": "sankey"
           }
          ],
          "scatter": [
           {
            "marker": {
             "line": {
              "width": 0
             }
            },
            "type": "scatter"
           }
          ],
          "table": [
           {
            "cells": {
             "fill": {
              "color": "#000038"
             },
             "font": {
              "color": "#000037"
             },
             "line": {
              "color": "#000039"
             }
            },
            "header": {
             "fill": {
              "color": "#000040"
             },
             "font": {
              "color": "#000036"
             },
             "line": {
              "color": "#000039"
             }
            },
            "type": "table"
           }
          ],
          "waterfall": [
           {
            "connector": {
             "line": {
              "color": "#000036",
              "width": 2
             }
            },
            "decreasing": {
             "marker": {
              "color": "#000033"
             }
            },
            "increasing": {
             "marker": {
              "color": "#000032"
             }
            },
            "totals": {
             "marker": {
              "color": "#000034"
             }
            },
            "type": "waterfall"
           }
          ]
         },
         "layout": {
          "coloraxis": {
           "colorscale": [
            [
             0,
             "#000011"
            ],
            [
             0.1111111111111111,
             "#000012"
            ],
            [
             0.2222222222222222,
             "#000013"
            ],
            [
             0.3333333333333333,
             "#000014"
            ],
            [
             0.4444444444444444,
             "#000015"
            ],
            [
             0.5555555555555556,
             "#000016"
            ],
            [
             0.6666666666666666,
             "#000017"
            ],
            [
             0.7777777777777778,
             "#000018"
            ],
            [
             0.8888888888888888,
             "#000019"
            ],
            [
             1,
             "#000020"
            ]
           ]
          },
          "colorscale": {
           "diverging": [
            [
             0,
             "#000021"
            ],
            [
             0.1,
             "#000022"
            ],
            [
             0.2,
             "#000023"
            ],
            [
             0.3,
             "#000024"
            ],
            [
             0.4,
             "#000025"
            ],
            [
             0.5,
             "#000026"
            ],
            [
             0.6,
             "#000027"
            ],
            [
             0.7,
             "#000028"
            ],
            [
             0.8,
             "#000029"
            ],
            [
             0.9,
             "#000030"
            ],
            [
             1,
             "#000031"
            ]
           ],
           "sequential": [
            [
             0,
             "#000011"
            ],
            [
             0.1111111111111111,
             "#000012"
            ],
            [
             0.2222222222222222,
             "#000013"
            ],
            [
             0.3333333333333333,
             "#000014"
            ],
            [
             0.4444444444444444,
             "#000015"
            ],
            [
             0.5555555555555556,
             "#000016"
            ],
            [
             0.6666666666666666,
             "#000017"
            ],
            [
             0.7777777777777778,
             "#000018"
            ],
            [
             0.8888888888888888,
             "#000019"
            ],
            [
             1,
             "#000020"
            ]
           ],
           "sequentialminus": [
            [
             0,
             "#000011"
            ],
            [
             0.1111111111111111,
             "#000012"
            ],
            [
             0.2222222222222222,
             "#000013"
            ],
            [
             0.3333333333333333,
             "#000014"
            ],
            [
             0.4444444444444444,
             "#000015"
            ],
            [
             0.5555555555555556,
             "#000016"
            ],
            [
             0.6666666666666666,
             "#000017"
            ],
            [
             0.7777777777777778,
             "#000018"
            ],
            [
             0.8888888888888888,
             "#000019"
            ],
            [
             1,
             "#000020"
            ]
           ]
          },
          "colorway": [
           "#000001",
           "#000002",
           "#000003",
           "#000004",
           "#000005",
           "#000006",
           "#000007",
           "#000008",
           "#000009",
           "#000010"
          ]
         }
        },
        "title": {
         "automargin": true,
         "font": {
          "color": "#164f5e",
          "size": 22
         },
         "text": "Soft Hit%+",
         "yref": "paper"
        },
        "width": 500,
        "xaxis": {
         "anchor": "y",
         "domain": [
          0,
          1
         ],
         "title": {
          "text": ""
         }
        },
        "yaxis": {
         "anchor": "x",
         "domain": [
          0,
          1
         ],
         "title": {
          "text": ""
         }
        }
       }
      },
      "text/html": [
       "<div>                            <div id=\"1288e06d-afe0-4392-bf7a-afdcbde42560\" class=\"plotly-graph-div\" style=\"height:500px; width:500px;\"></div>            <script type=\"text/javascript\">                require([\"plotly\"], function(Plotly) {                    window.PLOTLYENV=window.PLOTLYENV || {};                                    if (document.getElementById(\"1288e06d-afe0-4392-bf7a-afdcbde42560\")) {                    Plotly.newPlot(                        \"1288e06d-afe0-4392-bf7a-afdcbde42560\",                        [{\"alignmentgroup\":\"True\",\"boxpoints\":\"all\",\"hovertemplate\":\"\\u003cb\\u003e%{hovertext}\\u003c\\u002fb\\u003e\\u003cbr\\u003e\\u003cbr\\u003eSoft%+=%{y}\\u003cextra\\u003e\\u003c\\u002fextra\\u003e\",\"hovertext\":[\"Ronald Acuna Jr.\",\"Shohei Ohtani\",\"Mookie Betts\",\"Wander Franco\",\"Corbin Carroll\",\"Luis Robert\",\"Freddie Freeman\",\"Juan Soto\",\"Fernando Tatis Jr.\",\"Jose Ramirez\",\"Adolis Garcia\",\"Mike Trout\",\"Jonah Heim\",\"Marcus Semien\",\"Bo Bichette\",\"Christian Yelich\",\"Francisco Lindor\",\"Dansby Swanson\",\"Luis Arraez\",\"Will Smith\",\"Ha-seong Kim\",\"Randy Arozarena\",\"Paul Goldschmidt\",\"Matt Chapman\",\"Isaac Paredes\",\"Brandon Nimmo\",\"Jeimer Candelario\",\"Thairo Estrada\",\"Matt Olson\",\"Christian Walker\",\"Jack Suwinski\",\"Julio Rodriguez\",\"Yandy Diaz\",\"Kyle Tucker\",\"Josh Jung\",\"Ketel Marte\",\"Ozzie Albies\",\"William Contreras\",\"Xander Bogaerts\",\"Leody Taveras\",\"Adley Rutschman\",\"Nico Hoerner\",\"Lane Thomas\",\"Bobby Witt Jr.\",\"LaMonte Wade Jr.\",\"Austin Hays\",\"J.D. Davis\",\"Gunnar Henderson\",\"Alex Verdugo\",\"Nathaniel Lowe\",\"Jorge Soler\",\"Nolan Arenado\",\"Rafael Devers\",\"Austin Riley\",\"Brendan Donovan\",\"Bryson Stott\",\"Brandon Drury\",\"Brandon Marsh\",\"Ian Happ\",\"J.P. Crawford\",\"Alex Bregman\",\"Andres Gimenez\",\"Cal Raleigh\",\"Spencer Steer\",\"Nolan Gorman\",\"Ryan Noda\",\"Cedric Mullins II\",\"James Outman\",\"Nick Castellanos\",\"Pete Alonso\",\"Anthony Santander\",\"Ryan McMahon\",\"Zach McKinstry\",\"Trea Turner\",\"Anthony Volpe\",\"Masataka Yoshida\",\"Justin Turner\",\"Bryan Reynolds\",\"Manny Machado\",\"Whit Merrifield\",\"Jeremy Pena\",\"Josh Naylor\",\"Anthony Rizzo\",\"Jonathan India\",\"Jarred Kelenic\",\"George Springer\",\"Eugenio Suarez\",\"Joey Wiemer\",\"Andrew McCutchen\",\"Lourdes Gurriel Jr.\",\"Max Muncy\",\"Hunter Renfroe\",\"Mauricio Dubon\",\"Steven Kwan\",\"Tommy Edman\",\"Brent Rooker\",\"J.T. Realmuto\",\"Teoscar Hernandez\",\"Ezequiel Tovar\",\"Willson Contreras\",\"Carlos Correa\",\"Ke'Bryan Hayes\",\"Willy Adames\",\"Gleyber Torres\",\"Esteury Ruiz\",\"Marcell Ozuna\",\"Byron Buxton\",\"Andrew Benintendi\",\"Daulton Varsho\",\"J.D. Martinez\",\"Elias Diaz\",\"Ty France\",\"Taylor Ward\",\"Jeff McNeil\",\"Eddie Rosario\",\"Seiya Suzuki\",\"Carlos Santana\",\"Trent Grisham\",\"Vladimir Guerrero Jr.\",\"Michael Conforto\",\"Brian Anderson\",\"Jace Peterson\",\"Javier Baez\",\"Andrew Vaughn\",\"Alec Bohm\",\"Bryan De La Cruz\",\"Jake Cronenworth\",\"Salvador Perez\",\"CJ Abrams\",\"Spencer Torkelson\",\"Adam Frazier\",\"Miguel Vargas\",\"Amed Rosario\",\"Starling Marte\",\"Luis Garcia\",\"DJ LeMahieu\",\"Tyler Stephenson\",\"Kyle Schwarber\",\"Triston Casas\",\"Dominic Smith\",\"Shea Langeliers\",\"Josh Bell\",\"Myles Straw\",\"Joey Meneses\",\"Jose Abreu\",\"MJ Melendez\",\"Tim Anderson\",\"Rowdy Tellez\",\"Jurickson Profar\",\"Keibert Ruiz\",\"Enrique Hernandez\"],\"legendgroup\":\"\",\"marker\":{\"color\":\"#7284cc\"},\"name\":\"\",\"notched\":false,\"offsetgroup\":\"\",\"orientation\":\"v\",\"showlegend\":false,\"x0\":\" \",\"xaxis\":\"x\",\"y\":[64,65,63,91,77,133,66,109,83,117,69,96,101,94,77,90,82,80,70,94,102,86,72,83,109,99,103,108,80,112,114,97,55,67,47,83,69,104,104,84,103,130,129,110,101,86,74,66,120,107,92,121,81,90,79,69,98,39,111,105,101,149,145,92,89,84,107,126,81,103,132,51,91,115,81,148,70,72,101,91,87,104,85,96,76,102,86,105,74,112,93,114,105,96,109,76,98,108,89,88,112,53,126,81,137,87,125,80,139,57,110,123,63,116,82,97,127,90,85,112,124,122,94,86,104,57,115,101,142,93,93,130,101,91,105,104,87,103,97,105,152,103,109,119,126,52,83,121,125,116,124],\"y0\":\" \",\"yaxis\":\"y\",\"type\":\"box\"}],                        {\"template\":{\"data\":{\"candlestick\":[{\"decreasing\":{\"line\":{\"color\":\"#000033\"}},\"increasing\":{\"line\":{\"color\":\"#000032\"}},\"type\":\"candlestick\"}],\"contourcarpet\":[{\"colorscale\":[[0.0,\"#000011\"],[0.1111111111111111,\"#000012\"],[0.2222222222222222,\"#000013\"],[0.3333333333333333,\"#000014\"],[0.4444444444444444,\"#000015\"],[0.5555555555555556,\"#000016\"],[0.6666666666666666,\"#000017\"],[0.7777777777777778,\"#000018\"],[0.8888888888888888,\"#000019\"],[1.0,\"#000020\"]],\"type\":\"contourcarpet\"}],\"contour\":[{\"colorscale\":[[0.0,\"#000011\"],[0.1111111111111111,\"#000012\"],[0.2222222222222222,\"#000013\"],[0.3333333333333333,\"#000014\"],[0.4444444444444444,\"#000015\"],[0.5555555555555556,\"#000016\"],[0.6666666666666666,\"#000017\"],[0.7777777777777778,\"#000018\"],[0.8888888888888888,\"#000019\"],[1.0,\"#000020\"]],\"type\":\"contour\"}],\"heatmap\":[{\"colorscale\":[[0.0,\"#000011\"],[0.1111111111111111,\"#000012\"],[0.2222222222222222,\"#000013\"],[0.3333333333333333,\"#000014\"],[0.4444444444444444,\"#000015\"],[0.5555555555555556,\"#000016\"],[0.6666666666666666,\"#000017\"],[0.7777777777777778,\"#000018\"],[0.8888888888888888,\"#000019\"],[1.0,\"#000020\"]],\"type\":\"heatmap\"}],\"histogram2d\":[{\"colorscale\":[[0.0,\"#000011\"],[0.1111111111111111,\"#000012\"],[0.2222222222222222,\"#000013\"],[0.3333333333333333,\"#000014\"],[0.4444444444444444,\"#000015\"],[0.5555555555555556,\"#000016\"],[0.6666666666666666,\"#000017\"],[0.7777777777777778,\"#000018\"],[0.8888888888888888,\"#000019\"],[1.0,\"#000020\"]],\"type\":\"histogram2d\"}],\"icicle\":[{\"textfont\":{\"color\":\"white\"},\"type\":\"icicle\"}],\"sankey\":[{\"textfont\":{\"color\":\"#000036\"},\"type\":\"sankey\"}],\"scatter\":[{\"marker\":{\"line\":{\"width\":0}},\"type\":\"scatter\"}],\"table\":[{\"cells\":{\"fill\":{\"color\":\"#000038\"},\"font\":{\"color\":\"#000037\"},\"line\":{\"color\":\"#000039\"}},\"header\":{\"fill\":{\"color\":\"#000040\"},\"font\":{\"color\":\"#000036\"},\"line\":{\"color\":\"#000039\"}},\"type\":\"table\"}],\"waterfall\":[{\"connector\":{\"line\":{\"color\":\"#000036\",\"width\":2}},\"decreasing\":{\"marker\":{\"color\":\"#000033\"}},\"increasing\":{\"marker\":{\"color\":\"#000032\"}},\"totals\":{\"marker\":{\"color\":\"#000034\"}},\"type\":\"waterfall\"}]},\"layout\":{\"coloraxis\":{\"colorscale\":[[0.0,\"#000011\"],[0.1111111111111111,\"#000012\"],[0.2222222222222222,\"#000013\"],[0.3333333333333333,\"#000014\"],[0.4444444444444444,\"#000015\"],[0.5555555555555556,\"#000016\"],[0.6666666666666666,\"#000017\"],[0.7777777777777778,\"#000018\"],[0.8888888888888888,\"#000019\"],[1.0,\"#000020\"]]},\"colorscale\":{\"diverging\":[[0.0,\"#000021\"],[0.1,\"#000022\"],[0.2,\"#000023\"],[0.3,\"#000024\"],[0.4,\"#000025\"],[0.5,\"#000026\"],[0.6,\"#000027\"],[0.7,\"#000028\"],[0.8,\"#000029\"],[0.9,\"#000030\"],[1.0,\"#000031\"]],\"sequential\":[[0.0,\"#000011\"],[0.1111111111111111,\"#000012\"],[0.2222222222222222,\"#000013\"],[0.3333333333333333,\"#000014\"],[0.4444444444444444,\"#000015\"],[0.5555555555555556,\"#000016\"],[0.6666666666666666,\"#000017\"],[0.7777777777777778,\"#000018\"],[0.8888888888888888,\"#000019\"],[1.0,\"#000020\"]],\"sequentialminus\":[[0.0,\"#000011\"],[0.1111111111111111,\"#000012\"],[0.2222222222222222,\"#000013\"],[0.3333333333333333,\"#000014\"],[0.4444444444444444,\"#000015\"],[0.5555555555555556,\"#000016\"],[0.6666666666666666,\"#000017\"],[0.7777777777777778,\"#000018\"],[0.8888888888888888,\"#000019\"],[1.0,\"#000020\"]]},\"colorway\":[\"#000001\",\"#000002\",\"#000003\",\"#000004\",\"#000005\",\"#000006\",\"#000007\",\"#000008\",\"#000009\",\"#000010\"]}},\"xaxis\":{\"anchor\":\"y\",\"domain\":[0.0,1.0],\"title\":{\"text\":\"\"}},\"yaxis\":{\"anchor\":\"x\",\"domain\":[0.0,1.0],\"title\":{\"text\":\"\"}},\"legend\":{\"tracegroupgap\":0},\"margin\":{\"t\":60},\"boxmode\":\"group\",\"height\":500,\"width\":500,\"title\":{\"font\":{\"size\":22,\"color\":\"#164f5e\"},\"text\":\"Soft Hit%+\",\"automargin\":true,\"yref\":\"paper\"}},                        {\"responsive\": true}                    ).then(function(){\n",
       "                            \n",
       "var gd = document.getElementById('1288e06d-afe0-4392-bf7a-afdcbde42560');\n",
       "var x = new MutationObserver(function (mutations, observer) {{\n",
       "        var display = window.getComputedStyle(gd).display;\n",
       "        if (!display || display === 'none') {{\n",
       "            console.log([gd, 'removed!']);\n",
       "            Plotly.purge(gd);\n",
       "            observer.disconnect();\n",
       "        }}\n",
       "}});\n",
       "\n",
       "// Listen for the removal of the full notebook cells\n",
       "var notebookContainer = gd.closest('#notebook-container');\n",
       "if (notebookContainer) {{\n",
       "    x.observe(notebookContainer, {childList: true});\n",
       "}}\n",
       "\n",
       "// Listen for the clearing of the current output cell\n",
       "var outputEl = gd.closest('.output');\n",
       "if (outputEl) {{\n",
       "    x.observe(outputEl, {childList: true});\n",
       "}}\n",
       "\n",
       "                        })                };                });            </script>        </div>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "fig_21 = px.box(\n",
    "    df.query(\"Season==2023\"),\n",
    "    y = \"Soft%+\",\n",
    "    points=\"all\",\n",
    "    hover_name = \"Name\",\n",
    "    height = 500,\n",
    "    width = 500,\n",
    ")\n",
    "\n",
    "fig_21.update_traces(marker=dict(color=\"#7284cc\"))\n",
    "\n",
    "fig_21.update_layout(\n",
    "    title=dict(text=\"Soft Hit%+\", font=dict(size=22), automargin=True, yref='paper'),\n",
    "    title_font_color=\"#164f5e\",\n",
    "    yaxis=dict(title=\"\"),\n",
    "    xaxis=dict(title=\"\")\n",
    ")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 91,
   "id": "31c0f03d",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "application/vnd.plotly.v1+json": {
       "config": {
        "plotlyServerURL": "https://plot.ly"
       },
       "data": [
        {
         "alignmentgroup": "True",
         "boxpoints": "all",
         "hovertemplate": "<b>%{hovertext}</b><br><br>Hard%+=%{y}<extra></extra>",
         "hovertext": [
          "Ronald Acuna Jr.",
          "Shohei Ohtani",
          "Mookie Betts",
          "Wander Franco",
          "Corbin Carroll",
          "Luis Robert",
          "Freddie Freeman",
          "Juan Soto",
          "Fernando Tatis Jr.",
          "Jose Ramirez",
          "Adolis Garcia",
          "Mike Trout",
          "Jonah Heim",
          "Marcus Semien",
          "Bo Bichette",
          "Christian Yelich",
          "Francisco Lindor",
          "Dansby Swanson",
          "Luis Arraez",
          "Will Smith",
          "Ha-seong Kim",
          "Randy Arozarena",
          "Paul Goldschmidt",
          "Matt Chapman",
          "Isaac Paredes",
          "Brandon Nimmo",
          "Jeimer Candelario",
          "Thairo Estrada",
          "Matt Olson",
          "Christian Walker",
          "Jack Suwinski",
          "Julio Rodriguez",
          "Yandy Diaz",
          "Kyle Tucker",
          "Josh Jung",
          "Ketel Marte",
          "Ozzie Albies",
          "William Contreras",
          "Xander Bogaerts",
          "Leody Taveras",
          "Adley Rutschman",
          "Nico Hoerner",
          "Lane Thomas",
          "Bobby Witt Jr.",
          "LaMonte Wade Jr.",
          "Austin Hays",
          "J.D. Davis",
          "Gunnar Henderson",
          "Alex Verdugo",
          "Nathaniel Lowe",
          "Jorge Soler",
          "Nolan Arenado",
          "Rafael Devers",
          "Austin Riley",
          "Brendan Donovan",
          "Bryson Stott",
          "Brandon Drury",
          "Brandon Marsh",
          "Ian Happ",
          "J.P. Crawford",
          "Alex Bregman",
          "Andres Gimenez",
          "Cal Raleigh",
          "Spencer Steer",
          "Nolan Gorman",
          "Ryan Noda",
          "Cedric Mullins II",
          "James Outman",
          "Nick Castellanos",
          "Pete Alonso",
          "Anthony Santander",
          "Ryan McMahon",
          "Zach McKinstry",
          "Trea Turner",
          "Anthony Volpe",
          "Masataka Yoshida",
          "Justin Turner",
          "Bryan Reynolds",
          "Manny Machado",
          "Whit Merrifield",
          "Jeremy Pena",
          "Josh Naylor",
          "Anthony Rizzo",
          "Jonathan India",
          "Jarred Kelenic",
          "George Springer",
          "Eugenio Suarez",
          "Joey Wiemer",
          "Andrew McCutchen",
          "Lourdes Gurriel Jr.",
          "Max Muncy",
          "Hunter Renfroe",
          "Mauricio Dubon",
          "Steven Kwan",
          "Tommy Edman",
          "Brent Rooker",
          "J.T. Realmuto",
          "Teoscar Hernandez",
          "Ezequiel Tovar",
          "Willson Contreras",
          "Carlos Correa",
          "Ke'Bryan Hayes",
          "Willy Adames",
          "Gleyber Torres",
          "Esteury Ruiz",
          "Marcell Ozuna",
          "Byron Buxton",
          "Andrew Benintendi",
          "Daulton Varsho",
          "J.D. Martinez",
          "Elias Diaz",
          "Ty France",
          "Taylor Ward",
          "Jeff McNeil",
          "Eddie Rosario",
          "Seiya Suzuki",
          "Carlos Santana",
          "Trent Grisham",
          "Vladimir Guerrero Jr.",
          "Michael Conforto",
          "Brian Anderson",
          "Jace Peterson",
          "Javier Baez",
          "Andrew Vaughn",
          "Alec Bohm",
          "Bryan De La Cruz",
          "Jake Cronenworth",
          "Salvador Perez",
          "CJ Abrams",
          "Spencer Torkelson",
          "Adam Frazier",
          "Miguel Vargas",
          "Amed Rosario",
          "Starling Marte",
          "Luis Garcia",
          "DJ LeMahieu",
          "Tyler Stephenson",
          "Kyle Schwarber",
          "Triston Casas",
          "Dominic Smith",
          "Shea Langeliers",
          "Josh Bell",
          "Myles Straw",
          "Joey Meneses",
          "Jose Abreu",
          "MJ Melendez",
          "Tim Anderson",
          "Rowdy Tellez",
          "Jurickson Profar",
          "Keibert Ruiz",
          "Enrique Hernandez"
         ],
         "legendgroup": "",
         "marker": {
          "color": "#7284cc"
         },
         "name": "",
         "notched": false,
         "offsetgroup": "",
         "orientation": "v",
         "showlegend": false,
         "type": "box",
         "x0": " ",
         "xaxis": "x",
         "y": [
          135,
          124,
          134,
          109,
          100,
          106,
          121,
          117,
          124,
          93,
          140,
          125,
          117,
          106,
          119,
          127,
          120,
          110,
          87,
          110,
          83,
          133,
          133,
          141,
          98,
          117,
          105,
          92,
          130,
          106,
          121,
          122,
          123,
          122,
          137,
          112,
          111,
          96,
          92,
          100,
          87,
          61,
          106,
          118,
          100,
          116,
          114,
          129,
          110,
          111,
          130,
          108,
          124,
          112,
          104,
          86,
          103,
          101,
          86,
          99,
          96,
          82,
          101,
          105,
          101,
          117,
          92,
          97,
          112,
          111,
          112,
          135,
          87,
          95,
          111,
          95,
          102,
          103,
          95,
          78,
          92,
          111,
          91,
          99,
          105,
          105,
          121,
          112,
          102,
          114,
          121,
          114,
          74,
          48,
          123,
          112,
          96,
          119,
          98,
          127,
          104,
          103,
          100,
          85,
          48,
          115,
          101,
          77,
          96,
          146,
          119,
          78,
          114,
          64,
          115,
          122,
          93,
          102,
          121,
          100,
          100,
          86,
          84,
          111,
          92,
          110,
          81,
          109,
          82,
          120,
          75,
          92,
          92,
          88,
          102,
          99,
          94,
          114,
          113,
          71,
          95,
          98,
          49,
          91,
          85,
          122,
          93,
          98,
          106,
          97,
          77
         ],
         "y0": " ",
         "yaxis": "y"
        }
       ],
       "layout": {
        "boxmode": "group",
        "height": 500,
        "legend": {
         "tracegroupgap": 0
        },
        "margin": {
         "t": 60
        },
        "template": {
         "data": {
          "candlestick": [
           {
            "decreasing": {
             "line": {
              "color": "#000033"
             }
            },
            "increasing": {
             "line": {
              "color": "#000032"
             }
            },
            "type": "candlestick"
           }
          ],
          "contour": [
           {
            "colorscale": [
             [
              0,
              "#000011"
             ],
             [
              0.1111111111111111,
              "#000012"
             ],
             [
              0.2222222222222222,
              "#000013"
             ],
             [
              0.3333333333333333,
              "#000014"
             ],
             [
              0.4444444444444444,
              "#000015"
             ],
             [
              0.5555555555555556,
              "#000016"
             ],
             [
              0.6666666666666666,
              "#000017"
             ],
             [
              0.7777777777777778,
              "#000018"
             ],
             [
              0.8888888888888888,
              "#000019"
             ],
             [
              1,
              "#000020"
             ]
            ],
            "type": "contour"
           }
          ],
          "contourcarpet": [
           {
            "colorscale": [
             [
              0,
              "#000011"
             ],
             [
              0.1111111111111111,
              "#000012"
             ],
             [
              0.2222222222222222,
              "#000013"
             ],
             [
              0.3333333333333333,
              "#000014"
             ],
             [
              0.4444444444444444,
              "#000015"
             ],
             [
              0.5555555555555556,
              "#000016"
             ],
             [
              0.6666666666666666,
              "#000017"
             ],
             [
              0.7777777777777778,
              "#000018"
             ],
             [
              0.8888888888888888,
              "#000019"
             ],
             [
              1,
              "#000020"
             ]
            ],
            "type": "contourcarpet"
           }
          ],
          "heatmap": [
           {
            "colorscale": [
             [
              0,
              "#000011"
             ],
             [
              0.1111111111111111,
              "#000012"
             ],
             [
              0.2222222222222222,
              "#000013"
             ],
             [
              0.3333333333333333,
              "#000014"
             ],
             [
              0.4444444444444444,
              "#000015"
             ],
             [
              0.5555555555555556,
              "#000016"
             ],
             [
              0.6666666666666666,
              "#000017"
             ],
             [
              0.7777777777777778,
              "#000018"
             ],
             [
              0.8888888888888888,
              "#000019"
             ],
             [
              1,
              "#000020"
             ]
            ],
            "type": "heatmap"
           }
          ],
          "histogram2d": [
           {
            "colorscale": [
             [
              0,
              "#000011"
             ],
             [
              0.1111111111111111,
              "#000012"
             ],
             [
              0.2222222222222222,
              "#000013"
             ],
             [
              0.3333333333333333,
              "#000014"
             ],
             [
              0.4444444444444444,
              "#000015"
             ],
             [
              0.5555555555555556,
              "#000016"
             ],
             [
              0.6666666666666666,
              "#000017"
             ],
             [
              0.7777777777777778,
              "#000018"
             ],
             [
              0.8888888888888888,
              "#000019"
             ],
             [
              1,
              "#000020"
             ]
            ],
            "type": "histogram2d"
           }
          ],
          "icicle": [
           {
            "textfont": {
             "color": "white"
            },
            "type": "icicle"
           }
          ],
          "sankey": [
           {
            "textfont": {
             "color": "#000036"
            },
            "type": "sankey"
           }
          ],
          "scatter": [
           {
            "marker": {
             "line": {
              "width": 0
             }
            },
            "type": "scatter"
           }
          ],
          "table": [
           {
            "cells": {
             "fill": {
              "color": "#000038"
             },
             "font": {
              "color": "#000037"
             },
             "line": {
              "color": "#000039"
             }
            },
            "header": {
             "fill": {
              "color": "#000040"
             },
             "font": {
              "color": "#000036"
             },
             "line": {
              "color": "#000039"
             }
            },
            "type": "table"
           }
          ],
          "waterfall": [
           {
            "connector": {
             "line": {
              "color": "#000036",
              "width": 2
             }
            },
            "decreasing": {
             "marker": {
              "color": "#000033"
             }
            },
            "increasing": {
             "marker": {
              "color": "#000032"
             }
            },
            "totals": {
             "marker": {
              "color": "#000034"
             }
            },
            "type": "waterfall"
           }
          ]
         },
         "layout": {
          "coloraxis": {
           "colorscale": [
            [
             0,
             "#000011"
            ],
            [
             0.1111111111111111,
             "#000012"
            ],
            [
             0.2222222222222222,
             "#000013"
            ],
            [
             0.3333333333333333,
             "#000014"
            ],
            [
             0.4444444444444444,
             "#000015"
            ],
            [
             0.5555555555555556,
             "#000016"
            ],
            [
             0.6666666666666666,
             "#000017"
            ],
            [
             0.7777777777777778,
             "#000018"
            ],
            [
             0.8888888888888888,
             "#000019"
            ],
            [
             1,
             "#000020"
            ]
           ]
          },
          "colorscale": {
           "diverging": [
            [
             0,
             "#000021"
            ],
            [
             0.1,
             "#000022"
            ],
            [
             0.2,
             "#000023"
            ],
            [
             0.3,
             "#000024"
            ],
            [
             0.4,
             "#000025"
            ],
            [
             0.5,
             "#000026"
            ],
            [
             0.6,
             "#000027"
            ],
            [
             0.7,
             "#000028"
            ],
            [
             0.8,
             "#000029"
            ],
            [
             0.9,
             "#000030"
            ],
            [
             1,
             "#000031"
            ]
           ],
           "sequential": [
            [
             0,
             "#000011"
            ],
            [
             0.1111111111111111,
             "#000012"
            ],
            [
             0.2222222222222222,
             "#000013"
            ],
            [
             0.3333333333333333,
             "#000014"
            ],
            [
             0.4444444444444444,
             "#000015"
            ],
            [
             0.5555555555555556,
             "#000016"
            ],
            [
             0.6666666666666666,
             "#000017"
            ],
            [
             0.7777777777777778,
             "#000018"
            ],
            [
             0.8888888888888888,
             "#000019"
            ],
            [
             1,
             "#000020"
            ]
           ],
           "sequentialminus": [
            [
             0,
             "#000011"
            ],
            [
             0.1111111111111111,
             "#000012"
            ],
            [
             0.2222222222222222,
             "#000013"
            ],
            [
             0.3333333333333333,
             "#000014"
            ],
            [
             0.4444444444444444,
             "#000015"
            ],
            [
             0.5555555555555556,
             "#000016"
            ],
            [
             0.6666666666666666,
             "#000017"
            ],
            [
             0.7777777777777778,
             "#000018"
            ],
            [
             0.8888888888888888,
             "#000019"
            ],
            [
             1,
             "#000020"
            ]
           ]
          },
          "colorway": [
           "#000001",
           "#000002",
           "#000003",
           "#000004",
           "#000005",
           "#000006",
           "#000007",
           "#000008",
           "#000009",
           "#000010"
          ]
         }
        },
        "title": {
         "automargin": true,
         "font": {
          "color": "#164f5e",
          "size": 22
         },
         "text": "Hard Hit%+",
         "yref": "paper"
        },
        "width": 500,
        "xaxis": {
         "anchor": "y",
         "domain": [
          0,
          1
         ],
         "title": {
          "text": ""
         }
        },
        "yaxis": {
         "anchor": "x",
         "domain": [
          0,
          1
         ],
         "title": {
          "text": ""
         }
        }
       }
      },
      "text/html": [
       "<div>                            <div id=\"ce1f52c0-2efa-4afe-a3e9-ea751a71b0e3\" class=\"plotly-graph-div\" style=\"height:500px; width:500px;\"></div>            <script type=\"text/javascript\">                require([\"plotly\"], function(Plotly) {                    window.PLOTLYENV=window.PLOTLYENV || {};                                    if (document.getElementById(\"ce1f52c0-2efa-4afe-a3e9-ea751a71b0e3\")) {                    Plotly.newPlot(                        \"ce1f52c0-2efa-4afe-a3e9-ea751a71b0e3\",                        [{\"alignmentgroup\":\"True\",\"boxpoints\":\"all\",\"hovertemplate\":\"\\u003cb\\u003e%{hovertext}\\u003c\\u002fb\\u003e\\u003cbr\\u003e\\u003cbr\\u003eHard%+=%{y}\\u003cextra\\u003e\\u003c\\u002fextra\\u003e\",\"hovertext\":[\"Ronald Acuna Jr.\",\"Shohei Ohtani\",\"Mookie Betts\",\"Wander Franco\",\"Corbin Carroll\",\"Luis Robert\",\"Freddie Freeman\",\"Juan Soto\",\"Fernando Tatis Jr.\",\"Jose Ramirez\",\"Adolis Garcia\",\"Mike Trout\",\"Jonah Heim\",\"Marcus Semien\",\"Bo Bichette\",\"Christian Yelich\",\"Francisco Lindor\",\"Dansby Swanson\",\"Luis Arraez\",\"Will Smith\",\"Ha-seong Kim\",\"Randy Arozarena\",\"Paul Goldschmidt\",\"Matt Chapman\",\"Isaac Paredes\",\"Brandon Nimmo\",\"Jeimer Candelario\",\"Thairo Estrada\",\"Matt Olson\",\"Christian Walker\",\"Jack Suwinski\",\"Julio Rodriguez\",\"Yandy Diaz\",\"Kyle Tucker\",\"Josh Jung\",\"Ketel Marte\",\"Ozzie Albies\",\"William Contreras\",\"Xander Bogaerts\",\"Leody Taveras\",\"Adley Rutschman\",\"Nico Hoerner\",\"Lane Thomas\",\"Bobby Witt Jr.\",\"LaMonte Wade Jr.\",\"Austin Hays\",\"J.D. Davis\",\"Gunnar Henderson\",\"Alex Verdugo\",\"Nathaniel Lowe\",\"Jorge Soler\",\"Nolan Arenado\",\"Rafael Devers\",\"Austin Riley\",\"Brendan Donovan\",\"Bryson Stott\",\"Brandon Drury\",\"Brandon Marsh\",\"Ian Happ\",\"J.P. Crawford\",\"Alex Bregman\",\"Andres Gimenez\",\"Cal Raleigh\",\"Spencer Steer\",\"Nolan Gorman\",\"Ryan Noda\",\"Cedric Mullins II\",\"James Outman\",\"Nick Castellanos\",\"Pete Alonso\",\"Anthony Santander\",\"Ryan McMahon\",\"Zach McKinstry\",\"Trea Turner\",\"Anthony Volpe\",\"Masataka Yoshida\",\"Justin Turner\",\"Bryan Reynolds\",\"Manny Machado\",\"Whit Merrifield\",\"Jeremy Pena\",\"Josh Naylor\",\"Anthony Rizzo\",\"Jonathan India\",\"Jarred Kelenic\",\"George Springer\",\"Eugenio Suarez\",\"Joey Wiemer\",\"Andrew McCutchen\",\"Lourdes Gurriel Jr.\",\"Max Muncy\",\"Hunter Renfroe\",\"Mauricio Dubon\",\"Steven Kwan\",\"Tommy Edman\",\"Brent Rooker\",\"J.T. Realmuto\",\"Teoscar Hernandez\",\"Ezequiel Tovar\",\"Willson Contreras\",\"Carlos Correa\",\"Ke'Bryan Hayes\",\"Willy Adames\",\"Gleyber Torres\",\"Esteury Ruiz\",\"Marcell Ozuna\",\"Byron Buxton\",\"Andrew Benintendi\",\"Daulton Varsho\",\"J.D. Martinez\",\"Elias Diaz\",\"Ty France\",\"Taylor Ward\",\"Jeff McNeil\",\"Eddie Rosario\",\"Seiya Suzuki\",\"Carlos Santana\",\"Trent Grisham\",\"Vladimir Guerrero Jr.\",\"Michael Conforto\",\"Brian Anderson\",\"Jace Peterson\",\"Javier Baez\",\"Andrew Vaughn\",\"Alec Bohm\",\"Bryan De La Cruz\",\"Jake Cronenworth\",\"Salvador Perez\",\"CJ Abrams\",\"Spencer Torkelson\",\"Adam Frazier\",\"Miguel Vargas\",\"Amed Rosario\",\"Starling Marte\",\"Luis Garcia\",\"DJ LeMahieu\",\"Tyler Stephenson\",\"Kyle Schwarber\",\"Triston Casas\",\"Dominic Smith\",\"Shea Langeliers\",\"Josh Bell\",\"Myles Straw\",\"Joey Meneses\",\"Jose Abreu\",\"MJ Melendez\",\"Tim Anderson\",\"Rowdy Tellez\",\"Jurickson Profar\",\"Keibert Ruiz\",\"Enrique Hernandez\"],\"legendgroup\":\"\",\"marker\":{\"color\":\"#7284cc\"},\"name\":\"\",\"notched\":false,\"offsetgroup\":\"\",\"orientation\":\"v\",\"showlegend\":false,\"x0\":\" \",\"xaxis\":\"x\",\"y\":[135,124,134,109,100,106,121,117,124,93,140,125,117,106,119,127,120,110,87,110,83,133,133,141,98,117,105,92,130,106,121,122,123,122,137,112,111,96,92,100,87,61,106,118,100,116,114,129,110,111,130,108,124,112,104,86,103,101,86,99,96,82,101,105,101,117,92,97,112,111,112,135,87,95,111,95,102,103,95,78,92,111,91,99,105,105,121,112,102,114,121,114,74,48,123,112,96,119,98,127,104,103,100,85,48,115,101,77,96,146,119,78,114,64,115,122,93,102,121,100,100,86,84,111,92,110,81,109,82,120,75,92,92,88,102,99,94,114,113,71,95,98,49,91,85,122,93,98,106,97,77],\"y0\":\" \",\"yaxis\":\"y\",\"type\":\"box\"}],                        {\"template\":{\"data\":{\"candlestick\":[{\"decreasing\":{\"line\":{\"color\":\"#000033\"}},\"increasing\":{\"line\":{\"color\":\"#000032\"}},\"type\":\"candlestick\"}],\"contourcarpet\":[{\"colorscale\":[[0.0,\"#000011\"],[0.1111111111111111,\"#000012\"],[0.2222222222222222,\"#000013\"],[0.3333333333333333,\"#000014\"],[0.4444444444444444,\"#000015\"],[0.5555555555555556,\"#000016\"],[0.6666666666666666,\"#000017\"],[0.7777777777777778,\"#000018\"],[0.8888888888888888,\"#000019\"],[1.0,\"#000020\"]],\"type\":\"contourcarpet\"}],\"contour\":[{\"colorscale\":[[0.0,\"#000011\"],[0.1111111111111111,\"#000012\"],[0.2222222222222222,\"#000013\"],[0.3333333333333333,\"#000014\"],[0.4444444444444444,\"#000015\"],[0.5555555555555556,\"#000016\"],[0.6666666666666666,\"#000017\"],[0.7777777777777778,\"#000018\"],[0.8888888888888888,\"#000019\"],[1.0,\"#000020\"]],\"type\":\"contour\"}],\"heatmap\":[{\"colorscale\":[[0.0,\"#000011\"],[0.1111111111111111,\"#000012\"],[0.2222222222222222,\"#000013\"],[0.3333333333333333,\"#000014\"],[0.4444444444444444,\"#000015\"],[0.5555555555555556,\"#000016\"],[0.6666666666666666,\"#000017\"],[0.7777777777777778,\"#000018\"],[0.8888888888888888,\"#000019\"],[1.0,\"#000020\"]],\"type\":\"heatmap\"}],\"histogram2d\":[{\"colorscale\":[[0.0,\"#000011\"],[0.1111111111111111,\"#000012\"],[0.2222222222222222,\"#000013\"],[0.3333333333333333,\"#000014\"],[0.4444444444444444,\"#000015\"],[0.5555555555555556,\"#000016\"],[0.6666666666666666,\"#000017\"],[0.7777777777777778,\"#000018\"],[0.8888888888888888,\"#000019\"],[1.0,\"#000020\"]],\"type\":\"histogram2d\"}],\"icicle\":[{\"textfont\":{\"color\":\"white\"},\"type\":\"icicle\"}],\"sankey\":[{\"textfont\":{\"color\":\"#000036\"},\"type\":\"sankey\"}],\"scatter\":[{\"marker\":{\"line\":{\"width\":0}},\"type\":\"scatter\"}],\"table\":[{\"cells\":{\"fill\":{\"color\":\"#000038\"},\"font\":{\"color\":\"#000037\"},\"line\":{\"color\":\"#000039\"}},\"header\":{\"fill\":{\"color\":\"#000040\"},\"font\":{\"color\":\"#000036\"},\"line\":{\"color\":\"#000039\"}},\"type\":\"table\"}],\"waterfall\":[{\"connector\":{\"line\":{\"color\":\"#000036\",\"width\":2}},\"decreasing\":{\"marker\":{\"color\":\"#000033\"}},\"increasing\":{\"marker\":{\"color\":\"#000032\"}},\"totals\":{\"marker\":{\"color\":\"#000034\"}},\"type\":\"waterfall\"}]},\"layout\":{\"coloraxis\":{\"colorscale\":[[0.0,\"#000011\"],[0.1111111111111111,\"#000012\"],[0.2222222222222222,\"#000013\"],[0.3333333333333333,\"#000014\"],[0.4444444444444444,\"#000015\"],[0.5555555555555556,\"#000016\"],[0.6666666666666666,\"#000017\"],[0.7777777777777778,\"#000018\"],[0.8888888888888888,\"#000019\"],[1.0,\"#000020\"]]},\"colorscale\":{\"diverging\":[[0.0,\"#000021\"],[0.1,\"#000022\"],[0.2,\"#000023\"],[0.3,\"#000024\"],[0.4,\"#000025\"],[0.5,\"#000026\"],[0.6,\"#000027\"],[0.7,\"#000028\"],[0.8,\"#000029\"],[0.9,\"#000030\"],[1.0,\"#000031\"]],\"sequential\":[[0.0,\"#000011\"],[0.1111111111111111,\"#000012\"],[0.2222222222222222,\"#000013\"],[0.3333333333333333,\"#000014\"],[0.4444444444444444,\"#000015\"],[0.5555555555555556,\"#000016\"],[0.6666666666666666,\"#000017\"],[0.7777777777777778,\"#000018\"],[0.8888888888888888,\"#000019\"],[1.0,\"#000020\"]],\"sequentialminus\":[[0.0,\"#000011\"],[0.1111111111111111,\"#000012\"],[0.2222222222222222,\"#000013\"],[0.3333333333333333,\"#000014\"],[0.4444444444444444,\"#000015\"],[0.5555555555555556,\"#000016\"],[0.6666666666666666,\"#000017\"],[0.7777777777777778,\"#000018\"],[0.8888888888888888,\"#000019\"],[1.0,\"#000020\"]]},\"colorway\":[\"#000001\",\"#000002\",\"#000003\",\"#000004\",\"#000005\",\"#000006\",\"#000007\",\"#000008\",\"#000009\",\"#000010\"]}},\"xaxis\":{\"anchor\":\"y\",\"domain\":[0.0,1.0],\"title\":{\"text\":\"\"}},\"yaxis\":{\"anchor\":\"x\",\"domain\":[0.0,1.0],\"title\":{\"text\":\"\"}},\"legend\":{\"tracegroupgap\":0},\"margin\":{\"t\":60},\"boxmode\":\"group\",\"height\":500,\"width\":500,\"title\":{\"font\":{\"size\":22,\"color\":\"#164f5e\"},\"text\":\"Hard Hit%+\",\"automargin\":true,\"yref\":\"paper\"}},                        {\"responsive\": true}                    ).then(function(){\n",
       "                            \n",
       "var gd = document.getElementById('ce1f52c0-2efa-4afe-a3e9-ea751a71b0e3');\n",
       "var x = new MutationObserver(function (mutations, observer) {{\n",
       "        var display = window.getComputedStyle(gd).display;\n",
       "        if (!display || display === 'none') {{\n",
       "            console.log([gd, 'removed!']);\n",
       "            Plotly.purge(gd);\n",
       "            observer.disconnect();\n",
       "        }}\n",
       "}});\n",
       "\n",
       "// Listen for the removal of the full notebook cells\n",
       "var notebookContainer = gd.closest('#notebook-container');\n",
       "if (notebookContainer) {{\n",
       "    x.observe(notebookContainer, {childList: true});\n",
       "}}\n",
       "\n",
       "// Listen for the clearing of the current output cell\n",
       "var outputEl = gd.closest('.output');\n",
       "if (outputEl) {{\n",
       "    x.observe(outputEl, {childList: true});\n",
       "}}\n",
       "\n",
       "                        })                };                });            </script>        </div>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "fig_22 = px.box(\n",
    "    df.query(\"Season==2023\"),\n",
    "    y = \"Hard%+\",\n",
    "    points=\"all\",\n",
    "    hover_name = \"Name\",\n",
    "    height = 500,\n",
    "    width = 500,\n",
    ")\n",
    "\n",
    "fig_22.update_traces(marker=dict(color=\"#7284cc\"))\n",
    "\n",
    "fig_22.update_layout(\n",
    "    title=dict(text=\"Hard Hit%+\", font=dict(size=22), automargin=True, yref='paper'),\n",
    "    title_font_color=\"#164f5e\",\n",
    "    yaxis=dict(title=\"\"),\n",
    "    xaxis=dict(title=\"\")\n",
    ")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 92,
   "id": "2eb96303",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "application/vnd.plotly.v1+json": {
       "config": {
        "plotlyServerURL": "https://plot.ly"
       },
       "data": [
        {
         "alignmentgroup": "True",
         "boxpoints": "all",
         "hovertemplate": "<b>%{hovertext}</b><br><br>HR=%{y}<extra></extra>",
         "hovertext": [
          "Ronald Acuna Jr.",
          "Shohei Ohtani",
          "Mookie Betts",
          "Wander Franco",
          "Corbin Carroll",
          "Luis Robert",
          "Freddie Freeman",
          "Juan Soto",
          "Fernando Tatis Jr.",
          "Jose Ramirez",
          "Adolis Garcia",
          "Mike Trout",
          "Jonah Heim",
          "Marcus Semien",
          "Bo Bichette",
          "Christian Yelich",
          "Francisco Lindor",
          "Dansby Swanson",
          "Luis Arraez",
          "Will Smith",
          "Ha-seong Kim",
          "Randy Arozarena",
          "Paul Goldschmidt",
          "Matt Chapman",
          "Isaac Paredes",
          "Brandon Nimmo",
          "Jeimer Candelario",
          "Thairo Estrada",
          "Matt Olson",
          "Christian Walker",
          "Jack Suwinski",
          "Julio Rodriguez",
          "Yandy Diaz",
          "Kyle Tucker",
          "Josh Jung",
          "Ketel Marte",
          "Ozzie Albies",
          "William Contreras",
          "Xander Bogaerts",
          "Leody Taveras",
          "Adley Rutschman",
          "Nico Hoerner",
          "Lane Thomas",
          "Bobby Witt Jr.",
          "LaMonte Wade Jr.",
          "Austin Hays",
          "J.D. Davis",
          "Gunnar Henderson",
          "Alex Verdugo",
          "Nathaniel Lowe",
          "Jorge Soler",
          "Nolan Arenado",
          "Rafael Devers",
          "Austin Riley",
          "Brendan Donovan",
          "Bryson Stott",
          "Brandon Drury",
          "Brandon Marsh",
          "Ian Happ",
          "J.P. Crawford",
          "Alex Bregman",
          "Andres Gimenez",
          "Cal Raleigh",
          "Spencer Steer",
          "Nolan Gorman",
          "Ryan Noda",
          "Cedric Mullins II",
          "James Outman",
          "Nick Castellanos",
          "Pete Alonso",
          "Anthony Santander",
          "Ryan McMahon",
          "Zach McKinstry",
          "Trea Turner",
          "Anthony Volpe",
          "Masataka Yoshida",
          "Justin Turner",
          "Bryan Reynolds",
          "Manny Machado",
          "Whit Merrifield",
          "Jeremy Pena",
          "Josh Naylor",
          "Anthony Rizzo",
          "Jonathan India",
          "Jarred Kelenic",
          "George Springer",
          "Eugenio Suarez",
          "Joey Wiemer",
          "Andrew McCutchen",
          "Lourdes Gurriel Jr.",
          "Max Muncy",
          "Hunter Renfroe",
          "Mauricio Dubon",
          "Steven Kwan",
          "Tommy Edman",
          "Brent Rooker",
          "J.T. Realmuto",
          "Teoscar Hernandez",
          "Ezequiel Tovar",
          "Willson Contreras",
          "Carlos Correa",
          "Ke'Bryan Hayes",
          "Willy Adames",
          "Gleyber Torres",
          "Esteury Ruiz",
          "Marcell Ozuna",
          "Byron Buxton",
          "Andrew Benintendi",
          "Daulton Varsho",
          "J.D. Martinez",
          "Elias Diaz",
          "Ty France",
          "Taylor Ward",
          "Jeff McNeil",
          "Eddie Rosario",
          "Seiya Suzuki",
          "Carlos Santana",
          "Trent Grisham",
          "Vladimir Guerrero Jr.",
          "Michael Conforto",
          "Brian Anderson",
          "Jace Peterson",
          "Javier Baez",
          "Andrew Vaughn",
          "Alec Bohm",
          "Bryan De La Cruz",
          "Jake Cronenworth",
          "Salvador Perez",
          "CJ Abrams",
          "Spencer Torkelson",
          "Adam Frazier",
          "Miguel Vargas",
          "Amed Rosario",
          "Starling Marte",
          "Luis Garcia",
          "DJ LeMahieu",
          "Tyler Stephenson",
          "Kyle Schwarber",
          "Triston Casas",
          "Dominic Smith",
          "Shea Langeliers",
          "Josh Bell",
          "Myles Straw",
          "Joey Meneses",
          "Jose Abreu",
          "MJ Melendez",
          "Tim Anderson",
          "Rowdy Tellez",
          "Jurickson Profar",
          "Keibert Ruiz",
          "Enrique Hernandez"
         ],
         "legendgroup": "",
         "marker": {
          "color": "#7284cc"
         },
         "name": "",
         "notched": false,
         "offsetgroup": "",
         "orientation": "v",
         "showlegend": false,
         "type": "box",
         "x0": " ",
         "xaxis": "x",
         "y": [
          21,
          31,
          23,
          10,
          18,
          25,
          15,
          15,
          16,
          14,
          22,
          18,
          12,
          11,
          15,
          11,
          18,
          10,
          3,
          12,
          10,
          16,
          15,
          12,
          15,
          13,
          12,
          9,
          29,
          18,
          19,
          13,
          12,
          13,
          17,
          15,
          22,
          9,
          10,
          10,
          11,
          5,
          14,
          13,
          9,
          8,
          10,
          13,
          6,
          9,
          22,
          17,
          20,
          16,
          9,
          7,
          14,
          7,
          7,
          8,
          12,
          7,
          11,
          14,
          17,
          9,
          8,
          11,
          13,
          26,
          14,
          13,
          6,
          9,
          12,
          9,
          13,
          9,
          12,
          4,
          10,
          11,
          11,
          13,
          11,
          12,
          11,
          11,
          10,
          14,
          20,
          15,
          4,
          2,
          7,
          14,
          9,
          15,
          8,
          9,
          11,
          5,
          13,
          13,
          1,
          17,
          15,
          1,
          12,
          20,
          9,
          7,
          9,
          3,
          14,
          6,
          9,
          8,
          13,
          12,
          9,
          5,
          6,
          12,
          9,
          9,
          8,
          15,
          7,
          12,
          10,
          7,
          2,
          5,
          5,
          7,
          7,
          22,
          9,
          4,
          10,
          8,
          0,
          2,
          7,
          6,
          0,
          12,
          6,
          9,
          6
         ],
         "y0": " ",
         "yaxis": "y"
        }
       ],
       "layout": {
        "boxmode": "group",
        "height": 500,
        "legend": {
         "tracegroupgap": 0
        },
        "margin": {
         "t": 60
        },
        "template": {
         "data": {
          "candlestick": [
           {
            "decreasing": {
             "line": {
              "color": "#000033"
             }
            },
            "increasing": {
             "line": {
              "color": "#000032"
             }
            },
            "type": "candlestick"
           }
          ],
          "contour": [
           {
            "colorscale": [
             [
              0,
              "#000011"
             ],
             [
              0.1111111111111111,
              "#000012"
             ],
             [
              0.2222222222222222,
              "#000013"
             ],
             [
              0.3333333333333333,
              "#000014"
             ],
             [
              0.4444444444444444,
              "#000015"
             ],
             [
              0.5555555555555556,
              "#000016"
             ],
             [
              0.6666666666666666,
              "#000017"
             ],
             [
              0.7777777777777778,
              "#000018"
             ],
             [
              0.8888888888888888,
              "#000019"
             ],
             [
              1,
              "#000020"
             ]
            ],
            "type": "contour"
           }
          ],
          "contourcarpet": [
           {
            "colorscale": [
             [
              0,
              "#000011"
             ],
             [
              0.1111111111111111,
              "#000012"
             ],
             [
              0.2222222222222222,
              "#000013"
             ],
             [
              0.3333333333333333,
              "#000014"
             ],
             [
              0.4444444444444444,
              "#000015"
             ],
             [
              0.5555555555555556,
              "#000016"
             ],
             [
              0.6666666666666666,
              "#000017"
             ],
             [
              0.7777777777777778,
              "#000018"
             ],
             [
              0.8888888888888888,
              "#000019"
             ],
             [
              1,
              "#000020"
             ]
            ],
            "type": "contourcarpet"
           }
          ],
          "heatmap": [
           {
            "colorscale": [
             [
              0,
              "#000011"
             ],
             [
              0.1111111111111111,
              "#000012"
             ],
             [
              0.2222222222222222,
              "#000013"
             ],
             [
              0.3333333333333333,
              "#000014"
             ],
             [
              0.4444444444444444,
              "#000015"
             ],
             [
              0.5555555555555556,
              "#000016"
             ],
             [
              0.6666666666666666,
              "#000017"
             ],
             [
              0.7777777777777778,
              "#000018"
             ],
             [
              0.8888888888888888,
              "#000019"
             ],
             [
              1,
              "#000020"
             ]
            ],
            "type": "heatmap"
           }
          ],
          "histogram2d": [
           {
            "colorscale": [
             [
              0,
              "#000011"
             ],
             [
              0.1111111111111111,
              "#000012"
             ],
             [
              0.2222222222222222,
              "#000013"
             ],
             [
              0.3333333333333333,
              "#000014"
             ],
             [
              0.4444444444444444,
              "#000015"
             ],
             [
              0.5555555555555556,
              "#000016"
             ],
             [
              0.6666666666666666,
              "#000017"
             ],
             [
              0.7777777777777778,
              "#000018"
             ],
             [
              0.8888888888888888,
              "#000019"
             ],
             [
              1,
              "#000020"
             ]
            ],
            "type": "histogram2d"
           }
          ],
          "icicle": [
           {
            "textfont": {
             "color": "white"
            },
            "type": "icicle"
           }
          ],
          "sankey": [
           {
            "textfont": {
             "color": "#000036"
            },
            "type": "sankey"
           }
          ],
          "scatter": [
           {
            "marker": {
             "line": {
              "width": 0
             }
            },
            "type": "scatter"
           }
          ],
          "table": [
           {
            "cells": {
             "fill": {
              "color": "#000038"
             },
             "font": {
              "color": "#000037"
             },
             "line": {
              "color": "#000039"
             }
            },
            "header": {
             "fill": {
              "color": "#000040"
             },
             "font": {
              "color": "#000036"
             },
             "line": {
              "color": "#000039"
             }
            },
            "type": "table"
           }
          ],
          "waterfall": [
           {
            "connector": {
             "line": {
              "color": "#000036",
              "width": 2
             }
            },
            "decreasing": {
             "marker": {
              "color": "#000033"
             }
            },
            "increasing": {
             "marker": {
              "color": "#000032"
             }
            },
            "totals": {
             "marker": {
              "color": "#000034"
             }
            },
            "type": "waterfall"
           }
          ]
         },
         "layout": {
          "coloraxis": {
           "colorscale": [
            [
             0,
             "#000011"
            ],
            [
             0.1111111111111111,
             "#000012"
            ],
            [
             0.2222222222222222,
             "#000013"
            ],
            [
             0.3333333333333333,
             "#000014"
            ],
            [
             0.4444444444444444,
             "#000015"
            ],
            [
             0.5555555555555556,
             "#000016"
            ],
            [
             0.6666666666666666,
             "#000017"
            ],
            [
             0.7777777777777778,
             "#000018"
            ],
            [
             0.8888888888888888,
             "#000019"
            ],
            [
             1,
             "#000020"
            ]
           ]
          },
          "colorscale": {
           "diverging": [
            [
             0,
             "#000021"
            ],
            [
             0.1,
             "#000022"
            ],
            [
             0.2,
             "#000023"
            ],
            [
             0.3,
             "#000024"
            ],
            [
             0.4,
             "#000025"
            ],
            [
             0.5,
             "#000026"
            ],
            [
             0.6,
             "#000027"
            ],
            [
             0.7,
             "#000028"
            ],
            [
             0.8,
             "#000029"
            ],
            [
             0.9,
             "#000030"
            ],
            [
             1,
             "#000031"
            ]
           ],
           "sequential": [
            [
             0,
             "#000011"
            ],
            [
             0.1111111111111111,
             "#000012"
            ],
            [
             0.2222222222222222,
             "#000013"
            ],
            [
             0.3333333333333333,
             "#000014"
            ],
            [
             0.4444444444444444,
             "#000015"
            ],
            [
             0.5555555555555556,
             "#000016"
            ],
            [
             0.6666666666666666,
             "#000017"
            ],
            [
             0.7777777777777778,
             "#000018"
            ],
            [
             0.8888888888888888,
             "#000019"
            ],
            [
             1,
             "#000020"
            ]
           ],
           "sequentialminus": [
            [
             0,
             "#000011"
            ],
            [
             0.1111111111111111,
             "#000012"
            ],
            [
             0.2222222222222222,
             "#000013"
            ],
            [
             0.3333333333333333,
             "#000014"
            ],
            [
             0.4444444444444444,
             "#000015"
            ],
            [
             0.5555555555555556,
             "#000016"
            ],
            [
             0.6666666666666666,
             "#000017"
            ],
            [
             0.7777777777777778,
             "#000018"
            ],
            [
             0.8888888888888888,
             "#000019"
            ],
            [
             1,
             "#000020"
            ]
           ]
          },
          "colorway": [
           "#000001",
           "#000002",
           "#000003",
           "#000004",
           "#000005",
           "#000006",
           "#000007",
           "#000008",
           "#000009",
           "#000010"
          ]
         }
        },
        "title": {
         "automargin": true,
         "font": {
          "color": "#164f5e",
          "size": 22
         },
         "text": "Home Runs",
         "yref": "paper"
        },
        "width": 500,
        "xaxis": {
         "anchor": "y",
         "domain": [
          0,
          1
         ],
         "title": {
          "text": ""
         }
        },
        "yaxis": {
         "anchor": "x",
         "domain": [
          0,
          1
         ],
         "title": {
          "text": ""
         }
        }
       }
      },
      "text/html": [
       "<div>                            <div id=\"3a1bcd38-a2c4-4e3e-8df6-a8b01e5c879c\" class=\"plotly-graph-div\" style=\"height:500px; width:500px;\"></div>            <script type=\"text/javascript\">                require([\"plotly\"], function(Plotly) {                    window.PLOTLYENV=window.PLOTLYENV || {};                                    if (document.getElementById(\"3a1bcd38-a2c4-4e3e-8df6-a8b01e5c879c\")) {                    Plotly.newPlot(                        \"3a1bcd38-a2c4-4e3e-8df6-a8b01e5c879c\",                        [{\"alignmentgroup\":\"True\",\"boxpoints\":\"all\",\"hovertemplate\":\"\\u003cb\\u003e%{hovertext}\\u003c\\u002fb\\u003e\\u003cbr\\u003e\\u003cbr\\u003eHR=%{y}\\u003cextra\\u003e\\u003c\\u002fextra\\u003e\",\"hovertext\":[\"Ronald Acuna Jr.\",\"Shohei Ohtani\",\"Mookie Betts\",\"Wander Franco\",\"Corbin Carroll\",\"Luis Robert\",\"Freddie Freeman\",\"Juan Soto\",\"Fernando Tatis Jr.\",\"Jose Ramirez\",\"Adolis Garcia\",\"Mike Trout\",\"Jonah Heim\",\"Marcus Semien\",\"Bo Bichette\",\"Christian Yelich\",\"Francisco Lindor\",\"Dansby Swanson\",\"Luis Arraez\",\"Will Smith\",\"Ha-seong Kim\",\"Randy Arozarena\",\"Paul Goldschmidt\",\"Matt Chapman\",\"Isaac Paredes\",\"Brandon Nimmo\",\"Jeimer Candelario\",\"Thairo Estrada\",\"Matt Olson\",\"Christian Walker\",\"Jack Suwinski\",\"Julio Rodriguez\",\"Yandy Diaz\",\"Kyle Tucker\",\"Josh Jung\",\"Ketel Marte\",\"Ozzie Albies\",\"William Contreras\",\"Xander Bogaerts\",\"Leody Taveras\",\"Adley Rutschman\",\"Nico Hoerner\",\"Lane Thomas\",\"Bobby Witt Jr.\",\"LaMonte Wade Jr.\",\"Austin Hays\",\"J.D. Davis\",\"Gunnar Henderson\",\"Alex Verdugo\",\"Nathaniel Lowe\",\"Jorge Soler\",\"Nolan Arenado\",\"Rafael Devers\",\"Austin Riley\",\"Brendan Donovan\",\"Bryson Stott\",\"Brandon Drury\",\"Brandon Marsh\",\"Ian Happ\",\"J.P. Crawford\",\"Alex Bregman\",\"Andres Gimenez\",\"Cal Raleigh\",\"Spencer Steer\",\"Nolan Gorman\",\"Ryan Noda\",\"Cedric Mullins II\",\"James Outman\",\"Nick Castellanos\",\"Pete Alonso\",\"Anthony Santander\",\"Ryan McMahon\",\"Zach McKinstry\",\"Trea Turner\",\"Anthony Volpe\",\"Masataka Yoshida\",\"Justin Turner\",\"Bryan Reynolds\",\"Manny Machado\",\"Whit Merrifield\",\"Jeremy Pena\",\"Josh Naylor\",\"Anthony Rizzo\",\"Jonathan India\",\"Jarred Kelenic\",\"George Springer\",\"Eugenio Suarez\",\"Joey Wiemer\",\"Andrew McCutchen\",\"Lourdes Gurriel Jr.\",\"Max Muncy\",\"Hunter Renfroe\",\"Mauricio Dubon\",\"Steven Kwan\",\"Tommy Edman\",\"Brent Rooker\",\"J.T. Realmuto\",\"Teoscar Hernandez\",\"Ezequiel Tovar\",\"Willson Contreras\",\"Carlos Correa\",\"Ke'Bryan Hayes\",\"Willy Adames\",\"Gleyber Torres\",\"Esteury Ruiz\",\"Marcell Ozuna\",\"Byron Buxton\",\"Andrew Benintendi\",\"Daulton Varsho\",\"J.D. Martinez\",\"Elias Diaz\",\"Ty France\",\"Taylor Ward\",\"Jeff McNeil\",\"Eddie Rosario\",\"Seiya Suzuki\",\"Carlos Santana\",\"Trent Grisham\",\"Vladimir Guerrero Jr.\",\"Michael Conforto\",\"Brian Anderson\",\"Jace Peterson\",\"Javier Baez\",\"Andrew Vaughn\",\"Alec Bohm\",\"Bryan De La Cruz\",\"Jake Cronenworth\",\"Salvador Perez\",\"CJ Abrams\",\"Spencer Torkelson\",\"Adam Frazier\",\"Miguel Vargas\",\"Amed Rosario\",\"Starling Marte\",\"Luis Garcia\",\"DJ LeMahieu\",\"Tyler Stephenson\",\"Kyle Schwarber\",\"Triston Casas\",\"Dominic Smith\",\"Shea Langeliers\",\"Josh Bell\",\"Myles Straw\",\"Joey Meneses\",\"Jose Abreu\",\"MJ Melendez\",\"Tim Anderson\",\"Rowdy Tellez\",\"Jurickson Profar\",\"Keibert Ruiz\",\"Enrique Hernandez\"],\"legendgroup\":\"\",\"marker\":{\"color\":\"#7284cc\"},\"name\":\"\",\"notched\":false,\"offsetgroup\":\"\",\"orientation\":\"v\",\"showlegend\":false,\"x0\":\" \",\"xaxis\":\"x\",\"y\":[21,31,23,10,18,25,15,15,16,14,22,18,12,11,15,11,18,10,3,12,10,16,15,12,15,13,12,9,29,18,19,13,12,13,17,15,22,9,10,10,11,5,14,13,9,8,10,13,6,9,22,17,20,16,9,7,14,7,7,8,12,7,11,14,17,9,8,11,13,26,14,13,6,9,12,9,13,9,12,4,10,11,11,13,11,12,11,11,10,14,20,15,4,2,7,14,9,15,8,9,11,5,13,13,1,17,15,1,12,20,9,7,9,3,14,6,9,8,13,12,9,5,6,12,9,9,8,15,7,12,10,7,2,5,5,7,7,22,9,4,10,8,0,2,7,6,0,12,6,9,6],\"y0\":\" \",\"yaxis\":\"y\",\"type\":\"box\"}],                        {\"template\":{\"data\":{\"candlestick\":[{\"decreasing\":{\"line\":{\"color\":\"#000033\"}},\"increasing\":{\"line\":{\"color\":\"#000032\"}},\"type\":\"candlestick\"}],\"contourcarpet\":[{\"colorscale\":[[0.0,\"#000011\"],[0.1111111111111111,\"#000012\"],[0.2222222222222222,\"#000013\"],[0.3333333333333333,\"#000014\"],[0.4444444444444444,\"#000015\"],[0.5555555555555556,\"#000016\"],[0.6666666666666666,\"#000017\"],[0.7777777777777778,\"#000018\"],[0.8888888888888888,\"#000019\"],[1.0,\"#000020\"]],\"type\":\"contourcarpet\"}],\"contour\":[{\"colorscale\":[[0.0,\"#000011\"],[0.1111111111111111,\"#000012\"],[0.2222222222222222,\"#000013\"],[0.3333333333333333,\"#000014\"],[0.4444444444444444,\"#000015\"],[0.5555555555555556,\"#000016\"],[0.6666666666666666,\"#000017\"],[0.7777777777777778,\"#000018\"],[0.8888888888888888,\"#000019\"],[1.0,\"#000020\"]],\"type\":\"contour\"}],\"heatmap\":[{\"colorscale\":[[0.0,\"#000011\"],[0.1111111111111111,\"#000012\"],[0.2222222222222222,\"#000013\"],[0.3333333333333333,\"#000014\"],[0.4444444444444444,\"#000015\"],[0.5555555555555556,\"#000016\"],[0.6666666666666666,\"#000017\"],[0.7777777777777778,\"#000018\"],[0.8888888888888888,\"#000019\"],[1.0,\"#000020\"]],\"type\":\"heatmap\"}],\"histogram2d\":[{\"colorscale\":[[0.0,\"#000011\"],[0.1111111111111111,\"#000012\"],[0.2222222222222222,\"#000013\"],[0.3333333333333333,\"#000014\"],[0.4444444444444444,\"#000015\"],[0.5555555555555556,\"#000016\"],[0.6666666666666666,\"#000017\"],[0.7777777777777778,\"#000018\"],[0.8888888888888888,\"#000019\"],[1.0,\"#000020\"]],\"type\":\"histogram2d\"}],\"icicle\":[{\"textfont\":{\"color\":\"white\"},\"type\":\"icicle\"}],\"sankey\":[{\"textfont\":{\"color\":\"#000036\"},\"type\":\"sankey\"}],\"scatter\":[{\"marker\":{\"line\":{\"width\":0}},\"type\":\"scatter\"}],\"table\":[{\"cells\":{\"fill\":{\"color\":\"#000038\"},\"font\":{\"color\":\"#000037\"},\"line\":{\"color\":\"#000039\"}},\"header\":{\"fill\":{\"color\":\"#000040\"},\"font\":{\"color\":\"#000036\"},\"line\":{\"color\":\"#000039\"}},\"type\":\"table\"}],\"waterfall\":[{\"connector\":{\"line\":{\"color\":\"#000036\",\"width\":2}},\"decreasing\":{\"marker\":{\"color\":\"#000033\"}},\"increasing\":{\"marker\":{\"color\":\"#000032\"}},\"totals\":{\"marker\":{\"color\":\"#000034\"}},\"type\":\"waterfall\"}]},\"layout\":{\"coloraxis\":{\"colorscale\":[[0.0,\"#000011\"],[0.1111111111111111,\"#000012\"],[0.2222222222222222,\"#000013\"],[0.3333333333333333,\"#000014\"],[0.4444444444444444,\"#000015\"],[0.5555555555555556,\"#000016\"],[0.6666666666666666,\"#000017\"],[0.7777777777777778,\"#000018\"],[0.8888888888888888,\"#000019\"],[1.0,\"#000020\"]]},\"colorscale\":{\"diverging\":[[0.0,\"#000021\"],[0.1,\"#000022\"],[0.2,\"#000023\"],[0.3,\"#000024\"],[0.4,\"#000025\"],[0.5,\"#000026\"],[0.6,\"#000027\"],[0.7,\"#000028\"],[0.8,\"#000029\"],[0.9,\"#000030\"],[1.0,\"#000031\"]],\"sequential\":[[0.0,\"#000011\"],[0.1111111111111111,\"#000012\"],[0.2222222222222222,\"#000013\"],[0.3333333333333333,\"#000014\"],[0.4444444444444444,\"#000015\"],[0.5555555555555556,\"#000016\"],[0.6666666666666666,\"#000017\"],[0.7777777777777778,\"#000018\"],[0.8888888888888888,\"#000019\"],[1.0,\"#000020\"]],\"sequentialminus\":[[0.0,\"#000011\"],[0.1111111111111111,\"#000012\"],[0.2222222222222222,\"#000013\"],[0.3333333333333333,\"#000014\"],[0.4444444444444444,\"#000015\"],[0.5555555555555556,\"#000016\"],[0.6666666666666666,\"#000017\"],[0.7777777777777778,\"#000018\"],[0.8888888888888888,\"#000019\"],[1.0,\"#000020\"]]},\"colorway\":[\"#000001\",\"#000002\",\"#000003\",\"#000004\",\"#000005\",\"#000006\",\"#000007\",\"#000008\",\"#000009\",\"#000010\"]}},\"xaxis\":{\"anchor\":\"y\",\"domain\":[0.0,1.0],\"title\":{\"text\":\"\"}},\"yaxis\":{\"anchor\":\"x\",\"domain\":[0.0,1.0],\"title\":{\"text\":\"\"}},\"legend\":{\"tracegroupgap\":0},\"margin\":{\"t\":60},\"boxmode\":\"group\",\"height\":500,\"width\":500,\"title\":{\"font\":{\"size\":22,\"color\":\"#164f5e\"},\"text\":\"Home Runs\",\"automargin\":true,\"yref\":\"paper\"}},                        {\"responsive\": true}                    ).then(function(){\n",
       "                            \n",
       "var gd = document.getElementById('3a1bcd38-a2c4-4e3e-8df6-a8b01e5c879c');\n",
       "var x = new MutationObserver(function (mutations, observer) {{\n",
       "        var display = window.getComputedStyle(gd).display;\n",
       "        if (!display || display === 'none') {{\n",
       "            console.log([gd, 'removed!']);\n",
       "            Plotly.purge(gd);\n",
       "            observer.disconnect();\n",
       "        }}\n",
       "}});\n",
       "\n",
       "// Listen for the removal of the full notebook cells\n",
       "var notebookContainer = gd.closest('#notebook-container');\n",
       "if (notebookContainer) {{\n",
       "    x.observe(notebookContainer, {childList: true});\n",
       "}}\n",
       "\n",
       "// Listen for the clearing of the current output cell\n",
       "var outputEl = gd.closest('.output');\n",
       "if (outputEl) {{\n",
       "    x.observe(outputEl, {childList: true});\n",
       "}}\n",
       "\n",
       "                        })                };                });            </script>        </div>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "fig_23 = px.box(\n",
    "    df.query(\"Season==2023\"),\n",
    "    y = \"HR\",\n",
    "    points=\"all\",\n",
    "    hover_name = \"Name\",\n",
    "    height = 500,\n",
    "    width = 500,\n",
    ")\n",
    "\n",
    "fig_23.update_traces(marker=dict(color=\"#7284cc\"))\n",
    "\n",
    "fig_23.update_layout(\n",
    "    title=dict(text=\"Home Runs\", font=dict(size=22), automargin=True, yref='paper'),\n",
    "    title_font_color=\"#164f5e\",\n",
    "    yaxis=dict(title=\"\"),\n",
    "    xaxis=dict(title=\"\")\n",
    ")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "de290dae",
   "metadata": {},
   "source": [
    "### Row 1 - Tab 3"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 93,
   "id": "45de4f85",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "application/vnd.plotly.v1+json": {
       "config": {
        "plotlyServerURL": "https://plot.ly"
       },
       "data": [
        {
         "alignmentgroup": "True",
         "boxpoints": "all",
         "hovertemplate": "<b>%{hovertext}</b><br><br>Contact%=%{y}<extra></extra>",
         "hovertext": [
          "Ronald Acuna Jr.",
          "Shohei Ohtani",
          "Mookie Betts",
          "Wander Franco",
          "Corbin Carroll",
          "Luis Robert",
          "Freddie Freeman",
          "Juan Soto",
          "Fernando Tatis Jr.",
          "Jose Ramirez",
          "Adolis Garcia",
          "Mike Trout",
          "Jonah Heim",
          "Marcus Semien",
          "Bo Bichette",
          "Christian Yelich",
          "Francisco Lindor",
          "Dansby Swanson",
          "Luis Arraez",
          "Will Smith",
          "Ha-seong Kim",
          "Randy Arozarena",
          "Paul Goldschmidt",
          "Matt Chapman",
          "Isaac Paredes",
          "Brandon Nimmo",
          "Jeimer Candelario",
          "Thairo Estrada",
          "Matt Olson",
          "Christian Walker",
          "Jack Suwinski",
          "Julio Rodriguez",
          "Yandy Diaz",
          "Kyle Tucker",
          "Josh Jung",
          "Ketel Marte",
          "Ozzie Albies",
          "William Contreras",
          "Xander Bogaerts",
          "Leody Taveras",
          "Adley Rutschman",
          "Nico Hoerner",
          "Lane Thomas",
          "Bobby Witt Jr.",
          "LaMonte Wade Jr.",
          "Austin Hays",
          "J.D. Davis",
          "Gunnar Henderson",
          "Alex Verdugo",
          "Nathaniel Lowe",
          "Jorge Soler",
          "Nolan Arenado",
          "Rafael Devers",
          "Austin Riley",
          "Brendan Donovan",
          "Bryson Stott",
          "Brandon Drury",
          "Brandon Marsh",
          "Ian Happ",
          "J.P. Crawford",
          "Alex Bregman",
          "Andres Gimenez",
          "Cal Raleigh",
          "Spencer Steer",
          "Nolan Gorman",
          "Ryan Noda",
          "Cedric Mullins II",
          "James Outman",
          "Nick Castellanos",
          "Pete Alonso",
          "Anthony Santander",
          "Ryan McMahon",
          "Zach McKinstry",
          "Trea Turner",
          "Anthony Volpe",
          "Masataka Yoshida",
          "Justin Turner",
          "Bryan Reynolds",
          "Manny Machado",
          "Whit Merrifield",
          "Jeremy Pena",
          "Josh Naylor",
          "Anthony Rizzo",
          "Jonathan India",
          "Jarred Kelenic",
          "George Springer",
          "Eugenio Suarez",
          "Joey Wiemer",
          "Andrew McCutchen",
          "Lourdes Gurriel Jr.",
          "Max Muncy",
          "Hunter Renfroe",
          "Mauricio Dubon",
          "Steven Kwan",
          "Tommy Edman",
          "Brent Rooker",
          "J.T. Realmuto",
          "Teoscar Hernandez",
          "Ezequiel Tovar",
          "Willson Contreras",
          "Carlos Correa",
          "Ke'Bryan Hayes",
          "Willy Adames",
          "Gleyber Torres",
          "Esteury Ruiz",
          "Marcell Ozuna",
          "Byron Buxton",
          "Andrew Benintendi",
          "Daulton Varsho",
          "J.D. Martinez",
          "Elias Diaz",
          "Ty France",
          "Taylor Ward",
          "Jeff McNeil",
          "Eddie Rosario",
          "Seiya Suzuki",
          "Carlos Santana",
          "Trent Grisham",
          "Vladimir Guerrero Jr.",
          "Michael Conforto",
          "Brian Anderson",
          "Jace Peterson",
          "Javier Baez",
          "Andrew Vaughn",
          "Alec Bohm",
          "Bryan De La Cruz",
          "Jake Cronenworth",
          "Salvador Perez",
          "CJ Abrams",
          "Spencer Torkelson",
          "Adam Frazier",
          "Miguel Vargas",
          "Amed Rosario",
          "Starling Marte",
          "Luis Garcia",
          "DJ LeMahieu",
          "Tyler Stephenson",
          "Kyle Schwarber",
          "Triston Casas",
          "Dominic Smith",
          "Shea Langeliers",
          "Josh Bell",
          "Myles Straw",
          "Joey Meneses",
          "Jose Abreu",
          "MJ Melendez",
          "Tim Anderson",
          "Rowdy Tellez",
          "Jurickson Profar",
          "Keibert Ruiz",
          "Enrique Hernandez"
         ],
         "legendgroup": "",
         "marker": {
          "color": "#7284cc"
         },
         "name": "",
         "notched": false,
         "offsetgroup": "",
         "orientation": "v",
         "showlegend": false,
         "type": "box",
         "x0": " ",
         "xaxis": "x",
         "y": [
          0.8220000000000001,
          0.7140000000000001,
          0.8390000000000001,
          0.877,
          0.812,
          0.687,
          0.8029999999999999,
          0.807,
          0.743,
          0.862,
          0.722,
          0.757,
          0.8059999999999999,
          0.8340000000000001,
          0.826,
          0.768,
          0.785,
          0.732,
          0.949,
          0.841,
          0.828,
          0.715,
          0.753,
          0.741,
          0.838,
          0.79,
          0.7979999999999999,
          0.8029999999999999,
          0.713,
          0.772,
          0.71,
          0.726,
          0.845,
          0.856,
          0.757,
          0.812,
          0.812,
          0.76,
          0.804,
          0.78,
          0.868,
          0.897,
          0.802,
          0.758,
          0.813,
          0.748,
          0.698,
          0.721,
          0.877,
          0.8240000000000001,
          0.75,
          0.7929999999999999,
          0.75,
          0.753,
          0.865,
          0.8690000000000001,
          0.7290000000000001,
          0.757,
          0.7659999999999999,
          0.8370000000000001,
          0.867,
          0.7759999999999999,
          0.7340000000000001,
          0.8,
          0.6970000000000001,
          0.65,
          0.787,
          0.64,
          0.67,
          0.7709999999999999,
          0.777,
          0.7090000000000001,
          0.8290000000000001,
          0.711,
          0.725,
          0.846,
          0.841,
          0.7490000000000001,
          0.768,
          0.818,
          0.733,
          0.813,
          0.78,
          0.807,
          0.7040000000000001,
          0.812,
          0.716,
          0.674,
          0.741,
          0.846,
          0.695,
          0.765,
          0.845,
          0.903,
          0.846,
          0.631,
          0.768,
          0.679,
          0.7290000000000001,
          0.7390000000000001,
          0.763,
          0.816,
          0.718,
          0.8079999999999999,
          0.762,
          0.7390000000000001,
          0.726,
          0.833,
          0.79,
          0.6779999999999999,
          0.757,
          0.797,
          0.812,
          0.86,
          0.727,
          0.8029999999999999,
          0.779,
          0.7190000000000001,
          0.782,
          0.757,
          0.7020000000000001,
          0.7909999999999999,
          0.701,
          0.7759999999999999,
          0.848,
          0.726,
          0.85,
          0.705,
          0.7809999999999999,
          0.784,
          0.838,
          0.809,
          0.775,
          0.7609999999999999,
          0.8590000000000001,
          0.826,
          0.7290000000000001,
          0.695,
          0.7509999999999999,
          0.82,
          0.6890000000000001,
          0.773,
          0.885,
          0.78,
          0.764,
          0.665,
          0.779,
          0.805,
          0.823,
          0.872,
          0.7509999999999999
         ],
         "y0": " ",
         "yaxis": "y"
        }
       ],
       "layout": {
        "boxmode": "group",
        "height": 500,
        "legend": {
         "tracegroupgap": 0
        },
        "margin": {
         "t": 60
        },
        "template": {
         "data": {
          "candlestick": [
           {
            "decreasing": {
             "line": {
              "color": "#000033"
             }
            },
            "increasing": {
             "line": {
              "color": "#000032"
             }
            },
            "type": "candlestick"
           }
          ],
          "contour": [
           {
            "colorscale": [
             [
              0,
              "#000011"
             ],
             [
              0.1111111111111111,
              "#000012"
             ],
             [
              0.2222222222222222,
              "#000013"
             ],
             [
              0.3333333333333333,
              "#000014"
             ],
             [
              0.4444444444444444,
              "#000015"
             ],
             [
              0.5555555555555556,
              "#000016"
             ],
             [
              0.6666666666666666,
              "#000017"
             ],
             [
              0.7777777777777778,
              "#000018"
             ],
             [
              0.8888888888888888,
              "#000019"
             ],
             [
              1,
              "#000020"
             ]
            ],
            "type": "contour"
           }
          ],
          "contourcarpet": [
           {
            "colorscale": [
             [
              0,
              "#000011"
             ],
             [
              0.1111111111111111,
              "#000012"
             ],
             [
              0.2222222222222222,
              "#000013"
             ],
             [
              0.3333333333333333,
              "#000014"
             ],
             [
              0.4444444444444444,
              "#000015"
             ],
             [
              0.5555555555555556,
              "#000016"
             ],
             [
              0.6666666666666666,
              "#000017"
             ],
             [
              0.7777777777777778,
              "#000018"
             ],
             [
              0.8888888888888888,
              "#000019"
             ],
             [
              1,
              "#000020"
             ]
            ],
            "type": "contourcarpet"
           }
          ],
          "heatmap": [
           {
            "colorscale": [
             [
              0,
              "#000011"
             ],
             [
              0.1111111111111111,
              "#000012"
             ],
             [
              0.2222222222222222,
              "#000013"
             ],
             [
              0.3333333333333333,
              "#000014"
             ],
             [
              0.4444444444444444,
              "#000015"
             ],
             [
              0.5555555555555556,
              "#000016"
             ],
             [
              0.6666666666666666,
              "#000017"
             ],
             [
              0.7777777777777778,
              "#000018"
             ],
             [
              0.8888888888888888,
              "#000019"
             ],
             [
              1,
              "#000020"
             ]
            ],
            "type": "heatmap"
           }
          ],
          "histogram2d": [
           {
            "colorscale": [
             [
              0,
              "#000011"
             ],
             [
              0.1111111111111111,
              "#000012"
             ],
             [
              0.2222222222222222,
              "#000013"
             ],
             [
              0.3333333333333333,
              "#000014"
             ],
             [
              0.4444444444444444,
              "#000015"
             ],
             [
              0.5555555555555556,
              "#000016"
             ],
             [
              0.6666666666666666,
              "#000017"
             ],
             [
              0.7777777777777778,
              "#000018"
             ],
             [
              0.8888888888888888,
              "#000019"
             ],
             [
              1,
              "#000020"
             ]
            ],
            "type": "histogram2d"
           }
          ],
          "icicle": [
           {
            "textfont": {
             "color": "white"
            },
            "type": "icicle"
           }
          ],
          "sankey": [
           {
            "textfont": {
             "color": "#000036"
            },
            "type": "sankey"
           }
          ],
          "scatter": [
           {
            "marker": {
             "line": {
              "width": 0
             }
            },
            "type": "scatter"
           }
          ],
          "table": [
           {
            "cells": {
             "fill": {
              "color": "#000038"
             },
             "font": {
              "color": "#000037"
             },
             "line": {
              "color": "#000039"
             }
            },
            "header": {
             "fill": {
              "color": "#000040"
             },
             "font": {
              "color": "#000036"
             },
             "line": {
              "color": "#000039"
             }
            },
            "type": "table"
           }
          ],
          "waterfall": [
           {
            "connector": {
             "line": {
              "color": "#000036",
              "width": 2
             }
            },
            "decreasing": {
             "marker": {
              "color": "#000033"
             }
            },
            "increasing": {
             "marker": {
              "color": "#000032"
             }
            },
            "totals": {
             "marker": {
              "color": "#000034"
             }
            },
            "type": "waterfall"
           }
          ]
         },
         "layout": {
          "coloraxis": {
           "colorscale": [
            [
             0,
             "#000011"
            ],
            [
             0.1111111111111111,
             "#000012"
            ],
            [
             0.2222222222222222,
             "#000013"
            ],
            [
             0.3333333333333333,
             "#000014"
            ],
            [
             0.4444444444444444,
             "#000015"
            ],
            [
             0.5555555555555556,
             "#000016"
            ],
            [
             0.6666666666666666,
             "#000017"
            ],
            [
             0.7777777777777778,
             "#000018"
            ],
            [
             0.8888888888888888,
             "#000019"
            ],
            [
             1,
             "#000020"
            ]
           ]
          },
          "colorscale": {
           "diverging": [
            [
             0,
             "#000021"
            ],
            [
             0.1,
             "#000022"
            ],
            [
             0.2,
             "#000023"
            ],
            [
             0.3,
             "#000024"
            ],
            [
             0.4,
             "#000025"
            ],
            [
             0.5,
             "#000026"
            ],
            [
             0.6,
             "#000027"
            ],
            [
             0.7,
             "#000028"
            ],
            [
             0.8,
             "#000029"
            ],
            [
             0.9,
             "#000030"
            ],
            [
             1,
             "#000031"
            ]
           ],
           "sequential": [
            [
             0,
             "#000011"
            ],
            [
             0.1111111111111111,
             "#000012"
            ],
            [
             0.2222222222222222,
             "#000013"
            ],
            [
             0.3333333333333333,
             "#000014"
            ],
            [
             0.4444444444444444,
             "#000015"
            ],
            [
             0.5555555555555556,
             "#000016"
            ],
            [
             0.6666666666666666,
             "#000017"
            ],
            [
             0.7777777777777778,
             "#000018"
            ],
            [
             0.8888888888888888,
             "#000019"
            ],
            [
             1,
             "#000020"
            ]
           ],
           "sequentialminus": [
            [
             0,
             "#000011"
            ],
            [
             0.1111111111111111,
             "#000012"
            ],
            [
             0.2222222222222222,
             "#000013"
            ],
            [
             0.3333333333333333,
             "#000014"
            ],
            [
             0.4444444444444444,
             "#000015"
            ],
            [
             0.5555555555555556,
             "#000016"
            ],
            [
             0.6666666666666666,
             "#000017"
            ],
            [
             0.7777777777777778,
             "#000018"
            ],
            [
             0.8888888888888888,
             "#000019"
            ],
            [
             1,
             "#000020"
            ]
           ]
          },
          "colorway": [
           "#000001",
           "#000002",
           "#000003",
           "#000004",
           "#000005",
           "#000006",
           "#000007",
           "#000008",
           "#000009",
           "#000010"
          ]
         }
        },
        "title": {
         "automargin": true,
         "font": {
          "color": "#164f5e",
          "size": 22
         },
         "text": "Contact%",
         "yref": "paper"
        },
        "width": 500,
        "xaxis": {
         "anchor": "y",
         "domain": [
          0,
          1
         ],
         "title": {
          "text": ""
         }
        },
        "yaxis": {
         "anchor": "x",
         "domain": [
          0,
          1
         ],
         "title": {
          "text": ""
         }
        }
       }
      },
      "text/html": [
       "<div>                            <div id=\"e9b9e2a6-1f29-4922-bde5-ec87582a3b71\" class=\"plotly-graph-div\" style=\"height:500px; width:500px;\"></div>            <script type=\"text/javascript\">                require([\"plotly\"], function(Plotly) {                    window.PLOTLYENV=window.PLOTLYENV || {};                                    if (document.getElementById(\"e9b9e2a6-1f29-4922-bde5-ec87582a3b71\")) {                    Plotly.newPlot(                        \"e9b9e2a6-1f29-4922-bde5-ec87582a3b71\",                        [{\"alignmentgroup\":\"True\",\"boxpoints\":\"all\",\"hovertemplate\":\"\\u003cb\\u003e%{hovertext}\\u003c\\u002fb\\u003e\\u003cbr\\u003e\\u003cbr\\u003eContact%=%{y}\\u003cextra\\u003e\\u003c\\u002fextra\\u003e\",\"hovertext\":[\"Ronald Acuna Jr.\",\"Shohei Ohtani\",\"Mookie Betts\",\"Wander Franco\",\"Corbin Carroll\",\"Luis Robert\",\"Freddie Freeman\",\"Juan Soto\",\"Fernando Tatis Jr.\",\"Jose Ramirez\",\"Adolis Garcia\",\"Mike Trout\",\"Jonah Heim\",\"Marcus Semien\",\"Bo Bichette\",\"Christian Yelich\",\"Francisco Lindor\",\"Dansby Swanson\",\"Luis Arraez\",\"Will Smith\",\"Ha-seong Kim\",\"Randy Arozarena\",\"Paul Goldschmidt\",\"Matt Chapman\",\"Isaac Paredes\",\"Brandon Nimmo\",\"Jeimer Candelario\",\"Thairo Estrada\",\"Matt Olson\",\"Christian Walker\",\"Jack Suwinski\",\"Julio Rodriguez\",\"Yandy Diaz\",\"Kyle Tucker\",\"Josh Jung\",\"Ketel Marte\",\"Ozzie Albies\",\"William Contreras\",\"Xander Bogaerts\",\"Leody Taveras\",\"Adley Rutschman\",\"Nico Hoerner\",\"Lane Thomas\",\"Bobby Witt Jr.\",\"LaMonte Wade Jr.\",\"Austin Hays\",\"J.D. Davis\",\"Gunnar Henderson\",\"Alex Verdugo\",\"Nathaniel Lowe\",\"Jorge Soler\",\"Nolan Arenado\",\"Rafael Devers\",\"Austin Riley\",\"Brendan Donovan\",\"Bryson Stott\",\"Brandon Drury\",\"Brandon Marsh\",\"Ian Happ\",\"J.P. Crawford\",\"Alex Bregman\",\"Andres Gimenez\",\"Cal Raleigh\",\"Spencer Steer\",\"Nolan Gorman\",\"Ryan Noda\",\"Cedric Mullins II\",\"James Outman\",\"Nick Castellanos\",\"Pete Alonso\",\"Anthony Santander\",\"Ryan McMahon\",\"Zach McKinstry\",\"Trea Turner\",\"Anthony Volpe\",\"Masataka Yoshida\",\"Justin Turner\",\"Bryan Reynolds\",\"Manny Machado\",\"Whit Merrifield\",\"Jeremy Pena\",\"Josh Naylor\",\"Anthony Rizzo\",\"Jonathan India\",\"Jarred Kelenic\",\"George Springer\",\"Eugenio Suarez\",\"Joey Wiemer\",\"Andrew McCutchen\",\"Lourdes Gurriel Jr.\",\"Max Muncy\",\"Hunter Renfroe\",\"Mauricio Dubon\",\"Steven Kwan\",\"Tommy Edman\",\"Brent Rooker\",\"J.T. Realmuto\",\"Teoscar Hernandez\",\"Ezequiel Tovar\",\"Willson Contreras\",\"Carlos Correa\",\"Ke'Bryan Hayes\",\"Willy Adames\",\"Gleyber Torres\",\"Esteury Ruiz\",\"Marcell Ozuna\",\"Byron Buxton\",\"Andrew Benintendi\",\"Daulton Varsho\",\"J.D. Martinez\",\"Elias Diaz\",\"Ty France\",\"Taylor Ward\",\"Jeff McNeil\",\"Eddie Rosario\",\"Seiya Suzuki\",\"Carlos Santana\",\"Trent Grisham\",\"Vladimir Guerrero Jr.\",\"Michael Conforto\",\"Brian Anderson\",\"Jace Peterson\",\"Javier Baez\",\"Andrew Vaughn\",\"Alec Bohm\",\"Bryan De La Cruz\",\"Jake Cronenworth\",\"Salvador Perez\",\"CJ Abrams\",\"Spencer Torkelson\",\"Adam Frazier\",\"Miguel Vargas\",\"Amed Rosario\",\"Starling Marte\",\"Luis Garcia\",\"DJ LeMahieu\",\"Tyler Stephenson\",\"Kyle Schwarber\",\"Triston Casas\",\"Dominic Smith\",\"Shea Langeliers\",\"Josh Bell\",\"Myles Straw\",\"Joey Meneses\",\"Jose Abreu\",\"MJ Melendez\",\"Tim Anderson\",\"Rowdy Tellez\",\"Jurickson Profar\",\"Keibert Ruiz\",\"Enrique Hernandez\"],\"legendgroup\":\"\",\"marker\":{\"color\":\"#7284cc\"},\"name\":\"\",\"notched\":false,\"offsetgroup\":\"\",\"orientation\":\"v\",\"showlegend\":false,\"x0\":\" \",\"xaxis\":\"x\",\"y\":[0.8220000000000001,0.7140000000000001,0.8390000000000001,0.877,0.812,0.687,0.8029999999999999,0.807,0.743,0.862,0.722,0.757,0.8059999999999999,0.8340000000000001,0.826,0.768,0.785,0.732,0.949,0.841,0.828,0.715,0.753,0.741,0.838,0.79,0.7979999999999999,0.8029999999999999,0.713,0.772,0.71,0.726,0.845,0.856,0.757,0.812,0.812,0.76,0.804,0.78,0.868,0.897,0.802,0.758,0.813,0.748,0.698,0.721,0.877,0.8240000000000001,0.75,0.7929999999999999,0.75,0.753,0.865,0.8690000000000001,0.7290000000000001,0.757,0.7659999999999999,0.8370000000000001,0.867,0.7759999999999999,0.7340000000000001,0.8,0.6970000000000001,0.65,0.787,0.64,0.67,0.7709999999999999,0.777,0.7090000000000001,0.8290000000000001,0.711,0.725,0.846,0.841,0.7490000000000001,0.768,0.818,0.733,0.813,0.78,0.807,0.7040000000000001,0.812,0.716,0.674,0.741,0.846,0.695,0.765,0.845,0.903,0.846,0.631,0.768,0.679,0.7290000000000001,0.7390000000000001,0.763,0.816,0.718,0.8079999999999999,0.762,0.7390000000000001,0.726,0.833,0.79,0.6779999999999999,0.757,0.797,0.812,0.86,0.727,0.8029999999999999,0.779,0.7190000000000001,0.782,0.757,0.7020000000000001,0.7909999999999999,0.701,0.7759999999999999,0.848,0.726,0.85,0.705,0.7809999999999999,0.784,0.838,0.809,0.775,0.7609999999999999,0.8590000000000001,0.826,0.7290000000000001,0.695,0.7509999999999999,0.82,0.6890000000000001,0.773,0.885,0.78,0.764,0.665,0.779,0.805,0.823,0.872,0.7509999999999999],\"y0\":\" \",\"yaxis\":\"y\",\"type\":\"box\"}],                        {\"template\":{\"data\":{\"candlestick\":[{\"decreasing\":{\"line\":{\"color\":\"#000033\"}},\"increasing\":{\"line\":{\"color\":\"#000032\"}},\"type\":\"candlestick\"}],\"contourcarpet\":[{\"colorscale\":[[0.0,\"#000011\"],[0.1111111111111111,\"#000012\"],[0.2222222222222222,\"#000013\"],[0.3333333333333333,\"#000014\"],[0.4444444444444444,\"#000015\"],[0.5555555555555556,\"#000016\"],[0.6666666666666666,\"#000017\"],[0.7777777777777778,\"#000018\"],[0.8888888888888888,\"#000019\"],[1.0,\"#000020\"]],\"type\":\"contourcarpet\"}],\"contour\":[{\"colorscale\":[[0.0,\"#000011\"],[0.1111111111111111,\"#000012\"],[0.2222222222222222,\"#000013\"],[0.3333333333333333,\"#000014\"],[0.4444444444444444,\"#000015\"],[0.5555555555555556,\"#000016\"],[0.6666666666666666,\"#000017\"],[0.7777777777777778,\"#000018\"],[0.8888888888888888,\"#000019\"],[1.0,\"#000020\"]],\"type\":\"contour\"}],\"heatmap\":[{\"colorscale\":[[0.0,\"#000011\"],[0.1111111111111111,\"#000012\"],[0.2222222222222222,\"#000013\"],[0.3333333333333333,\"#000014\"],[0.4444444444444444,\"#000015\"],[0.5555555555555556,\"#000016\"],[0.6666666666666666,\"#000017\"],[0.7777777777777778,\"#000018\"],[0.8888888888888888,\"#000019\"],[1.0,\"#000020\"]],\"type\":\"heatmap\"}],\"histogram2d\":[{\"colorscale\":[[0.0,\"#000011\"],[0.1111111111111111,\"#000012\"],[0.2222222222222222,\"#000013\"],[0.3333333333333333,\"#000014\"],[0.4444444444444444,\"#000015\"],[0.5555555555555556,\"#000016\"],[0.6666666666666666,\"#000017\"],[0.7777777777777778,\"#000018\"],[0.8888888888888888,\"#000019\"],[1.0,\"#000020\"]],\"type\":\"histogram2d\"}],\"icicle\":[{\"textfont\":{\"color\":\"white\"},\"type\":\"icicle\"}],\"sankey\":[{\"textfont\":{\"color\":\"#000036\"},\"type\":\"sankey\"}],\"scatter\":[{\"marker\":{\"line\":{\"width\":0}},\"type\":\"scatter\"}],\"table\":[{\"cells\":{\"fill\":{\"color\":\"#000038\"},\"font\":{\"color\":\"#000037\"},\"line\":{\"color\":\"#000039\"}},\"header\":{\"fill\":{\"color\":\"#000040\"},\"font\":{\"color\":\"#000036\"},\"line\":{\"color\":\"#000039\"}},\"type\":\"table\"}],\"waterfall\":[{\"connector\":{\"line\":{\"color\":\"#000036\",\"width\":2}},\"decreasing\":{\"marker\":{\"color\":\"#000033\"}},\"increasing\":{\"marker\":{\"color\":\"#000032\"}},\"totals\":{\"marker\":{\"color\":\"#000034\"}},\"type\":\"waterfall\"}]},\"layout\":{\"coloraxis\":{\"colorscale\":[[0.0,\"#000011\"],[0.1111111111111111,\"#000012\"],[0.2222222222222222,\"#000013\"],[0.3333333333333333,\"#000014\"],[0.4444444444444444,\"#000015\"],[0.5555555555555556,\"#000016\"],[0.6666666666666666,\"#000017\"],[0.7777777777777778,\"#000018\"],[0.8888888888888888,\"#000019\"],[1.0,\"#000020\"]]},\"colorscale\":{\"diverging\":[[0.0,\"#000021\"],[0.1,\"#000022\"],[0.2,\"#000023\"],[0.3,\"#000024\"],[0.4,\"#000025\"],[0.5,\"#000026\"],[0.6,\"#000027\"],[0.7,\"#000028\"],[0.8,\"#000029\"],[0.9,\"#000030\"],[1.0,\"#000031\"]],\"sequential\":[[0.0,\"#000011\"],[0.1111111111111111,\"#000012\"],[0.2222222222222222,\"#000013\"],[0.3333333333333333,\"#000014\"],[0.4444444444444444,\"#000015\"],[0.5555555555555556,\"#000016\"],[0.6666666666666666,\"#000017\"],[0.7777777777777778,\"#000018\"],[0.8888888888888888,\"#000019\"],[1.0,\"#000020\"]],\"sequentialminus\":[[0.0,\"#000011\"],[0.1111111111111111,\"#000012\"],[0.2222222222222222,\"#000013\"],[0.3333333333333333,\"#000014\"],[0.4444444444444444,\"#000015\"],[0.5555555555555556,\"#000016\"],[0.6666666666666666,\"#000017\"],[0.7777777777777778,\"#000018\"],[0.8888888888888888,\"#000019\"],[1.0,\"#000020\"]]},\"colorway\":[\"#000001\",\"#000002\",\"#000003\",\"#000004\",\"#000005\",\"#000006\",\"#000007\",\"#000008\",\"#000009\",\"#000010\"]}},\"xaxis\":{\"anchor\":\"y\",\"domain\":[0.0,1.0],\"title\":{\"text\":\"\"}},\"yaxis\":{\"anchor\":\"x\",\"domain\":[0.0,1.0],\"title\":{\"text\":\"\"}},\"legend\":{\"tracegroupgap\":0},\"margin\":{\"t\":60},\"boxmode\":\"group\",\"height\":500,\"width\":500,\"title\":{\"font\":{\"size\":22,\"color\":\"#164f5e\"},\"text\":\"Contact%\",\"automargin\":true,\"yref\":\"paper\"}},                        {\"responsive\": true}                    ).then(function(){\n",
       "                            \n",
       "var gd = document.getElementById('e9b9e2a6-1f29-4922-bde5-ec87582a3b71');\n",
       "var x = new MutationObserver(function (mutations, observer) {{\n",
       "        var display = window.getComputedStyle(gd).display;\n",
       "        if (!display || display === 'none') {{\n",
       "            console.log([gd, 'removed!']);\n",
       "            Plotly.purge(gd);\n",
       "            observer.disconnect();\n",
       "        }}\n",
       "}});\n",
       "\n",
       "// Listen for the removal of the full notebook cells\n",
       "var notebookContainer = gd.closest('#notebook-container');\n",
       "if (notebookContainer) {{\n",
       "    x.observe(notebookContainer, {childList: true});\n",
       "}}\n",
       "\n",
       "// Listen for the clearing of the current output cell\n",
       "var outputEl = gd.closest('.output');\n",
       "if (outputEl) {{\n",
       "    x.observe(outputEl, {childList: true});\n",
       "}}\n",
       "\n",
       "                        })                };                });            </script>        </div>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "fig_31 = px.box(\n",
    "    df.query(\"Season==2023\"),\n",
    "    y = \"Contact%\",\n",
    "    points=\"all\",\n",
    "    hover_name = \"Name\",\n",
    "    height = 500,\n",
    "    width = 500,\n",
    ")\n",
    "\n",
    "fig_31.update_traces(marker=dict(color=\"#7284cc\"))\n",
    "\n",
    "fig_31.update_layout(\n",
    "    title=dict(text=\"Contact%\", font=dict(size=22), automargin=True, yref='paper'),\n",
    "    title_font_color=\"#164f5e\",\n",
    "    yaxis=dict(title=\"\"),\n",
    "    xaxis=dict(title=\"\")\n",
    ")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 94,
   "id": "db727fa0",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "application/vnd.plotly.v1+json": {
       "config": {
        "plotlyServerURL": "https://plot.ly"
       },
       "data": [
        {
         "alignmentgroup": "True",
         "boxpoints": "all",
         "hovertemplate": "<b>%{hovertext}</b><br><br>Z-Contact%=%{y}<extra></extra>",
         "hovertext": [
          "Ronald Acuna Jr.",
          "Shohei Ohtani",
          "Mookie Betts",
          "Wander Franco",
          "Corbin Carroll",
          "Luis Robert",
          "Freddie Freeman",
          "Juan Soto",
          "Fernando Tatis Jr.",
          "Jose Ramirez",
          "Adolis Garcia",
          "Mike Trout",
          "Jonah Heim",
          "Marcus Semien",
          "Bo Bichette",
          "Christian Yelich",
          "Francisco Lindor",
          "Dansby Swanson",
          "Luis Arraez",
          "Will Smith",
          "Ha-seong Kim",
          "Randy Arozarena",
          "Paul Goldschmidt",
          "Matt Chapman",
          "Isaac Paredes",
          "Brandon Nimmo",
          "Jeimer Candelario",
          "Thairo Estrada",
          "Matt Olson",
          "Christian Walker",
          "Jack Suwinski",
          "Julio Rodriguez",
          "Yandy Diaz",
          "Kyle Tucker",
          "Josh Jung",
          "Ketel Marte",
          "Ozzie Albies",
          "William Contreras",
          "Xander Bogaerts",
          "Leody Taveras",
          "Adley Rutschman",
          "Nico Hoerner",
          "Lane Thomas",
          "Bobby Witt Jr.",
          "LaMonte Wade Jr.",
          "Austin Hays",
          "J.D. Davis",
          "Gunnar Henderson",
          "Alex Verdugo",
          "Nathaniel Lowe",
          "Jorge Soler",
          "Nolan Arenado",
          "Rafael Devers",
          "Austin Riley",
          "Brendan Donovan",
          "Bryson Stott",
          "Brandon Drury",
          "Brandon Marsh",
          "Ian Happ",
          "J.P. Crawford",
          "Alex Bregman",
          "Andres Gimenez",
          "Cal Raleigh",
          "Spencer Steer",
          "Nolan Gorman",
          "Ryan Noda",
          "Cedric Mullins II",
          "James Outman",
          "Nick Castellanos",
          "Pete Alonso",
          "Anthony Santander",
          "Ryan McMahon",
          "Zach McKinstry",
          "Trea Turner",
          "Anthony Volpe",
          "Masataka Yoshida",
          "Justin Turner",
          "Bryan Reynolds",
          "Manny Machado",
          "Whit Merrifield",
          "Jeremy Pena",
          "Josh Naylor",
          "Anthony Rizzo",
          "Jonathan India",
          "Jarred Kelenic",
          "George Springer",
          "Eugenio Suarez",
          "Joey Wiemer",
          "Andrew McCutchen",
          "Lourdes Gurriel Jr.",
          "Max Muncy",
          "Hunter Renfroe",
          "Mauricio Dubon",
          "Steven Kwan",
          "Tommy Edman",
          "Brent Rooker",
          "J.T. Realmuto",
          "Teoscar Hernandez",
          "Ezequiel Tovar",
          "Willson Contreras",
          "Carlos Correa",
          "Ke'Bryan Hayes",
          "Willy Adames",
          "Gleyber Torres",
          "Esteury Ruiz",
          "Marcell Ozuna",
          "Byron Buxton",
          "Andrew Benintendi",
          "Daulton Varsho",
          "J.D. Martinez",
          "Elias Diaz",
          "Ty France",
          "Taylor Ward",
          "Jeff McNeil",
          "Eddie Rosario",
          "Seiya Suzuki",
          "Carlos Santana",
          "Trent Grisham",
          "Vladimir Guerrero Jr.",
          "Michael Conforto",
          "Brian Anderson",
          "Jace Peterson",
          "Javier Baez",
          "Andrew Vaughn",
          "Alec Bohm",
          "Bryan De La Cruz",
          "Jake Cronenworth",
          "Salvador Perez",
          "CJ Abrams",
          "Spencer Torkelson",
          "Adam Frazier",
          "Miguel Vargas",
          "Amed Rosario",
          "Starling Marte",
          "Luis Garcia",
          "DJ LeMahieu",
          "Tyler Stephenson",
          "Kyle Schwarber",
          "Triston Casas",
          "Dominic Smith",
          "Shea Langeliers",
          "Josh Bell",
          "Myles Straw",
          "Joey Meneses",
          "Jose Abreu",
          "MJ Melendez",
          "Tim Anderson",
          "Rowdy Tellez",
          "Jurickson Profar",
          "Keibert Ruiz",
          "Enrique Hernandez"
         ],
         "legendgroup": "",
         "marker": {
          "color": "#7284cc"
         },
         "name": "",
         "notched": false,
         "offsetgroup": "",
         "orientation": "v",
         "showlegend": false,
         "type": "box",
         "x0": " ",
         "xaxis": "x",
         "y": [
          0.871,
          0.7959999999999999,
          0.935,
          0.92,
          0.863,
          0.82,
          0.86,
          0.899,
          0.821,
          0.932,
          0.789,
          0.823,
          0.882,
          0.92,
          0.902,
          0.852,
          0.8759999999999999,
          0.7809999999999999,
          0.957,
          0.866,
          0.875,
          0.7829999999999999,
          0.7979999999999999,
          0.797,
          0.92,
          0.877,
          0.884,
          0.911,
          0.754,
          0.847,
          0.772,
          0.841,
          0.919,
          0.922,
          0.86,
          0.899,
          0.895,
          0.847,
          0.875,
          0.865,
          0.921,
          0.946,
          0.895,
          0.8370000000000001,
          0.888,
          0.883,
          0.8,
          0.799,
          0.954,
          0.903,
          0.8540000000000001,
          0.91,
          0.8029999999999999,
          0.845,
          0.933,
          0.894,
          0.8640000000000001,
          0.8740000000000001,
          0.84,
          0.914,
          0.936,
          0.831,
          0.807,
          0.861,
          0.81,
          0.765,
          0.823,
          0.7659999999999999,
          0.8220000000000001,
          0.8440000000000001,
          0.8490000000000001,
          0.774,
          0.907,
          0.8340000000000001,
          0.843,
          0.8959999999999999,
          0.908,
          0.853,
          0.861,
          0.877,
          0.899,
          0.9,
          0.8859999999999999,
          0.894,
          0.8079999999999999,
          0.889,
          0.82,
          0.7809999999999999,
          0.826,
          0.934,
          0.7979999999999999,
          0.863,
          0.879,
          0.953,
          0.942,
          0.748,
          0.8540000000000001,
          0.804,
          0.848,
          0.8690000000000001,
          0.851,
          0.936,
          0.843,
          0.879,
          0.8759999999999999,
          0.8370000000000001,
          0.825,
          0.893,
          0.871,
          0.809,
          0.8540000000000001,
          0.92,
          0.915,
          0.925,
          0.777,
          0.877,
          0.846,
          0.782,
          0.867,
          0.8420000000000001,
          0.797,
          0.8740000000000001,
          0.812,
          0.893,
          0.911,
          0.8109999999999999,
          0.926,
          0.8220000000000001,
          0.865,
          0.865,
          0.915,
          0.88,
          0.875,
          0.8740000000000001,
          0.909,
          0.913,
          0.84,
          0.8029999999999999,
          0.8170000000000001,
          0.8740000000000001,
          0.8109999999999999,
          0.84,
          0.911,
          0.889,
          0.868,
          0.7509999999999999,
          0.865,
          0.889,
          0.898,
          0.948,
          0.862
         ],
         "y0": " ",
         "yaxis": "y"
        }
       ],
       "layout": {
        "boxmode": "group",
        "height": 500,
        "legend": {
         "tracegroupgap": 0
        },
        "margin": {
         "t": 60
        },
        "template": {
         "data": {
          "candlestick": [
           {
            "decreasing": {
             "line": {
              "color": "#000033"
             }
            },
            "increasing": {
             "line": {
              "color": "#000032"
             }
            },
            "type": "candlestick"
           }
          ],
          "contour": [
           {
            "colorscale": [
             [
              0,
              "#000011"
             ],
             [
              0.1111111111111111,
              "#000012"
             ],
             [
              0.2222222222222222,
              "#000013"
             ],
             [
              0.3333333333333333,
              "#000014"
             ],
             [
              0.4444444444444444,
              "#000015"
             ],
             [
              0.5555555555555556,
              "#000016"
             ],
             [
              0.6666666666666666,
              "#000017"
             ],
             [
              0.7777777777777778,
              "#000018"
             ],
             [
              0.8888888888888888,
              "#000019"
             ],
             [
              1,
              "#000020"
             ]
            ],
            "type": "contour"
           }
          ],
          "contourcarpet": [
           {
            "colorscale": [
             [
              0,
              "#000011"
             ],
             [
              0.1111111111111111,
              "#000012"
             ],
             [
              0.2222222222222222,
              "#000013"
             ],
             [
              0.3333333333333333,
              "#000014"
             ],
             [
              0.4444444444444444,
              "#000015"
             ],
             [
              0.5555555555555556,
              "#000016"
             ],
             [
              0.6666666666666666,
              "#000017"
             ],
             [
              0.7777777777777778,
              "#000018"
             ],
             [
              0.8888888888888888,
              "#000019"
             ],
             [
              1,
              "#000020"
             ]
            ],
            "type": "contourcarpet"
           }
          ],
          "heatmap": [
           {
            "colorscale": [
             [
              0,
              "#000011"
             ],
             [
              0.1111111111111111,
              "#000012"
             ],
             [
              0.2222222222222222,
              "#000013"
             ],
             [
              0.3333333333333333,
              "#000014"
             ],
             [
              0.4444444444444444,
              "#000015"
             ],
             [
              0.5555555555555556,
              "#000016"
             ],
             [
              0.6666666666666666,
              "#000017"
             ],
             [
              0.7777777777777778,
              "#000018"
             ],
             [
              0.8888888888888888,
              "#000019"
             ],
             [
              1,
              "#000020"
             ]
            ],
            "type": "heatmap"
           }
          ],
          "histogram2d": [
           {
            "colorscale": [
             [
              0,
              "#000011"
             ],
             [
              0.1111111111111111,
              "#000012"
             ],
             [
              0.2222222222222222,
              "#000013"
             ],
             [
              0.3333333333333333,
              "#000014"
             ],
             [
              0.4444444444444444,
              "#000015"
             ],
             [
              0.5555555555555556,
              "#000016"
             ],
             [
              0.6666666666666666,
              "#000017"
             ],
             [
              0.7777777777777778,
              "#000018"
             ],
             [
              0.8888888888888888,
              "#000019"
             ],
             [
              1,
              "#000020"
             ]
            ],
            "type": "histogram2d"
           }
          ],
          "icicle": [
           {
            "textfont": {
             "color": "white"
            },
            "type": "icicle"
           }
          ],
          "sankey": [
           {
            "textfont": {
             "color": "#000036"
            },
            "type": "sankey"
           }
          ],
          "scatter": [
           {
            "marker": {
             "line": {
              "width": 0
             }
            },
            "type": "scatter"
           }
          ],
          "table": [
           {
            "cells": {
             "fill": {
              "color": "#000038"
             },
             "font": {
              "color": "#000037"
             },
             "line": {
              "color": "#000039"
             }
            },
            "header": {
             "fill": {
              "color": "#000040"
             },
             "font": {
              "color": "#000036"
             },
             "line": {
              "color": "#000039"
             }
            },
            "type": "table"
           }
          ],
          "waterfall": [
           {
            "connector": {
             "line": {
              "color": "#000036",
              "width": 2
             }
            },
            "decreasing": {
             "marker": {
              "color": "#000033"
             }
            },
            "increasing": {
             "marker": {
              "color": "#000032"
             }
            },
            "totals": {
             "marker": {
              "color": "#000034"
             }
            },
            "type": "waterfall"
           }
          ]
         },
         "layout": {
          "coloraxis": {
           "colorscale": [
            [
             0,
             "#000011"
            ],
            [
             0.1111111111111111,
             "#000012"
            ],
            [
             0.2222222222222222,
             "#000013"
            ],
            [
             0.3333333333333333,
             "#000014"
            ],
            [
             0.4444444444444444,
             "#000015"
            ],
            [
             0.5555555555555556,
             "#000016"
            ],
            [
             0.6666666666666666,
             "#000017"
            ],
            [
             0.7777777777777778,
             "#000018"
            ],
            [
             0.8888888888888888,
             "#000019"
            ],
            [
             1,
             "#000020"
            ]
           ]
          },
          "colorscale": {
           "diverging": [
            [
             0,
             "#000021"
            ],
            [
             0.1,
             "#000022"
            ],
            [
             0.2,
             "#000023"
            ],
            [
             0.3,
             "#000024"
            ],
            [
             0.4,
             "#000025"
            ],
            [
             0.5,
             "#000026"
            ],
            [
             0.6,
             "#000027"
            ],
            [
             0.7,
             "#000028"
            ],
            [
             0.8,
             "#000029"
            ],
            [
             0.9,
             "#000030"
            ],
            [
             1,
             "#000031"
            ]
           ],
           "sequential": [
            [
             0,
             "#000011"
            ],
            [
             0.1111111111111111,
             "#000012"
            ],
            [
             0.2222222222222222,
             "#000013"
            ],
            [
             0.3333333333333333,
             "#000014"
            ],
            [
             0.4444444444444444,
             "#000015"
            ],
            [
             0.5555555555555556,
             "#000016"
            ],
            [
             0.6666666666666666,
             "#000017"
            ],
            [
             0.7777777777777778,
             "#000018"
            ],
            [
             0.8888888888888888,
             "#000019"
            ],
            [
             1,
             "#000020"
            ]
           ],
           "sequentialminus": [
            [
             0,
             "#000011"
            ],
            [
             0.1111111111111111,
             "#000012"
            ],
            [
             0.2222222222222222,
             "#000013"
            ],
            [
             0.3333333333333333,
             "#000014"
            ],
            [
             0.4444444444444444,
             "#000015"
            ],
            [
             0.5555555555555556,
             "#000016"
            ],
            [
             0.6666666666666666,
             "#000017"
            ],
            [
             0.7777777777777778,
             "#000018"
            ],
            [
             0.8888888888888888,
             "#000019"
            ],
            [
             1,
             "#000020"
            ]
           ]
          },
          "colorway": [
           "#000001",
           "#000002",
           "#000003",
           "#000004",
           "#000005",
           "#000006",
           "#000007",
           "#000008",
           "#000009",
           "#000010"
          ]
         }
        },
        "title": {
         "automargin": true,
         "font": {
          "color": "#164f5e",
          "size": 22
         },
         "text": "In-Zone Contact%",
         "yref": "paper"
        },
        "width": 500,
        "xaxis": {
         "anchor": "y",
         "domain": [
          0,
          1
         ],
         "title": {
          "text": ""
         }
        },
        "yaxis": {
         "anchor": "x",
         "domain": [
          0,
          1
         ],
         "title": {
          "text": ""
         }
        }
       }
      },
      "text/html": [
       "<div>                            <div id=\"7bb394eb-4286-44b7-ba79-cf778e362ad0\" class=\"plotly-graph-div\" style=\"height:500px; width:500px;\"></div>            <script type=\"text/javascript\">                require([\"plotly\"], function(Plotly) {                    window.PLOTLYENV=window.PLOTLYENV || {};                                    if (document.getElementById(\"7bb394eb-4286-44b7-ba79-cf778e362ad0\")) {                    Plotly.newPlot(                        \"7bb394eb-4286-44b7-ba79-cf778e362ad0\",                        [{\"alignmentgroup\":\"True\",\"boxpoints\":\"all\",\"hovertemplate\":\"\\u003cb\\u003e%{hovertext}\\u003c\\u002fb\\u003e\\u003cbr\\u003e\\u003cbr\\u003eZ-Contact%=%{y}\\u003cextra\\u003e\\u003c\\u002fextra\\u003e\",\"hovertext\":[\"Ronald Acuna Jr.\",\"Shohei Ohtani\",\"Mookie Betts\",\"Wander Franco\",\"Corbin Carroll\",\"Luis Robert\",\"Freddie Freeman\",\"Juan Soto\",\"Fernando Tatis Jr.\",\"Jose Ramirez\",\"Adolis Garcia\",\"Mike Trout\",\"Jonah Heim\",\"Marcus Semien\",\"Bo Bichette\",\"Christian Yelich\",\"Francisco Lindor\",\"Dansby Swanson\",\"Luis Arraez\",\"Will Smith\",\"Ha-seong Kim\",\"Randy Arozarena\",\"Paul Goldschmidt\",\"Matt Chapman\",\"Isaac Paredes\",\"Brandon Nimmo\",\"Jeimer Candelario\",\"Thairo Estrada\",\"Matt Olson\",\"Christian Walker\",\"Jack Suwinski\",\"Julio Rodriguez\",\"Yandy Diaz\",\"Kyle Tucker\",\"Josh Jung\",\"Ketel Marte\",\"Ozzie Albies\",\"William Contreras\",\"Xander Bogaerts\",\"Leody Taveras\",\"Adley Rutschman\",\"Nico Hoerner\",\"Lane Thomas\",\"Bobby Witt Jr.\",\"LaMonte Wade Jr.\",\"Austin Hays\",\"J.D. Davis\",\"Gunnar Henderson\",\"Alex Verdugo\",\"Nathaniel Lowe\",\"Jorge Soler\",\"Nolan Arenado\",\"Rafael Devers\",\"Austin Riley\",\"Brendan Donovan\",\"Bryson Stott\",\"Brandon Drury\",\"Brandon Marsh\",\"Ian Happ\",\"J.P. Crawford\",\"Alex Bregman\",\"Andres Gimenez\",\"Cal Raleigh\",\"Spencer Steer\",\"Nolan Gorman\",\"Ryan Noda\",\"Cedric Mullins II\",\"James Outman\",\"Nick Castellanos\",\"Pete Alonso\",\"Anthony Santander\",\"Ryan McMahon\",\"Zach McKinstry\",\"Trea Turner\",\"Anthony Volpe\",\"Masataka Yoshida\",\"Justin Turner\",\"Bryan Reynolds\",\"Manny Machado\",\"Whit Merrifield\",\"Jeremy Pena\",\"Josh Naylor\",\"Anthony Rizzo\",\"Jonathan India\",\"Jarred Kelenic\",\"George Springer\",\"Eugenio Suarez\",\"Joey Wiemer\",\"Andrew McCutchen\",\"Lourdes Gurriel Jr.\",\"Max Muncy\",\"Hunter Renfroe\",\"Mauricio Dubon\",\"Steven Kwan\",\"Tommy Edman\",\"Brent Rooker\",\"J.T. Realmuto\",\"Teoscar Hernandez\",\"Ezequiel Tovar\",\"Willson Contreras\",\"Carlos Correa\",\"Ke'Bryan Hayes\",\"Willy Adames\",\"Gleyber Torres\",\"Esteury Ruiz\",\"Marcell Ozuna\",\"Byron Buxton\",\"Andrew Benintendi\",\"Daulton Varsho\",\"J.D. Martinez\",\"Elias Diaz\",\"Ty France\",\"Taylor Ward\",\"Jeff McNeil\",\"Eddie Rosario\",\"Seiya Suzuki\",\"Carlos Santana\",\"Trent Grisham\",\"Vladimir Guerrero Jr.\",\"Michael Conforto\",\"Brian Anderson\",\"Jace Peterson\",\"Javier Baez\",\"Andrew Vaughn\",\"Alec Bohm\",\"Bryan De La Cruz\",\"Jake Cronenworth\",\"Salvador Perez\",\"CJ Abrams\",\"Spencer Torkelson\",\"Adam Frazier\",\"Miguel Vargas\",\"Amed Rosario\",\"Starling Marte\",\"Luis Garcia\",\"DJ LeMahieu\",\"Tyler Stephenson\",\"Kyle Schwarber\",\"Triston Casas\",\"Dominic Smith\",\"Shea Langeliers\",\"Josh Bell\",\"Myles Straw\",\"Joey Meneses\",\"Jose Abreu\",\"MJ Melendez\",\"Tim Anderson\",\"Rowdy Tellez\",\"Jurickson Profar\",\"Keibert Ruiz\",\"Enrique Hernandez\"],\"legendgroup\":\"\",\"marker\":{\"color\":\"#7284cc\"},\"name\":\"\",\"notched\":false,\"offsetgroup\":\"\",\"orientation\":\"v\",\"showlegend\":false,\"x0\":\" \",\"xaxis\":\"x\",\"y\":[0.871,0.7959999999999999,0.935,0.92,0.863,0.82,0.86,0.899,0.821,0.932,0.789,0.823,0.882,0.92,0.902,0.852,0.8759999999999999,0.7809999999999999,0.957,0.866,0.875,0.7829999999999999,0.7979999999999999,0.797,0.92,0.877,0.884,0.911,0.754,0.847,0.772,0.841,0.919,0.922,0.86,0.899,0.895,0.847,0.875,0.865,0.921,0.946,0.895,0.8370000000000001,0.888,0.883,0.8,0.799,0.954,0.903,0.8540000000000001,0.91,0.8029999999999999,0.845,0.933,0.894,0.8640000000000001,0.8740000000000001,0.84,0.914,0.936,0.831,0.807,0.861,0.81,0.765,0.823,0.7659999999999999,0.8220000000000001,0.8440000000000001,0.8490000000000001,0.774,0.907,0.8340000000000001,0.843,0.8959999999999999,0.908,0.853,0.861,0.877,0.899,0.9,0.8859999999999999,0.894,0.8079999999999999,0.889,0.82,0.7809999999999999,0.826,0.934,0.7979999999999999,0.863,0.879,0.953,0.942,0.748,0.8540000000000001,0.804,0.848,0.8690000000000001,0.851,0.936,0.843,0.879,0.8759999999999999,0.8370000000000001,0.825,0.893,0.871,0.809,0.8540000000000001,0.92,0.915,0.925,0.777,0.877,0.846,0.782,0.867,0.8420000000000001,0.797,0.8740000000000001,0.812,0.893,0.911,0.8109999999999999,0.926,0.8220000000000001,0.865,0.865,0.915,0.88,0.875,0.8740000000000001,0.909,0.913,0.84,0.8029999999999999,0.8170000000000001,0.8740000000000001,0.8109999999999999,0.84,0.911,0.889,0.868,0.7509999999999999,0.865,0.889,0.898,0.948,0.862],\"y0\":\" \",\"yaxis\":\"y\",\"type\":\"box\"}],                        {\"template\":{\"data\":{\"candlestick\":[{\"decreasing\":{\"line\":{\"color\":\"#000033\"}},\"increasing\":{\"line\":{\"color\":\"#000032\"}},\"type\":\"candlestick\"}],\"contourcarpet\":[{\"colorscale\":[[0.0,\"#000011\"],[0.1111111111111111,\"#000012\"],[0.2222222222222222,\"#000013\"],[0.3333333333333333,\"#000014\"],[0.4444444444444444,\"#000015\"],[0.5555555555555556,\"#000016\"],[0.6666666666666666,\"#000017\"],[0.7777777777777778,\"#000018\"],[0.8888888888888888,\"#000019\"],[1.0,\"#000020\"]],\"type\":\"contourcarpet\"}],\"contour\":[{\"colorscale\":[[0.0,\"#000011\"],[0.1111111111111111,\"#000012\"],[0.2222222222222222,\"#000013\"],[0.3333333333333333,\"#000014\"],[0.4444444444444444,\"#000015\"],[0.5555555555555556,\"#000016\"],[0.6666666666666666,\"#000017\"],[0.7777777777777778,\"#000018\"],[0.8888888888888888,\"#000019\"],[1.0,\"#000020\"]],\"type\":\"contour\"}],\"heatmap\":[{\"colorscale\":[[0.0,\"#000011\"],[0.1111111111111111,\"#000012\"],[0.2222222222222222,\"#000013\"],[0.3333333333333333,\"#000014\"],[0.4444444444444444,\"#000015\"],[0.5555555555555556,\"#000016\"],[0.6666666666666666,\"#000017\"],[0.7777777777777778,\"#000018\"],[0.8888888888888888,\"#000019\"],[1.0,\"#000020\"]],\"type\":\"heatmap\"}],\"histogram2d\":[{\"colorscale\":[[0.0,\"#000011\"],[0.1111111111111111,\"#000012\"],[0.2222222222222222,\"#000013\"],[0.3333333333333333,\"#000014\"],[0.4444444444444444,\"#000015\"],[0.5555555555555556,\"#000016\"],[0.6666666666666666,\"#000017\"],[0.7777777777777778,\"#000018\"],[0.8888888888888888,\"#000019\"],[1.0,\"#000020\"]],\"type\":\"histogram2d\"}],\"icicle\":[{\"textfont\":{\"color\":\"white\"},\"type\":\"icicle\"}],\"sankey\":[{\"textfont\":{\"color\":\"#000036\"},\"type\":\"sankey\"}],\"scatter\":[{\"marker\":{\"line\":{\"width\":0}},\"type\":\"scatter\"}],\"table\":[{\"cells\":{\"fill\":{\"color\":\"#000038\"},\"font\":{\"color\":\"#000037\"},\"line\":{\"color\":\"#000039\"}},\"header\":{\"fill\":{\"color\":\"#000040\"},\"font\":{\"color\":\"#000036\"},\"line\":{\"color\":\"#000039\"}},\"type\":\"table\"}],\"waterfall\":[{\"connector\":{\"line\":{\"color\":\"#000036\",\"width\":2}},\"decreasing\":{\"marker\":{\"color\":\"#000033\"}},\"increasing\":{\"marker\":{\"color\":\"#000032\"}},\"totals\":{\"marker\":{\"color\":\"#000034\"}},\"type\":\"waterfall\"}]},\"layout\":{\"coloraxis\":{\"colorscale\":[[0.0,\"#000011\"],[0.1111111111111111,\"#000012\"],[0.2222222222222222,\"#000013\"],[0.3333333333333333,\"#000014\"],[0.4444444444444444,\"#000015\"],[0.5555555555555556,\"#000016\"],[0.6666666666666666,\"#000017\"],[0.7777777777777778,\"#000018\"],[0.8888888888888888,\"#000019\"],[1.0,\"#000020\"]]},\"colorscale\":{\"diverging\":[[0.0,\"#000021\"],[0.1,\"#000022\"],[0.2,\"#000023\"],[0.3,\"#000024\"],[0.4,\"#000025\"],[0.5,\"#000026\"],[0.6,\"#000027\"],[0.7,\"#000028\"],[0.8,\"#000029\"],[0.9,\"#000030\"],[1.0,\"#000031\"]],\"sequential\":[[0.0,\"#000011\"],[0.1111111111111111,\"#000012\"],[0.2222222222222222,\"#000013\"],[0.3333333333333333,\"#000014\"],[0.4444444444444444,\"#000015\"],[0.5555555555555556,\"#000016\"],[0.6666666666666666,\"#000017\"],[0.7777777777777778,\"#000018\"],[0.8888888888888888,\"#000019\"],[1.0,\"#000020\"]],\"sequentialminus\":[[0.0,\"#000011\"],[0.1111111111111111,\"#000012\"],[0.2222222222222222,\"#000013\"],[0.3333333333333333,\"#000014\"],[0.4444444444444444,\"#000015\"],[0.5555555555555556,\"#000016\"],[0.6666666666666666,\"#000017\"],[0.7777777777777778,\"#000018\"],[0.8888888888888888,\"#000019\"],[1.0,\"#000020\"]]},\"colorway\":[\"#000001\",\"#000002\",\"#000003\",\"#000004\",\"#000005\",\"#000006\",\"#000007\",\"#000008\",\"#000009\",\"#000010\"]}},\"xaxis\":{\"anchor\":\"y\",\"domain\":[0.0,1.0],\"title\":{\"text\":\"\"}},\"yaxis\":{\"anchor\":\"x\",\"domain\":[0.0,1.0],\"title\":{\"text\":\"\"}},\"legend\":{\"tracegroupgap\":0},\"margin\":{\"t\":60},\"boxmode\":\"group\",\"height\":500,\"width\":500,\"title\":{\"font\":{\"size\":22,\"color\":\"#164f5e\"},\"text\":\"In-Zone Contact%\",\"automargin\":true,\"yref\":\"paper\"}},                        {\"responsive\": true}                    ).then(function(){\n",
       "                            \n",
       "var gd = document.getElementById('7bb394eb-4286-44b7-ba79-cf778e362ad0');\n",
       "var x = new MutationObserver(function (mutations, observer) {{\n",
       "        var display = window.getComputedStyle(gd).display;\n",
       "        if (!display || display === 'none') {{\n",
       "            console.log([gd, 'removed!']);\n",
       "            Plotly.purge(gd);\n",
       "            observer.disconnect();\n",
       "        }}\n",
       "}});\n",
       "\n",
       "// Listen for the removal of the full notebook cells\n",
       "var notebookContainer = gd.closest('#notebook-container');\n",
       "if (notebookContainer) {{\n",
       "    x.observe(notebookContainer, {childList: true});\n",
       "}}\n",
       "\n",
       "// Listen for the clearing of the current output cell\n",
       "var outputEl = gd.closest('.output');\n",
       "if (outputEl) {{\n",
       "    x.observe(outputEl, {childList: true});\n",
       "}}\n",
       "\n",
       "                        })                };                });            </script>        </div>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "fig_32 = px.box(\n",
    "    df.query(\"Season==2023\"),\n",
    "    y = \"Z-Contact%\",\n",
    "    points=\"all\",\n",
    "    hover_name = \"Name\",\n",
    "    height = 500,\n",
    "    width = 500,\n",
    ")\n",
    "\n",
    "fig_32.update_traces(marker=dict(color=\"#7284cc\"))\n",
    "\n",
    "fig_32.update_layout(\n",
    "    title=dict(text=\"In-Zone Contact%\", font=dict(size=22), automargin=True, yref='paper'),\n",
    "    title_font_color=\"#164f5e\",\n",
    "    yaxis=dict(title=\"\"),\n",
    "    xaxis=dict(title=\"\")\n",
    ")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 95,
   "id": "f00649e3",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "application/vnd.plotly.v1+json": {
       "config": {
        "plotlyServerURL": "https://plot.ly"
       },
       "data": [
        {
         "alignmentgroup": "True",
         "boxpoints": "all",
         "hovertemplate": "<b>%{hovertext}</b><br><br>O-Contact%=%{y}<extra></extra>",
         "hovertext": [
          "Ronald Acuna Jr.",
          "Shohei Ohtani",
          "Mookie Betts",
          "Wander Franco",
          "Corbin Carroll",
          "Luis Robert",
          "Freddie Freeman",
          "Juan Soto",
          "Fernando Tatis Jr.",
          "Jose Ramirez",
          "Adolis Garcia",
          "Mike Trout",
          "Jonah Heim",
          "Marcus Semien",
          "Bo Bichette",
          "Christian Yelich",
          "Francisco Lindor",
          "Dansby Swanson",
          "Luis Arraez",
          "Will Smith",
          "Ha-seong Kim",
          "Randy Arozarena",
          "Paul Goldschmidt",
          "Matt Chapman",
          "Isaac Paredes",
          "Brandon Nimmo",
          "Jeimer Candelario",
          "Thairo Estrada",
          "Matt Olson",
          "Christian Walker",
          "Jack Suwinski",
          "Julio Rodriguez",
          "Yandy Diaz",
          "Kyle Tucker",
          "Josh Jung",
          "Ketel Marte",
          "Ozzie Albies",
          "William Contreras",
          "Xander Bogaerts",
          "Leody Taveras",
          "Adley Rutschman",
          "Nico Hoerner",
          "Lane Thomas",
          "Bobby Witt Jr.",
          "LaMonte Wade Jr.",
          "Austin Hays",
          "J.D. Davis",
          "Gunnar Henderson",
          "Alex Verdugo",
          "Nathaniel Lowe",
          "Jorge Soler",
          "Nolan Arenado",
          "Rafael Devers",
          "Austin Riley",
          "Brendan Donovan",
          "Bryson Stott",
          "Brandon Drury",
          "Brandon Marsh",
          "Ian Happ",
          "J.P. Crawford",
          "Alex Bregman",
          "Andres Gimenez",
          "Cal Raleigh",
          "Spencer Steer",
          "Nolan Gorman",
          "Ryan Noda",
          "Cedric Mullins II",
          "James Outman",
          "Nick Castellanos",
          "Pete Alonso",
          "Anthony Santander",
          "Ryan McMahon",
          "Zach McKinstry",
          "Trea Turner",
          "Anthony Volpe",
          "Masataka Yoshida",
          "Justin Turner",
          "Bryan Reynolds",
          "Manny Machado",
          "Whit Merrifield",
          "Jeremy Pena",
          "Josh Naylor",
          "Anthony Rizzo",
          "Jonathan India",
          "Jarred Kelenic",
          "George Springer",
          "Eugenio Suarez",
          "Joey Wiemer",
          "Andrew McCutchen",
          "Lourdes Gurriel Jr.",
          "Max Muncy",
          "Hunter Renfroe",
          "Mauricio Dubon",
          "Steven Kwan",
          "Tommy Edman",
          "Brent Rooker",
          "J.T. Realmuto",
          "Teoscar Hernandez",
          "Ezequiel Tovar",
          "Willson Contreras",
          "Carlos Correa",
          "Ke'Bryan Hayes",
          "Willy Adames",
          "Gleyber Torres",
          "Esteury Ruiz",
          "Marcell Ozuna",
          "Byron Buxton",
          "Andrew Benintendi",
          "Daulton Varsho",
          "J.D. Martinez",
          "Elias Diaz",
          "Ty France",
          "Taylor Ward",
          "Jeff McNeil",
          "Eddie Rosario",
          "Seiya Suzuki",
          "Carlos Santana",
          "Trent Grisham",
          "Vladimir Guerrero Jr.",
          "Michael Conforto",
          "Brian Anderson",
          "Jace Peterson",
          "Javier Baez",
          "Andrew Vaughn",
          "Alec Bohm",
          "Bryan De La Cruz",
          "Jake Cronenworth",
          "Salvador Perez",
          "CJ Abrams",
          "Spencer Torkelson",
          "Adam Frazier",
          "Miguel Vargas",
          "Amed Rosario",
          "Starling Marte",
          "Luis Garcia",
          "DJ LeMahieu",
          "Tyler Stephenson",
          "Kyle Schwarber",
          "Triston Casas",
          "Dominic Smith",
          "Shea Langeliers",
          "Josh Bell",
          "Myles Straw",
          "Joey Meneses",
          "Jose Abreu",
          "MJ Melendez",
          "Tim Anderson",
          "Rowdy Tellez",
          "Jurickson Profar",
          "Keibert Ruiz",
          "Enrique Hernandez"
         ],
         "legendgroup": "",
         "marker": {
          "color": "#7284cc"
         },
         "name": "",
         "notched": false,
         "offsetgroup": "",
         "orientation": "v",
         "showlegend": false,
         "type": "box",
         "x0": " ",
         "xaxis": "x",
         "y": [
          0.727,
          0.602,
          0.604,
          0.8009999999999999,
          0.73,
          0.522,
          0.685,
          0.619,
          0.608,
          0.7559999999999999,
          0.617,
          0.596,
          0.68,
          0.643,
          0.711,
          0.612,
          0.627,
          0.634,
          0.937,
          0.792,
          0.7290000000000001,
          0.606,
          0.677,
          0.616,
          0.7340000000000001,
          0.617,
          0.665,
          0.685,
          0.654,
          0.63,
          0.563,
          0.585,
          0.6829999999999999,
          0.7140000000000001,
          0.608,
          0.647,
          0.7140000000000001,
          0.619,
          0.685,
          0.634,
          0.789,
          0.83,
          0.67,
          0.644,
          0.642,
          0.574,
          0.469,
          0.564,
          0.7170000000000001,
          0.6859999999999999,
          0.591,
          0.65,
          0.6779999999999999,
          0.5920000000000001,
          0.7490000000000001,
          0.83,
          0.562,
          0.563,
          0.627,
          0.68,
          0.74,
          0.711,
          0.627,
          0.68,
          0.49,
          0.365,
          0.706,
          0.412,
          0.493,
          0.6709999999999999,
          0.7,
          0.586,
          0.691,
          0.574,
          0.534,
          0.7609999999999999,
          0.718,
          0.565,
          0.624,
          0.728,
          0.522,
          0.713,
          0.639,
          0.632,
          0.544,
          0.633,
          0.511,
          0.527,
          0.542,
          0.7090000000000001,
          0.5429999999999999,
          0.636,
          0.799,
          0.794,
          0.696,
          0.456,
          0.642,
          0.509,
          0.573,
          0.565,
          0.645,
          0.667,
          0.563,
          0.69,
          0.616,
          0.573,
          0.55,
          0.726,
          0.643,
          0.504,
          0.62,
          0.637,
          0.636,
          0.745,
          0.6679999999999999,
          0.647,
          0.659,
          0.605,
          0.652,
          0.621,
          0.541,
          0.626,
          0.603,
          0.631,
          0.7559999999999999,
          0.62,
          0.7090000000000001,
          0.591,
          0.675,
          0.627,
          0.72,
          0.652,
          0.675,
          0.604,
          0.782,
          0.6709999999999999,
          0.561,
          0.519,
          0.636,
          0.738,
          0.517,
          0.6759999999999999,
          0.835,
          0.623,
          0.639,
          0.526,
          0.6409999999999999,
          0.684,
          0.6709999999999999,
          0.764,
          0.574
         ],
         "y0": " ",
         "yaxis": "y"
        }
       ],
       "layout": {
        "boxmode": "group",
        "height": 500,
        "legend": {
         "tracegroupgap": 0
        },
        "margin": {
         "t": 60
        },
        "template": {
         "data": {
          "candlestick": [
           {
            "decreasing": {
             "line": {
              "color": "#000033"
             }
            },
            "increasing": {
             "line": {
              "color": "#000032"
             }
            },
            "type": "candlestick"
           }
          ],
          "contour": [
           {
            "colorscale": [
             [
              0,
              "#000011"
             ],
             [
              0.1111111111111111,
              "#000012"
             ],
             [
              0.2222222222222222,
              "#000013"
             ],
             [
              0.3333333333333333,
              "#000014"
             ],
             [
              0.4444444444444444,
              "#000015"
             ],
             [
              0.5555555555555556,
              "#000016"
             ],
             [
              0.6666666666666666,
              "#000017"
             ],
             [
              0.7777777777777778,
              "#000018"
             ],
             [
              0.8888888888888888,
              "#000019"
             ],
             [
              1,
              "#000020"
             ]
            ],
            "type": "contour"
           }
          ],
          "contourcarpet": [
           {
            "colorscale": [
             [
              0,
              "#000011"
             ],
             [
              0.1111111111111111,
              "#000012"
             ],
             [
              0.2222222222222222,
              "#000013"
             ],
             [
              0.3333333333333333,
              "#000014"
             ],
             [
              0.4444444444444444,
              "#000015"
             ],
             [
              0.5555555555555556,
              "#000016"
             ],
             [
              0.6666666666666666,
              "#000017"
             ],
             [
              0.7777777777777778,
              "#000018"
             ],
             [
              0.8888888888888888,
              "#000019"
             ],
             [
              1,
              "#000020"
             ]
            ],
            "type": "contourcarpet"
           }
          ],
          "heatmap": [
           {
            "colorscale": [
             [
              0,
              "#000011"
             ],
             [
              0.1111111111111111,
              "#000012"
             ],
             [
              0.2222222222222222,
              "#000013"
             ],
             [
              0.3333333333333333,
              "#000014"
             ],
             [
              0.4444444444444444,
              "#000015"
             ],
             [
              0.5555555555555556,
              "#000016"
             ],
             [
              0.6666666666666666,
              "#000017"
             ],
             [
              0.7777777777777778,
              "#000018"
             ],
             [
              0.8888888888888888,
              "#000019"
             ],
             [
              1,
              "#000020"
             ]
            ],
            "type": "heatmap"
           }
          ],
          "histogram2d": [
           {
            "colorscale": [
             [
              0,
              "#000011"
             ],
             [
              0.1111111111111111,
              "#000012"
             ],
             [
              0.2222222222222222,
              "#000013"
             ],
             [
              0.3333333333333333,
              "#000014"
             ],
             [
              0.4444444444444444,
              "#000015"
             ],
             [
              0.5555555555555556,
              "#000016"
             ],
             [
              0.6666666666666666,
              "#000017"
             ],
             [
              0.7777777777777778,
              "#000018"
             ],
             [
              0.8888888888888888,
              "#000019"
             ],
             [
              1,
              "#000020"
             ]
            ],
            "type": "histogram2d"
           }
          ],
          "icicle": [
           {
            "textfont": {
             "color": "white"
            },
            "type": "icicle"
           }
          ],
          "sankey": [
           {
            "textfont": {
             "color": "#000036"
            },
            "type": "sankey"
           }
          ],
          "scatter": [
           {
            "marker": {
             "line": {
              "width": 0
             }
            },
            "type": "scatter"
           }
          ],
          "table": [
           {
            "cells": {
             "fill": {
              "color": "#000038"
             },
             "font": {
              "color": "#000037"
             },
             "line": {
              "color": "#000039"
             }
            },
            "header": {
             "fill": {
              "color": "#000040"
             },
             "font": {
              "color": "#000036"
             },
             "line": {
              "color": "#000039"
             }
            },
            "type": "table"
           }
          ],
          "waterfall": [
           {
            "connector": {
             "line": {
              "color": "#000036",
              "width": 2
             }
            },
            "decreasing": {
             "marker": {
              "color": "#000033"
             }
            },
            "increasing": {
             "marker": {
              "color": "#000032"
             }
            },
            "totals": {
             "marker": {
              "color": "#000034"
             }
            },
            "type": "waterfall"
           }
          ]
         },
         "layout": {
          "coloraxis": {
           "colorscale": [
            [
             0,
             "#000011"
            ],
            [
             0.1111111111111111,
             "#000012"
            ],
            [
             0.2222222222222222,
             "#000013"
            ],
            [
             0.3333333333333333,
             "#000014"
            ],
            [
             0.4444444444444444,
             "#000015"
            ],
            [
             0.5555555555555556,
             "#000016"
            ],
            [
             0.6666666666666666,
             "#000017"
            ],
            [
             0.7777777777777778,
             "#000018"
            ],
            [
             0.8888888888888888,
             "#000019"
            ],
            [
             1,
             "#000020"
            ]
           ]
          },
          "colorscale": {
           "diverging": [
            [
             0,
             "#000021"
            ],
            [
             0.1,
             "#000022"
            ],
            [
             0.2,
             "#000023"
            ],
            [
             0.3,
             "#000024"
            ],
            [
             0.4,
             "#000025"
            ],
            [
             0.5,
             "#000026"
            ],
            [
             0.6,
             "#000027"
            ],
            [
             0.7,
             "#000028"
            ],
            [
             0.8,
             "#000029"
            ],
            [
             0.9,
             "#000030"
            ],
            [
             1,
             "#000031"
            ]
           ],
           "sequential": [
            [
             0,
             "#000011"
            ],
            [
             0.1111111111111111,
             "#000012"
            ],
            [
             0.2222222222222222,
             "#000013"
            ],
            [
             0.3333333333333333,
             "#000014"
            ],
            [
             0.4444444444444444,
             "#000015"
            ],
            [
             0.5555555555555556,
             "#000016"
            ],
            [
             0.6666666666666666,
             "#000017"
            ],
            [
             0.7777777777777778,
             "#000018"
            ],
            [
             0.8888888888888888,
             "#000019"
            ],
            [
             1,
             "#000020"
            ]
           ],
           "sequentialminus": [
            [
             0,
             "#000011"
            ],
            [
             0.1111111111111111,
             "#000012"
            ],
            [
             0.2222222222222222,
             "#000013"
            ],
            [
             0.3333333333333333,
             "#000014"
            ],
            [
             0.4444444444444444,
             "#000015"
            ],
            [
             0.5555555555555556,
             "#000016"
            ],
            [
             0.6666666666666666,
             "#000017"
            ],
            [
             0.7777777777777778,
             "#000018"
            ],
            [
             0.8888888888888888,
             "#000019"
            ],
            [
             1,
             "#000020"
            ]
           ]
          },
          "colorway": [
           "#000001",
           "#000002",
           "#000003",
           "#000004",
           "#000005",
           "#000006",
           "#000007",
           "#000008",
           "#000009",
           "#000010"
          ]
         }
        },
        "title": {
         "automargin": true,
         "font": {
          "color": "#164f5e",
          "size": 22
         },
         "text": "Out-Zone Contact%",
         "yref": "paper"
        },
        "width": 500,
        "xaxis": {
         "anchor": "y",
         "domain": [
          0,
          1
         ],
         "title": {
          "text": ""
         }
        },
        "yaxis": {
         "anchor": "x",
         "domain": [
          0,
          1
         ],
         "title": {
          "text": ""
         }
        }
       }
      },
      "text/html": [
       "<div>                            <div id=\"dbcb0310-113f-496f-8287-2196d39fb49e\" class=\"plotly-graph-div\" style=\"height:500px; width:500px;\"></div>            <script type=\"text/javascript\">                require([\"plotly\"], function(Plotly) {                    window.PLOTLYENV=window.PLOTLYENV || {};                                    if (document.getElementById(\"dbcb0310-113f-496f-8287-2196d39fb49e\")) {                    Plotly.newPlot(                        \"dbcb0310-113f-496f-8287-2196d39fb49e\",                        [{\"alignmentgroup\":\"True\",\"boxpoints\":\"all\",\"hovertemplate\":\"\\u003cb\\u003e%{hovertext}\\u003c\\u002fb\\u003e\\u003cbr\\u003e\\u003cbr\\u003eO-Contact%=%{y}\\u003cextra\\u003e\\u003c\\u002fextra\\u003e\",\"hovertext\":[\"Ronald Acuna Jr.\",\"Shohei Ohtani\",\"Mookie Betts\",\"Wander Franco\",\"Corbin Carroll\",\"Luis Robert\",\"Freddie Freeman\",\"Juan Soto\",\"Fernando Tatis Jr.\",\"Jose Ramirez\",\"Adolis Garcia\",\"Mike Trout\",\"Jonah Heim\",\"Marcus Semien\",\"Bo Bichette\",\"Christian Yelich\",\"Francisco Lindor\",\"Dansby Swanson\",\"Luis Arraez\",\"Will Smith\",\"Ha-seong Kim\",\"Randy Arozarena\",\"Paul Goldschmidt\",\"Matt Chapman\",\"Isaac Paredes\",\"Brandon Nimmo\",\"Jeimer Candelario\",\"Thairo Estrada\",\"Matt Olson\",\"Christian Walker\",\"Jack Suwinski\",\"Julio Rodriguez\",\"Yandy Diaz\",\"Kyle Tucker\",\"Josh Jung\",\"Ketel Marte\",\"Ozzie Albies\",\"William Contreras\",\"Xander Bogaerts\",\"Leody Taveras\",\"Adley Rutschman\",\"Nico Hoerner\",\"Lane Thomas\",\"Bobby Witt Jr.\",\"LaMonte Wade Jr.\",\"Austin Hays\",\"J.D. Davis\",\"Gunnar Henderson\",\"Alex Verdugo\",\"Nathaniel Lowe\",\"Jorge Soler\",\"Nolan Arenado\",\"Rafael Devers\",\"Austin Riley\",\"Brendan Donovan\",\"Bryson Stott\",\"Brandon Drury\",\"Brandon Marsh\",\"Ian Happ\",\"J.P. Crawford\",\"Alex Bregman\",\"Andres Gimenez\",\"Cal Raleigh\",\"Spencer Steer\",\"Nolan Gorman\",\"Ryan Noda\",\"Cedric Mullins II\",\"James Outman\",\"Nick Castellanos\",\"Pete Alonso\",\"Anthony Santander\",\"Ryan McMahon\",\"Zach McKinstry\",\"Trea Turner\",\"Anthony Volpe\",\"Masataka Yoshida\",\"Justin Turner\",\"Bryan Reynolds\",\"Manny Machado\",\"Whit Merrifield\",\"Jeremy Pena\",\"Josh Naylor\",\"Anthony Rizzo\",\"Jonathan India\",\"Jarred Kelenic\",\"George Springer\",\"Eugenio Suarez\",\"Joey Wiemer\",\"Andrew McCutchen\",\"Lourdes Gurriel Jr.\",\"Max Muncy\",\"Hunter Renfroe\",\"Mauricio Dubon\",\"Steven Kwan\",\"Tommy Edman\",\"Brent Rooker\",\"J.T. Realmuto\",\"Teoscar Hernandez\",\"Ezequiel Tovar\",\"Willson Contreras\",\"Carlos Correa\",\"Ke'Bryan Hayes\",\"Willy Adames\",\"Gleyber Torres\",\"Esteury Ruiz\",\"Marcell Ozuna\",\"Byron Buxton\",\"Andrew Benintendi\",\"Daulton Varsho\",\"J.D. Martinez\",\"Elias Diaz\",\"Ty France\",\"Taylor Ward\",\"Jeff McNeil\",\"Eddie Rosario\",\"Seiya Suzuki\",\"Carlos Santana\",\"Trent Grisham\",\"Vladimir Guerrero Jr.\",\"Michael Conforto\",\"Brian Anderson\",\"Jace Peterson\",\"Javier Baez\",\"Andrew Vaughn\",\"Alec Bohm\",\"Bryan De La Cruz\",\"Jake Cronenworth\",\"Salvador Perez\",\"CJ Abrams\",\"Spencer Torkelson\",\"Adam Frazier\",\"Miguel Vargas\",\"Amed Rosario\",\"Starling Marte\",\"Luis Garcia\",\"DJ LeMahieu\",\"Tyler Stephenson\",\"Kyle Schwarber\",\"Triston Casas\",\"Dominic Smith\",\"Shea Langeliers\",\"Josh Bell\",\"Myles Straw\",\"Joey Meneses\",\"Jose Abreu\",\"MJ Melendez\",\"Tim Anderson\",\"Rowdy Tellez\",\"Jurickson Profar\",\"Keibert Ruiz\",\"Enrique Hernandez\"],\"legendgroup\":\"\",\"marker\":{\"color\":\"#7284cc\"},\"name\":\"\",\"notched\":false,\"offsetgroup\":\"\",\"orientation\":\"v\",\"showlegend\":false,\"x0\":\" \",\"xaxis\":\"x\",\"y\":[0.727,0.602,0.604,0.8009999999999999,0.73,0.522,0.685,0.619,0.608,0.7559999999999999,0.617,0.596,0.68,0.643,0.711,0.612,0.627,0.634,0.937,0.792,0.7290000000000001,0.606,0.677,0.616,0.7340000000000001,0.617,0.665,0.685,0.654,0.63,0.563,0.585,0.6829999999999999,0.7140000000000001,0.608,0.647,0.7140000000000001,0.619,0.685,0.634,0.789,0.83,0.67,0.644,0.642,0.574,0.469,0.564,0.7170000000000001,0.6859999999999999,0.591,0.65,0.6779999999999999,0.5920000000000001,0.7490000000000001,0.83,0.562,0.563,0.627,0.68,0.74,0.711,0.627,0.68,0.49,0.365,0.706,0.412,0.493,0.6709999999999999,0.7,0.586,0.691,0.574,0.534,0.7609999999999999,0.718,0.565,0.624,0.728,0.522,0.713,0.639,0.632,0.544,0.633,0.511,0.527,0.542,0.7090000000000001,0.5429999999999999,0.636,0.799,0.794,0.696,0.456,0.642,0.509,0.573,0.565,0.645,0.667,0.563,0.69,0.616,0.573,0.55,0.726,0.643,0.504,0.62,0.637,0.636,0.745,0.6679999999999999,0.647,0.659,0.605,0.652,0.621,0.541,0.626,0.603,0.631,0.7559999999999999,0.62,0.7090000000000001,0.591,0.675,0.627,0.72,0.652,0.675,0.604,0.782,0.6709999999999999,0.561,0.519,0.636,0.738,0.517,0.6759999999999999,0.835,0.623,0.639,0.526,0.6409999999999999,0.684,0.6709999999999999,0.764,0.574],\"y0\":\" \",\"yaxis\":\"y\",\"type\":\"box\"}],                        {\"template\":{\"data\":{\"candlestick\":[{\"decreasing\":{\"line\":{\"color\":\"#000033\"}},\"increasing\":{\"line\":{\"color\":\"#000032\"}},\"type\":\"candlestick\"}],\"contourcarpet\":[{\"colorscale\":[[0.0,\"#000011\"],[0.1111111111111111,\"#000012\"],[0.2222222222222222,\"#000013\"],[0.3333333333333333,\"#000014\"],[0.4444444444444444,\"#000015\"],[0.5555555555555556,\"#000016\"],[0.6666666666666666,\"#000017\"],[0.7777777777777778,\"#000018\"],[0.8888888888888888,\"#000019\"],[1.0,\"#000020\"]],\"type\":\"contourcarpet\"}],\"contour\":[{\"colorscale\":[[0.0,\"#000011\"],[0.1111111111111111,\"#000012\"],[0.2222222222222222,\"#000013\"],[0.3333333333333333,\"#000014\"],[0.4444444444444444,\"#000015\"],[0.5555555555555556,\"#000016\"],[0.6666666666666666,\"#000017\"],[0.7777777777777778,\"#000018\"],[0.8888888888888888,\"#000019\"],[1.0,\"#000020\"]],\"type\":\"contour\"}],\"heatmap\":[{\"colorscale\":[[0.0,\"#000011\"],[0.1111111111111111,\"#000012\"],[0.2222222222222222,\"#000013\"],[0.3333333333333333,\"#000014\"],[0.4444444444444444,\"#000015\"],[0.5555555555555556,\"#000016\"],[0.6666666666666666,\"#000017\"],[0.7777777777777778,\"#000018\"],[0.8888888888888888,\"#000019\"],[1.0,\"#000020\"]],\"type\":\"heatmap\"}],\"histogram2d\":[{\"colorscale\":[[0.0,\"#000011\"],[0.1111111111111111,\"#000012\"],[0.2222222222222222,\"#000013\"],[0.3333333333333333,\"#000014\"],[0.4444444444444444,\"#000015\"],[0.5555555555555556,\"#000016\"],[0.6666666666666666,\"#000017\"],[0.7777777777777778,\"#000018\"],[0.8888888888888888,\"#000019\"],[1.0,\"#000020\"]],\"type\":\"histogram2d\"}],\"icicle\":[{\"textfont\":{\"color\":\"white\"},\"type\":\"icicle\"}],\"sankey\":[{\"textfont\":{\"color\":\"#000036\"},\"type\":\"sankey\"}],\"scatter\":[{\"marker\":{\"line\":{\"width\":0}},\"type\":\"scatter\"}],\"table\":[{\"cells\":{\"fill\":{\"color\":\"#000038\"},\"font\":{\"color\":\"#000037\"},\"line\":{\"color\":\"#000039\"}},\"header\":{\"fill\":{\"color\":\"#000040\"},\"font\":{\"color\":\"#000036\"},\"line\":{\"color\":\"#000039\"}},\"type\":\"table\"}],\"waterfall\":[{\"connector\":{\"line\":{\"color\":\"#000036\",\"width\":2}},\"decreasing\":{\"marker\":{\"color\":\"#000033\"}},\"increasing\":{\"marker\":{\"color\":\"#000032\"}},\"totals\":{\"marker\":{\"color\":\"#000034\"}},\"type\":\"waterfall\"}]},\"layout\":{\"coloraxis\":{\"colorscale\":[[0.0,\"#000011\"],[0.1111111111111111,\"#000012\"],[0.2222222222222222,\"#000013\"],[0.3333333333333333,\"#000014\"],[0.4444444444444444,\"#000015\"],[0.5555555555555556,\"#000016\"],[0.6666666666666666,\"#000017\"],[0.7777777777777778,\"#000018\"],[0.8888888888888888,\"#000019\"],[1.0,\"#000020\"]]},\"colorscale\":{\"diverging\":[[0.0,\"#000021\"],[0.1,\"#000022\"],[0.2,\"#000023\"],[0.3,\"#000024\"],[0.4,\"#000025\"],[0.5,\"#000026\"],[0.6,\"#000027\"],[0.7,\"#000028\"],[0.8,\"#000029\"],[0.9,\"#000030\"],[1.0,\"#000031\"]],\"sequential\":[[0.0,\"#000011\"],[0.1111111111111111,\"#000012\"],[0.2222222222222222,\"#000013\"],[0.3333333333333333,\"#000014\"],[0.4444444444444444,\"#000015\"],[0.5555555555555556,\"#000016\"],[0.6666666666666666,\"#000017\"],[0.7777777777777778,\"#000018\"],[0.8888888888888888,\"#000019\"],[1.0,\"#000020\"]],\"sequentialminus\":[[0.0,\"#000011\"],[0.1111111111111111,\"#000012\"],[0.2222222222222222,\"#000013\"],[0.3333333333333333,\"#000014\"],[0.4444444444444444,\"#000015\"],[0.5555555555555556,\"#000016\"],[0.6666666666666666,\"#000017\"],[0.7777777777777778,\"#000018\"],[0.8888888888888888,\"#000019\"],[1.0,\"#000020\"]]},\"colorway\":[\"#000001\",\"#000002\",\"#000003\",\"#000004\",\"#000005\",\"#000006\",\"#000007\",\"#000008\",\"#000009\",\"#000010\"]}},\"xaxis\":{\"anchor\":\"y\",\"domain\":[0.0,1.0],\"title\":{\"text\":\"\"}},\"yaxis\":{\"anchor\":\"x\",\"domain\":[0.0,1.0],\"title\":{\"text\":\"\"}},\"legend\":{\"tracegroupgap\":0},\"margin\":{\"t\":60},\"boxmode\":\"group\",\"height\":500,\"width\":500,\"title\":{\"font\":{\"size\":22,\"color\":\"#164f5e\"},\"text\":\"Out-Zone Contact%\",\"automargin\":true,\"yref\":\"paper\"}},                        {\"responsive\": true}                    ).then(function(){\n",
       "                            \n",
       "var gd = document.getElementById('dbcb0310-113f-496f-8287-2196d39fb49e');\n",
       "var x = new MutationObserver(function (mutations, observer) {{\n",
       "        var display = window.getComputedStyle(gd).display;\n",
       "        if (!display || display === 'none') {{\n",
       "            console.log([gd, 'removed!']);\n",
       "            Plotly.purge(gd);\n",
       "            observer.disconnect();\n",
       "        }}\n",
       "}});\n",
       "\n",
       "// Listen for the removal of the full notebook cells\n",
       "var notebookContainer = gd.closest('#notebook-container');\n",
       "if (notebookContainer) {{\n",
       "    x.observe(notebookContainer, {childList: true});\n",
       "}}\n",
       "\n",
       "// Listen for the clearing of the current output cell\n",
       "var outputEl = gd.closest('.output');\n",
       "if (outputEl) {{\n",
       "    x.observe(outputEl, {childList: true});\n",
       "}}\n",
       "\n",
       "                        })                };                });            </script>        </div>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "fig_33 = px.box(\n",
    "    df.query(\"Season==2023\"),\n",
    "    y = \"O-Contact%\",\n",
    "    points=\"all\",\n",
    "    hover_name = \"Name\",\n",
    "    height = 500,\n",
    "    width = 500,\n",
    ")\n",
    "\n",
    "fig_33.update_traces(marker=dict(color=\"#7284cc\"))\n",
    "\n",
    "fig_33.update_layout(\n",
    "    title=dict(text=\"Out-Zone Contact%\", font=dict(size=22), automargin=True, yref='paper'),\n",
    "    title_font_color=\"#164f5e\",\n",
    "    yaxis=dict(title=\"\"),\n",
    "    xaxis=dict(title=\"\")\n",
    ")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "247a4e3a",
   "metadata": {},
   "source": [
    "### Row 1 - Tab 4"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 96,
   "id": "53feb05e",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "application/vnd.plotly.v1+json": {
       "config": {
        "plotlyServerURL": "https://plot.ly"
       },
       "data": [
        {
         "alignmentgroup": "True",
         "boxpoints": "all",
         "hovertemplate": "<b>%{hovertext}</b><br><br>BB%+=%{y}<extra></extra>",
         "hovertext": [
          "Ronald Acuna Jr.",
          "Shohei Ohtani",
          "Mookie Betts",
          "Wander Franco",
          "Corbin Carroll",
          "Luis Robert",
          "Freddie Freeman",
          "Juan Soto",
          "Fernando Tatis Jr.",
          "Jose Ramirez",
          "Adolis Garcia",
          "Mike Trout",
          "Jonah Heim",
          "Marcus Semien",
          "Bo Bichette",
          "Christian Yelich",
          "Francisco Lindor",
          "Dansby Swanson",
          "Luis Arraez",
          "Will Smith",
          "Ha-seong Kim",
          "Randy Arozarena",
          "Paul Goldschmidt",
          "Matt Chapman",
          "Isaac Paredes",
          "Brandon Nimmo",
          "Jeimer Candelario",
          "Thairo Estrada",
          "Matt Olson",
          "Christian Walker",
          "Jack Suwinski",
          "Julio Rodriguez",
          "Yandy Diaz",
          "Kyle Tucker",
          "Josh Jung",
          "Ketel Marte",
          "Ozzie Albies",
          "William Contreras",
          "Xander Bogaerts",
          "Leody Taveras",
          "Adley Rutschman",
          "Nico Hoerner",
          "Lane Thomas",
          "Bobby Witt Jr.",
          "LaMonte Wade Jr.",
          "Austin Hays",
          "J.D. Davis",
          "Gunnar Henderson",
          "Alex Verdugo",
          "Nathaniel Lowe",
          "Jorge Soler",
          "Nolan Arenado",
          "Rafael Devers",
          "Austin Riley",
          "Brendan Donovan",
          "Bryson Stott",
          "Brandon Drury",
          "Brandon Marsh",
          "Ian Happ",
          "J.P. Crawford",
          "Alex Bregman",
          "Andres Gimenez",
          "Cal Raleigh",
          "Spencer Steer",
          "Nolan Gorman",
          "Ryan Noda",
          "Cedric Mullins II",
          "James Outman",
          "Nick Castellanos",
          "Pete Alonso",
          "Anthony Santander",
          "Ryan McMahon",
          "Zach McKinstry",
          "Trea Turner",
          "Anthony Volpe",
          "Masataka Yoshida",
          "Justin Turner",
          "Bryan Reynolds",
          "Manny Machado",
          "Whit Merrifield",
          "Jeremy Pena",
          "Josh Naylor",
          "Anthony Rizzo",
          "Jonathan India",
          "Jarred Kelenic",
          "George Springer",
          "Eugenio Suarez",
          "Joey Wiemer",
          "Andrew McCutchen",
          "Lourdes Gurriel Jr.",
          "Max Muncy",
          "Hunter Renfroe",
          "Mauricio Dubon",
          "Steven Kwan",
          "Tommy Edman",
          "Brent Rooker",
          "J.T. Realmuto",
          "Teoscar Hernandez",
          "Ezequiel Tovar",
          "Willson Contreras",
          "Carlos Correa",
          "Ke'Bryan Hayes",
          "Willy Adames",
          "Gleyber Torres",
          "Esteury Ruiz",
          "Marcell Ozuna",
          "Byron Buxton",
          "Andrew Benintendi",
          "Daulton Varsho",
          "J.D. Martinez",
          "Elias Diaz",
          "Ty France",
          "Taylor Ward",
          "Jeff McNeil",
          "Eddie Rosario",
          "Seiya Suzuki",
          "Carlos Santana",
          "Trent Grisham",
          "Vladimir Guerrero Jr.",
          "Michael Conforto",
          "Brian Anderson",
          "Jace Peterson",
          "Javier Baez",
          "Andrew Vaughn",
          "Alec Bohm",
          "Bryan De La Cruz",
          "Jake Cronenworth",
          "Salvador Perez",
          "CJ Abrams",
          "Spencer Torkelson",
          "Adam Frazier",
          "Miguel Vargas",
          "Amed Rosario",
          "Starling Marte",
          "Luis Garcia",
          "DJ LeMahieu",
          "Tyler Stephenson",
          "Kyle Schwarber",
          "Triston Casas",
          "Dominic Smith",
          "Shea Langeliers",
          "Josh Bell",
          "Myles Straw",
          "Joey Meneses",
          "Jose Abreu",
          "MJ Melendez",
          "Tim Anderson",
          "Rowdy Tellez",
          "Jurickson Profar",
          "Keibert Ruiz",
          "Enrique Hernandez"
         ],
         "legendgroup": "",
         "marker": {
          "color": "#7284cc"
         },
         "name": "",
         "notched": false,
         "offsetgroup": "",
         "orientation": "v",
         "showlegend": false,
         "type": "box",
         "x0": " ",
         "xaxis": "x",
         "y": [
          122,
          144,
          152,
          95,
          101,
          69,
          113,
          238,
          90,
          128,
          110,
          150,
          89,
          106,
          46,
          140,
          106,
          123,
          86,
          174,
          133,
          148,
          132,
          117,
          128,
          125,
          96,
          54,
          157,
          101,
          178,
          84,
          142,
          128,
          72,
          112,
          77,
          116,
          123,
          76,
          173,
          63,
          64,
          66,
          191,
          71,
          108,
          139,
          103,
          144,
          136,
          77,
          102,
          92,
          111,
          58,
          62,
          118,
          189,
          175,
          154,
          65,
          118,
          127,
          128,
          223,
          151,
          100,
          72,
          105,
          102,
          125,
          124,
          74,
          106,
          99,
          108,
          107,
          70,
          87,
          62,
          74,
          115,
          101,
          112,
          93,
          115,
          104,
          175,
          68,
          172,
          72,
          41,
          116,
          88,
          132,
          78,
          70,
          47,
          107,
          112,
          59,
          114,
          119,
          45,
          111,
          134,
          104,
          95,
          67,
          84,
          63,
          105,
          87,
          79,
          130,
          119,
          148,
          97,
          133,
          119,
          125,
          45,
          92,
          67,
          80,
          124,
          44,
          43,
          122,
          98,
          136,
          71,
          57,
          61,
          97,
          114,
          172,
          165,
          86,
          75,
          137,
          105,
          69,
          74,
          122,
          61,
          106,
          118,
          61,
          85
         ],
         "y0": " ",
         "yaxis": "y"
        }
       ],
       "layout": {
        "boxmode": "group",
        "height": 500,
        "legend": {
         "tracegroupgap": 0
        },
        "margin": {
         "t": 60
        },
        "template": {
         "data": {
          "candlestick": [
           {
            "decreasing": {
             "line": {
              "color": "#000033"
             }
            },
            "increasing": {
             "line": {
              "color": "#000032"
             }
            },
            "type": "candlestick"
           }
          ],
          "contour": [
           {
            "colorscale": [
             [
              0,
              "#000011"
             ],
             [
              0.1111111111111111,
              "#000012"
             ],
             [
              0.2222222222222222,
              "#000013"
             ],
             [
              0.3333333333333333,
              "#000014"
             ],
             [
              0.4444444444444444,
              "#000015"
             ],
             [
              0.5555555555555556,
              "#000016"
             ],
             [
              0.6666666666666666,
              "#000017"
             ],
             [
              0.7777777777777778,
              "#000018"
             ],
             [
              0.8888888888888888,
              "#000019"
             ],
             [
              1,
              "#000020"
             ]
            ],
            "type": "contour"
           }
          ],
          "contourcarpet": [
           {
            "colorscale": [
             [
              0,
              "#000011"
             ],
             [
              0.1111111111111111,
              "#000012"
             ],
             [
              0.2222222222222222,
              "#000013"
             ],
             [
              0.3333333333333333,
              "#000014"
             ],
             [
              0.4444444444444444,
              "#000015"
             ],
             [
              0.5555555555555556,
              "#000016"
             ],
             [
              0.6666666666666666,
              "#000017"
             ],
             [
              0.7777777777777778,
              "#000018"
             ],
             [
              0.8888888888888888,
              "#000019"
             ],
             [
              1,
              "#000020"
             ]
            ],
            "type": "contourcarpet"
           }
          ],
          "heatmap": [
           {
            "colorscale": [
             [
              0,
              "#000011"
             ],
             [
              0.1111111111111111,
              "#000012"
             ],
             [
              0.2222222222222222,
              "#000013"
             ],
             [
              0.3333333333333333,
              "#000014"
             ],
             [
              0.4444444444444444,
              "#000015"
             ],
             [
              0.5555555555555556,
              "#000016"
             ],
             [
              0.6666666666666666,
              "#000017"
             ],
             [
              0.7777777777777778,
              "#000018"
             ],
             [
              0.8888888888888888,
              "#000019"
             ],
             [
              1,
              "#000020"
             ]
            ],
            "type": "heatmap"
           }
          ],
          "histogram2d": [
           {
            "colorscale": [
             [
              0,
              "#000011"
             ],
             [
              0.1111111111111111,
              "#000012"
             ],
             [
              0.2222222222222222,
              "#000013"
             ],
             [
              0.3333333333333333,
              "#000014"
             ],
             [
              0.4444444444444444,
              "#000015"
             ],
             [
              0.5555555555555556,
              "#000016"
             ],
             [
              0.6666666666666666,
              "#000017"
             ],
             [
              0.7777777777777778,
              "#000018"
             ],
             [
              0.8888888888888888,
              "#000019"
             ],
             [
              1,
              "#000020"
             ]
            ],
            "type": "histogram2d"
           }
          ],
          "icicle": [
           {
            "textfont": {
             "color": "white"
            },
            "type": "icicle"
           }
          ],
          "sankey": [
           {
            "textfont": {
             "color": "#000036"
            },
            "type": "sankey"
           }
          ],
          "scatter": [
           {
            "marker": {
             "line": {
              "width": 0
             }
            },
            "type": "scatter"
           }
          ],
          "table": [
           {
            "cells": {
             "fill": {
              "color": "#000038"
             },
             "font": {
              "color": "#000037"
             },
             "line": {
              "color": "#000039"
             }
            },
            "header": {
             "fill": {
              "color": "#000040"
             },
             "font": {
              "color": "#000036"
             },
             "line": {
              "color": "#000039"
             }
            },
            "type": "table"
           }
          ],
          "waterfall": [
           {
            "connector": {
             "line": {
              "color": "#000036",
              "width": 2
             }
            },
            "decreasing": {
             "marker": {
              "color": "#000033"
             }
            },
            "increasing": {
             "marker": {
              "color": "#000032"
             }
            },
            "totals": {
             "marker": {
              "color": "#000034"
             }
            },
            "type": "waterfall"
           }
          ]
         },
         "layout": {
          "coloraxis": {
           "colorscale": [
            [
             0,
             "#000011"
            ],
            [
             0.1111111111111111,
             "#000012"
            ],
            [
             0.2222222222222222,
             "#000013"
            ],
            [
             0.3333333333333333,
             "#000014"
            ],
            [
             0.4444444444444444,
             "#000015"
            ],
            [
             0.5555555555555556,
             "#000016"
            ],
            [
             0.6666666666666666,
             "#000017"
            ],
            [
             0.7777777777777778,
             "#000018"
            ],
            [
             0.8888888888888888,
             "#000019"
            ],
            [
             1,
             "#000020"
            ]
           ]
          },
          "colorscale": {
           "diverging": [
            [
             0,
             "#000021"
            ],
            [
             0.1,
             "#000022"
            ],
            [
             0.2,
             "#000023"
            ],
            [
             0.3,
             "#000024"
            ],
            [
             0.4,
             "#000025"
            ],
            [
             0.5,
             "#000026"
            ],
            [
             0.6,
             "#000027"
            ],
            [
             0.7,
             "#000028"
            ],
            [
             0.8,
             "#000029"
            ],
            [
             0.9,
             "#000030"
            ],
            [
             1,
             "#000031"
            ]
           ],
           "sequential": [
            [
             0,
             "#000011"
            ],
            [
             0.1111111111111111,
             "#000012"
            ],
            [
             0.2222222222222222,
             "#000013"
            ],
            [
             0.3333333333333333,
             "#000014"
            ],
            [
             0.4444444444444444,
             "#000015"
            ],
            [
             0.5555555555555556,
             "#000016"
            ],
            [
             0.6666666666666666,
             "#000017"
            ],
            [
             0.7777777777777778,
             "#000018"
            ],
            [
             0.8888888888888888,
             "#000019"
            ],
            [
             1,
             "#000020"
            ]
           ],
           "sequentialminus": [
            [
             0,
             "#000011"
            ],
            [
             0.1111111111111111,
             "#000012"
            ],
            [
             0.2222222222222222,
             "#000013"
            ],
            [
             0.3333333333333333,
             "#000014"
            ],
            [
             0.4444444444444444,
             "#000015"
            ],
            [
             0.5555555555555556,
             "#000016"
            ],
            [
             0.6666666666666666,
             "#000017"
            ],
            [
             0.7777777777777778,
             "#000018"
            ],
            [
             0.8888888888888888,
             "#000019"
            ],
            [
             1,
             "#000020"
            ]
           ]
          },
          "colorway": [
           "#000001",
           "#000002",
           "#000003",
           "#000004",
           "#000005",
           "#000006",
           "#000007",
           "#000008",
           "#000009",
           "#000010"
          ]
         }
        },
        "title": {
         "automargin": true,
         "font": {
          "color": "#164f5e",
          "size": 22
         },
         "text": "Walk%+",
         "yref": "paper"
        },
        "width": 500,
        "xaxis": {
         "anchor": "y",
         "domain": [
          0,
          1
         ],
         "title": {
          "text": ""
         }
        },
        "yaxis": {
         "anchor": "x",
         "domain": [
          0,
          1
         ],
         "title": {
          "text": ""
         }
        }
       }
      },
      "text/html": [
       "<div>                            <div id=\"bc201b96-4f57-4a1e-825c-75805a2410cf\" class=\"plotly-graph-div\" style=\"height:500px; width:500px;\"></div>            <script type=\"text/javascript\">                require([\"plotly\"], function(Plotly) {                    window.PLOTLYENV=window.PLOTLYENV || {};                                    if (document.getElementById(\"bc201b96-4f57-4a1e-825c-75805a2410cf\")) {                    Plotly.newPlot(                        \"bc201b96-4f57-4a1e-825c-75805a2410cf\",                        [{\"alignmentgroup\":\"True\",\"boxpoints\":\"all\",\"hovertemplate\":\"\\u003cb\\u003e%{hovertext}\\u003c\\u002fb\\u003e\\u003cbr\\u003e\\u003cbr\\u003eBB%+=%{y}\\u003cextra\\u003e\\u003c\\u002fextra\\u003e\",\"hovertext\":[\"Ronald Acuna Jr.\",\"Shohei Ohtani\",\"Mookie Betts\",\"Wander Franco\",\"Corbin Carroll\",\"Luis Robert\",\"Freddie Freeman\",\"Juan Soto\",\"Fernando Tatis Jr.\",\"Jose Ramirez\",\"Adolis Garcia\",\"Mike Trout\",\"Jonah Heim\",\"Marcus Semien\",\"Bo Bichette\",\"Christian Yelich\",\"Francisco Lindor\",\"Dansby Swanson\",\"Luis Arraez\",\"Will Smith\",\"Ha-seong Kim\",\"Randy Arozarena\",\"Paul Goldschmidt\",\"Matt Chapman\",\"Isaac Paredes\",\"Brandon Nimmo\",\"Jeimer Candelario\",\"Thairo Estrada\",\"Matt Olson\",\"Christian Walker\",\"Jack Suwinski\",\"Julio Rodriguez\",\"Yandy Diaz\",\"Kyle Tucker\",\"Josh Jung\",\"Ketel Marte\",\"Ozzie Albies\",\"William Contreras\",\"Xander Bogaerts\",\"Leody Taveras\",\"Adley Rutschman\",\"Nico Hoerner\",\"Lane Thomas\",\"Bobby Witt Jr.\",\"LaMonte Wade Jr.\",\"Austin Hays\",\"J.D. Davis\",\"Gunnar Henderson\",\"Alex Verdugo\",\"Nathaniel Lowe\",\"Jorge Soler\",\"Nolan Arenado\",\"Rafael Devers\",\"Austin Riley\",\"Brendan Donovan\",\"Bryson Stott\",\"Brandon Drury\",\"Brandon Marsh\",\"Ian Happ\",\"J.P. Crawford\",\"Alex Bregman\",\"Andres Gimenez\",\"Cal Raleigh\",\"Spencer Steer\",\"Nolan Gorman\",\"Ryan Noda\",\"Cedric Mullins II\",\"James Outman\",\"Nick Castellanos\",\"Pete Alonso\",\"Anthony Santander\",\"Ryan McMahon\",\"Zach McKinstry\",\"Trea Turner\",\"Anthony Volpe\",\"Masataka Yoshida\",\"Justin Turner\",\"Bryan Reynolds\",\"Manny Machado\",\"Whit Merrifield\",\"Jeremy Pena\",\"Josh Naylor\",\"Anthony Rizzo\",\"Jonathan India\",\"Jarred Kelenic\",\"George Springer\",\"Eugenio Suarez\",\"Joey Wiemer\",\"Andrew McCutchen\",\"Lourdes Gurriel Jr.\",\"Max Muncy\",\"Hunter Renfroe\",\"Mauricio Dubon\",\"Steven Kwan\",\"Tommy Edman\",\"Brent Rooker\",\"J.T. Realmuto\",\"Teoscar Hernandez\",\"Ezequiel Tovar\",\"Willson Contreras\",\"Carlos Correa\",\"Ke'Bryan Hayes\",\"Willy Adames\",\"Gleyber Torres\",\"Esteury Ruiz\",\"Marcell Ozuna\",\"Byron Buxton\",\"Andrew Benintendi\",\"Daulton Varsho\",\"J.D. Martinez\",\"Elias Diaz\",\"Ty France\",\"Taylor Ward\",\"Jeff McNeil\",\"Eddie Rosario\",\"Seiya Suzuki\",\"Carlos Santana\",\"Trent Grisham\",\"Vladimir Guerrero Jr.\",\"Michael Conforto\",\"Brian Anderson\",\"Jace Peterson\",\"Javier Baez\",\"Andrew Vaughn\",\"Alec Bohm\",\"Bryan De La Cruz\",\"Jake Cronenworth\",\"Salvador Perez\",\"CJ Abrams\",\"Spencer Torkelson\",\"Adam Frazier\",\"Miguel Vargas\",\"Amed Rosario\",\"Starling Marte\",\"Luis Garcia\",\"DJ LeMahieu\",\"Tyler Stephenson\",\"Kyle Schwarber\",\"Triston Casas\",\"Dominic Smith\",\"Shea Langeliers\",\"Josh Bell\",\"Myles Straw\",\"Joey Meneses\",\"Jose Abreu\",\"MJ Melendez\",\"Tim Anderson\",\"Rowdy Tellez\",\"Jurickson Profar\",\"Keibert Ruiz\",\"Enrique Hernandez\"],\"legendgroup\":\"\",\"marker\":{\"color\":\"#7284cc\"},\"name\":\"\",\"notched\":false,\"offsetgroup\":\"\",\"orientation\":\"v\",\"showlegend\":false,\"x0\":\" \",\"xaxis\":\"x\",\"y\":[122,144,152,95,101,69,113,238,90,128,110,150,89,106,46,140,106,123,86,174,133,148,132,117,128,125,96,54,157,101,178,84,142,128,72,112,77,116,123,76,173,63,64,66,191,71,108,139,103,144,136,77,102,92,111,58,62,118,189,175,154,65,118,127,128,223,151,100,72,105,102,125,124,74,106,99,108,107,70,87,62,74,115,101,112,93,115,104,175,68,172,72,41,116,88,132,78,70,47,107,112,59,114,119,45,111,134,104,95,67,84,63,105,87,79,130,119,148,97,133,119,125,45,92,67,80,124,44,43,122,98,136,71,57,61,97,114,172,165,86,75,137,105,69,74,122,61,106,118,61,85],\"y0\":\" \",\"yaxis\":\"y\",\"type\":\"box\"}],                        {\"template\":{\"data\":{\"candlestick\":[{\"decreasing\":{\"line\":{\"color\":\"#000033\"}},\"increasing\":{\"line\":{\"color\":\"#000032\"}},\"type\":\"candlestick\"}],\"contourcarpet\":[{\"colorscale\":[[0.0,\"#000011\"],[0.1111111111111111,\"#000012\"],[0.2222222222222222,\"#000013\"],[0.3333333333333333,\"#000014\"],[0.4444444444444444,\"#000015\"],[0.5555555555555556,\"#000016\"],[0.6666666666666666,\"#000017\"],[0.7777777777777778,\"#000018\"],[0.8888888888888888,\"#000019\"],[1.0,\"#000020\"]],\"type\":\"contourcarpet\"}],\"contour\":[{\"colorscale\":[[0.0,\"#000011\"],[0.1111111111111111,\"#000012\"],[0.2222222222222222,\"#000013\"],[0.3333333333333333,\"#000014\"],[0.4444444444444444,\"#000015\"],[0.5555555555555556,\"#000016\"],[0.6666666666666666,\"#000017\"],[0.7777777777777778,\"#000018\"],[0.8888888888888888,\"#000019\"],[1.0,\"#000020\"]],\"type\":\"contour\"}],\"heatmap\":[{\"colorscale\":[[0.0,\"#000011\"],[0.1111111111111111,\"#000012\"],[0.2222222222222222,\"#000013\"],[0.3333333333333333,\"#000014\"],[0.4444444444444444,\"#000015\"],[0.5555555555555556,\"#000016\"],[0.6666666666666666,\"#000017\"],[0.7777777777777778,\"#000018\"],[0.8888888888888888,\"#000019\"],[1.0,\"#000020\"]],\"type\":\"heatmap\"}],\"histogram2d\":[{\"colorscale\":[[0.0,\"#000011\"],[0.1111111111111111,\"#000012\"],[0.2222222222222222,\"#000013\"],[0.3333333333333333,\"#000014\"],[0.4444444444444444,\"#000015\"],[0.5555555555555556,\"#000016\"],[0.6666666666666666,\"#000017\"],[0.7777777777777778,\"#000018\"],[0.8888888888888888,\"#000019\"],[1.0,\"#000020\"]],\"type\":\"histogram2d\"}],\"icicle\":[{\"textfont\":{\"color\":\"white\"},\"type\":\"icicle\"}],\"sankey\":[{\"textfont\":{\"color\":\"#000036\"},\"type\":\"sankey\"}],\"scatter\":[{\"marker\":{\"line\":{\"width\":0}},\"type\":\"scatter\"}],\"table\":[{\"cells\":{\"fill\":{\"color\":\"#000038\"},\"font\":{\"color\":\"#000037\"},\"line\":{\"color\":\"#000039\"}},\"header\":{\"fill\":{\"color\":\"#000040\"},\"font\":{\"color\":\"#000036\"},\"line\":{\"color\":\"#000039\"}},\"type\":\"table\"}],\"waterfall\":[{\"connector\":{\"line\":{\"color\":\"#000036\",\"width\":2}},\"decreasing\":{\"marker\":{\"color\":\"#000033\"}},\"increasing\":{\"marker\":{\"color\":\"#000032\"}},\"totals\":{\"marker\":{\"color\":\"#000034\"}},\"type\":\"waterfall\"}]},\"layout\":{\"coloraxis\":{\"colorscale\":[[0.0,\"#000011\"],[0.1111111111111111,\"#000012\"],[0.2222222222222222,\"#000013\"],[0.3333333333333333,\"#000014\"],[0.4444444444444444,\"#000015\"],[0.5555555555555556,\"#000016\"],[0.6666666666666666,\"#000017\"],[0.7777777777777778,\"#000018\"],[0.8888888888888888,\"#000019\"],[1.0,\"#000020\"]]},\"colorscale\":{\"diverging\":[[0.0,\"#000021\"],[0.1,\"#000022\"],[0.2,\"#000023\"],[0.3,\"#000024\"],[0.4,\"#000025\"],[0.5,\"#000026\"],[0.6,\"#000027\"],[0.7,\"#000028\"],[0.8,\"#000029\"],[0.9,\"#000030\"],[1.0,\"#000031\"]],\"sequential\":[[0.0,\"#000011\"],[0.1111111111111111,\"#000012\"],[0.2222222222222222,\"#000013\"],[0.3333333333333333,\"#000014\"],[0.4444444444444444,\"#000015\"],[0.5555555555555556,\"#000016\"],[0.6666666666666666,\"#000017\"],[0.7777777777777778,\"#000018\"],[0.8888888888888888,\"#000019\"],[1.0,\"#000020\"]],\"sequentialminus\":[[0.0,\"#000011\"],[0.1111111111111111,\"#000012\"],[0.2222222222222222,\"#000013\"],[0.3333333333333333,\"#000014\"],[0.4444444444444444,\"#000015\"],[0.5555555555555556,\"#000016\"],[0.6666666666666666,\"#000017\"],[0.7777777777777778,\"#000018\"],[0.8888888888888888,\"#000019\"],[1.0,\"#000020\"]]},\"colorway\":[\"#000001\",\"#000002\",\"#000003\",\"#000004\",\"#000005\",\"#000006\",\"#000007\",\"#000008\",\"#000009\",\"#000010\"]}},\"xaxis\":{\"anchor\":\"y\",\"domain\":[0.0,1.0],\"title\":{\"text\":\"\"}},\"yaxis\":{\"anchor\":\"x\",\"domain\":[0.0,1.0],\"title\":{\"text\":\"\"}},\"legend\":{\"tracegroupgap\":0},\"margin\":{\"t\":60},\"boxmode\":\"group\",\"height\":500,\"width\":500,\"title\":{\"font\":{\"size\":22,\"color\":\"#164f5e\"},\"text\":\"Walk%+\",\"automargin\":true,\"yref\":\"paper\"}},                        {\"responsive\": true}                    ).then(function(){\n",
       "                            \n",
       "var gd = document.getElementById('bc201b96-4f57-4a1e-825c-75805a2410cf');\n",
       "var x = new MutationObserver(function (mutations, observer) {{\n",
       "        var display = window.getComputedStyle(gd).display;\n",
       "        if (!display || display === 'none') {{\n",
       "            console.log([gd, 'removed!']);\n",
       "            Plotly.purge(gd);\n",
       "            observer.disconnect();\n",
       "        }}\n",
       "}});\n",
       "\n",
       "// Listen for the removal of the full notebook cells\n",
       "var notebookContainer = gd.closest('#notebook-container');\n",
       "if (notebookContainer) {{\n",
       "    x.observe(notebookContainer, {childList: true});\n",
       "}}\n",
       "\n",
       "// Listen for the clearing of the current output cell\n",
       "var outputEl = gd.closest('.output');\n",
       "if (outputEl) {{\n",
       "    x.observe(outputEl, {childList: true});\n",
       "}}\n",
       "\n",
       "                        })                };                });            </script>        </div>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "fig_41 = px.box(\n",
    "    df.query(\"Season==2023\"),\n",
    "    y = \"BB%+\",\n",
    "    points=\"all\",\n",
    "    hover_name = \"Name\",\n",
    "    height = 500,\n",
    "    width = 500,\n",
    ")\n",
    "\n",
    "fig_41.update_traces(marker=dict(color=\"#7284cc\"))\n",
    "\n",
    "fig_41.update_layout(\n",
    "    title=dict(text=\"Walk%+\", font=dict(size=22), automargin=True, yref='paper'),\n",
    "    title_font_color=\"#164f5e\",\n",
    "    yaxis=dict(title=\"\"),\n",
    "    xaxis=dict(title=\"\")\n",
    ")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 97,
   "id": "6bd2126c",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "application/vnd.plotly.v1+json": {
       "config": {
        "plotlyServerURL": "https://plot.ly"
       },
       "data": [
        {
         "alignmentgroup": "True",
         "boxpoints": "all",
         "hovertemplate": "<b>%{hovertext}</b><br><br>K%+=%{y}<extra></extra>",
         "hovertext": [
          "Ronald Acuna Jr.",
          "Shohei Ohtani",
          "Mookie Betts",
          "Wander Franco",
          "Corbin Carroll",
          "Luis Robert",
          "Freddie Freeman",
          "Juan Soto",
          "Fernando Tatis Jr.",
          "Jose Ramirez",
          "Adolis Garcia",
          "Mike Trout",
          "Jonah Heim",
          "Marcus Semien",
          "Bo Bichette",
          "Christian Yelich",
          "Francisco Lindor",
          "Dansby Swanson",
          "Luis Arraez",
          "Will Smith",
          "Ha-seong Kim",
          "Randy Arozarena",
          "Paul Goldschmidt",
          "Matt Chapman",
          "Isaac Paredes",
          "Brandon Nimmo",
          "Jeimer Candelario",
          "Thairo Estrada",
          "Matt Olson",
          "Christian Walker",
          "Jack Suwinski",
          "Julio Rodriguez",
          "Yandy Diaz",
          "Kyle Tucker",
          "Josh Jung",
          "Ketel Marte",
          "Ozzie Albies",
          "William Contreras",
          "Xander Bogaerts",
          "Leody Taveras",
          "Adley Rutschman",
          "Nico Hoerner",
          "Lane Thomas",
          "Bobby Witt Jr.",
          "LaMonte Wade Jr.",
          "Austin Hays",
          "J.D. Davis",
          "Gunnar Henderson",
          "Alex Verdugo",
          "Nathaniel Lowe",
          "Jorge Soler",
          "Nolan Arenado",
          "Rafael Devers",
          "Austin Riley",
          "Brendan Donovan",
          "Bryson Stott",
          "Brandon Drury",
          "Brandon Marsh",
          "Ian Happ",
          "J.P. Crawford",
          "Alex Bregman",
          "Andres Gimenez",
          "Cal Raleigh",
          "Spencer Steer",
          "Nolan Gorman",
          "Ryan Noda",
          "Cedric Mullins II",
          "James Outman",
          "Nick Castellanos",
          "Pete Alonso",
          "Anthony Santander",
          "Ryan McMahon",
          "Zach McKinstry",
          "Trea Turner",
          "Anthony Volpe",
          "Masataka Yoshida",
          "Justin Turner",
          "Bryan Reynolds",
          "Manny Machado",
          "Whit Merrifield",
          "Jeremy Pena",
          "Josh Naylor",
          "Anthony Rizzo",
          "Jonathan India",
          "Jarred Kelenic",
          "George Springer",
          "Eugenio Suarez",
          "Joey Wiemer",
          "Andrew McCutchen",
          "Lourdes Gurriel Jr.",
          "Max Muncy",
          "Hunter Renfroe",
          "Mauricio Dubon",
          "Steven Kwan",
          "Tommy Edman",
          "Brent Rooker",
          "J.T. Realmuto",
          "Teoscar Hernandez",
          "Ezequiel Tovar",
          "Willson Contreras",
          "Carlos Correa",
          "Ke'Bryan Hayes",
          "Willy Adames",
          "Gleyber Torres",
          "Esteury Ruiz",
          "Marcell Ozuna",
          "Byron Buxton",
          "Andrew Benintendi",
          "Daulton Varsho",
          "J.D. Martinez",
          "Elias Diaz",
          "Ty France",
          "Taylor Ward",
          "Jeff McNeil",
          "Eddie Rosario",
          "Seiya Suzuki",
          "Carlos Santana",
          "Trent Grisham",
          "Vladimir Guerrero Jr.",
          "Michael Conforto",
          "Brian Anderson",
          "Jace Peterson",
          "Javier Baez",
          "Andrew Vaughn",
          "Alec Bohm",
          "Bryan De La Cruz",
          "Jake Cronenworth",
          "Salvador Perez",
          "CJ Abrams",
          "Spencer Torkelson",
          "Adam Frazier",
          "Miguel Vargas",
          "Amed Rosario",
          "Starling Marte",
          "Luis Garcia",
          "DJ LeMahieu",
          "Tyler Stephenson",
          "Kyle Schwarber",
          "Triston Casas",
          "Dominic Smith",
          "Shea Langeliers",
          "Josh Bell",
          "Myles Straw",
          "Joey Meneses",
          "Jose Abreu",
          "MJ Melendez",
          "Tim Anderson",
          "Rowdy Tellez",
          "Jurickson Profar",
          "Keibert Ruiz",
          "Enrique Hernandez"
         ],
         "legendgroup": "",
         "marker": {
          "color": "#7284cc"
         },
         "name": "",
         "notched": false,
         "offsetgroup": "",
         "orientation": "v",
         "showlegend": false,
         "type": "box",
         "x0": " ",
         "xaxis": "x",
         "y": [
          55,
          97,
          74,
          59,
          88,
          123,
          76,
          89,
          85,
          42,
          111,
          126,
          77,
          62,
          79,
          94,
          93,
          102,
          23,
          61,
          101,
          107,
          96,
          124,
          76,
          100,
          89,
          109,
          120,
          78,
          139,
          112,
          68,
          57,
          126,
          72,
          66,
          89,
          83,
          86,
          63,
          51,
          113,
          90,
          83,
          102,
          122,
          135,
          56,
          89,
          100,
          82,
          88,
          104,
          66,
          71,
          114,
          142,
          110,
          82,
          55,
          73,
          111,
          79,
          134,
          145,
          84,
          154,
          112,
          92,
          97,
          138,
          88,
          107,
          129,
          47,
          71,
          84,
          83,
          77,
          99,
          73,
          99,
          83,
          147,
          72,
          122,
          127,
          90,
          80,
          126,
          95,
          53,
          53,
          72,
          135,
          107,
          138,
          119,
          101,
          104,
          90,
          114,
          62,
          81,
          96,
          129,
          65,
          99,
          137,
          93,
          75,
          87,
          51,
          105,
          112,
          79,
          125,
          71,
          111,
          134,
          102,
          98,
          83,
          75,
          110,
          91,
          105,
          101,
          103,
          52,
          91,
          83,
          84,
          52,
          105,
          119,
          130,
          117,
          67,
          129,
          96,
          88,
          90,
          101,
          130,
          92,
          106,
          80,
          39,
          93
         ],
         "y0": " ",
         "yaxis": "y"
        }
       ],
       "layout": {
        "boxmode": "group",
        "height": 500,
        "legend": {
         "tracegroupgap": 0
        },
        "margin": {
         "t": 60
        },
        "template": {
         "data": {
          "candlestick": [
           {
            "decreasing": {
             "line": {
              "color": "#000033"
             }
            },
            "increasing": {
             "line": {
              "color": "#000032"
             }
            },
            "type": "candlestick"
           }
          ],
          "contour": [
           {
            "colorscale": [
             [
              0,
              "#000011"
             ],
             [
              0.1111111111111111,
              "#000012"
             ],
             [
              0.2222222222222222,
              "#000013"
             ],
             [
              0.3333333333333333,
              "#000014"
             ],
             [
              0.4444444444444444,
              "#000015"
             ],
             [
              0.5555555555555556,
              "#000016"
             ],
             [
              0.6666666666666666,
              "#000017"
             ],
             [
              0.7777777777777778,
              "#000018"
             ],
             [
              0.8888888888888888,
              "#000019"
             ],
             [
              1,
              "#000020"
             ]
            ],
            "type": "contour"
           }
          ],
          "contourcarpet": [
           {
            "colorscale": [
             [
              0,
              "#000011"
             ],
             [
              0.1111111111111111,
              "#000012"
             ],
             [
              0.2222222222222222,
              "#000013"
             ],
             [
              0.3333333333333333,
              "#000014"
             ],
             [
              0.4444444444444444,
              "#000015"
             ],
             [
              0.5555555555555556,
              "#000016"
             ],
             [
              0.6666666666666666,
              "#000017"
             ],
             [
              0.7777777777777778,
              "#000018"
             ],
             [
              0.8888888888888888,
              "#000019"
             ],
             [
              1,
              "#000020"
             ]
            ],
            "type": "contourcarpet"
           }
          ],
          "heatmap": [
           {
            "colorscale": [
             [
              0,
              "#000011"
             ],
             [
              0.1111111111111111,
              "#000012"
             ],
             [
              0.2222222222222222,
              "#000013"
             ],
             [
              0.3333333333333333,
              "#000014"
             ],
             [
              0.4444444444444444,
              "#000015"
             ],
             [
              0.5555555555555556,
              "#000016"
             ],
             [
              0.6666666666666666,
              "#000017"
             ],
             [
              0.7777777777777778,
              "#000018"
             ],
             [
              0.8888888888888888,
              "#000019"
             ],
             [
              1,
              "#000020"
             ]
            ],
            "type": "heatmap"
           }
          ],
          "histogram2d": [
           {
            "colorscale": [
             [
              0,
              "#000011"
             ],
             [
              0.1111111111111111,
              "#000012"
             ],
             [
              0.2222222222222222,
              "#000013"
             ],
             [
              0.3333333333333333,
              "#000014"
             ],
             [
              0.4444444444444444,
              "#000015"
             ],
             [
              0.5555555555555556,
              "#000016"
             ],
             [
              0.6666666666666666,
              "#000017"
             ],
             [
              0.7777777777777778,
              "#000018"
             ],
             [
              0.8888888888888888,
              "#000019"
             ],
             [
              1,
              "#000020"
             ]
            ],
            "type": "histogram2d"
           }
          ],
          "icicle": [
           {
            "textfont": {
             "color": "white"
            },
            "type": "icicle"
           }
          ],
          "sankey": [
           {
            "textfont": {
             "color": "#000036"
            },
            "type": "sankey"
           }
          ],
          "scatter": [
           {
            "marker": {
             "line": {
              "width": 0
             }
            },
            "type": "scatter"
           }
          ],
          "table": [
           {
            "cells": {
             "fill": {
              "color": "#000038"
             },
             "font": {
              "color": "#000037"
             },
             "line": {
              "color": "#000039"
             }
            },
            "header": {
             "fill": {
              "color": "#000040"
             },
             "font": {
              "color": "#000036"
             },
             "line": {
              "color": "#000039"
             }
            },
            "type": "table"
           }
          ],
          "waterfall": [
           {
            "connector": {
             "line": {
              "color": "#000036",
              "width": 2
             }
            },
            "decreasing": {
             "marker": {
              "color": "#000033"
             }
            },
            "increasing": {
             "marker": {
              "color": "#000032"
             }
            },
            "totals": {
             "marker": {
              "color": "#000034"
             }
            },
            "type": "waterfall"
           }
          ]
         },
         "layout": {
          "coloraxis": {
           "colorscale": [
            [
             0,
             "#000011"
            ],
            [
             0.1111111111111111,
             "#000012"
            ],
            [
             0.2222222222222222,
             "#000013"
            ],
            [
             0.3333333333333333,
             "#000014"
            ],
            [
             0.4444444444444444,
             "#000015"
            ],
            [
             0.5555555555555556,
             "#000016"
            ],
            [
             0.6666666666666666,
             "#000017"
            ],
            [
             0.7777777777777778,
             "#000018"
            ],
            [
             0.8888888888888888,
             "#000019"
            ],
            [
             1,
             "#000020"
            ]
           ]
          },
          "colorscale": {
           "diverging": [
            [
             0,
             "#000021"
            ],
            [
             0.1,
             "#000022"
            ],
            [
             0.2,
             "#000023"
            ],
            [
             0.3,
             "#000024"
            ],
            [
             0.4,
             "#000025"
            ],
            [
             0.5,
             "#000026"
            ],
            [
             0.6,
             "#000027"
            ],
            [
             0.7,
             "#000028"
            ],
            [
             0.8,
             "#000029"
            ],
            [
             0.9,
             "#000030"
            ],
            [
             1,
             "#000031"
            ]
           ],
           "sequential": [
            [
             0,
             "#000011"
            ],
            [
             0.1111111111111111,
             "#000012"
            ],
            [
             0.2222222222222222,
             "#000013"
            ],
            [
             0.3333333333333333,
             "#000014"
            ],
            [
             0.4444444444444444,
             "#000015"
            ],
            [
             0.5555555555555556,
             "#000016"
            ],
            [
             0.6666666666666666,
             "#000017"
            ],
            [
             0.7777777777777778,
             "#000018"
            ],
            [
             0.8888888888888888,
             "#000019"
            ],
            [
             1,
             "#000020"
            ]
           ],
           "sequentialminus": [
            [
             0,
             "#000011"
            ],
            [
             0.1111111111111111,
             "#000012"
            ],
            [
             0.2222222222222222,
             "#000013"
            ],
            [
             0.3333333333333333,
             "#000014"
            ],
            [
             0.4444444444444444,
             "#000015"
            ],
            [
             0.5555555555555556,
             "#000016"
            ],
            [
             0.6666666666666666,
             "#000017"
            ],
            [
             0.7777777777777778,
             "#000018"
            ],
            [
             0.8888888888888888,
             "#000019"
            ],
            [
             1,
             "#000020"
            ]
           ]
          },
          "colorway": [
           "#000001",
           "#000002",
           "#000003",
           "#000004",
           "#000005",
           "#000006",
           "#000007",
           "#000008",
           "#000009",
           "#000010"
          ]
         }
        },
        "title": {
         "automargin": true,
         "font": {
          "color": "#164f5e",
          "size": 22
         },
         "text": "Strikeout%+",
         "yref": "paper"
        },
        "width": 500,
        "xaxis": {
         "anchor": "y",
         "domain": [
          0,
          1
         ],
         "title": {
          "text": ""
         }
        },
        "yaxis": {
         "anchor": "x",
         "domain": [
          0,
          1
         ],
         "title": {
          "text": ""
         }
        }
       }
      },
      "text/html": [
       "<div>                            <div id=\"f30aab5f-6c60-4056-89b2-66254de4ddea\" class=\"plotly-graph-div\" style=\"height:500px; width:500px;\"></div>            <script type=\"text/javascript\">                require([\"plotly\"], function(Plotly) {                    window.PLOTLYENV=window.PLOTLYENV || {};                                    if (document.getElementById(\"f30aab5f-6c60-4056-89b2-66254de4ddea\")) {                    Plotly.newPlot(                        \"f30aab5f-6c60-4056-89b2-66254de4ddea\",                        [{\"alignmentgroup\":\"True\",\"boxpoints\":\"all\",\"hovertemplate\":\"\\u003cb\\u003e%{hovertext}\\u003c\\u002fb\\u003e\\u003cbr\\u003e\\u003cbr\\u003eK%+=%{y}\\u003cextra\\u003e\\u003c\\u002fextra\\u003e\",\"hovertext\":[\"Ronald Acuna Jr.\",\"Shohei Ohtani\",\"Mookie Betts\",\"Wander Franco\",\"Corbin Carroll\",\"Luis Robert\",\"Freddie Freeman\",\"Juan Soto\",\"Fernando Tatis Jr.\",\"Jose Ramirez\",\"Adolis Garcia\",\"Mike Trout\",\"Jonah Heim\",\"Marcus Semien\",\"Bo Bichette\",\"Christian Yelich\",\"Francisco Lindor\",\"Dansby Swanson\",\"Luis Arraez\",\"Will Smith\",\"Ha-seong Kim\",\"Randy Arozarena\",\"Paul Goldschmidt\",\"Matt Chapman\",\"Isaac Paredes\",\"Brandon Nimmo\",\"Jeimer Candelario\",\"Thairo Estrada\",\"Matt Olson\",\"Christian Walker\",\"Jack Suwinski\",\"Julio Rodriguez\",\"Yandy Diaz\",\"Kyle Tucker\",\"Josh Jung\",\"Ketel Marte\",\"Ozzie Albies\",\"William Contreras\",\"Xander Bogaerts\",\"Leody Taveras\",\"Adley Rutschman\",\"Nico Hoerner\",\"Lane Thomas\",\"Bobby Witt Jr.\",\"LaMonte Wade Jr.\",\"Austin Hays\",\"J.D. Davis\",\"Gunnar Henderson\",\"Alex Verdugo\",\"Nathaniel Lowe\",\"Jorge Soler\",\"Nolan Arenado\",\"Rafael Devers\",\"Austin Riley\",\"Brendan Donovan\",\"Bryson Stott\",\"Brandon Drury\",\"Brandon Marsh\",\"Ian Happ\",\"J.P. Crawford\",\"Alex Bregman\",\"Andres Gimenez\",\"Cal Raleigh\",\"Spencer Steer\",\"Nolan Gorman\",\"Ryan Noda\",\"Cedric Mullins II\",\"James Outman\",\"Nick Castellanos\",\"Pete Alonso\",\"Anthony Santander\",\"Ryan McMahon\",\"Zach McKinstry\",\"Trea Turner\",\"Anthony Volpe\",\"Masataka Yoshida\",\"Justin Turner\",\"Bryan Reynolds\",\"Manny Machado\",\"Whit Merrifield\",\"Jeremy Pena\",\"Josh Naylor\",\"Anthony Rizzo\",\"Jonathan India\",\"Jarred Kelenic\",\"George Springer\",\"Eugenio Suarez\",\"Joey Wiemer\",\"Andrew McCutchen\",\"Lourdes Gurriel Jr.\",\"Max Muncy\",\"Hunter Renfroe\",\"Mauricio Dubon\",\"Steven Kwan\",\"Tommy Edman\",\"Brent Rooker\",\"J.T. Realmuto\",\"Teoscar Hernandez\",\"Ezequiel Tovar\",\"Willson Contreras\",\"Carlos Correa\",\"Ke'Bryan Hayes\",\"Willy Adames\",\"Gleyber Torres\",\"Esteury Ruiz\",\"Marcell Ozuna\",\"Byron Buxton\",\"Andrew Benintendi\",\"Daulton Varsho\",\"J.D. Martinez\",\"Elias Diaz\",\"Ty France\",\"Taylor Ward\",\"Jeff McNeil\",\"Eddie Rosario\",\"Seiya Suzuki\",\"Carlos Santana\",\"Trent Grisham\",\"Vladimir Guerrero Jr.\",\"Michael Conforto\",\"Brian Anderson\",\"Jace Peterson\",\"Javier Baez\",\"Andrew Vaughn\",\"Alec Bohm\",\"Bryan De La Cruz\",\"Jake Cronenworth\",\"Salvador Perez\",\"CJ Abrams\",\"Spencer Torkelson\",\"Adam Frazier\",\"Miguel Vargas\",\"Amed Rosario\",\"Starling Marte\",\"Luis Garcia\",\"DJ LeMahieu\",\"Tyler Stephenson\",\"Kyle Schwarber\",\"Triston Casas\",\"Dominic Smith\",\"Shea Langeliers\",\"Josh Bell\",\"Myles Straw\",\"Joey Meneses\",\"Jose Abreu\",\"MJ Melendez\",\"Tim Anderson\",\"Rowdy Tellez\",\"Jurickson Profar\",\"Keibert Ruiz\",\"Enrique Hernandez\"],\"legendgroup\":\"\",\"marker\":{\"color\":\"#7284cc\"},\"name\":\"\",\"notched\":false,\"offsetgroup\":\"\",\"orientation\":\"v\",\"showlegend\":false,\"x0\":\" \",\"xaxis\":\"x\",\"y\":[55,97,74,59,88,123,76,89,85,42,111,126,77,62,79,94,93,102,23,61,101,107,96,124,76,100,89,109,120,78,139,112,68,57,126,72,66,89,83,86,63,51,113,90,83,102,122,135,56,89,100,82,88,104,66,71,114,142,110,82,55,73,111,79,134,145,84,154,112,92,97,138,88,107,129,47,71,84,83,77,99,73,99,83,147,72,122,127,90,80,126,95,53,53,72,135,107,138,119,101,104,90,114,62,81,96,129,65,99,137,93,75,87,51,105,112,79,125,71,111,134,102,98,83,75,110,91,105,101,103,52,91,83,84,52,105,119,130,117,67,129,96,88,90,101,130,92,106,80,39,93],\"y0\":\" \",\"yaxis\":\"y\",\"type\":\"box\"}],                        {\"template\":{\"data\":{\"candlestick\":[{\"decreasing\":{\"line\":{\"color\":\"#000033\"}},\"increasing\":{\"line\":{\"color\":\"#000032\"}},\"type\":\"candlestick\"}],\"contourcarpet\":[{\"colorscale\":[[0.0,\"#000011\"],[0.1111111111111111,\"#000012\"],[0.2222222222222222,\"#000013\"],[0.3333333333333333,\"#000014\"],[0.4444444444444444,\"#000015\"],[0.5555555555555556,\"#000016\"],[0.6666666666666666,\"#000017\"],[0.7777777777777778,\"#000018\"],[0.8888888888888888,\"#000019\"],[1.0,\"#000020\"]],\"type\":\"contourcarpet\"}],\"contour\":[{\"colorscale\":[[0.0,\"#000011\"],[0.1111111111111111,\"#000012\"],[0.2222222222222222,\"#000013\"],[0.3333333333333333,\"#000014\"],[0.4444444444444444,\"#000015\"],[0.5555555555555556,\"#000016\"],[0.6666666666666666,\"#000017\"],[0.7777777777777778,\"#000018\"],[0.8888888888888888,\"#000019\"],[1.0,\"#000020\"]],\"type\":\"contour\"}],\"heatmap\":[{\"colorscale\":[[0.0,\"#000011\"],[0.1111111111111111,\"#000012\"],[0.2222222222222222,\"#000013\"],[0.3333333333333333,\"#000014\"],[0.4444444444444444,\"#000015\"],[0.5555555555555556,\"#000016\"],[0.6666666666666666,\"#000017\"],[0.7777777777777778,\"#000018\"],[0.8888888888888888,\"#000019\"],[1.0,\"#000020\"]],\"type\":\"heatmap\"}],\"histogram2d\":[{\"colorscale\":[[0.0,\"#000011\"],[0.1111111111111111,\"#000012\"],[0.2222222222222222,\"#000013\"],[0.3333333333333333,\"#000014\"],[0.4444444444444444,\"#000015\"],[0.5555555555555556,\"#000016\"],[0.6666666666666666,\"#000017\"],[0.7777777777777778,\"#000018\"],[0.8888888888888888,\"#000019\"],[1.0,\"#000020\"]],\"type\":\"histogram2d\"}],\"icicle\":[{\"textfont\":{\"color\":\"white\"},\"type\":\"icicle\"}],\"sankey\":[{\"textfont\":{\"color\":\"#000036\"},\"type\":\"sankey\"}],\"scatter\":[{\"marker\":{\"line\":{\"width\":0}},\"type\":\"scatter\"}],\"table\":[{\"cells\":{\"fill\":{\"color\":\"#000038\"},\"font\":{\"color\":\"#000037\"},\"line\":{\"color\":\"#000039\"}},\"header\":{\"fill\":{\"color\":\"#000040\"},\"font\":{\"color\":\"#000036\"},\"line\":{\"color\":\"#000039\"}},\"type\":\"table\"}],\"waterfall\":[{\"connector\":{\"line\":{\"color\":\"#000036\",\"width\":2}},\"decreasing\":{\"marker\":{\"color\":\"#000033\"}},\"increasing\":{\"marker\":{\"color\":\"#000032\"}},\"totals\":{\"marker\":{\"color\":\"#000034\"}},\"type\":\"waterfall\"}]},\"layout\":{\"coloraxis\":{\"colorscale\":[[0.0,\"#000011\"],[0.1111111111111111,\"#000012\"],[0.2222222222222222,\"#000013\"],[0.3333333333333333,\"#000014\"],[0.4444444444444444,\"#000015\"],[0.5555555555555556,\"#000016\"],[0.6666666666666666,\"#000017\"],[0.7777777777777778,\"#000018\"],[0.8888888888888888,\"#000019\"],[1.0,\"#000020\"]]},\"colorscale\":{\"diverging\":[[0.0,\"#000021\"],[0.1,\"#000022\"],[0.2,\"#000023\"],[0.3,\"#000024\"],[0.4,\"#000025\"],[0.5,\"#000026\"],[0.6,\"#000027\"],[0.7,\"#000028\"],[0.8,\"#000029\"],[0.9,\"#000030\"],[1.0,\"#000031\"]],\"sequential\":[[0.0,\"#000011\"],[0.1111111111111111,\"#000012\"],[0.2222222222222222,\"#000013\"],[0.3333333333333333,\"#000014\"],[0.4444444444444444,\"#000015\"],[0.5555555555555556,\"#000016\"],[0.6666666666666666,\"#000017\"],[0.7777777777777778,\"#000018\"],[0.8888888888888888,\"#000019\"],[1.0,\"#000020\"]],\"sequentialminus\":[[0.0,\"#000011\"],[0.1111111111111111,\"#000012\"],[0.2222222222222222,\"#000013\"],[0.3333333333333333,\"#000014\"],[0.4444444444444444,\"#000015\"],[0.5555555555555556,\"#000016\"],[0.6666666666666666,\"#000017\"],[0.7777777777777778,\"#000018\"],[0.8888888888888888,\"#000019\"],[1.0,\"#000020\"]]},\"colorway\":[\"#000001\",\"#000002\",\"#000003\",\"#000004\",\"#000005\",\"#000006\",\"#000007\",\"#000008\",\"#000009\",\"#000010\"]}},\"xaxis\":{\"anchor\":\"y\",\"domain\":[0.0,1.0],\"title\":{\"text\":\"\"}},\"yaxis\":{\"anchor\":\"x\",\"domain\":[0.0,1.0],\"title\":{\"text\":\"\"}},\"legend\":{\"tracegroupgap\":0},\"margin\":{\"t\":60},\"boxmode\":\"group\",\"height\":500,\"width\":500,\"title\":{\"font\":{\"size\":22,\"color\":\"#164f5e\"},\"text\":\"Strikeout%+\",\"automargin\":true,\"yref\":\"paper\"}},                        {\"responsive\": true}                    ).then(function(){\n",
       "                            \n",
       "var gd = document.getElementById('f30aab5f-6c60-4056-89b2-66254de4ddea');\n",
       "var x = new MutationObserver(function (mutations, observer) {{\n",
       "        var display = window.getComputedStyle(gd).display;\n",
       "        if (!display || display === 'none') {{\n",
       "            console.log([gd, 'removed!']);\n",
       "            Plotly.purge(gd);\n",
       "            observer.disconnect();\n",
       "        }}\n",
       "}});\n",
       "\n",
       "// Listen for the removal of the full notebook cells\n",
       "var notebookContainer = gd.closest('#notebook-container');\n",
       "if (notebookContainer) {{\n",
       "    x.observe(notebookContainer, {childList: true});\n",
       "}}\n",
       "\n",
       "// Listen for the clearing of the current output cell\n",
       "var outputEl = gd.closest('.output');\n",
       "if (outputEl) {{\n",
       "    x.observe(outputEl, {childList: true});\n",
       "}}\n",
       "\n",
       "                        })                };                });            </script>        </div>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "fig_42 = px.box(\n",
    "    df.query(\"Season==2023\"),\n",
    "    y = \"K%+\",\n",
    "    points=\"all\",\n",
    "    hover_name = \"Name\",\n",
    "    height = 500,\n",
    "    width = 500,\n",
    ")\n",
    "\n",
    "fig_42.update_traces(marker=dict(color=\"#7284cc\"))\n",
    "\n",
    "fig_42.update_layout(\n",
    "    title=dict(text=\"Strikeout%+\", font=dict(size=22), automargin=True, yref='paper'),\n",
    "    title_font_color=\"#164f5e\",\n",
    "    yaxis=dict(title=\"\"),\n",
    "    xaxis=dict(title=\"\")\n",
    ")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 98,
   "id": "e2cf8281",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "application/vnd.plotly.v1+json": {
       "config": {
        "plotlyServerURL": "https://plot.ly"
       },
       "data": [
        {
         "alignmentgroup": "True",
         "boxpoints": "all",
         "hovertemplate": "<b>%{hovertext}</b><br><br>O-Swing%=%{y}<extra></extra>",
         "hovertext": [
          "Ronald Acuna Jr.",
          "Shohei Ohtani",
          "Mookie Betts",
          "Wander Franco",
          "Corbin Carroll",
          "Luis Robert",
          "Freddie Freeman",
          "Juan Soto",
          "Fernando Tatis Jr.",
          "Jose Ramirez",
          "Adolis Garcia",
          "Mike Trout",
          "Jonah Heim",
          "Marcus Semien",
          "Bo Bichette",
          "Christian Yelich",
          "Francisco Lindor",
          "Dansby Swanson",
          "Luis Arraez",
          "Will Smith",
          "Ha-seong Kim",
          "Randy Arozarena",
          "Paul Goldschmidt",
          "Matt Chapman",
          "Isaac Paredes",
          "Brandon Nimmo",
          "Jeimer Candelario",
          "Thairo Estrada",
          "Matt Olson",
          "Christian Walker",
          "Jack Suwinski",
          "Julio Rodriguez",
          "Yandy Diaz",
          "Kyle Tucker",
          "Josh Jung",
          "Ketel Marte",
          "Ozzie Albies",
          "William Contreras",
          "Xander Bogaerts",
          "Leody Taveras",
          "Adley Rutschman",
          "Nico Hoerner",
          "Lane Thomas",
          "Bobby Witt Jr.",
          "LaMonte Wade Jr.",
          "Austin Hays",
          "J.D. Davis",
          "Gunnar Henderson",
          "Alex Verdugo",
          "Nathaniel Lowe",
          "Jorge Soler",
          "Nolan Arenado",
          "Rafael Devers",
          "Austin Riley",
          "Brendan Donovan",
          "Bryson Stott",
          "Brandon Drury",
          "Brandon Marsh",
          "Ian Happ",
          "J.P. Crawford",
          "Alex Bregman",
          "Andres Gimenez",
          "Cal Raleigh",
          "Spencer Steer",
          "Nolan Gorman",
          "Ryan Noda",
          "Cedric Mullins II",
          "James Outman",
          "Nick Castellanos",
          "Pete Alonso",
          "Anthony Santander",
          "Ryan McMahon",
          "Zach McKinstry",
          "Trea Turner",
          "Anthony Volpe",
          "Masataka Yoshida",
          "Justin Turner",
          "Bryan Reynolds",
          "Manny Machado",
          "Whit Merrifield",
          "Jeremy Pena",
          "Josh Naylor",
          "Anthony Rizzo",
          "Jonathan India",
          "Jarred Kelenic",
          "George Springer",
          "Eugenio Suarez",
          "Joey Wiemer",
          "Andrew McCutchen",
          "Lourdes Gurriel Jr.",
          "Max Muncy",
          "Hunter Renfroe",
          "Mauricio Dubon",
          "Steven Kwan",
          "Tommy Edman",
          "Brent Rooker",
          "J.T. Realmuto",
          "Teoscar Hernandez",
          "Ezequiel Tovar",
          "Willson Contreras",
          "Carlos Correa",
          "Ke'Bryan Hayes",
          "Willy Adames",
          "Gleyber Torres",
          "Esteury Ruiz",
          "Marcell Ozuna",
          "Byron Buxton",
          "Andrew Benintendi",
          "Daulton Varsho",
          "J.D. Martinez",
          "Elias Diaz",
          "Ty France",
          "Taylor Ward",
          "Jeff McNeil",
          "Eddie Rosario",
          "Seiya Suzuki",
          "Carlos Santana",
          "Trent Grisham",
          "Vladimir Guerrero Jr.",
          "Michael Conforto",
          "Brian Anderson",
          "Jace Peterson",
          "Javier Baez",
          "Andrew Vaughn",
          "Alec Bohm",
          "Bryan De La Cruz",
          "Jake Cronenworth",
          "Salvador Perez",
          "CJ Abrams",
          "Spencer Torkelson",
          "Adam Frazier",
          "Miguel Vargas",
          "Amed Rosario",
          "Starling Marte",
          "Luis Garcia",
          "DJ LeMahieu",
          "Tyler Stephenson",
          "Kyle Schwarber",
          "Triston Casas",
          "Dominic Smith",
          "Shea Langeliers",
          "Josh Bell",
          "Myles Straw",
          "Joey Meneses",
          "Jose Abreu",
          "MJ Melendez",
          "Tim Anderson",
          "Rowdy Tellez",
          "Jurickson Profar",
          "Keibert Ruiz",
          "Enrique Hernandez"
         ],
         "legendgroup": "",
         "marker": {
          "color": "#7284cc"
         },
         "name": "",
         "notched": false,
         "offsetgroup": "",
         "orientation": "v",
         "showlegend": false,
         "type": "box",
         "x0": " ",
         "xaxis": "x",
         "y": [
          0.267,
          0.3329999999999999,
          0.1939999999999999,
          0.293,
          0.292,
          0.412,
          0.281,
          0.183,
          0.348,
          0.305,
          0.316,
          0.2269999999999999,
          0.363,
          0.26,
          0.396,
          0.258,
          0.296,
          0.265,
          0.344,
          0.233,
          0.22,
          0.272,
          0.285,
          0.241,
          0.305,
          0.254,
          0.3229999999999999,
          0.409,
          0.318,
          0.3,
          0.19,
          0.3989999999999999,
          0.231,
          0.276,
          0.347,
          0.273,
          0.391,
          0.2739999999999999,
          0.2739999999999999,
          0.309,
          0.259,
          0.351,
          0.3,
          0.354,
          0.19,
          0.33,
          0.286,
          0.252,
          0.244,
          0.271,
          0.288,
          0.367,
          0.366,
          0.303,
          0.268,
          0.326,
          0.379,
          0.282,
          0.261,
          0.223,
          0.2269999999999999,
          0.414,
          0.336,
          0.252,
          0.286,
          0.212,
          0.259,
          0.285,
          0.416,
          0.296,
          0.389,
          0.283,
          0.289,
          0.406,
          0.326,
          0.271,
          0.282,
          0.278,
          0.347,
          0.35,
          0.387,
          0.422,
          0.35,
          0.233,
          0.315,
          0.271,
          0.263,
          0.3279999999999999,
          0.2189999999999999,
          0.319,
          0.246,
          0.3929999999999999,
          0.4479999999999999,
          0.233,
          0.317,
          0.312,
          0.345,
          0.384,
          0.418,
          0.354,
          0.308,
          0.34,
          0.356,
          0.292,
          0.364,
          0.318,
          0.321,
          0.312,
          0.327,
          0.3779999999999999,
          0.373,
          0.402,
          0.281,
          0.321,
          0.447,
          0.223,
          0.286,
          0.273,
          0.34,
          0.289,
          0.307,
          0.253,
          0.48,
          0.318,
          0.3429999999999999,
          0.35,
          0.288,
          0.482,
          0.407,
          0.273,
          0.3339999999999999,
          0.244,
          0.42,
          0.38,
          0.3389999999999999,
          0.281,
          0.28,
          0.263,
          0.2769999999999999,
          0.345,
          0.379,
          0.31,
          0.2689999999999999,
          0.3429999999999999,
          0.3879999999999999,
          0.314,
          0.373,
          0.278,
          0.283,
          0.371,
          0.292
         ],
         "y0": " ",
         "yaxis": "y"
        }
       ],
       "layout": {
        "boxmode": "group",
        "height": 500,
        "legend": {
         "tracegroupgap": 0
        },
        "margin": {
         "t": 60
        },
        "template": {
         "data": {
          "candlestick": [
           {
            "decreasing": {
             "line": {
              "color": "#000033"
             }
            },
            "increasing": {
             "line": {
              "color": "#000032"
             }
            },
            "type": "candlestick"
           }
          ],
          "contour": [
           {
            "colorscale": [
             [
              0,
              "#000011"
             ],
             [
              0.1111111111111111,
              "#000012"
             ],
             [
              0.2222222222222222,
              "#000013"
             ],
             [
              0.3333333333333333,
              "#000014"
             ],
             [
              0.4444444444444444,
              "#000015"
             ],
             [
              0.5555555555555556,
              "#000016"
             ],
             [
              0.6666666666666666,
              "#000017"
             ],
             [
              0.7777777777777778,
              "#000018"
             ],
             [
              0.8888888888888888,
              "#000019"
             ],
             [
              1,
              "#000020"
             ]
            ],
            "type": "contour"
           }
          ],
          "contourcarpet": [
           {
            "colorscale": [
             [
              0,
              "#000011"
             ],
             [
              0.1111111111111111,
              "#000012"
             ],
             [
              0.2222222222222222,
              "#000013"
             ],
             [
              0.3333333333333333,
              "#000014"
             ],
             [
              0.4444444444444444,
              "#000015"
             ],
             [
              0.5555555555555556,
              "#000016"
             ],
             [
              0.6666666666666666,
              "#000017"
             ],
             [
              0.7777777777777778,
              "#000018"
             ],
             [
              0.8888888888888888,
              "#000019"
             ],
             [
              1,
              "#000020"
             ]
            ],
            "type": "contourcarpet"
           }
          ],
          "heatmap": [
           {
            "colorscale": [
             [
              0,
              "#000011"
             ],
             [
              0.1111111111111111,
              "#000012"
             ],
             [
              0.2222222222222222,
              "#000013"
             ],
             [
              0.3333333333333333,
              "#000014"
             ],
             [
              0.4444444444444444,
              "#000015"
             ],
             [
              0.5555555555555556,
              "#000016"
             ],
             [
              0.6666666666666666,
              "#000017"
             ],
             [
              0.7777777777777778,
              "#000018"
             ],
             [
              0.8888888888888888,
              "#000019"
             ],
             [
              1,
              "#000020"
             ]
            ],
            "type": "heatmap"
           }
          ],
          "histogram2d": [
           {
            "colorscale": [
             [
              0,
              "#000011"
             ],
             [
              0.1111111111111111,
              "#000012"
             ],
             [
              0.2222222222222222,
              "#000013"
             ],
             [
              0.3333333333333333,
              "#000014"
             ],
             [
              0.4444444444444444,
              "#000015"
             ],
             [
              0.5555555555555556,
              "#000016"
             ],
             [
              0.6666666666666666,
              "#000017"
             ],
             [
              0.7777777777777778,
              "#000018"
             ],
             [
              0.8888888888888888,
              "#000019"
             ],
             [
              1,
              "#000020"
             ]
            ],
            "type": "histogram2d"
           }
          ],
          "icicle": [
           {
            "textfont": {
             "color": "white"
            },
            "type": "icicle"
           }
          ],
          "sankey": [
           {
            "textfont": {
             "color": "#000036"
            },
            "type": "sankey"
           }
          ],
          "scatter": [
           {
            "marker": {
             "line": {
              "width": 0
             }
            },
            "type": "scatter"
           }
          ],
          "table": [
           {
            "cells": {
             "fill": {
              "color": "#000038"
             },
             "font": {
              "color": "#000037"
             },
             "line": {
              "color": "#000039"
             }
            },
            "header": {
             "fill": {
              "color": "#000040"
             },
             "font": {
              "color": "#000036"
             },
             "line": {
              "color": "#000039"
             }
            },
            "type": "table"
           }
          ],
          "waterfall": [
           {
            "connector": {
             "line": {
              "color": "#000036",
              "width": 2
             }
            },
            "decreasing": {
             "marker": {
              "color": "#000033"
             }
            },
            "increasing": {
             "marker": {
              "color": "#000032"
             }
            },
            "totals": {
             "marker": {
              "color": "#000034"
             }
            },
            "type": "waterfall"
           }
          ]
         },
         "layout": {
          "coloraxis": {
           "colorscale": [
            [
             0,
             "#000011"
            ],
            [
             0.1111111111111111,
             "#000012"
            ],
            [
             0.2222222222222222,
             "#000013"
            ],
            [
             0.3333333333333333,
             "#000014"
            ],
            [
             0.4444444444444444,
             "#000015"
            ],
            [
             0.5555555555555556,
             "#000016"
            ],
            [
             0.6666666666666666,
             "#000017"
            ],
            [
             0.7777777777777778,
             "#000018"
            ],
            [
             0.8888888888888888,
             "#000019"
            ],
            [
             1,
             "#000020"
            ]
           ]
          },
          "colorscale": {
           "diverging": [
            [
             0,
             "#000021"
            ],
            [
             0.1,
             "#000022"
            ],
            [
             0.2,
             "#000023"
            ],
            [
             0.3,
             "#000024"
            ],
            [
             0.4,
             "#000025"
            ],
            [
             0.5,
             "#000026"
            ],
            [
             0.6,
             "#000027"
            ],
            [
             0.7,
             "#000028"
            ],
            [
             0.8,
             "#000029"
            ],
            [
             0.9,
             "#000030"
            ],
            [
             1,
             "#000031"
            ]
           ],
           "sequential": [
            [
             0,
             "#000011"
            ],
            [
             0.1111111111111111,
             "#000012"
            ],
            [
             0.2222222222222222,
             "#000013"
            ],
            [
             0.3333333333333333,
             "#000014"
            ],
            [
             0.4444444444444444,
             "#000015"
            ],
            [
             0.5555555555555556,
             "#000016"
            ],
            [
             0.6666666666666666,
             "#000017"
            ],
            [
             0.7777777777777778,
             "#000018"
            ],
            [
             0.8888888888888888,
             "#000019"
            ],
            [
             1,
             "#000020"
            ]
           ],
           "sequentialminus": [
            [
             0,
             "#000011"
            ],
            [
             0.1111111111111111,
             "#000012"
            ],
            [
             0.2222222222222222,
             "#000013"
            ],
            [
             0.3333333333333333,
             "#000014"
            ],
            [
             0.4444444444444444,
             "#000015"
            ],
            [
             0.5555555555555556,
             "#000016"
            ],
            [
             0.6666666666666666,
             "#000017"
            ],
            [
             0.7777777777777778,
             "#000018"
            ],
            [
             0.8888888888888888,
             "#000019"
            ],
            [
             1,
             "#000020"
            ]
           ]
          },
          "colorway": [
           "#000001",
           "#000002",
           "#000003",
           "#000004",
           "#000005",
           "#000006",
           "#000007",
           "#000008",
           "#000009",
           "#000010"
          ]
         }
        },
        "title": {
         "automargin": true,
         "font": {
          "color": "#164f5e",
          "size": 22
         },
         "text": "Out-Zone Swing%",
         "yref": "paper"
        },
        "width": 500,
        "xaxis": {
         "anchor": "y",
         "domain": [
          0,
          1
         ],
         "title": {
          "text": ""
         }
        },
        "yaxis": {
         "anchor": "x",
         "domain": [
          0,
          1
         ],
         "title": {
          "text": ""
         }
        }
       }
      },
      "text/html": [
       "<div>                            <div id=\"4343deab-c5c4-467a-a799-93e721d455e0\" class=\"plotly-graph-div\" style=\"height:500px; width:500px;\"></div>            <script type=\"text/javascript\">                require([\"plotly\"], function(Plotly) {                    window.PLOTLYENV=window.PLOTLYENV || {};                                    if (document.getElementById(\"4343deab-c5c4-467a-a799-93e721d455e0\")) {                    Plotly.newPlot(                        \"4343deab-c5c4-467a-a799-93e721d455e0\",                        [{\"alignmentgroup\":\"True\",\"boxpoints\":\"all\",\"hovertemplate\":\"\\u003cb\\u003e%{hovertext}\\u003c\\u002fb\\u003e\\u003cbr\\u003e\\u003cbr\\u003eO-Swing%=%{y}\\u003cextra\\u003e\\u003c\\u002fextra\\u003e\",\"hovertext\":[\"Ronald Acuna Jr.\",\"Shohei Ohtani\",\"Mookie Betts\",\"Wander Franco\",\"Corbin Carroll\",\"Luis Robert\",\"Freddie Freeman\",\"Juan Soto\",\"Fernando Tatis Jr.\",\"Jose Ramirez\",\"Adolis Garcia\",\"Mike Trout\",\"Jonah Heim\",\"Marcus Semien\",\"Bo Bichette\",\"Christian Yelich\",\"Francisco Lindor\",\"Dansby Swanson\",\"Luis Arraez\",\"Will Smith\",\"Ha-seong Kim\",\"Randy Arozarena\",\"Paul Goldschmidt\",\"Matt Chapman\",\"Isaac Paredes\",\"Brandon Nimmo\",\"Jeimer Candelario\",\"Thairo Estrada\",\"Matt Olson\",\"Christian Walker\",\"Jack Suwinski\",\"Julio Rodriguez\",\"Yandy Diaz\",\"Kyle Tucker\",\"Josh Jung\",\"Ketel Marte\",\"Ozzie Albies\",\"William Contreras\",\"Xander Bogaerts\",\"Leody Taveras\",\"Adley Rutschman\",\"Nico Hoerner\",\"Lane Thomas\",\"Bobby Witt Jr.\",\"LaMonte Wade Jr.\",\"Austin Hays\",\"J.D. Davis\",\"Gunnar Henderson\",\"Alex Verdugo\",\"Nathaniel Lowe\",\"Jorge Soler\",\"Nolan Arenado\",\"Rafael Devers\",\"Austin Riley\",\"Brendan Donovan\",\"Bryson Stott\",\"Brandon Drury\",\"Brandon Marsh\",\"Ian Happ\",\"J.P. Crawford\",\"Alex Bregman\",\"Andres Gimenez\",\"Cal Raleigh\",\"Spencer Steer\",\"Nolan Gorman\",\"Ryan Noda\",\"Cedric Mullins II\",\"James Outman\",\"Nick Castellanos\",\"Pete Alonso\",\"Anthony Santander\",\"Ryan McMahon\",\"Zach McKinstry\",\"Trea Turner\",\"Anthony Volpe\",\"Masataka Yoshida\",\"Justin Turner\",\"Bryan Reynolds\",\"Manny Machado\",\"Whit Merrifield\",\"Jeremy Pena\",\"Josh Naylor\",\"Anthony Rizzo\",\"Jonathan India\",\"Jarred Kelenic\",\"George Springer\",\"Eugenio Suarez\",\"Joey Wiemer\",\"Andrew McCutchen\",\"Lourdes Gurriel Jr.\",\"Max Muncy\",\"Hunter Renfroe\",\"Mauricio Dubon\",\"Steven Kwan\",\"Tommy Edman\",\"Brent Rooker\",\"J.T. Realmuto\",\"Teoscar Hernandez\",\"Ezequiel Tovar\",\"Willson Contreras\",\"Carlos Correa\",\"Ke'Bryan Hayes\",\"Willy Adames\",\"Gleyber Torres\",\"Esteury Ruiz\",\"Marcell Ozuna\",\"Byron Buxton\",\"Andrew Benintendi\",\"Daulton Varsho\",\"J.D. Martinez\",\"Elias Diaz\",\"Ty France\",\"Taylor Ward\",\"Jeff McNeil\",\"Eddie Rosario\",\"Seiya Suzuki\",\"Carlos Santana\",\"Trent Grisham\",\"Vladimir Guerrero Jr.\",\"Michael Conforto\",\"Brian Anderson\",\"Jace Peterson\",\"Javier Baez\",\"Andrew Vaughn\",\"Alec Bohm\",\"Bryan De La Cruz\",\"Jake Cronenworth\",\"Salvador Perez\",\"CJ Abrams\",\"Spencer Torkelson\",\"Adam Frazier\",\"Miguel Vargas\",\"Amed Rosario\",\"Starling Marte\",\"Luis Garcia\",\"DJ LeMahieu\",\"Tyler Stephenson\",\"Kyle Schwarber\",\"Triston Casas\",\"Dominic Smith\",\"Shea Langeliers\",\"Josh Bell\",\"Myles Straw\",\"Joey Meneses\",\"Jose Abreu\",\"MJ Melendez\",\"Tim Anderson\",\"Rowdy Tellez\",\"Jurickson Profar\",\"Keibert Ruiz\",\"Enrique Hernandez\"],\"legendgroup\":\"\",\"marker\":{\"color\":\"#7284cc\"},\"name\":\"\",\"notched\":false,\"offsetgroup\":\"\",\"orientation\":\"v\",\"showlegend\":false,\"x0\":\" \",\"xaxis\":\"x\",\"y\":[0.267,0.3329999999999999,0.1939999999999999,0.293,0.292,0.412,0.281,0.183,0.348,0.305,0.316,0.2269999999999999,0.363,0.26,0.396,0.258,0.296,0.265,0.344,0.233,0.22,0.272,0.285,0.241,0.305,0.254,0.3229999999999999,0.409,0.318,0.3,0.19,0.3989999999999999,0.231,0.276,0.347,0.273,0.391,0.2739999999999999,0.2739999999999999,0.309,0.259,0.351,0.3,0.354,0.19,0.33,0.286,0.252,0.244,0.271,0.288,0.367,0.366,0.303,0.268,0.326,0.379,0.282,0.261,0.223,0.2269999999999999,0.414,0.336,0.252,0.286,0.212,0.259,0.285,0.416,0.296,0.389,0.283,0.289,0.406,0.326,0.271,0.282,0.278,0.347,0.35,0.387,0.422,0.35,0.233,0.315,0.271,0.263,0.3279999999999999,0.2189999999999999,0.319,0.246,0.3929999999999999,0.4479999999999999,0.233,0.317,0.312,0.345,0.384,0.418,0.354,0.308,0.34,0.356,0.292,0.364,0.318,0.321,0.312,0.327,0.3779999999999999,0.373,0.402,0.281,0.321,0.447,0.223,0.286,0.273,0.34,0.289,0.307,0.253,0.48,0.318,0.3429999999999999,0.35,0.288,0.482,0.407,0.273,0.3339999999999999,0.244,0.42,0.38,0.3389999999999999,0.281,0.28,0.263,0.2769999999999999,0.345,0.379,0.31,0.2689999999999999,0.3429999999999999,0.3879999999999999,0.314,0.373,0.278,0.283,0.371,0.292],\"y0\":\" \",\"yaxis\":\"y\",\"type\":\"box\"}],                        {\"template\":{\"data\":{\"candlestick\":[{\"decreasing\":{\"line\":{\"color\":\"#000033\"}},\"increasing\":{\"line\":{\"color\":\"#000032\"}},\"type\":\"candlestick\"}],\"contourcarpet\":[{\"colorscale\":[[0.0,\"#000011\"],[0.1111111111111111,\"#000012\"],[0.2222222222222222,\"#000013\"],[0.3333333333333333,\"#000014\"],[0.4444444444444444,\"#000015\"],[0.5555555555555556,\"#000016\"],[0.6666666666666666,\"#000017\"],[0.7777777777777778,\"#000018\"],[0.8888888888888888,\"#000019\"],[1.0,\"#000020\"]],\"type\":\"contourcarpet\"}],\"contour\":[{\"colorscale\":[[0.0,\"#000011\"],[0.1111111111111111,\"#000012\"],[0.2222222222222222,\"#000013\"],[0.3333333333333333,\"#000014\"],[0.4444444444444444,\"#000015\"],[0.5555555555555556,\"#000016\"],[0.6666666666666666,\"#000017\"],[0.7777777777777778,\"#000018\"],[0.8888888888888888,\"#000019\"],[1.0,\"#000020\"]],\"type\":\"contour\"}],\"heatmap\":[{\"colorscale\":[[0.0,\"#000011\"],[0.1111111111111111,\"#000012\"],[0.2222222222222222,\"#000013\"],[0.3333333333333333,\"#000014\"],[0.4444444444444444,\"#000015\"],[0.5555555555555556,\"#000016\"],[0.6666666666666666,\"#000017\"],[0.7777777777777778,\"#000018\"],[0.8888888888888888,\"#000019\"],[1.0,\"#000020\"]],\"type\":\"heatmap\"}],\"histogram2d\":[{\"colorscale\":[[0.0,\"#000011\"],[0.1111111111111111,\"#000012\"],[0.2222222222222222,\"#000013\"],[0.3333333333333333,\"#000014\"],[0.4444444444444444,\"#000015\"],[0.5555555555555556,\"#000016\"],[0.6666666666666666,\"#000017\"],[0.7777777777777778,\"#000018\"],[0.8888888888888888,\"#000019\"],[1.0,\"#000020\"]],\"type\":\"histogram2d\"}],\"icicle\":[{\"textfont\":{\"color\":\"white\"},\"type\":\"icicle\"}],\"sankey\":[{\"textfont\":{\"color\":\"#000036\"},\"type\":\"sankey\"}],\"scatter\":[{\"marker\":{\"line\":{\"width\":0}},\"type\":\"scatter\"}],\"table\":[{\"cells\":{\"fill\":{\"color\":\"#000038\"},\"font\":{\"color\":\"#000037\"},\"line\":{\"color\":\"#000039\"}},\"header\":{\"fill\":{\"color\":\"#000040\"},\"font\":{\"color\":\"#000036\"},\"line\":{\"color\":\"#000039\"}},\"type\":\"table\"}],\"waterfall\":[{\"connector\":{\"line\":{\"color\":\"#000036\",\"width\":2}},\"decreasing\":{\"marker\":{\"color\":\"#000033\"}},\"increasing\":{\"marker\":{\"color\":\"#000032\"}},\"totals\":{\"marker\":{\"color\":\"#000034\"}},\"type\":\"waterfall\"}]},\"layout\":{\"coloraxis\":{\"colorscale\":[[0.0,\"#000011\"],[0.1111111111111111,\"#000012\"],[0.2222222222222222,\"#000013\"],[0.3333333333333333,\"#000014\"],[0.4444444444444444,\"#000015\"],[0.5555555555555556,\"#000016\"],[0.6666666666666666,\"#000017\"],[0.7777777777777778,\"#000018\"],[0.8888888888888888,\"#000019\"],[1.0,\"#000020\"]]},\"colorscale\":{\"diverging\":[[0.0,\"#000021\"],[0.1,\"#000022\"],[0.2,\"#000023\"],[0.3,\"#000024\"],[0.4,\"#000025\"],[0.5,\"#000026\"],[0.6,\"#000027\"],[0.7,\"#000028\"],[0.8,\"#000029\"],[0.9,\"#000030\"],[1.0,\"#000031\"]],\"sequential\":[[0.0,\"#000011\"],[0.1111111111111111,\"#000012\"],[0.2222222222222222,\"#000013\"],[0.3333333333333333,\"#000014\"],[0.4444444444444444,\"#000015\"],[0.5555555555555556,\"#000016\"],[0.6666666666666666,\"#000017\"],[0.7777777777777778,\"#000018\"],[0.8888888888888888,\"#000019\"],[1.0,\"#000020\"]],\"sequentialminus\":[[0.0,\"#000011\"],[0.1111111111111111,\"#000012\"],[0.2222222222222222,\"#000013\"],[0.3333333333333333,\"#000014\"],[0.4444444444444444,\"#000015\"],[0.5555555555555556,\"#000016\"],[0.6666666666666666,\"#000017\"],[0.7777777777777778,\"#000018\"],[0.8888888888888888,\"#000019\"],[1.0,\"#000020\"]]},\"colorway\":[\"#000001\",\"#000002\",\"#000003\",\"#000004\",\"#000005\",\"#000006\",\"#000007\",\"#000008\",\"#000009\",\"#000010\"]}},\"xaxis\":{\"anchor\":\"y\",\"domain\":[0.0,1.0],\"title\":{\"text\":\"\"}},\"yaxis\":{\"anchor\":\"x\",\"domain\":[0.0,1.0],\"title\":{\"text\":\"\"}},\"legend\":{\"tracegroupgap\":0},\"margin\":{\"t\":60},\"boxmode\":\"group\",\"height\":500,\"width\":500,\"title\":{\"font\":{\"size\":22,\"color\":\"#164f5e\"},\"text\":\"Out-Zone Swing%\",\"automargin\":true,\"yref\":\"paper\"}},                        {\"responsive\": true}                    ).then(function(){\n",
       "                            \n",
       "var gd = document.getElementById('4343deab-c5c4-467a-a799-93e721d455e0');\n",
       "var x = new MutationObserver(function (mutations, observer) {{\n",
       "        var display = window.getComputedStyle(gd).display;\n",
       "        if (!display || display === 'none') {{\n",
       "            console.log([gd, 'removed!']);\n",
       "            Plotly.purge(gd);\n",
       "            observer.disconnect();\n",
       "        }}\n",
       "}});\n",
       "\n",
       "// Listen for the removal of the full notebook cells\n",
       "var notebookContainer = gd.closest('#notebook-container');\n",
       "if (notebookContainer) {{\n",
       "    x.observe(notebookContainer, {childList: true});\n",
       "}}\n",
       "\n",
       "// Listen for the clearing of the current output cell\n",
       "var outputEl = gd.closest('.output');\n",
       "if (outputEl) {{\n",
       "    x.observe(outputEl, {childList: true});\n",
       "}}\n",
       "\n",
       "                        })                };                });            </script>        </div>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "fig_43 = px.box(\n",
    "    df.query(\"Season==2023\"),\n",
    "    y = \"O-Swing%\",\n",
    "    points=\"all\",\n",
    "    hover_name = \"Name\",\n",
    "    height = 500,\n",
    "    width = 500,\n",
    ")\n",
    "\n",
    "fig_43.update_traces(marker=dict(color=\"#7284cc\"))\n",
    "\n",
    "fig_43.update_layout(\n",
    "    title=dict(text=\"Out-Zone Swing%\", font=dict(size=22), automargin=True, yref='paper'),\n",
    "    title_font_color=\"#164f5e\",\n",
    "    yaxis=dict(title=\"\"),\n",
    "    xaxis=dict(title=\"\")\n",
    ")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "79df56a9",
   "metadata": {},
   "source": [
    "### Row 1 - Tab 5"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 99,
   "id": "0a2e39c8",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "application/vnd.plotly.v1+json": {
       "config": {
        "plotlyServerURL": "https://plot.ly"
       },
       "data": [
        {
         "alignmentgroup": "True",
         "boxpoints": "all",
         "hovertemplate": "<b>%{hovertext}</b><br><br>Pull%+=%{y}<extra></extra>",
         "hovertext": [
          "Ronald Acuna Jr.",
          "Shohei Ohtani",
          "Mookie Betts",
          "Wander Franco",
          "Corbin Carroll",
          "Luis Robert",
          "Freddie Freeman",
          "Juan Soto",
          "Fernando Tatis Jr.",
          "Jose Ramirez",
          "Adolis Garcia",
          "Mike Trout",
          "Jonah Heim",
          "Marcus Semien",
          "Bo Bichette",
          "Christian Yelich",
          "Francisco Lindor",
          "Dansby Swanson",
          "Luis Arraez",
          "Will Smith",
          "Ha-seong Kim",
          "Randy Arozarena",
          "Paul Goldschmidt",
          "Matt Chapman",
          "Isaac Paredes",
          "Brandon Nimmo",
          "Jeimer Candelario",
          "Thairo Estrada",
          "Matt Olson",
          "Christian Walker",
          "Jack Suwinski",
          "Julio Rodriguez",
          "Yandy Diaz",
          "Kyle Tucker",
          "Josh Jung",
          "Ketel Marte",
          "Ozzie Albies",
          "William Contreras",
          "Xander Bogaerts",
          "Leody Taveras",
          "Adley Rutschman",
          "Nico Hoerner",
          "Lane Thomas",
          "Bobby Witt Jr.",
          "LaMonte Wade Jr.",
          "Austin Hays",
          "J.D. Davis",
          "Gunnar Henderson",
          "Alex Verdugo",
          "Nathaniel Lowe",
          "Jorge Soler",
          "Nolan Arenado",
          "Rafael Devers",
          "Austin Riley",
          "Brendan Donovan",
          "Bryson Stott",
          "Brandon Drury",
          "Brandon Marsh",
          "Ian Happ",
          "J.P. Crawford",
          "Alex Bregman",
          "Andres Gimenez",
          "Cal Raleigh",
          "Spencer Steer",
          "Nolan Gorman",
          "Ryan Noda",
          "Cedric Mullins II",
          "James Outman",
          "Nick Castellanos",
          "Pete Alonso",
          "Anthony Santander",
          "Ryan McMahon",
          "Zach McKinstry",
          "Trea Turner",
          "Anthony Volpe",
          "Masataka Yoshida",
          "Justin Turner",
          "Bryan Reynolds",
          "Manny Machado",
          "Whit Merrifield",
          "Jeremy Pena",
          "Josh Naylor",
          "Anthony Rizzo",
          "Jonathan India",
          "Jarred Kelenic",
          "George Springer",
          "Eugenio Suarez",
          "Joey Wiemer",
          "Andrew McCutchen",
          "Lourdes Gurriel Jr.",
          "Max Muncy",
          "Hunter Renfroe",
          "Mauricio Dubon",
          "Steven Kwan",
          "Tommy Edman",
          "Brent Rooker",
          "J.T. Realmuto",
          "Teoscar Hernandez",
          "Ezequiel Tovar",
          "Willson Contreras",
          "Carlos Correa",
          "Ke'Bryan Hayes",
          "Willy Adames",
          "Gleyber Torres",
          "Esteury Ruiz",
          "Marcell Ozuna",
          "Byron Buxton",
          "Andrew Benintendi",
          "Daulton Varsho",
          "J.D. Martinez",
          "Elias Diaz",
          "Ty France",
          "Taylor Ward",
          "Jeff McNeil",
          "Eddie Rosario",
          "Seiya Suzuki",
          "Carlos Santana",
          "Trent Grisham",
          "Vladimir Guerrero Jr.",
          "Michael Conforto",
          "Brian Anderson",
          "Jace Peterson",
          "Javier Baez",
          "Andrew Vaughn",
          "Alec Bohm",
          "Bryan De La Cruz",
          "Jake Cronenworth",
          "Salvador Perez",
          "CJ Abrams",
          "Spencer Torkelson",
          "Adam Frazier",
          "Miguel Vargas",
          "Amed Rosario",
          "Starling Marte",
          "Luis Garcia",
          "DJ LeMahieu",
          "Tyler Stephenson",
          "Kyle Schwarber",
          "Triston Casas",
          "Dominic Smith",
          "Shea Langeliers",
          "Josh Bell",
          "Myles Straw",
          "Joey Meneses",
          "Jose Abreu",
          "MJ Melendez",
          "Tim Anderson",
          "Rowdy Tellez",
          "Jurickson Profar",
          "Keibert Ruiz",
          "Enrique Hernandez"
         ],
         "legendgroup": "",
         "marker": {
          "color": "#7284cc"
         },
         "name": "",
         "notched": false,
         "offsetgroup": "",
         "orientation": "v",
         "showlegend": false,
         "type": "box",
         "x0": " ",
         "xaxis": "x",
         "y": [
          112,
          97,
          117,
          102,
          107,
          103,
          91,
          105,
          107,
          128,
          94,
          107,
          123,
          122,
          56,
          83,
          115,
          110,
          69,
          89,
          113,
          101,
          80,
          93,
          131,
          88,
          108,
          112,
          93,
          100,
          110,
          93,
          76,
          107,
          94,
          98,
          133,
          85,
          86,
          70,
          89,
          73,
          123,
          87,
          104,
          93,
          104,
          97,
          87,
          71,
          111,
          111,
          100,
          105,
          100,
          84,
          106,
          91,
          97,
          98,
          111,
          109,
          114,
          98,
          114,
          112,
          115,
          117,
          109,
          100,
          121,
          81,
          84,
          95,
          106,
          88,
          98,
          96,
          95,
          81,
          119,
          93,
          107,
          106,
          105,
          95,
          102,
          109,
          123,
          102,
          128,
          128,
          79,
          68,
          107,
          93,
          107,
          89,
          75,
          89,
          103,
          68,
          125,
          80,
          92,
          108,
          130,
          84,
          127,
          103,
          113,
          107,
          95,
          102,
          116,
          97,
          112,
          107,
          96,
          92,
          77,
          84,
          94,
          94,
          67,
          98,
          95,
          103,
          91,
          115,
          93,
          93,
          85,
          89,
          81,
          82,
          97,
          135,
          111,
          96,
          122,
          112,
          57,
          92,
          80,
          108,
          82,
          94,
          118,
          100,
          96
         ],
         "y0": " ",
         "yaxis": "y"
        }
       ],
       "layout": {
        "boxmode": "group",
        "height": 500,
        "legend": {
         "tracegroupgap": 0
        },
        "margin": {
         "t": 60
        },
        "template": {
         "data": {
          "candlestick": [
           {
            "decreasing": {
             "line": {
              "color": "#000033"
             }
            },
            "increasing": {
             "line": {
              "color": "#000032"
             }
            },
            "type": "candlestick"
           }
          ],
          "contour": [
           {
            "colorscale": [
             [
              0,
              "#000011"
             ],
             [
              0.1111111111111111,
              "#000012"
             ],
             [
              0.2222222222222222,
              "#000013"
             ],
             [
              0.3333333333333333,
              "#000014"
             ],
             [
              0.4444444444444444,
              "#000015"
             ],
             [
              0.5555555555555556,
              "#000016"
             ],
             [
              0.6666666666666666,
              "#000017"
             ],
             [
              0.7777777777777778,
              "#000018"
             ],
             [
              0.8888888888888888,
              "#000019"
             ],
             [
              1,
              "#000020"
             ]
            ],
            "type": "contour"
           }
          ],
          "contourcarpet": [
           {
            "colorscale": [
             [
              0,
              "#000011"
             ],
             [
              0.1111111111111111,
              "#000012"
             ],
             [
              0.2222222222222222,
              "#000013"
             ],
             [
              0.3333333333333333,
              "#000014"
             ],
             [
              0.4444444444444444,
              "#000015"
             ],
             [
              0.5555555555555556,
              "#000016"
             ],
             [
              0.6666666666666666,
              "#000017"
             ],
             [
              0.7777777777777778,
              "#000018"
             ],
             [
              0.8888888888888888,
              "#000019"
             ],
             [
              1,
              "#000020"
             ]
            ],
            "type": "contourcarpet"
           }
          ],
          "heatmap": [
           {
            "colorscale": [
             [
              0,
              "#000011"
             ],
             [
              0.1111111111111111,
              "#000012"
             ],
             [
              0.2222222222222222,
              "#000013"
             ],
             [
              0.3333333333333333,
              "#000014"
             ],
             [
              0.4444444444444444,
              "#000015"
             ],
             [
              0.5555555555555556,
              "#000016"
             ],
             [
              0.6666666666666666,
              "#000017"
             ],
             [
              0.7777777777777778,
              "#000018"
             ],
             [
              0.8888888888888888,
              "#000019"
             ],
             [
              1,
              "#000020"
             ]
            ],
            "type": "heatmap"
           }
          ],
          "histogram2d": [
           {
            "colorscale": [
             [
              0,
              "#000011"
             ],
             [
              0.1111111111111111,
              "#000012"
             ],
             [
              0.2222222222222222,
              "#000013"
             ],
             [
              0.3333333333333333,
              "#000014"
             ],
             [
              0.4444444444444444,
              "#000015"
             ],
             [
              0.5555555555555556,
              "#000016"
             ],
             [
              0.6666666666666666,
              "#000017"
             ],
             [
              0.7777777777777778,
              "#000018"
             ],
             [
              0.8888888888888888,
              "#000019"
             ],
             [
              1,
              "#000020"
             ]
            ],
            "type": "histogram2d"
           }
          ],
          "icicle": [
           {
            "textfont": {
             "color": "white"
            },
            "type": "icicle"
           }
          ],
          "sankey": [
           {
            "textfont": {
             "color": "#000036"
            },
            "type": "sankey"
           }
          ],
          "scatter": [
           {
            "marker": {
             "line": {
              "width": 0
             }
            },
            "type": "scatter"
           }
          ],
          "table": [
           {
            "cells": {
             "fill": {
              "color": "#000038"
             },
             "font": {
              "color": "#000037"
             },
             "line": {
              "color": "#000039"
             }
            },
            "header": {
             "fill": {
              "color": "#000040"
             },
             "font": {
              "color": "#000036"
             },
             "line": {
              "color": "#000039"
             }
            },
            "type": "table"
           }
          ],
          "waterfall": [
           {
            "connector": {
             "line": {
              "color": "#000036",
              "width": 2
             }
            },
            "decreasing": {
             "marker": {
              "color": "#000033"
             }
            },
            "increasing": {
             "marker": {
              "color": "#000032"
             }
            },
            "totals": {
             "marker": {
              "color": "#000034"
             }
            },
            "type": "waterfall"
           }
          ]
         },
         "layout": {
          "coloraxis": {
           "colorscale": [
            [
             0,
             "#000011"
            ],
            [
             0.1111111111111111,
             "#000012"
            ],
            [
             0.2222222222222222,
             "#000013"
            ],
            [
             0.3333333333333333,
             "#000014"
            ],
            [
             0.4444444444444444,
             "#000015"
            ],
            [
             0.5555555555555556,
             "#000016"
            ],
            [
             0.6666666666666666,
             "#000017"
            ],
            [
             0.7777777777777778,
             "#000018"
            ],
            [
             0.8888888888888888,
             "#000019"
            ],
            [
             1,
             "#000020"
            ]
           ]
          },
          "colorscale": {
           "diverging": [
            [
             0,
             "#000021"
            ],
            [
             0.1,
             "#000022"
            ],
            [
             0.2,
             "#000023"
            ],
            [
             0.3,
             "#000024"
            ],
            [
             0.4,
             "#000025"
            ],
            [
             0.5,
             "#000026"
            ],
            [
             0.6,
             "#000027"
            ],
            [
             0.7,
             "#000028"
            ],
            [
             0.8,
             "#000029"
            ],
            [
             0.9,
             "#000030"
            ],
            [
             1,
             "#000031"
            ]
           ],
           "sequential": [
            [
             0,
             "#000011"
            ],
            [
             0.1111111111111111,
             "#000012"
            ],
            [
             0.2222222222222222,
             "#000013"
            ],
            [
             0.3333333333333333,
             "#000014"
            ],
            [
             0.4444444444444444,
             "#000015"
            ],
            [
             0.5555555555555556,
             "#000016"
            ],
            [
             0.6666666666666666,
             "#000017"
            ],
            [
             0.7777777777777778,
             "#000018"
            ],
            [
             0.8888888888888888,
             "#000019"
            ],
            [
             1,
             "#000020"
            ]
           ],
           "sequentialminus": [
            [
             0,
             "#000011"
            ],
            [
             0.1111111111111111,
             "#000012"
            ],
            [
             0.2222222222222222,
             "#000013"
            ],
            [
             0.3333333333333333,
             "#000014"
            ],
            [
             0.4444444444444444,
             "#000015"
            ],
            [
             0.5555555555555556,
             "#000016"
            ],
            [
             0.6666666666666666,
             "#000017"
            ],
            [
             0.7777777777777778,
             "#000018"
            ],
            [
             0.8888888888888888,
             "#000019"
            ],
            [
             1,
             "#000020"
            ]
           ]
          },
          "colorway": [
           "#000001",
           "#000002",
           "#000003",
           "#000004",
           "#000005",
           "#000006",
           "#000007",
           "#000008",
           "#000009",
           "#000010"
          ]
         }
        },
        "title": {
         "automargin": true,
         "font": {
          "color": "#164f5e",
          "size": 22
         },
         "text": "Pull%+",
         "yref": "paper"
        },
        "width": 500,
        "xaxis": {
         "anchor": "y",
         "domain": [
          0,
          1
         ],
         "title": {
          "text": ""
         }
        },
        "yaxis": {
         "anchor": "x",
         "domain": [
          0,
          1
         ],
         "title": {
          "text": ""
         }
        }
       }
      },
      "text/html": [
       "<div>                            <div id=\"79ca8d63-eec4-443d-a7f7-7265450aabef\" class=\"plotly-graph-div\" style=\"height:500px; width:500px;\"></div>            <script type=\"text/javascript\">                require([\"plotly\"], function(Plotly) {                    window.PLOTLYENV=window.PLOTLYENV || {};                                    if (document.getElementById(\"79ca8d63-eec4-443d-a7f7-7265450aabef\")) {                    Plotly.newPlot(                        \"79ca8d63-eec4-443d-a7f7-7265450aabef\",                        [{\"alignmentgroup\":\"True\",\"boxpoints\":\"all\",\"hovertemplate\":\"\\u003cb\\u003e%{hovertext}\\u003c\\u002fb\\u003e\\u003cbr\\u003e\\u003cbr\\u003ePull%+=%{y}\\u003cextra\\u003e\\u003c\\u002fextra\\u003e\",\"hovertext\":[\"Ronald Acuna Jr.\",\"Shohei Ohtani\",\"Mookie Betts\",\"Wander Franco\",\"Corbin Carroll\",\"Luis Robert\",\"Freddie Freeman\",\"Juan Soto\",\"Fernando Tatis Jr.\",\"Jose Ramirez\",\"Adolis Garcia\",\"Mike Trout\",\"Jonah Heim\",\"Marcus Semien\",\"Bo Bichette\",\"Christian Yelich\",\"Francisco Lindor\",\"Dansby Swanson\",\"Luis Arraez\",\"Will Smith\",\"Ha-seong Kim\",\"Randy Arozarena\",\"Paul Goldschmidt\",\"Matt Chapman\",\"Isaac Paredes\",\"Brandon Nimmo\",\"Jeimer Candelario\",\"Thairo Estrada\",\"Matt Olson\",\"Christian Walker\",\"Jack Suwinski\",\"Julio Rodriguez\",\"Yandy Diaz\",\"Kyle Tucker\",\"Josh Jung\",\"Ketel Marte\",\"Ozzie Albies\",\"William Contreras\",\"Xander Bogaerts\",\"Leody Taveras\",\"Adley Rutschman\",\"Nico Hoerner\",\"Lane Thomas\",\"Bobby Witt Jr.\",\"LaMonte Wade Jr.\",\"Austin Hays\",\"J.D. Davis\",\"Gunnar Henderson\",\"Alex Verdugo\",\"Nathaniel Lowe\",\"Jorge Soler\",\"Nolan Arenado\",\"Rafael Devers\",\"Austin Riley\",\"Brendan Donovan\",\"Bryson Stott\",\"Brandon Drury\",\"Brandon Marsh\",\"Ian Happ\",\"J.P. Crawford\",\"Alex Bregman\",\"Andres Gimenez\",\"Cal Raleigh\",\"Spencer Steer\",\"Nolan Gorman\",\"Ryan Noda\",\"Cedric Mullins II\",\"James Outman\",\"Nick Castellanos\",\"Pete Alonso\",\"Anthony Santander\",\"Ryan McMahon\",\"Zach McKinstry\",\"Trea Turner\",\"Anthony Volpe\",\"Masataka Yoshida\",\"Justin Turner\",\"Bryan Reynolds\",\"Manny Machado\",\"Whit Merrifield\",\"Jeremy Pena\",\"Josh Naylor\",\"Anthony Rizzo\",\"Jonathan India\",\"Jarred Kelenic\",\"George Springer\",\"Eugenio Suarez\",\"Joey Wiemer\",\"Andrew McCutchen\",\"Lourdes Gurriel Jr.\",\"Max Muncy\",\"Hunter Renfroe\",\"Mauricio Dubon\",\"Steven Kwan\",\"Tommy Edman\",\"Brent Rooker\",\"J.T. Realmuto\",\"Teoscar Hernandez\",\"Ezequiel Tovar\",\"Willson Contreras\",\"Carlos Correa\",\"Ke'Bryan Hayes\",\"Willy Adames\",\"Gleyber Torres\",\"Esteury Ruiz\",\"Marcell Ozuna\",\"Byron Buxton\",\"Andrew Benintendi\",\"Daulton Varsho\",\"J.D. Martinez\",\"Elias Diaz\",\"Ty France\",\"Taylor Ward\",\"Jeff McNeil\",\"Eddie Rosario\",\"Seiya Suzuki\",\"Carlos Santana\",\"Trent Grisham\",\"Vladimir Guerrero Jr.\",\"Michael Conforto\",\"Brian Anderson\",\"Jace Peterson\",\"Javier Baez\",\"Andrew Vaughn\",\"Alec Bohm\",\"Bryan De La Cruz\",\"Jake Cronenworth\",\"Salvador Perez\",\"CJ Abrams\",\"Spencer Torkelson\",\"Adam Frazier\",\"Miguel Vargas\",\"Amed Rosario\",\"Starling Marte\",\"Luis Garcia\",\"DJ LeMahieu\",\"Tyler Stephenson\",\"Kyle Schwarber\",\"Triston Casas\",\"Dominic Smith\",\"Shea Langeliers\",\"Josh Bell\",\"Myles Straw\",\"Joey Meneses\",\"Jose Abreu\",\"MJ Melendez\",\"Tim Anderson\",\"Rowdy Tellez\",\"Jurickson Profar\",\"Keibert Ruiz\",\"Enrique Hernandez\"],\"legendgroup\":\"\",\"marker\":{\"color\":\"#7284cc\"},\"name\":\"\",\"notched\":false,\"offsetgroup\":\"\",\"orientation\":\"v\",\"showlegend\":false,\"x0\":\" \",\"xaxis\":\"x\",\"y\":[112,97,117,102,107,103,91,105,107,128,94,107,123,122,56,83,115,110,69,89,113,101,80,93,131,88,108,112,93,100,110,93,76,107,94,98,133,85,86,70,89,73,123,87,104,93,104,97,87,71,111,111,100,105,100,84,106,91,97,98,111,109,114,98,114,112,115,117,109,100,121,81,84,95,106,88,98,96,95,81,119,93,107,106,105,95,102,109,123,102,128,128,79,68,107,93,107,89,75,89,103,68,125,80,92,108,130,84,127,103,113,107,95,102,116,97,112,107,96,92,77,84,94,94,67,98,95,103,91,115,93,93,85,89,81,82,97,135,111,96,122,112,57,92,80,108,82,94,118,100,96],\"y0\":\" \",\"yaxis\":\"y\",\"type\":\"box\"}],                        {\"template\":{\"data\":{\"candlestick\":[{\"decreasing\":{\"line\":{\"color\":\"#000033\"}},\"increasing\":{\"line\":{\"color\":\"#000032\"}},\"type\":\"candlestick\"}],\"contourcarpet\":[{\"colorscale\":[[0.0,\"#000011\"],[0.1111111111111111,\"#000012\"],[0.2222222222222222,\"#000013\"],[0.3333333333333333,\"#000014\"],[0.4444444444444444,\"#000015\"],[0.5555555555555556,\"#000016\"],[0.6666666666666666,\"#000017\"],[0.7777777777777778,\"#000018\"],[0.8888888888888888,\"#000019\"],[1.0,\"#000020\"]],\"type\":\"contourcarpet\"}],\"contour\":[{\"colorscale\":[[0.0,\"#000011\"],[0.1111111111111111,\"#000012\"],[0.2222222222222222,\"#000013\"],[0.3333333333333333,\"#000014\"],[0.4444444444444444,\"#000015\"],[0.5555555555555556,\"#000016\"],[0.6666666666666666,\"#000017\"],[0.7777777777777778,\"#000018\"],[0.8888888888888888,\"#000019\"],[1.0,\"#000020\"]],\"type\":\"contour\"}],\"heatmap\":[{\"colorscale\":[[0.0,\"#000011\"],[0.1111111111111111,\"#000012\"],[0.2222222222222222,\"#000013\"],[0.3333333333333333,\"#000014\"],[0.4444444444444444,\"#000015\"],[0.5555555555555556,\"#000016\"],[0.6666666666666666,\"#000017\"],[0.7777777777777778,\"#000018\"],[0.8888888888888888,\"#000019\"],[1.0,\"#000020\"]],\"type\":\"heatmap\"}],\"histogram2d\":[{\"colorscale\":[[0.0,\"#000011\"],[0.1111111111111111,\"#000012\"],[0.2222222222222222,\"#000013\"],[0.3333333333333333,\"#000014\"],[0.4444444444444444,\"#000015\"],[0.5555555555555556,\"#000016\"],[0.6666666666666666,\"#000017\"],[0.7777777777777778,\"#000018\"],[0.8888888888888888,\"#000019\"],[1.0,\"#000020\"]],\"type\":\"histogram2d\"}],\"icicle\":[{\"textfont\":{\"color\":\"white\"},\"type\":\"icicle\"}],\"sankey\":[{\"textfont\":{\"color\":\"#000036\"},\"type\":\"sankey\"}],\"scatter\":[{\"marker\":{\"line\":{\"width\":0}},\"type\":\"scatter\"}],\"table\":[{\"cells\":{\"fill\":{\"color\":\"#000038\"},\"font\":{\"color\":\"#000037\"},\"line\":{\"color\":\"#000039\"}},\"header\":{\"fill\":{\"color\":\"#000040\"},\"font\":{\"color\":\"#000036\"},\"line\":{\"color\":\"#000039\"}},\"type\":\"table\"}],\"waterfall\":[{\"connector\":{\"line\":{\"color\":\"#000036\",\"width\":2}},\"decreasing\":{\"marker\":{\"color\":\"#000033\"}},\"increasing\":{\"marker\":{\"color\":\"#000032\"}},\"totals\":{\"marker\":{\"color\":\"#000034\"}},\"type\":\"waterfall\"}]},\"layout\":{\"coloraxis\":{\"colorscale\":[[0.0,\"#000011\"],[0.1111111111111111,\"#000012\"],[0.2222222222222222,\"#000013\"],[0.3333333333333333,\"#000014\"],[0.4444444444444444,\"#000015\"],[0.5555555555555556,\"#000016\"],[0.6666666666666666,\"#000017\"],[0.7777777777777778,\"#000018\"],[0.8888888888888888,\"#000019\"],[1.0,\"#000020\"]]},\"colorscale\":{\"diverging\":[[0.0,\"#000021\"],[0.1,\"#000022\"],[0.2,\"#000023\"],[0.3,\"#000024\"],[0.4,\"#000025\"],[0.5,\"#000026\"],[0.6,\"#000027\"],[0.7,\"#000028\"],[0.8,\"#000029\"],[0.9,\"#000030\"],[1.0,\"#000031\"]],\"sequential\":[[0.0,\"#000011\"],[0.1111111111111111,\"#000012\"],[0.2222222222222222,\"#000013\"],[0.3333333333333333,\"#000014\"],[0.4444444444444444,\"#000015\"],[0.5555555555555556,\"#000016\"],[0.6666666666666666,\"#000017\"],[0.7777777777777778,\"#000018\"],[0.8888888888888888,\"#000019\"],[1.0,\"#000020\"]],\"sequentialminus\":[[0.0,\"#000011\"],[0.1111111111111111,\"#000012\"],[0.2222222222222222,\"#000013\"],[0.3333333333333333,\"#000014\"],[0.4444444444444444,\"#000015\"],[0.5555555555555556,\"#000016\"],[0.6666666666666666,\"#000017\"],[0.7777777777777778,\"#000018\"],[0.8888888888888888,\"#000019\"],[1.0,\"#000020\"]]},\"colorway\":[\"#000001\",\"#000002\",\"#000003\",\"#000004\",\"#000005\",\"#000006\",\"#000007\",\"#000008\",\"#000009\",\"#000010\"]}},\"xaxis\":{\"anchor\":\"y\",\"domain\":[0.0,1.0],\"title\":{\"text\":\"\"}},\"yaxis\":{\"anchor\":\"x\",\"domain\":[0.0,1.0],\"title\":{\"text\":\"\"}},\"legend\":{\"tracegroupgap\":0},\"margin\":{\"t\":60},\"boxmode\":\"group\",\"height\":500,\"width\":500,\"title\":{\"font\":{\"size\":22,\"color\":\"#164f5e\"},\"text\":\"Pull%+\",\"automargin\":true,\"yref\":\"paper\"}},                        {\"responsive\": true}                    ).then(function(){\n",
       "                            \n",
       "var gd = document.getElementById('79ca8d63-eec4-443d-a7f7-7265450aabef');\n",
       "var x = new MutationObserver(function (mutations, observer) {{\n",
       "        var display = window.getComputedStyle(gd).display;\n",
       "        if (!display || display === 'none') {{\n",
       "            console.log([gd, 'removed!']);\n",
       "            Plotly.purge(gd);\n",
       "            observer.disconnect();\n",
       "        }}\n",
       "}});\n",
       "\n",
       "// Listen for the removal of the full notebook cells\n",
       "var notebookContainer = gd.closest('#notebook-container');\n",
       "if (notebookContainer) {{\n",
       "    x.observe(notebookContainer, {childList: true});\n",
       "}}\n",
       "\n",
       "// Listen for the clearing of the current output cell\n",
       "var outputEl = gd.closest('.output');\n",
       "if (outputEl) {{\n",
       "    x.observe(outputEl, {childList: true});\n",
       "}}\n",
       "\n",
       "                        })                };                });            </script>        </div>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "fig_51 = px.box(\n",
    "    df.query(\"Season==2023\"),\n",
    "    y = \"Pull%+\",\n",
    "    points=\"all\",\n",
    "    hover_name = \"Name\",\n",
    "    height = 500,\n",
    "    width = 500,\n",
    ")\n",
    "\n",
    "fig_51.update_traces(marker=dict(color=\"#7284cc\"))\n",
    "\n",
    "fig_51.update_layout(\n",
    "    title=dict(text=\"Pull%+\", font=dict(size=22), automargin=True, yref='paper'),\n",
    "    title_font_color=\"#164f5e\",\n",
    "    yaxis=dict(title=\"\"),\n",
    "    xaxis=dict(title=\"\")\n",
    ")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 100,
   "id": "0a27671f",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "application/vnd.plotly.v1+json": {
       "config": {
        "plotlyServerURL": "https://plot.ly"
       },
       "data": [
        {
         "alignmentgroup": "True",
         "boxpoints": "all",
         "hovertemplate": "<b>%{hovertext}</b><br><br>Cent%+=%{y}<extra></extra>",
         "hovertext": [
          "Ronald Acuna Jr.",
          "Shohei Ohtani",
          "Mookie Betts",
          "Wander Franco",
          "Corbin Carroll",
          "Luis Robert",
          "Freddie Freeman",
          "Juan Soto",
          "Fernando Tatis Jr.",
          "Jose Ramirez",
          "Adolis Garcia",
          "Mike Trout",
          "Jonah Heim",
          "Marcus Semien",
          "Bo Bichette",
          "Christian Yelich",
          "Francisco Lindor",
          "Dansby Swanson",
          "Luis Arraez",
          "Will Smith",
          "Ha-seong Kim",
          "Randy Arozarena",
          "Paul Goldschmidt",
          "Matt Chapman",
          "Isaac Paredes",
          "Brandon Nimmo",
          "Jeimer Candelario",
          "Thairo Estrada",
          "Matt Olson",
          "Christian Walker",
          "Jack Suwinski",
          "Julio Rodriguez",
          "Yandy Diaz",
          "Kyle Tucker",
          "Josh Jung",
          "Ketel Marte",
          "Ozzie Albies",
          "William Contreras",
          "Xander Bogaerts",
          "Leody Taveras",
          "Adley Rutschman",
          "Nico Hoerner",
          "Lane Thomas",
          "Bobby Witt Jr.",
          "LaMonte Wade Jr.",
          "Austin Hays",
          "J.D. Davis",
          "Gunnar Henderson",
          "Alex Verdugo",
          "Nathaniel Lowe",
          "Jorge Soler",
          "Nolan Arenado",
          "Rafael Devers",
          "Austin Riley",
          "Brendan Donovan",
          "Bryson Stott",
          "Brandon Drury",
          "Brandon Marsh",
          "Ian Happ",
          "J.P. Crawford",
          "Alex Bregman",
          "Andres Gimenez",
          "Cal Raleigh",
          "Spencer Steer",
          "Nolan Gorman",
          "Ryan Noda",
          "Cedric Mullins II",
          "James Outman",
          "Nick Castellanos",
          "Pete Alonso",
          "Anthony Santander",
          "Ryan McMahon",
          "Zach McKinstry",
          "Trea Turner",
          "Anthony Volpe",
          "Masataka Yoshida",
          "Justin Turner",
          "Bryan Reynolds",
          "Manny Machado",
          "Whit Merrifield",
          "Jeremy Pena",
          "Josh Naylor",
          "Anthony Rizzo",
          "Jonathan India",
          "Jarred Kelenic",
          "George Springer",
          "Eugenio Suarez",
          "Joey Wiemer",
          "Andrew McCutchen",
          "Lourdes Gurriel Jr.",
          "Max Muncy",
          "Hunter Renfroe",
          "Mauricio Dubon",
          "Steven Kwan",
          "Tommy Edman",
          "Brent Rooker",
          "J.T. Realmuto",
          "Teoscar Hernandez",
          "Ezequiel Tovar",
          "Willson Contreras",
          "Carlos Correa",
          "Ke'Bryan Hayes",
          "Willy Adames",
          "Gleyber Torres",
          "Esteury Ruiz",
          "Marcell Ozuna",
          "Byron Buxton",
          "Andrew Benintendi",
          "Daulton Varsho",
          "J.D. Martinez",
          "Elias Diaz",
          "Ty France",
          "Taylor Ward",
          "Jeff McNeil",
          "Eddie Rosario",
          "Seiya Suzuki",
          "Carlos Santana",
          "Trent Grisham",
          "Vladimir Guerrero Jr.",
          "Michael Conforto",
          "Brian Anderson",
          "Jace Peterson",
          "Javier Baez",
          "Andrew Vaughn",
          "Alec Bohm",
          "Bryan De La Cruz",
          "Jake Cronenworth",
          "Salvador Perez",
          "CJ Abrams",
          "Spencer Torkelson",
          "Adam Frazier",
          "Miguel Vargas",
          "Amed Rosario",
          "Starling Marte",
          "Luis Garcia",
          "DJ LeMahieu",
          "Tyler Stephenson",
          "Kyle Schwarber",
          "Triston Casas",
          "Dominic Smith",
          "Shea Langeliers",
          "Josh Bell",
          "Myles Straw",
          "Joey Meneses",
          "Jose Abreu",
          "MJ Melendez",
          "Tim Anderson",
          "Rowdy Tellez",
          "Jurickson Profar",
          "Keibert Ruiz",
          "Enrique Hernandez"
         ],
         "legendgroup": "",
         "marker": {
          "color": "#7284cc"
         },
         "name": "",
         "notched": false,
         "offsetgroup": "",
         "orientation": "v",
         "showlegend": false,
         "type": "box",
         "x0": " ",
         "xaxis": "x",
         "y": [
          97,
          103,
          102,
          101,
          88,
          101,
          102,
          113,
          120,
          87,
          109,
          84,
          92,
          81,
          101,
          98,
          101,
          100,
          112,
          104,
          111,
          101,
          99,
          107,
          72,
          98,
          92,
          91,
          109,
          105,
          108,
          101,
          119,
          95,
          111,
          105,
          88,
          109,
          100,
          118,
          96,
          117,
          100,
          100,
          96,
          101,
          100,
          99,
          111,
          112,
          110,
          94,
          101,
          106,
          84,
          95,
          99,
          92,
          106,
          104,
          99,
          96,
          91,
          98,
          78,
          85,
          104,
          87,
          97,
          100,
          88,
          113,
          113,
          102,
          95,
          104,
          102,
          100,
          90,
          110,
          85,
          110,
          105,
          88,
          103,
          110,
          105,
          99,
          78,
          86,
          87,
          93,
          118,
          116,
          105,
          122,
          105,
          108,
          106,
          103,
          84,
          105,
          102,
          113,
          97,
          83,
          85,
          106,
          71,
          103,
          98,
          97,
          98,
          98,
          88,
          117,
          96,
          93,
          112,
          107,
          124,
          108,
          111,
          99,
          125,
          102,
          106,
          100,
          115,
          80,
          101,
          102,
          114,
          104,
          118,
          114,
          90,
          87,
          103,
          95,
          74,
          90,
          115,
          92,
          127,
          93,
          99,
          115,
          95,
          107,
          99
         ],
         "y0": " ",
         "yaxis": "y"
        }
       ],
       "layout": {
        "boxmode": "group",
        "height": 500,
        "legend": {
         "tracegroupgap": 0
        },
        "margin": {
         "t": 60
        },
        "template": {
         "data": {
          "candlestick": [
           {
            "decreasing": {
             "line": {
              "color": "#000033"
             }
            },
            "increasing": {
             "line": {
              "color": "#000032"
             }
            },
            "type": "candlestick"
           }
          ],
          "contour": [
           {
            "colorscale": [
             [
              0,
              "#000011"
             ],
             [
              0.1111111111111111,
              "#000012"
             ],
             [
              0.2222222222222222,
              "#000013"
             ],
             [
              0.3333333333333333,
              "#000014"
             ],
             [
              0.4444444444444444,
              "#000015"
             ],
             [
              0.5555555555555556,
              "#000016"
             ],
             [
              0.6666666666666666,
              "#000017"
             ],
             [
              0.7777777777777778,
              "#000018"
             ],
             [
              0.8888888888888888,
              "#000019"
             ],
             [
              1,
              "#000020"
             ]
            ],
            "type": "contour"
           }
          ],
          "contourcarpet": [
           {
            "colorscale": [
             [
              0,
              "#000011"
             ],
             [
              0.1111111111111111,
              "#000012"
             ],
             [
              0.2222222222222222,
              "#000013"
             ],
             [
              0.3333333333333333,
              "#000014"
             ],
             [
              0.4444444444444444,
              "#000015"
             ],
             [
              0.5555555555555556,
              "#000016"
             ],
             [
              0.6666666666666666,
              "#000017"
             ],
             [
              0.7777777777777778,
              "#000018"
             ],
             [
              0.8888888888888888,
              "#000019"
             ],
             [
              1,
              "#000020"
             ]
            ],
            "type": "contourcarpet"
           }
          ],
          "heatmap": [
           {
            "colorscale": [
             [
              0,
              "#000011"
             ],
             [
              0.1111111111111111,
              "#000012"
             ],
             [
              0.2222222222222222,
              "#000013"
             ],
             [
              0.3333333333333333,
              "#000014"
             ],
             [
              0.4444444444444444,
              "#000015"
             ],
             [
              0.5555555555555556,
              "#000016"
             ],
             [
              0.6666666666666666,
              "#000017"
             ],
             [
              0.7777777777777778,
              "#000018"
             ],
             [
              0.8888888888888888,
              "#000019"
             ],
             [
              1,
              "#000020"
             ]
            ],
            "type": "heatmap"
           }
          ],
          "histogram2d": [
           {
            "colorscale": [
             [
              0,
              "#000011"
             ],
             [
              0.1111111111111111,
              "#000012"
             ],
             [
              0.2222222222222222,
              "#000013"
             ],
             [
              0.3333333333333333,
              "#000014"
             ],
             [
              0.4444444444444444,
              "#000015"
             ],
             [
              0.5555555555555556,
              "#000016"
             ],
             [
              0.6666666666666666,
              "#000017"
             ],
             [
              0.7777777777777778,
              "#000018"
             ],
             [
              0.8888888888888888,
              "#000019"
             ],
             [
              1,
              "#000020"
             ]
            ],
            "type": "histogram2d"
           }
          ],
          "icicle": [
           {
            "textfont": {
             "color": "white"
            },
            "type": "icicle"
           }
          ],
          "sankey": [
           {
            "textfont": {
             "color": "#000036"
            },
            "type": "sankey"
           }
          ],
          "scatter": [
           {
            "marker": {
             "line": {
              "width": 0
             }
            },
            "type": "scatter"
           }
          ],
          "table": [
           {
            "cells": {
             "fill": {
              "color": "#000038"
             },
             "font": {
              "color": "#000037"
             },
             "line": {
              "color": "#000039"
             }
            },
            "header": {
             "fill": {
              "color": "#000040"
             },
             "font": {
              "color": "#000036"
             },
             "line": {
              "color": "#000039"
             }
            },
            "type": "table"
           }
          ],
          "waterfall": [
           {
            "connector": {
             "line": {
              "color": "#000036",
              "width": 2
             }
            },
            "decreasing": {
             "marker": {
              "color": "#000033"
             }
            },
            "increasing": {
             "marker": {
              "color": "#000032"
             }
            },
            "totals": {
             "marker": {
              "color": "#000034"
             }
            },
            "type": "waterfall"
           }
          ]
         },
         "layout": {
          "coloraxis": {
           "colorscale": [
            [
             0,
             "#000011"
            ],
            [
             0.1111111111111111,
             "#000012"
            ],
            [
             0.2222222222222222,
             "#000013"
            ],
            [
             0.3333333333333333,
             "#000014"
            ],
            [
             0.4444444444444444,
             "#000015"
            ],
            [
             0.5555555555555556,
             "#000016"
            ],
            [
             0.6666666666666666,
             "#000017"
            ],
            [
             0.7777777777777778,
             "#000018"
            ],
            [
             0.8888888888888888,
             "#000019"
            ],
            [
             1,
             "#000020"
            ]
           ]
          },
          "colorscale": {
           "diverging": [
            [
             0,
             "#000021"
            ],
            [
             0.1,
             "#000022"
            ],
            [
             0.2,
             "#000023"
            ],
            [
             0.3,
             "#000024"
            ],
            [
             0.4,
             "#000025"
            ],
            [
             0.5,
             "#000026"
            ],
            [
             0.6,
             "#000027"
            ],
            [
             0.7,
             "#000028"
            ],
            [
             0.8,
             "#000029"
            ],
            [
             0.9,
             "#000030"
            ],
            [
             1,
             "#000031"
            ]
           ],
           "sequential": [
            [
             0,
             "#000011"
            ],
            [
             0.1111111111111111,
             "#000012"
            ],
            [
             0.2222222222222222,
             "#000013"
            ],
            [
             0.3333333333333333,
             "#000014"
            ],
            [
             0.4444444444444444,
             "#000015"
            ],
            [
             0.5555555555555556,
             "#000016"
            ],
            [
             0.6666666666666666,
             "#000017"
            ],
            [
             0.7777777777777778,
             "#000018"
            ],
            [
             0.8888888888888888,
             "#000019"
            ],
            [
             1,
             "#000020"
            ]
           ],
           "sequentialminus": [
            [
             0,
             "#000011"
            ],
            [
             0.1111111111111111,
             "#000012"
            ],
            [
             0.2222222222222222,
             "#000013"
            ],
            [
             0.3333333333333333,
             "#000014"
            ],
            [
             0.4444444444444444,
             "#000015"
            ],
            [
             0.5555555555555556,
             "#000016"
            ],
            [
             0.6666666666666666,
             "#000017"
            ],
            [
             0.7777777777777778,
             "#000018"
            ],
            [
             0.8888888888888888,
             "#000019"
            ],
            [
             1,
             "#000020"
            ]
           ]
          },
          "colorway": [
           "#000001",
           "#000002",
           "#000003",
           "#000004",
           "#000005",
           "#000006",
           "#000007",
           "#000008",
           "#000009",
           "#000010"
          ]
         }
        },
        "title": {
         "automargin": true,
         "font": {
          "color": "#164f5e",
          "size": 22
         },
         "text": "Center%+",
         "yref": "paper"
        },
        "width": 500,
        "xaxis": {
         "anchor": "y",
         "domain": [
          0,
          1
         ],
         "title": {
          "text": ""
         }
        },
        "yaxis": {
         "anchor": "x",
         "domain": [
          0,
          1
         ],
         "title": {
          "text": ""
         }
        }
       }
      },
      "text/html": [
       "<div>                            <div id=\"b4a1076b-7ca7-44de-a68f-4ccad532127d\" class=\"plotly-graph-div\" style=\"height:500px; width:500px;\"></div>            <script type=\"text/javascript\">                require([\"plotly\"], function(Plotly) {                    window.PLOTLYENV=window.PLOTLYENV || {};                                    if (document.getElementById(\"b4a1076b-7ca7-44de-a68f-4ccad532127d\")) {                    Plotly.newPlot(                        \"b4a1076b-7ca7-44de-a68f-4ccad532127d\",                        [{\"alignmentgroup\":\"True\",\"boxpoints\":\"all\",\"hovertemplate\":\"\\u003cb\\u003e%{hovertext}\\u003c\\u002fb\\u003e\\u003cbr\\u003e\\u003cbr\\u003eCent%+=%{y}\\u003cextra\\u003e\\u003c\\u002fextra\\u003e\",\"hovertext\":[\"Ronald Acuna Jr.\",\"Shohei Ohtani\",\"Mookie Betts\",\"Wander Franco\",\"Corbin Carroll\",\"Luis Robert\",\"Freddie Freeman\",\"Juan Soto\",\"Fernando Tatis Jr.\",\"Jose Ramirez\",\"Adolis Garcia\",\"Mike Trout\",\"Jonah Heim\",\"Marcus Semien\",\"Bo Bichette\",\"Christian Yelich\",\"Francisco Lindor\",\"Dansby Swanson\",\"Luis Arraez\",\"Will Smith\",\"Ha-seong Kim\",\"Randy Arozarena\",\"Paul Goldschmidt\",\"Matt Chapman\",\"Isaac Paredes\",\"Brandon Nimmo\",\"Jeimer Candelario\",\"Thairo Estrada\",\"Matt Olson\",\"Christian Walker\",\"Jack Suwinski\",\"Julio Rodriguez\",\"Yandy Diaz\",\"Kyle Tucker\",\"Josh Jung\",\"Ketel Marte\",\"Ozzie Albies\",\"William Contreras\",\"Xander Bogaerts\",\"Leody Taveras\",\"Adley Rutschman\",\"Nico Hoerner\",\"Lane Thomas\",\"Bobby Witt Jr.\",\"LaMonte Wade Jr.\",\"Austin Hays\",\"J.D. Davis\",\"Gunnar Henderson\",\"Alex Verdugo\",\"Nathaniel Lowe\",\"Jorge Soler\",\"Nolan Arenado\",\"Rafael Devers\",\"Austin Riley\",\"Brendan Donovan\",\"Bryson Stott\",\"Brandon Drury\",\"Brandon Marsh\",\"Ian Happ\",\"J.P. Crawford\",\"Alex Bregman\",\"Andres Gimenez\",\"Cal Raleigh\",\"Spencer Steer\",\"Nolan Gorman\",\"Ryan Noda\",\"Cedric Mullins II\",\"James Outman\",\"Nick Castellanos\",\"Pete Alonso\",\"Anthony Santander\",\"Ryan McMahon\",\"Zach McKinstry\",\"Trea Turner\",\"Anthony Volpe\",\"Masataka Yoshida\",\"Justin Turner\",\"Bryan Reynolds\",\"Manny Machado\",\"Whit Merrifield\",\"Jeremy Pena\",\"Josh Naylor\",\"Anthony Rizzo\",\"Jonathan India\",\"Jarred Kelenic\",\"George Springer\",\"Eugenio Suarez\",\"Joey Wiemer\",\"Andrew McCutchen\",\"Lourdes Gurriel Jr.\",\"Max Muncy\",\"Hunter Renfroe\",\"Mauricio Dubon\",\"Steven Kwan\",\"Tommy Edman\",\"Brent Rooker\",\"J.T. Realmuto\",\"Teoscar Hernandez\",\"Ezequiel Tovar\",\"Willson Contreras\",\"Carlos Correa\",\"Ke'Bryan Hayes\",\"Willy Adames\",\"Gleyber Torres\",\"Esteury Ruiz\",\"Marcell Ozuna\",\"Byron Buxton\",\"Andrew Benintendi\",\"Daulton Varsho\",\"J.D. Martinez\",\"Elias Diaz\",\"Ty France\",\"Taylor Ward\",\"Jeff McNeil\",\"Eddie Rosario\",\"Seiya Suzuki\",\"Carlos Santana\",\"Trent Grisham\",\"Vladimir Guerrero Jr.\",\"Michael Conforto\",\"Brian Anderson\",\"Jace Peterson\",\"Javier Baez\",\"Andrew Vaughn\",\"Alec Bohm\",\"Bryan De La Cruz\",\"Jake Cronenworth\",\"Salvador Perez\",\"CJ Abrams\",\"Spencer Torkelson\",\"Adam Frazier\",\"Miguel Vargas\",\"Amed Rosario\",\"Starling Marte\",\"Luis Garcia\",\"DJ LeMahieu\",\"Tyler Stephenson\",\"Kyle Schwarber\",\"Triston Casas\",\"Dominic Smith\",\"Shea Langeliers\",\"Josh Bell\",\"Myles Straw\",\"Joey Meneses\",\"Jose Abreu\",\"MJ Melendez\",\"Tim Anderson\",\"Rowdy Tellez\",\"Jurickson Profar\",\"Keibert Ruiz\",\"Enrique Hernandez\"],\"legendgroup\":\"\",\"marker\":{\"color\":\"#7284cc\"},\"name\":\"\",\"notched\":false,\"offsetgroup\":\"\",\"orientation\":\"v\",\"showlegend\":false,\"x0\":\" \",\"xaxis\":\"x\",\"y\":[97,103,102,101,88,101,102,113,120,87,109,84,92,81,101,98,101,100,112,104,111,101,99,107,72,98,92,91,109,105,108,101,119,95,111,105,88,109,100,118,96,117,100,100,96,101,100,99,111,112,110,94,101,106,84,95,99,92,106,104,99,96,91,98,78,85,104,87,97,100,88,113,113,102,95,104,102,100,90,110,85,110,105,88,103,110,105,99,78,86,87,93,118,116,105,122,105,108,106,103,84,105,102,113,97,83,85,106,71,103,98,97,98,98,88,117,96,93,112,107,124,108,111,99,125,102,106,100,115,80,101,102,114,104,118,114,90,87,103,95,74,90,115,92,127,93,99,115,95,107,99],\"y0\":\" \",\"yaxis\":\"y\",\"type\":\"box\"}],                        {\"template\":{\"data\":{\"candlestick\":[{\"decreasing\":{\"line\":{\"color\":\"#000033\"}},\"increasing\":{\"line\":{\"color\":\"#000032\"}},\"type\":\"candlestick\"}],\"contourcarpet\":[{\"colorscale\":[[0.0,\"#000011\"],[0.1111111111111111,\"#000012\"],[0.2222222222222222,\"#000013\"],[0.3333333333333333,\"#000014\"],[0.4444444444444444,\"#000015\"],[0.5555555555555556,\"#000016\"],[0.6666666666666666,\"#000017\"],[0.7777777777777778,\"#000018\"],[0.8888888888888888,\"#000019\"],[1.0,\"#000020\"]],\"type\":\"contourcarpet\"}],\"contour\":[{\"colorscale\":[[0.0,\"#000011\"],[0.1111111111111111,\"#000012\"],[0.2222222222222222,\"#000013\"],[0.3333333333333333,\"#000014\"],[0.4444444444444444,\"#000015\"],[0.5555555555555556,\"#000016\"],[0.6666666666666666,\"#000017\"],[0.7777777777777778,\"#000018\"],[0.8888888888888888,\"#000019\"],[1.0,\"#000020\"]],\"type\":\"contour\"}],\"heatmap\":[{\"colorscale\":[[0.0,\"#000011\"],[0.1111111111111111,\"#000012\"],[0.2222222222222222,\"#000013\"],[0.3333333333333333,\"#000014\"],[0.4444444444444444,\"#000015\"],[0.5555555555555556,\"#000016\"],[0.6666666666666666,\"#000017\"],[0.7777777777777778,\"#000018\"],[0.8888888888888888,\"#000019\"],[1.0,\"#000020\"]],\"type\":\"heatmap\"}],\"histogram2d\":[{\"colorscale\":[[0.0,\"#000011\"],[0.1111111111111111,\"#000012\"],[0.2222222222222222,\"#000013\"],[0.3333333333333333,\"#000014\"],[0.4444444444444444,\"#000015\"],[0.5555555555555556,\"#000016\"],[0.6666666666666666,\"#000017\"],[0.7777777777777778,\"#000018\"],[0.8888888888888888,\"#000019\"],[1.0,\"#000020\"]],\"type\":\"histogram2d\"}],\"icicle\":[{\"textfont\":{\"color\":\"white\"},\"type\":\"icicle\"}],\"sankey\":[{\"textfont\":{\"color\":\"#000036\"},\"type\":\"sankey\"}],\"scatter\":[{\"marker\":{\"line\":{\"width\":0}},\"type\":\"scatter\"}],\"table\":[{\"cells\":{\"fill\":{\"color\":\"#000038\"},\"font\":{\"color\":\"#000037\"},\"line\":{\"color\":\"#000039\"}},\"header\":{\"fill\":{\"color\":\"#000040\"},\"font\":{\"color\":\"#000036\"},\"line\":{\"color\":\"#000039\"}},\"type\":\"table\"}],\"waterfall\":[{\"connector\":{\"line\":{\"color\":\"#000036\",\"width\":2}},\"decreasing\":{\"marker\":{\"color\":\"#000033\"}},\"increasing\":{\"marker\":{\"color\":\"#000032\"}},\"totals\":{\"marker\":{\"color\":\"#000034\"}},\"type\":\"waterfall\"}]},\"layout\":{\"coloraxis\":{\"colorscale\":[[0.0,\"#000011\"],[0.1111111111111111,\"#000012\"],[0.2222222222222222,\"#000013\"],[0.3333333333333333,\"#000014\"],[0.4444444444444444,\"#000015\"],[0.5555555555555556,\"#000016\"],[0.6666666666666666,\"#000017\"],[0.7777777777777778,\"#000018\"],[0.8888888888888888,\"#000019\"],[1.0,\"#000020\"]]},\"colorscale\":{\"diverging\":[[0.0,\"#000021\"],[0.1,\"#000022\"],[0.2,\"#000023\"],[0.3,\"#000024\"],[0.4,\"#000025\"],[0.5,\"#000026\"],[0.6,\"#000027\"],[0.7,\"#000028\"],[0.8,\"#000029\"],[0.9,\"#000030\"],[1.0,\"#000031\"]],\"sequential\":[[0.0,\"#000011\"],[0.1111111111111111,\"#000012\"],[0.2222222222222222,\"#000013\"],[0.3333333333333333,\"#000014\"],[0.4444444444444444,\"#000015\"],[0.5555555555555556,\"#000016\"],[0.6666666666666666,\"#000017\"],[0.7777777777777778,\"#000018\"],[0.8888888888888888,\"#000019\"],[1.0,\"#000020\"]],\"sequentialminus\":[[0.0,\"#000011\"],[0.1111111111111111,\"#000012\"],[0.2222222222222222,\"#000013\"],[0.3333333333333333,\"#000014\"],[0.4444444444444444,\"#000015\"],[0.5555555555555556,\"#000016\"],[0.6666666666666666,\"#000017\"],[0.7777777777777778,\"#000018\"],[0.8888888888888888,\"#000019\"],[1.0,\"#000020\"]]},\"colorway\":[\"#000001\",\"#000002\",\"#000003\",\"#000004\",\"#000005\",\"#000006\",\"#000007\",\"#000008\",\"#000009\",\"#000010\"]}},\"xaxis\":{\"anchor\":\"y\",\"domain\":[0.0,1.0],\"title\":{\"text\":\"\"}},\"yaxis\":{\"anchor\":\"x\",\"domain\":[0.0,1.0],\"title\":{\"text\":\"\"}},\"legend\":{\"tracegroupgap\":0},\"margin\":{\"t\":60},\"boxmode\":\"group\",\"height\":500,\"width\":500,\"title\":{\"font\":{\"size\":22,\"color\":\"#164f5e\"},\"text\":\"Center%+\",\"automargin\":true,\"yref\":\"paper\"}},                        {\"responsive\": true}                    ).then(function(){\n",
       "                            \n",
       "var gd = document.getElementById('b4a1076b-7ca7-44de-a68f-4ccad532127d');\n",
       "var x = new MutationObserver(function (mutations, observer) {{\n",
       "        var display = window.getComputedStyle(gd).display;\n",
       "        if (!display || display === 'none') {{\n",
       "            console.log([gd, 'removed!']);\n",
       "            Plotly.purge(gd);\n",
       "            observer.disconnect();\n",
       "        }}\n",
       "}});\n",
       "\n",
       "// Listen for the removal of the full notebook cells\n",
       "var notebookContainer = gd.closest('#notebook-container');\n",
       "if (notebookContainer) {{\n",
       "    x.observe(notebookContainer, {childList: true});\n",
       "}}\n",
       "\n",
       "// Listen for the clearing of the current output cell\n",
       "var outputEl = gd.closest('.output');\n",
       "if (outputEl) {{\n",
       "    x.observe(outputEl, {childList: true});\n",
       "}}\n",
       "\n",
       "                        })                };                });            </script>        </div>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "fig_52 = px.box(\n",
    "    df.query(\"Season==2023\"),\n",
    "    y = \"Cent%+\",\n",
    "    points=\"all\",\n",
    "    hover_name = \"Name\",\n",
    "    height = 500,\n",
    "    width = 500,\n",
    ")\n",
    "\n",
    "fig_52.update_traces(marker=dict(color=\"#7284cc\"))\n",
    "\n",
    "fig_52.update_layout(\n",
    "    title=dict(text=\"Center%+\", font=dict(size=22), automargin=True, yref='paper'),\n",
    "    title_font_color=\"#164f5e\",\n",
    "    yaxis=dict(title=\"\"),\n",
    "    xaxis=dict(title=\"\")\n",
    ")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 101,
   "id": "93546703",
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "data": {
      "application/vnd.plotly.v1+json": {
       "config": {
        "plotlyServerURL": "https://plot.ly"
       },
       "data": [
        {
         "alignmentgroup": "True",
         "boxpoints": "all",
         "hovertemplate": "<b>%{hovertext}</b><br><br>Oppo%+=%{y}<extra></extra>",
         "hovertext": [
          "Ronald Acuna Jr.",
          "Shohei Ohtani",
          "Mookie Betts",
          "Wander Franco",
          "Corbin Carroll",
          "Luis Robert",
          "Freddie Freeman",
          "Juan Soto",
          "Fernando Tatis Jr.",
          "Jose Ramirez",
          "Adolis Garcia",
          "Mike Trout",
          "Jonah Heim",
          "Marcus Semien",
          "Bo Bichette",
          "Christian Yelich",
          "Francisco Lindor",
          "Dansby Swanson",
          "Luis Arraez",
          "Will Smith",
          "Ha-seong Kim",
          "Randy Arozarena",
          "Paul Goldschmidt",
          "Matt Chapman",
          "Isaac Paredes",
          "Brandon Nimmo",
          "Jeimer Candelario",
          "Thairo Estrada",
          "Matt Olson",
          "Christian Walker",
          "Jack Suwinski",
          "Julio Rodriguez",
          "Yandy Diaz",
          "Kyle Tucker",
          "Josh Jung",
          "Ketel Marte",
          "Ozzie Albies",
          "William Contreras",
          "Xander Bogaerts",
          "Leody Taveras",
          "Adley Rutschman",
          "Nico Hoerner",
          "Lane Thomas",
          "Bobby Witt Jr.",
          "LaMonte Wade Jr.",
          "Austin Hays",
          "J.D. Davis",
          "Gunnar Henderson",
          "Alex Verdugo",
          "Nathaniel Lowe",
          "Jorge Soler",
          "Nolan Arenado",
          "Rafael Devers",
          "Austin Riley",
          "Brendan Donovan",
          "Bryson Stott",
          "Brandon Drury",
          "Brandon Marsh",
          "Ian Happ",
          "J.P. Crawford",
          "Alex Bregman",
          "Andres Gimenez",
          "Cal Raleigh",
          "Spencer Steer",
          "Nolan Gorman",
          "Ryan Noda",
          "Cedric Mullins II",
          "James Outman",
          "Nick Castellanos",
          "Pete Alonso",
          "Anthony Santander",
          "Ryan McMahon",
          "Zach McKinstry",
          "Trea Turner",
          "Anthony Volpe",
          "Masataka Yoshida",
          "Justin Turner",
          "Bryan Reynolds",
          "Manny Machado",
          "Whit Merrifield",
          "Jeremy Pena",
          "Josh Naylor",
          "Anthony Rizzo",
          "Jonathan India",
          "Jarred Kelenic",
          "George Springer",
          "Eugenio Suarez",
          "Joey Wiemer",
          "Andrew McCutchen",
          "Lourdes Gurriel Jr.",
          "Max Muncy",
          "Hunter Renfroe",
          "Mauricio Dubon",
          "Steven Kwan",
          "Tommy Edman",
          "Brent Rooker",
          "J.T. Realmuto",
          "Teoscar Hernandez",
          "Ezequiel Tovar",
          "Willson Contreras",
          "Carlos Correa",
          "Ke'Bryan Hayes",
          "Willy Adames",
          "Gleyber Torres",
          "Esteury Ruiz",
          "Marcell Ozuna",
          "Byron Buxton",
          "Andrew Benintendi",
          "Daulton Varsho",
          "J.D. Martinez",
          "Elias Diaz",
          "Ty France",
          "Taylor Ward",
          "Jeff McNeil",
          "Eddie Rosario",
          "Seiya Suzuki",
          "Carlos Santana",
          "Trent Grisham",
          "Vladimir Guerrero Jr.",
          "Michael Conforto",
          "Brian Anderson",
          "Jace Peterson",
          "Javier Baez",
          "Andrew Vaughn",
          "Alec Bohm",
          "Bryan De La Cruz",
          "Jake Cronenworth",
          "Salvador Perez",
          "CJ Abrams",
          "Spencer Torkelson",
          "Adam Frazier",
          "Miguel Vargas",
          "Amed Rosario",
          "Starling Marte",
          "Luis Garcia",
          "DJ LeMahieu",
          "Tyler Stephenson",
          "Kyle Schwarber",
          "Triston Casas",
          "Dominic Smith",
          "Shea Langeliers",
          "Josh Bell",
          "Myles Straw",
          "Joey Meneses",
          "Jose Abreu",
          "MJ Melendez",
          "Tim Anderson",
          "Rowdy Tellez",
          "Jurickson Profar",
          "Keibert Ruiz",
          "Enrique Hernandez"
         ],
         "legendgroup": "",
         "marker": {
          "color": "#7284cc"
         },
         "name": "",
         "notched": false,
         "offsetgroup": "",
         "orientation": "v",
         "showlegend": false,
         "type": "box",
         "x0": " ",
         "xaxis": "x",
         "y": [
          85,
          102,
          69,
          96,
          105,
          93,
          112,
          74,
          61,
          72,
          97,
          111,
          73,
          90,
          172,
          132,
          74,
          84,
          135,
          112,
          62,
          97,
          135,
          102,
          87,
          123,
          98,
          93,
          100,
          92,
          72,
          110,
          112,
          95,
          95,
          97,
          62,
          112,
          123,
          124,
          125,
          121,
          62,
          121,
          99,
          110,
          94,
          106,
          107,
          133,
          69,
          90,
          100,
          84,
          123,
          134,
          92,
          126,
          97,
          98,
          83,
          91,
          89,
          106,
          107,
          101,
          70,
          89,
          89,
          99,
          82,
          114,
          108,
          106,
          98,
          114,
          100,
          107,
          122,
          117,
          89,
          97,
          81,
          107,
          88,
          95,
          90,
          87,
          93,
          116,
          71,
          63,
          110,
          131,
          81,
          80,
          82,
          107,
          133,
          114,
          117,
          145,
          56,
          116,
          118,
          111,
          72,
          118,
          96,
          91,
          83,
          92,
          112,
          100,
          91,
          82,
          85,
          97,
          88,
          104,
          104,
          115,
          94,
          112,
          120,
          101,
          100,
          96,
          95,
          103,
          110,
          109,
          106,
          114,
          106,
          111,
          120,
          61,
          78,
          113,
          101,
          95,
          151,
          123,
          96,
          97,
          133,
          89,
          77,
          91,
          109
         ],
         "y0": " ",
         "yaxis": "y"
        }
       ],
       "layout": {
        "boxmode": "group",
        "height": 500,
        "legend": {
         "tracegroupgap": 0
        },
        "margin": {
         "t": 60
        },
        "template": {
         "data": {
          "candlestick": [
           {
            "decreasing": {
             "line": {
              "color": "#000033"
             }
            },
            "increasing": {
             "line": {
              "color": "#000032"
             }
            },
            "type": "candlestick"
           }
          ],
          "contour": [
           {
            "colorscale": [
             [
              0,
              "#000011"
             ],
             [
              0.1111111111111111,
              "#000012"
             ],
             [
              0.2222222222222222,
              "#000013"
             ],
             [
              0.3333333333333333,
              "#000014"
             ],
             [
              0.4444444444444444,
              "#000015"
             ],
             [
              0.5555555555555556,
              "#000016"
             ],
             [
              0.6666666666666666,
              "#000017"
             ],
             [
              0.7777777777777778,
              "#000018"
             ],
             [
              0.8888888888888888,
              "#000019"
             ],
             [
              1,
              "#000020"
             ]
            ],
            "type": "contour"
           }
          ],
          "contourcarpet": [
           {
            "colorscale": [
             [
              0,
              "#000011"
             ],
             [
              0.1111111111111111,
              "#000012"
             ],
             [
              0.2222222222222222,
              "#000013"
             ],
             [
              0.3333333333333333,
              "#000014"
             ],
             [
              0.4444444444444444,
              "#000015"
             ],
             [
              0.5555555555555556,
              "#000016"
             ],
             [
              0.6666666666666666,
              "#000017"
             ],
             [
              0.7777777777777778,
              "#000018"
             ],
             [
              0.8888888888888888,
              "#000019"
             ],
             [
              1,
              "#000020"
             ]
            ],
            "type": "contourcarpet"
           }
          ],
          "heatmap": [
           {
            "colorscale": [
             [
              0,
              "#000011"
             ],
             [
              0.1111111111111111,
              "#000012"
             ],
             [
              0.2222222222222222,
              "#000013"
             ],
             [
              0.3333333333333333,
              "#000014"
             ],
             [
              0.4444444444444444,
              "#000015"
             ],
             [
              0.5555555555555556,
              "#000016"
             ],
             [
              0.6666666666666666,
              "#000017"
             ],
             [
              0.7777777777777778,
              "#000018"
             ],
             [
              0.8888888888888888,
              "#000019"
             ],
             [
              1,
              "#000020"
             ]
            ],
            "type": "heatmap"
           }
          ],
          "histogram2d": [
           {
            "colorscale": [
             [
              0,
              "#000011"
             ],
             [
              0.1111111111111111,
              "#000012"
             ],
             [
              0.2222222222222222,
              "#000013"
             ],
             [
              0.3333333333333333,
              "#000014"
             ],
             [
              0.4444444444444444,
              "#000015"
             ],
             [
              0.5555555555555556,
              "#000016"
             ],
             [
              0.6666666666666666,
              "#000017"
             ],
             [
              0.7777777777777778,
              "#000018"
             ],
             [
              0.8888888888888888,
              "#000019"
             ],
             [
              1,
              "#000020"
             ]
            ],
            "type": "histogram2d"
           }
          ],
          "icicle": [
           {
            "textfont": {
             "color": "white"
            },
            "type": "icicle"
           }
          ],
          "sankey": [
           {
            "textfont": {
             "color": "#000036"
            },
            "type": "sankey"
           }
          ],
          "scatter": [
           {
            "marker": {
             "line": {
              "width": 0
             }
            },
            "type": "scatter"
           }
          ],
          "table": [
           {
            "cells": {
             "fill": {
              "color": "#000038"
             },
             "font": {
              "color": "#000037"
             },
             "line": {
              "color": "#000039"
             }
            },
            "header": {
             "fill": {
              "color": "#000040"
             },
             "font": {
              "color": "#000036"
             },
             "line": {
              "color": "#000039"
             }
            },
            "type": "table"
           }
          ],
          "waterfall": [
           {
            "connector": {
             "line": {
              "color": "#000036",
              "width": 2
             }
            },
            "decreasing": {
             "marker": {
              "color": "#000033"
             }
            },
            "increasing": {
             "marker": {
              "color": "#000032"
             }
            },
            "totals": {
             "marker": {
              "color": "#000034"
             }
            },
            "type": "waterfall"
           }
          ]
         },
         "layout": {
          "coloraxis": {
           "colorscale": [
            [
             0,
             "#000011"
            ],
            [
             0.1111111111111111,
             "#000012"
            ],
            [
             0.2222222222222222,
             "#000013"
            ],
            [
             0.3333333333333333,
             "#000014"
            ],
            [
             0.4444444444444444,
             "#000015"
            ],
            [
             0.5555555555555556,
             "#000016"
            ],
            [
             0.6666666666666666,
             "#000017"
            ],
            [
             0.7777777777777778,
             "#000018"
            ],
            [
             0.8888888888888888,
             "#000019"
            ],
            [
             1,
             "#000020"
            ]
           ]
          },
          "colorscale": {
           "diverging": [
            [
             0,
             "#000021"
            ],
            [
             0.1,
             "#000022"
            ],
            [
             0.2,
             "#000023"
            ],
            [
             0.3,
             "#000024"
            ],
            [
             0.4,
             "#000025"
            ],
            [
             0.5,
             "#000026"
            ],
            [
             0.6,
             "#000027"
            ],
            [
             0.7,
             "#000028"
            ],
            [
             0.8,
             "#000029"
            ],
            [
             0.9,
             "#000030"
            ],
            [
             1,
             "#000031"
            ]
           ],
           "sequential": [
            [
             0,
             "#000011"
            ],
            [
             0.1111111111111111,
             "#000012"
            ],
            [
             0.2222222222222222,
             "#000013"
            ],
            [
             0.3333333333333333,
             "#000014"
            ],
            [
             0.4444444444444444,
             "#000015"
            ],
            [
             0.5555555555555556,
             "#000016"
            ],
            [
             0.6666666666666666,
             "#000017"
            ],
            [
             0.7777777777777778,
             "#000018"
            ],
            [
             0.8888888888888888,
             "#000019"
            ],
            [
             1,
             "#000020"
            ]
           ],
           "sequentialminus": [
            [
             0,
             "#000011"
            ],
            [
             0.1111111111111111,
             "#000012"
            ],
            [
             0.2222222222222222,
             "#000013"
            ],
            [
             0.3333333333333333,
             "#000014"
            ],
            [
             0.4444444444444444,
             "#000015"
            ],
            [
             0.5555555555555556,
             "#000016"
            ],
            [
             0.6666666666666666,
             "#000017"
            ],
            [
             0.7777777777777778,
             "#000018"
            ],
            [
             0.8888888888888888,
             "#000019"
            ],
            [
             1,
             "#000020"
            ]
           ]
          },
          "colorway": [
           "#000001",
           "#000002",
           "#000003",
           "#000004",
           "#000005",
           "#000006",
           "#000007",
           "#000008",
           "#000009",
           "#000010"
          ]
         }
        },
        "title": {
         "automargin": true,
         "font": {
          "color": "#164f5e",
          "size": 22
         },
         "text": "Oppo%+",
         "yref": "paper"
        },
        "width": 500,
        "xaxis": {
         "anchor": "y",
         "domain": [
          0,
          1
         ],
         "title": {
          "text": ""
         }
        },
        "yaxis": {
         "anchor": "x",
         "domain": [
          0,
          1
         ],
         "title": {
          "text": ""
         }
        }
       }
      },
      "text/html": [
       "<div>                            <div id=\"4329593b-802b-41fc-820a-47113563268c\" class=\"plotly-graph-div\" style=\"height:500px; width:500px;\"></div>            <script type=\"text/javascript\">                require([\"plotly\"], function(Plotly) {                    window.PLOTLYENV=window.PLOTLYENV || {};                                    if (document.getElementById(\"4329593b-802b-41fc-820a-47113563268c\")) {                    Plotly.newPlot(                        \"4329593b-802b-41fc-820a-47113563268c\",                        [{\"alignmentgroup\":\"True\",\"boxpoints\":\"all\",\"hovertemplate\":\"\\u003cb\\u003e%{hovertext}\\u003c\\u002fb\\u003e\\u003cbr\\u003e\\u003cbr\\u003eOppo%+=%{y}\\u003cextra\\u003e\\u003c\\u002fextra\\u003e\",\"hovertext\":[\"Ronald Acuna Jr.\",\"Shohei Ohtani\",\"Mookie Betts\",\"Wander Franco\",\"Corbin Carroll\",\"Luis Robert\",\"Freddie Freeman\",\"Juan Soto\",\"Fernando Tatis Jr.\",\"Jose Ramirez\",\"Adolis Garcia\",\"Mike Trout\",\"Jonah Heim\",\"Marcus Semien\",\"Bo Bichette\",\"Christian Yelich\",\"Francisco Lindor\",\"Dansby Swanson\",\"Luis Arraez\",\"Will Smith\",\"Ha-seong Kim\",\"Randy Arozarena\",\"Paul Goldschmidt\",\"Matt Chapman\",\"Isaac Paredes\",\"Brandon Nimmo\",\"Jeimer Candelario\",\"Thairo Estrada\",\"Matt Olson\",\"Christian Walker\",\"Jack Suwinski\",\"Julio Rodriguez\",\"Yandy Diaz\",\"Kyle Tucker\",\"Josh Jung\",\"Ketel Marte\",\"Ozzie Albies\",\"William Contreras\",\"Xander Bogaerts\",\"Leody Taveras\",\"Adley Rutschman\",\"Nico Hoerner\",\"Lane Thomas\",\"Bobby Witt Jr.\",\"LaMonte Wade Jr.\",\"Austin Hays\",\"J.D. Davis\",\"Gunnar Henderson\",\"Alex Verdugo\",\"Nathaniel Lowe\",\"Jorge Soler\",\"Nolan Arenado\",\"Rafael Devers\",\"Austin Riley\",\"Brendan Donovan\",\"Bryson Stott\",\"Brandon Drury\",\"Brandon Marsh\",\"Ian Happ\",\"J.P. Crawford\",\"Alex Bregman\",\"Andres Gimenez\",\"Cal Raleigh\",\"Spencer Steer\",\"Nolan Gorman\",\"Ryan Noda\",\"Cedric Mullins II\",\"James Outman\",\"Nick Castellanos\",\"Pete Alonso\",\"Anthony Santander\",\"Ryan McMahon\",\"Zach McKinstry\",\"Trea Turner\",\"Anthony Volpe\",\"Masataka Yoshida\",\"Justin Turner\",\"Bryan Reynolds\",\"Manny Machado\",\"Whit Merrifield\",\"Jeremy Pena\",\"Josh Naylor\",\"Anthony Rizzo\",\"Jonathan India\",\"Jarred Kelenic\",\"George Springer\",\"Eugenio Suarez\",\"Joey Wiemer\",\"Andrew McCutchen\",\"Lourdes Gurriel Jr.\",\"Max Muncy\",\"Hunter Renfroe\",\"Mauricio Dubon\",\"Steven Kwan\",\"Tommy Edman\",\"Brent Rooker\",\"J.T. Realmuto\",\"Teoscar Hernandez\",\"Ezequiel Tovar\",\"Willson Contreras\",\"Carlos Correa\",\"Ke'Bryan Hayes\",\"Willy Adames\",\"Gleyber Torres\",\"Esteury Ruiz\",\"Marcell Ozuna\",\"Byron Buxton\",\"Andrew Benintendi\",\"Daulton Varsho\",\"J.D. Martinez\",\"Elias Diaz\",\"Ty France\",\"Taylor Ward\",\"Jeff McNeil\",\"Eddie Rosario\",\"Seiya Suzuki\",\"Carlos Santana\",\"Trent Grisham\",\"Vladimir Guerrero Jr.\",\"Michael Conforto\",\"Brian Anderson\",\"Jace Peterson\",\"Javier Baez\",\"Andrew Vaughn\",\"Alec Bohm\",\"Bryan De La Cruz\",\"Jake Cronenworth\",\"Salvador Perez\",\"CJ Abrams\",\"Spencer Torkelson\",\"Adam Frazier\",\"Miguel Vargas\",\"Amed Rosario\",\"Starling Marte\",\"Luis Garcia\",\"DJ LeMahieu\",\"Tyler Stephenson\",\"Kyle Schwarber\",\"Triston Casas\",\"Dominic Smith\",\"Shea Langeliers\",\"Josh Bell\",\"Myles Straw\",\"Joey Meneses\",\"Jose Abreu\",\"MJ Melendez\",\"Tim Anderson\",\"Rowdy Tellez\",\"Jurickson Profar\",\"Keibert Ruiz\",\"Enrique Hernandez\"],\"legendgroup\":\"\",\"marker\":{\"color\":\"#7284cc\"},\"name\":\"\",\"notched\":false,\"offsetgroup\":\"\",\"orientation\":\"v\",\"showlegend\":false,\"x0\":\" \",\"xaxis\":\"x\",\"y\":[85,102,69,96,105,93,112,74,61,72,97,111,73,90,172,132,74,84,135,112,62,97,135,102,87,123,98,93,100,92,72,110,112,95,95,97,62,112,123,124,125,121,62,121,99,110,94,106,107,133,69,90,100,84,123,134,92,126,97,98,83,91,89,106,107,101,70,89,89,99,82,114,108,106,98,114,100,107,122,117,89,97,81,107,88,95,90,87,93,116,71,63,110,131,81,80,82,107,133,114,117,145,56,116,118,111,72,118,96,91,83,92,112,100,91,82,85,97,88,104,104,115,94,112,120,101,100,96,95,103,110,109,106,114,106,111,120,61,78,113,101,95,151,123,96,97,133,89,77,91,109],\"y0\":\" \",\"yaxis\":\"y\",\"type\":\"box\"}],                        {\"template\":{\"data\":{\"candlestick\":[{\"decreasing\":{\"line\":{\"color\":\"#000033\"}},\"increasing\":{\"line\":{\"color\":\"#000032\"}},\"type\":\"candlestick\"}],\"contourcarpet\":[{\"colorscale\":[[0.0,\"#000011\"],[0.1111111111111111,\"#000012\"],[0.2222222222222222,\"#000013\"],[0.3333333333333333,\"#000014\"],[0.4444444444444444,\"#000015\"],[0.5555555555555556,\"#000016\"],[0.6666666666666666,\"#000017\"],[0.7777777777777778,\"#000018\"],[0.8888888888888888,\"#000019\"],[1.0,\"#000020\"]],\"type\":\"contourcarpet\"}],\"contour\":[{\"colorscale\":[[0.0,\"#000011\"],[0.1111111111111111,\"#000012\"],[0.2222222222222222,\"#000013\"],[0.3333333333333333,\"#000014\"],[0.4444444444444444,\"#000015\"],[0.5555555555555556,\"#000016\"],[0.6666666666666666,\"#000017\"],[0.7777777777777778,\"#000018\"],[0.8888888888888888,\"#000019\"],[1.0,\"#000020\"]],\"type\":\"contour\"}],\"heatmap\":[{\"colorscale\":[[0.0,\"#000011\"],[0.1111111111111111,\"#000012\"],[0.2222222222222222,\"#000013\"],[0.3333333333333333,\"#000014\"],[0.4444444444444444,\"#000015\"],[0.5555555555555556,\"#000016\"],[0.6666666666666666,\"#000017\"],[0.7777777777777778,\"#000018\"],[0.8888888888888888,\"#000019\"],[1.0,\"#000020\"]],\"type\":\"heatmap\"}],\"histogram2d\":[{\"colorscale\":[[0.0,\"#000011\"],[0.1111111111111111,\"#000012\"],[0.2222222222222222,\"#000013\"],[0.3333333333333333,\"#000014\"],[0.4444444444444444,\"#000015\"],[0.5555555555555556,\"#000016\"],[0.6666666666666666,\"#000017\"],[0.7777777777777778,\"#000018\"],[0.8888888888888888,\"#000019\"],[1.0,\"#000020\"]],\"type\":\"histogram2d\"}],\"icicle\":[{\"textfont\":{\"color\":\"white\"},\"type\":\"icicle\"}],\"sankey\":[{\"textfont\":{\"color\":\"#000036\"},\"type\":\"sankey\"}],\"scatter\":[{\"marker\":{\"line\":{\"width\":0}},\"type\":\"scatter\"}],\"table\":[{\"cells\":{\"fill\":{\"color\":\"#000038\"},\"font\":{\"color\":\"#000037\"},\"line\":{\"color\":\"#000039\"}},\"header\":{\"fill\":{\"color\":\"#000040\"},\"font\":{\"color\":\"#000036\"},\"line\":{\"color\":\"#000039\"}},\"type\":\"table\"}],\"waterfall\":[{\"connector\":{\"line\":{\"color\":\"#000036\",\"width\":2}},\"decreasing\":{\"marker\":{\"color\":\"#000033\"}},\"increasing\":{\"marker\":{\"color\":\"#000032\"}},\"totals\":{\"marker\":{\"color\":\"#000034\"}},\"type\":\"waterfall\"}]},\"layout\":{\"coloraxis\":{\"colorscale\":[[0.0,\"#000011\"],[0.1111111111111111,\"#000012\"],[0.2222222222222222,\"#000013\"],[0.3333333333333333,\"#000014\"],[0.4444444444444444,\"#000015\"],[0.5555555555555556,\"#000016\"],[0.6666666666666666,\"#000017\"],[0.7777777777777778,\"#000018\"],[0.8888888888888888,\"#000019\"],[1.0,\"#000020\"]]},\"colorscale\":{\"diverging\":[[0.0,\"#000021\"],[0.1,\"#000022\"],[0.2,\"#000023\"],[0.3,\"#000024\"],[0.4,\"#000025\"],[0.5,\"#000026\"],[0.6,\"#000027\"],[0.7,\"#000028\"],[0.8,\"#000029\"],[0.9,\"#000030\"],[1.0,\"#000031\"]],\"sequential\":[[0.0,\"#000011\"],[0.1111111111111111,\"#000012\"],[0.2222222222222222,\"#000013\"],[0.3333333333333333,\"#000014\"],[0.4444444444444444,\"#000015\"],[0.5555555555555556,\"#000016\"],[0.6666666666666666,\"#000017\"],[0.7777777777777778,\"#000018\"],[0.8888888888888888,\"#000019\"],[1.0,\"#000020\"]],\"sequentialminus\":[[0.0,\"#000011\"],[0.1111111111111111,\"#000012\"],[0.2222222222222222,\"#000013\"],[0.3333333333333333,\"#000014\"],[0.4444444444444444,\"#000015\"],[0.5555555555555556,\"#000016\"],[0.6666666666666666,\"#000017\"],[0.7777777777777778,\"#000018\"],[0.8888888888888888,\"#000019\"],[1.0,\"#000020\"]]},\"colorway\":[\"#000001\",\"#000002\",\"#000003\",\"#000004\",\"#000005\",\"#000006\",\"#000007\",\"#000008\",\"#000009\",\"#000010\"]}},\"xaxis\":{\"anchor\":\"y\",\"domain\":[0.0,1.0],\"title\":{\"text\":\"\"}},\"yaxis\":{\"anchor\":\"x\",\"domain\":[0.0,1.0],\"title\":{\"text\":\"\"}},\"legend\":{\"tracegroupgap\":0},\"margin\":{\"t\":60},\"boxmode\":\"group\",\"height\":500,\"width\":500,\"title\":{\"font\":{\"size\":22,\"color\":\"#164f5e\"},\"text\":\"Oppo%+\",\"automargin\":true,\"yref\":\"paper\"}},                        {\"responsive\": true}                    ).then(function(){\n",
       "                            \n",
       "var gd = document.getElementById('4329593b-802b-41fc-820a-47113563268c');\n",
       "var x = new MutationObserver(function (mutations, observer) {{\n",
       "        var display = window.getComputedStyle(gd).display;\n",
       "        if (!display || display === 'none') {{\n",
       "            console.log([gd, 'removed!']);\n",
       "            Plotly.purge(gd);\n",
       "            observer.disconnect();\n",
       "        }}\n",
       "}});\n",
       "\n",
       "// Listen for the removal of the full notebook cells\n",
       "var notebookContainer = gd.closest('#notebook-container');\n",
       "if (notebookContainer) {{\n",
       "    x.observe(notebookContainer, {childList: true});\n",
       "}}\n",
       "\n",
       "// Listen for the clearing of the current output cell\n",
       "var outputEl = gd.closest('.output');\n",
       "if (outputEl) {{\n",
       "    x.observe(outputEl, {childList: true});\n",
       "}}\n",
       "\n",
       "                        })                };                });            </script>        </div>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "fig_53 = px.box(\n",
    "    df.query(\"Season==2023\"),\n",
    "    y = \"Oppo%+\",\n",
    "    points=\"all\",\n",
    "    hover_name = \"Name\",\n",
    "    height = 500,\n",
    "    width = 500,\n",
    ")\n",
    "\n",
    "fig_53.update_traces(marker=dict(color=\"#7284cc\"))\n",
    "\n",
    "fig_53.update_layout(\n",
    "    title=dict(text=\"Oppo%+\", font=dict(size=22), automargin=True, yref='paper'),\n",
    "    title_font_color=\"#164f5e\",\n",
    "    yaxis=dict(title=\"\"),\n",
    "    xaxis=dict(title=\"\")\n",
    ")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "aa83dad3",
   "metadata": {},
   "source": [
    "### Row 1 - Print"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 102,
   "id": "aab386d4",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Title\n",
    "st.markdown('<span style=\"font-family: Lato, sans-serif; font-size: 28px; color: #2f4858; font-weight: bold;\">Batting Domains</span>', unsafe_allow_html=True)\n",
    "\n",
    "# Create the tabs\n",
    "tabs = st.tabs([\"Overall\", \"Power\", \"Contact\", \"Plate Discipline\", \"Pull/Oppo\"])\n",
    "\n",
    "# Display the charts within the tabs\n",
    "with tabs[0]:\n",
    "    col1, col2, col3 = st.columns(3)\n",
    "    col1.plotly_chart(fig_11, theme=\"streamlit\", use_container_width=False)\n",
    "    col2.plotly_chart(fig_12, theme=\"streamlit\", use_container_width=False)\n",
    "    col3.plotly_chart(fig_13, theme=\"streamlit\", use_container_width=False)\n",
    "\n",
    "with tabs[1]:\n",
    "    col4, col5, col6 = st.columns(3)\n",
    "    col4.plotly_chart(fig_21, theme=\"streamlit\", use_container_width=False)\n",
    "    col5.plotly_chart(fig_22, theme=\"streamlit\", use_container_width=False)\n",
    "    col6.plotly_chart(fig_23, theme=\"streamlit\", use_container_width=False)\n",
    "\n",
    "with tabs[2]:\n",
    "    col7, col8, col9 = st.columns(3)\n",
    "    col7.plotly_chart(fig_31, theme=\"streamlit\", use_container_width=False)\n",
    "    col8.plotly_chart(fig_32, theme=\"streamlit\", use_container_width=False)\n",
    "    col9.plotly_chart(fig_33, theme=\"streamlit\", use_container_width=False)\n",
    "    \n",
    "with tabs[3]:\n",
    "    col10, col11, col12 = st.columns(3)\n",
    "    col10.plotly_chart(fig_41, theme=\"streamlit\", use_container_width=False)\n",
    "    col11.plotly_chart(fig_42, theme=\"streamlit\", use_container_width=False)\n",
    "    col12.plotly_chart(fig_43, theme=\"streamlit\", use_container_width=False)\n",
    "    \n",
    "with tabs[4]:\n",
    "    col13, col14, col15 = st.columns(3)\n",
    "    col13.plotly_chart(fig_51, theme=\"streamlit\", use_container_width=False)\n",
    "    col14.plotly_chart(fig_52, theme=\"streamlit\", use_container_width=False)\n",
    "    col15.plotly_chart(fig_53, theme=\"streamlit\", use_container_width=False)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "ee538f99",
   "metadata": {},
   "source": [
    "## Row 2"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "a54f05ee",
   "metadata": {},
   "source": [
    "### Raw Data"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 103,
   "id": "e9fe8535",
   "metadata": {},
   "outputs": [],
   "source": [
    "from st_aggrid import AgGrid, GridOptionsBuilder, DataReturnMode, JsCode"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 104,
   "id": "b3172d4a",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Builds a gridOptions dictionary using a GridOptionsBuilder instance.\n",
    "builder = GridOptionsBuilder.from_dataframe(df)\n",
    "\n",
    "# Configs\n",
    "builder.configure_side_bar(filters_panel=True, columns_panel=True)\n",
    "\n",
    "# Column Grouping\n",
    "column_defs = [\n",
    "    {\n",
    "        \"headerName\": \"Player\",\n",
    "        \"field\": \"Name\",\n",
    "        \"headerClass\": \"column-header\",\n",
    "        \"width\": 150,\n",
    "        \"pinned\": \"left\",\n",
    "        \"enableRowGroup\": True,  # Enable row grouping on the \"Name\" column\n",
    "        \"enableValue\": False,  # Disable column aggregation for the \"Name\" column\n",
    "    },\n",
    "    {\n",
    "        \"headerName\": \"Player Details\",\n",
    "        \"children\": [\n",
    "            {\n",
    "                \"field\": \"Team\",\n",
    "                \"headerName\": \"Team\",\n",
    "                \"width\": 150,\n",
    "                \"enableRowGroup\": True,  # Enable row grouping on the \"Team\" column\n",
    "                \"enableValue\": False,  # Disable column aggregation for the \"Team\" column\n",
    "            },\n",
    "            {\"field\": \"Age\", \"headerName\": \"Age\", \"width\": 150, \"enableValue\": True},\n",
    "            {\"field\": \"AB\", \"headerName\": \"At Bats\", \"width\": 150, \"enableValue\": True},\n",
    "        ],\n",
    "    },\n",
    "    {\n",
    "        \"headerName\": \"Batting Summary\",\n",
    "        \"children\": [\n",
    "            {\"field\": \"wRC+\", \"headerName\": \"wRC+\", \"sort\": \"desc\", \"width\": 150, \"enableValue\": True},\n",
    "            {\"field\": \"Bat\", \"headerName\": \"Batting WAR\", \"width\": 150, \"enableValue\": True},\n",
    "            {\"field\": \"Pos\", \"headerName\": \"Pos Batting WAR\", \"width\": 150, \"enableValue\": True},\n",
    "        ],\n",
    "    },\n",
    "    {\n",
    "        \"headerName\": \"Power\",\n",
    "        \"children\": [\n",
    "            {\"field\": \"Soft%+\", \"headerName\": \"Soft Hit%+\", \"width\": 150, \"enableValue\": True},\n",
    "            {\"field\": \"Med%+\", \"headerName\": \"Med Hit%+\", \"width\": 150, \"enableValue\": True},\n",
    "            {\"field\": \"Hard%+\", \"headerName\": \"Hard Hit%+\", \"width\": 150, \"enableValue\": True},\n",
    "            {\"field\": \"HR\", \"headerName\": \"Home Runs\", \"width\": 150, \"enableValue\": True},\n",
    "        ],\n",
    "    },\n",
    "    {\n",
    "        \"headerName\": \"Contact\",\n",
    "        \"children\": [\n",
    "            {\"field\": \"Contact%\", \"headerName\": \"Contact%\", \"width\": 150, \"enableValue\": True},\n",
    "            {\"field\": \"Z-Contact%\", \"headerName\": \"In-Zone Contact%\", \"width\": 150, \"enableValue\": True},\n",
    "            {\"field\": \"O-Contact%\", \"headerName\": \"Out-Zone Contact%\", \"width\": 150, \"enableValue\": True},\n",
    "            {\"field\": \"BABIP+\", \"headerName\": \"BABIP+\", \"width\": 150, \"enableValue\": True},\n",
    "        ],\n",
    "    },\n",
    "    {\n",
    "        \"headerName\": \"Plate Discipline\",\n",
    "        \"children\": [\n",
    "            {\"field\": \"BB%+\", \"headerName\": \"Walk%+\", \"width\": 150, \"enableValue\": True},\n",
    "            {\"field\": \"K%+\", \"headerName\": \"Strikeout%+\", \"width\": 150, \"enableValue\": True},\n",
    "            {\"field\": \"Swing%\", \"headerName\": \"Swing%\", \"width\": 150, \"enableValue\": True},\n",
    "            {\"field\": \"Z-Swing%\", \"headerName\": \"In-Zone Swing%\", \"width\": 150, \"enableValue\": True},\n",
    "            {\"field\": \"O-Swing%\", \"headerName\": \"Out-Zone Swing%\", \"width\": 150, \"enableValue\": True},\n",
    "        ],\n",
    "    },\n",
    "    {\n",
    "        \"headerName\": \"Pull/Oppo\",\n",
    "        \"children\": [\n",
    "            {\"field\": \"Pull%+\", \"headerName\": \"Pull%+\", \"width\": 150, \"enableValue\": True},\n",
    "            {\"field\": \"Cent%+\", \"headerName\": \"Cent%+\", \"width\": 150, \"enableValue\": True},\n",
    "            {\"field\": \"Oppo%+\", \"headerName\": \"Oppo%+\", \"width\": 150, \"enableValue\": True},\n",
    "        ],\n",
    "    },\n",
    "]\n",
    "\n",
    "\n",
    "# Merge columnDefs with existing column definitions\n",
    "grid_options = {\"columnDefs\": column_defs}\n",
    "\n",
    "# Launch\n",
    "go = grid_options\n",
    "\n",
    "col1, col2 = st.columns([98, 2])\n",
    "\n",
    "with col1:\n",
    "    st.write('<div style=\"display: flex; align-items: baseline;\"><span style=\"font-family: Lato, sans-serif; font-size: 28px; font-weight: bold; color: #2f4858; margin-right: auto;\">Browse Data</span><span>Default Sort: wRC+</span></div>', unsafe_allow_html=True)\n",
    "    grid_response = AgGrid(\n",
    "        df,\n",
    "        gridOptions=go,\n",
    "        theme=\"streamlit\",\n",
    "        height=600\n",
    "    )\n",
    "\n",
    "with col2:\n",
    "    st.subheader(\"\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 105,
   "id": "fb6c2c89",
   "metadata": {},
   "outputs": [
    {
     "ename": "FileNotFoundError",
     "evalue": "[Errno 2] No such file or directory: 'assets/stevens_bat.jpg'",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mFileNotFoundError\u001b[0m                         Traceback (most recent call last)",
      "Cell \u001b[1;32mIn[105], line 3\u001b[0m\n\u001b[0;32m      1\u001b[0m \u001b[38;5;66;03m# Import Asset\u001b[39;00m\n\u001b[0;32m      2\u001b[0m \u001b[38;5;28;01mfrom\u001b[39;00m \u001b[38;5;21;01mPIL\u001b[39;00m \u001b[38;5;28;01mimport\u001b[39;00m Image\n\u001b[1;32m----> 3\u001b[0m header_img \u001b[38;5;241m=\u001b[39m \u001b[43mImage\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mopen\u001b[49m\u001b[43m(\u001b[49m\u001b[38;5;124;43m'\u001b[39;49m\u001b[38;5;124;43massets/stevens_bat.jpg\u001b[39;49m\u001b[38;5;124;43m'\u001b[39;49m\u001b[43m)\u001b[49m\n\u001b[0;32m      5\u001b[0m \u001b[38;5;66;03m# Print as Columns\u001b[39;00m\n\u001b[0;32m      6\u001b[0m st\u001b[38;5;241m.\u001b[39mmarkdown(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m\"\u001b[39m)\n",
      "File \u001b[1;32m~\\anaconda3\\envs\\ninebase\\lib\\site-packages\\PIL\\Image.py:3236\u001b[0m, in \u001b[0;36mopen\u001b[1;34m(fp, mode, formats)\u001b[0m\n\u001b[0;32m   3233\u001b[0m     filename \u001b[38;5;241m=\u001b[39m fp\n\u001b[0;32m   3235\u001b[0m \u001b[38;5;28;01mif\u001b[39;00m filename:\n\u001b[1;32m-> 3236\u001b[0m     fp \u001b[38;5;241m=\u001b[39m \u001b[43mbuiltins\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mopen\u001b[49m\u001b[43m(\u001b[49m\u001b[43mfilename\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[38;5;124;43m\"\u001b[39;49m\u001b[38;5;124;43mrb\u001b[39;49m\u001b[38;5;124;43m\"\u001b[39;49m\u001b[43m)\u001b[49m\n\u001b[0;32m   3237\u001b[0m     exclusive_fp \u001b[38;5;241m=\u001b[39m \u001b[38;5;28;01mTrue\u001b[39;00m\n\u001b[0;32m   3239\u001b[0m \u001b[38;5;28;01mtry\u001b[39;00m:\n",
      "\u001b[1;31mFileNotFoundError\u001b[0m: [Errno 2] No such file or directory: 'assets/stevens_bat.jpg'"
     ]
    }
   ],
   "source": [
    "# Import Asset\n",
    "from PIL import Image\n",
    "header_img = Image.open('assets/stevens_bat.jpg')\n",
    "\n",
    "# Print as Columns\n",
    "st.markdown(\"\")\n",
    "img_col1, img_col2, img_col3 = st.columns([20,60,20])\n",
    "\n",
    "with img_col1:\n",
    "    pass\n",
    "\n",
    "with img_col2:\n",
    "    st.image('assets/cards_at_mets.jpg')\n",
    "\n",
    "with img_col3:\n",
    "    pass"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "0590a229",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "id": "d1a7bb72",
   "metadata": {},
   "source": [
    "### Playground"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f6425657",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ee211706",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "bd3c5b56",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.11"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
