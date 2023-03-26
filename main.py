import pickle
from pathlib import Path
import streamlit as st 
import streamlit_authenticator as stauth 
import pandas as pd
from cleaner import cleaner
from users import users
st.set_page_config(page_title='Room Cleaning Tracker', page_icon=':broom:')
hide_streamlit_footer = """<style>#MainMenu {visibility: hidden;}
                        footer {visibility: hidden;}</style>"""
st.markdown(hide_streamlit_footer, unsafe_allow_html=True)

names = ["Ritik", "Raju"]
usernames = ["104", "admin"]

# load hashed passwords
file_path = Path(__file__).parent / "hashed_pw.pkl"
with file_path.open("rb") as file:
    hashed_passwords = pickle.load(file)

authenticator = stauth.Authenticate(names, usernames, hashed_passwords,
    "PRO4", "abcdef", cookie_expiry_days=30)

name, authentication_status, username = authenticator.login("Login", "main")

if authentication_status == False:
    st.error("Username/password is incorrect")

# if authentication_status == None:
#     st.warning("Please enter your username and password")

if authentication_status and username=='admin':
    authenticator.logout("Logout", "sidebar")
    st.sidebar.title(f"Welcome {name}")
    cleaner()

if authentication_status and username!='admin':
    st.write(f"<h1 style='text-align:left; color:blck; font-size: 30px;'>Welcome {name}!</h1>", unsafe_allow_html=True)
    authenticator.logout("Logout", "sidebar")
    st.sidebar.title(f"Welcome {name}")
    users(username)
