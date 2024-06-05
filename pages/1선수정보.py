import streamlit as st
import pandas as pd

def load_players():
    return pd.read_csv('data/players.csv', dtype={'학번': str})

def display_roster():
    st.header("Player Roster")

    # 선수 데이터 불러오기
    players_df = load_players()

    # 기수 및 종목 선택
    selected_team = st.selectbox("Select Team", players_df['기수'].unique())
    selected_game = st.selectbox("Select Game", players_df['종목'].unique())

    # 선택된 기수 및 종목에 따라 데이터 필터링
    filtered_df = players_df[(players_df['기수'] == selected_team) & (players_df['종목'] == selected_game)]

    # 인덱스를 리셋하여 제거
    filtered_df = filtered_df.reset_index(drop=True)

    st.subheader(f"Players in {selected_team} - {selected_game}")
    st.table(filtered_df)

if __name__ == '__main__':
    display_roster()