import streamlit as st
import pyodbc
import pandas as pd
import numpy as np


 
#conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=D:\CCLPIHybridweb\Database3_be.accdb;')
#users_agent = 'SELECT users.userid, users.username, agents.AgentID FROM agents INNER JOIN users ON agents.AgentID = users.agent_ID;'

#cursor = conn.cursor(conn)

#cursor.execute('SELECT username, userid from users')

# Title
st.title("Login Page")

# Username input
username = st.text_input("Username")

# Password input
password = st.text_input("Password", type="password")

# Login button
if st.button("Login"):
    if username == "admin" and password == "password":
        st.success("Logged in successfully!")
    else:
        st.error("Invalid username or password")



