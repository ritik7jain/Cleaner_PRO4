import streamlit as st
import pandas as pd
from datetime import date, timedelta, datetime

def users(username):
    df = pd.read_csv('data.csv')
    df['Room'] = df['Room'].astype(str)
    Room = username
    searched = df[df['Room'].str.contains(Room, case=False)]  
    index = searched.index[0]
    row = searched.iloc[0]
    if df.at[index,'Status']=='Clean':
        st.write(f"Room {row['Room']} has already been cleaned.")
    else:
        checkbox_placeholder = st.empty()
        new_status = checkbox_placeholder.checkbox(f"Room {row['Room']}: {row['Status']} - Mark as clean")
        if new_status:
            new_status = 'Clean'
            if new_status!= df.at[index,'Status']:
                df.at[index, 'Last Cleaned'] = str(date.today())
            df.at[index, 'Status'] = new_status
            checkbox_placeholder.empty()
            new_date=(datetime.today()+timedelta(days=2)).date()

            checkbox_placeholder.text(f"Status Updated for your room - next cleaning will be on {new_date}")
        df.to_csv('data.csv', index=False)
