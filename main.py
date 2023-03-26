import pickle
from pathlib import Path
import streamlit as st 
import streamlit_authenticator as stauth 
import pandas as pd
from cleaner import cleaner
from users import users
names = ["Ritik", "Raju"]
usernames = ["104", "admin"]
st.set_page_config(page_title='Room Cleaning Tracker', page_icon=':broom:')
# load hashed passwords
file_path = Path(__file__).parent / "hashed_pw.pkl"
with file_path.open("rb") as file:
    hashed_passwords = pickle.load(file)

authenticator = stauth.Authenticate(names, usernames, hashed_passwords,
    "PRO4", "abcdef", cookie_expiry_days=30)

name, authentication_status, username = authenticator.login("Login", "main")

if authentication_status == False:
    st.error("Username/password is incorrect")

if authentication_status == None:
    st.warning("Please enter your username and password")

if authentication_status and username=='admin':
    st.write("welcome")
    authenticator.logout("Logout", "sidebar")
    st.sidebar.title(f"Welcome {name}")
    cleaner()

if authentication_status and username!='admin':
    st.write("welcome")
    authenticator.logout("Logout", "sidebar")
    st.sidebar.title(f"Welcome {name}")
    users(username)
