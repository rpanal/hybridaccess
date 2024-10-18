from sqlalchemy import ColumnElement, true
import streamlit as st
import pyodbc
import pandas as pd
import numpy as np
import streamlit as st
#from multipage import MultiPage
#from pages import page1, page2
 
#conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=Database3_be.accdb;')

#relate = 'SELECT username, password FROM users ORDER BY username;'

#relatefile = pd.read_sql(relate,conn,)

# Main


# Title with Markdown formatting

st.markdown("# CCLPI - Hybrid ")

# Add a title to the sidebar

# Add a selectbox to the sidebar
option = st.sidebar.selectbox(
    "Select an option:",
    ["Option 1", "Option 2", "Option 3"]
)

#app = MultiPage()

# Add pages to the app
#app.add_page("Page 1", page1.app)
#app.add_page("Page 2", page2.app)

# Run the app
#app.run()

