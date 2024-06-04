import streamlit as st
import pandas as pd

def load_schedule():
    return pd.read_csv('data/schedule.csv')

def save_schedule(schedule_df):
    schedule_df.to_csv('data/schedule.csv', index=False)

def manage_schedule():
    st.header("Manage Schedule")

    schedule_df = load_schedule()

    st.dataframe(schedule_df)

    if st.button("Add New Match"):
        new_match = {
            "game": st.selectbox("Game", ["LOL", "FIFA", "Valorant"]),
            "team1": st.text_input("Team 1"),
            "team2": st.text_input("Team 2"),
            "date": st.date_input("Match Date"),
            "time": st.time_input("Match Time")
        }

        if st.button("Save Match"):
            schedule_df = schedule_df.append(new_match, ignore_index=True)
            save_schedule(schedule_df)
            st.success("New match added!")

    st.write("To remove a match, select the index and press remove")
    index_to_remove = st.number_input("Index to remove", min_value=0, max_value=len(schedule_df)-1, step=1)

    if st.button("Remove Match"):
        schedule_df = schedule_df.drop(index_to_remove)
        save_schedule(schedule_df)
        st.success("Match removed!")

    st.dataframe(schedule_df)
