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
        last_cleaned_date = datetime.strptime(df.at[index,'Last Cleaned'], '%Y-%m-%d').date()
        new_date=(last_cleaned_date+timedelta(days=2))
        st.write(f"<span style='color:green'>Room {row['Room']} has already been cleaned</span>", unsafe_allow_html=True)
        st.write(f"<span style='color:green'>Next Cleaning date is {new_date}</span>", unsafe_allow_html=True)

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
            df.at[index,'Comment']=''
            checkbox_placeholder.empty()
            st.write(f"<span style='color:green'>Status Updated for your room</span>", unsafe_allow_html=True)
            st.write(f"<span style='color:green'>Next cleaning will be on {new_date}</span>", unsafe_allow_html=True)

    df['Comment'] = df['Comment'].fillna('')
    comment = df.at[index, 'Comment']
    if comment:
        st.markdown(f"<h6 style='color:red;margin-top:0;font-family:Arial;'>{comment}</h6>", unsafe_allow_html=True)




    df.to_csv('data.csv', index=False)
