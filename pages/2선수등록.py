import streamlit as st
import pandas as pd

def load_players():
    return pd.read_csv('data/players.csv', dtype={'학번': str})

def save_players(players_df):
    players_df.to_csv('data/players.csv', index=False)

def register_player():
    st.header("Register New Player")

    players_df = load_players()

    # 팀 기수를 맨 위로 배치
    team = st.selectbox("Team", ["1기", "2기", "3기", "4기"])

    # 게임 선택
    game = st.selectbox("Game", ["LOL", "FIFA", "Valorant"])

    if game in ["LOL", "Valorant"]:
        st.subheader(f"Register 5 Players for {game}")

        ids = []
        names = []
        nicks = []

        # 학번, 이름, 게임 아이디를 가로로 배치
        for i in range(5):
            cols = st.columns(3)
            with cols[0]:
                ids.append(st.text_input(label=f"학번 {i+1}", value=f"110{i+1}"))
            with cols[1]:
                names.append(st.text_input(label=f"이름 {i+1}", value=f"홍길동{i+1}"))
            with cols[2]:
                nicks.append(st.text_input(label=f"인게임 ID {i+1}", value=f"Hide on Bush#kr{i+1}"))

        if st.button("선수 등록하기"):
            errors = []
            for i in range(5):
                if ((players_df['학번'] == ids[i]) & (players_df['종목'] == game)).any():
                    errors.append(f"Player with ID {ids[i]} and Game {game} already exists!")
                else:
                    new_player = pd.DataFrame({
                        "학번": [ids[i]],
                        "이름": [names[i]],
                        "게임ID": [nicks[i]],
                        "기수": [team],
                        "종목": [game]
                    })
                    players_df = pd.concat([players_df, new_player], ignore_index=True)
            if errors:
                for error in errors:
                    st.error(error)
            else:
                save_players(players_df)
                st.success("Players registered successfully!")

    else:
        st.subheader(f"Register a Player for {game}")
        
        # 학번, 이름, 게임 아이디를 가로로 배치
        cols = st.columns(3)
        with cols[0]:
            id = st.text_input(label="학번", value="1101")
        with cols[1]:
            name = st.text_input(label="이름", value="홍길동")
        with cols[2]:
            nick = st.text_input(label="인게임 ID", value="Hide on Bush#kr1")

        if st.button("선수 등록하기"):
            if ((players_df['학번'] == id) & (players_df['종목'] == game)).any():
                st.error(f"Player with ID {id} and Game {game} already exists!")
            else:
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
