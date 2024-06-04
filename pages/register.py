import streamlit as st
import pandas as pd

def load_players():
    return pd.read_csv('data/players.csv')

def save_players(players_df):
    players_df.to_csv('data/players.csv', index=False)

def register_player():
    st.header("Register New Player")

    players_df = load_players()
    id = st.text_input(label="학번", value="1101")
    name = st.text_input(label="이름", value="홍길동")
    nick = st.text_input(label="인게임 ID", value="Hide on Bush#kr1")
    team = st.selectbox("Team", ["1기", "2기", "3기", "4기"])
    game = st.selectbox("Game", ["LOL", "FIFA", "Valorant"])

    if st.button("선수 등록하기"):
        new_player = pd.DataFrame({
            "학번": [id],
            "이름": [name],
            "게임ID": [nick],
            "기수": [team],
            "종목": [game]
        })
        players_df = pd.concat([players_df, new_player], ignore_index=True)
        save_players(players_df)
        st.success(f"Player {name} registered!")

    st.header("Registered Players")
    st.dataframe(players_df)

if __name__ == '__main__':
    register_player()
