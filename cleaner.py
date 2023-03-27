import streamlit as st
import pandas as pd
from datetime import date, timedelta, datetime


def cleaner():
    df = pd.read_csv('data.csv')

    df['Room'] = df['Room'].astype(str)
    df['Comment'] = df['Comment'].fillna('')


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
                comment_placeholder = st.empty()
                button_placeholder = st.empty()
                comment = comment_placeholder.text_input(f"Add a comment for Room {row['Room']}:")
                if button_placeholder.button("Submit"):
                    df.at[index, 'Comment'] = comment
                    comment_placeholder.write(f"Comment added for Room {row['Room']}.")
                    comment_placeholder.empty()
                    button_placeholder.empty()

        except:
            st.write(f"No such room found with name {search_term}.")

    show= df[df['Status'] == 'Dirty']
    if sort_by_last_cleaned:
        show = show.sort_values('Last Cleaned')
    show = show.reset_index(drop=True)

    st.table(show)

    df.to_csv('data.csv', index=False)
