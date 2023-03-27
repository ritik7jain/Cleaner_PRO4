import pickle
from pathlib import Path

import streamlit_authenticator as stauth

names = ["Ritik", "Niharika", "Gaurav", "Arun", "Hiten", "Ashima","Raju",'Ajith']
usernames = ["104", "105","4","507","106","107","admin","superadmin"]
passwords = ["Pro4@104", "Pro4@105","Pro4@004","Pro4@507","Pro4@106","Pro4@107","root@123","admin@123"]

hashed_passwords = stauth.Hasher(passwords).generate()

file_path = Path(__file__).parent / "hashed_pw.pkl"
with file_path.open("wb") as file:
    pickle.dump(hashed_passwords, file)