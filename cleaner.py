import streamlit as st
import pandas as pd
from datetime import date, timedelta, datetime

def cleaner():
    df = pd.read_csv('data.csv')

    df['Room'] = df['Room'].astype(str)


    sort_by_last_cleaned = st.sidebar.checkbox('Sort by last cleaned date')


    search_term = st.text_input("Search for room")


    for index, row in df.iterrows():
        last_cleaned_date = datetime.strptime(df.at[index,'Last Cleaned'], '%Y-%m-%d').date()
        days_since_cleaned = (date.today() - last_cleaned_date).days
        
        if days_since_cleaned >= 2:  
            df.at[index,'Status'] = 'Dirty'
    if search_term:
        try:
            searched = df[df['Room'].str.contains(search_term, case=False)]  
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
        except:
            st.write(f"No such room found with name {search_term}.")

    show= df[df['Status'] == 'Dirty']
    if sort_by_last_cleaned:
        show = show.sort_values('Last Cleaned')
    show = show.reset_index(drop=True)

    st.table(show)

    df.to_csv('data.csv', index=False)
