import streamlit as st
import pandas as pd
from datetime import date, timedelta, datetime

df = pd.read_csv('data.csv')
sort_by_last_cleaned = st.sidebar.checkbox('Sort by last cleaned date')

for index, row in df.iterrows():
    last_cleaned_date = datetime.strptime(df.at[index,'Last Cleaned'], '%Y-%m-%d').date()
    days_since_cleaned = (date.today() - last_cleaned_date).days
    
    if days_since_cleaned >= 2:  # room was last cleaned on 24 and today is 26 or later
        df.at[index,'Status'] = 'Dirty'

        
for index, row in df.iterrows():
    new_status = st.selectbox(f"Room {row['Room']}: {row['Status']}", ['', 'Clean'])
     
    if new_status:
        if new_status!= df.at[index,'Status']:
            df.at[index, 'Last Cleaned'] = str(date.today())
        df.at[index, 'Status'] = new_status

df.to_csv('data.csv', index=False)
st.table(df)
