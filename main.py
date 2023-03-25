import streamlit as st
from datetime import date, datetime, timedelta
import pandas as pd
import csv

data = {
    'Room': ['101', '102', '103', '104', '105'],
    'Status': ['Clean', 'Clean', 'Clean', 'Clean', 'Clean'],
    'Last Cleaned': ['2023-03-24', '2023-03-23', '2023-03-22', '2023-03-21', '2023-03-20']
}
df = pd.DataFrame(data)
# status_options = ['All', 'Clean', 'Dirty']


# selected_status = st.sidebar.selectbox('Select status', status_options)

sort_by_last_cleaned = st.sidebar.checkbox('Sort by last cleaned date')


# if selected_status == 'All':
#     filtered_df = df
# else:
#     filtered_df = df[df['Status'] == selected_status]
# if sort_by_last_cleaned:
#     df = df.sort_values('Last Cleaned')
        
for index, row in df.iterrows():
    if df.at[index,'Last Cleaned'] != str(date.today()-timedelta(days=1)):
        df.at[index,'Status']='Dirty'
        
for index, row in df.iterrows():
    new_status = st.selectbox(f"Room {row['Room']}: {row['Status']}", ['', 'Clean'])
     
    if new_status:
        if new_status!= df.at[index,'Status']:
            df.at[index, 'Last Cleaned'] = str(date.today())
            if sort_by_last_cleaned:
                df = df.sort_values('Last Cleaned')
        df.at[index, 'Status'] = new_status

st.table(df)
