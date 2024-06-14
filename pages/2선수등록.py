import streamlit as st
import pandas as pd
import pymysql
import json
from Modules.Module_sendDiscord import sendDiscord

def get_SQL():
    try:
        db = pymysql.connect(
            host=st.secrets["MYSQL"]["host"], 
            user=st.secrets["MYSQL"]["user"], 
            password=st.secrets["MYSQL"]["password"], 
            db=st.secrets["MYSQL"]["db"], 
            charset="utf8mb4"
        )
        SQL = db.cursor()
        SQL.execute("SET NAMES utf8mb4")
        return db, SQL
    except Exception as e:
        print(e)
        return False, False

def load_players():
    db, SQL = get_SQL()
    if not db:
        return pd.DataFrame()

    try:
        query = "SELECT datas FROM bssmEsport"
        SQL.execute(query)
        rows = SQL.fetchall()
        data = [json.loads(row[0]) for row in rows]  # JSON 문자열을 파이썬 딕셔너리로 변환
        players_df = pd.DataFrame(data)
        return players_df
    except Exception as e:
        print(e)
        return pd.DataFrame()
    finally:
        db.close()

def save_players(new_players_json):
    db, SQL = get_SQL()
    if not db:
        return

    try:
        SQL.execute("INSERT INTO bssmEsport (datas) VALUES (%s)", (new_players_json,))
        db.commit()
    
    except Exception as e:
        print(e)
    
    finally:
        db.close()

def register_player():
    st.header("Register New Player")

    players_df = load_players()

    team = st.selectbox("Team", ["1기", "2기", "3기", "4기"])
    game = st.selectbox("Game", ["LOL", "FIFA", "Valorant"])

    if game in ["LOL", "Valorant"]:
        st.subheader(f"{game}의 게임은 7명의 플레이어(5명의 주전, 2명의 예비)를 등록 하여 주시기 바랍니다.")

        ids = []
        names = []
        nicks = []

        for i in range(7):
            cols = st.columns(3)
            with cols[0]:
                ids.append(st.text_input(label=f"학번 {i+1}", value=f"110{i+1}"))
            with cols[1]:
                names.append(st.text_input(label=f"이름 {i+1}", value=f"홍길동{i+1}"))
            with cols[2]:
                nicks.append(st.text_input(label=f"인게임 ID {i+1}", value=f"Hide on Bush#kr{i+1}"))

        if st.button("선수 등록하기"):
            errors = []
            new_players = []
            for i in range(7):
                try:
                    new_player = {
                        "학번": ids[i],
                        "이름": names[i],
                        "게임ID": nicks[i]
                    }
                    players_df = pd.concat([players_df, pd.DataFrame([new_player])], ignore_index=True)
                    new_players.append(new_player)
                except Exception as e:
                    errors.append(f"{e}")

            if errors:
                for error in errors:
                    st.error(error)
            else:
                # 팀과 게임 정보를 포함하여 JSON 문자열로 변환
                new_players_json = json.dumps({
                    "team": team,
                    "game": game,
                    "users": new_players
                }, ensure_ascii=False)  # ensure_ascii=False를 통해 한글이 깨지지 않게 함
                save_players(new_players_json)
                st.success("정상적으로 등록이 완료 되었습니다!")
                sendDiscord(
                    url=st.secrets["webhookURL"],
                    title=f"선수 등록 안내 - {game}",
                    text="\n\n".join([f"> **{player['이름']}({player['학번']})** \n  ㄴ 기수: {team} \n  ㄴ ID: {player['게임ID']}" for player in new_players])
                )

    else:
        st.subheader(f"Register a Player for {game}")
        
        cols = st.columns(3)
        with cols[0]:
            id = st.text_input(label="학번", value="1101")
        with cols[1]:
            name = st.text_input(label="이름", value="홍길동")
        with cols[2]:
            nick = st.text_input(label="인게임 ID", value="Hide on Bush#kr1")

        if st.button("선수 등록하기"):
            new_players = []
            try:
                new_player = {
                    "학번": id,
                    "이름": name,
                    "게임ID": nick,
                    "기수": team,
                    "종목": game
                }
                players_df = pd.concat([players_df, pd.DataFrame([new_player])], ignore_index=True)
                new_players.append(new_player)
                new_players_json = json.dumps({
                    "team": team,
                    "game": game,
                    "users": new_players
                }, ensure_ascii=False)  # ensure_ascii=False를 통해 한글이 깨지지 않게 함
                save_players(new_players_json)
                st.success(f"Player {name} registered!")
                sendDiscord(
                    url=st.secrets["webhookURL"],
                    title=f"선수 등록 안내 - {game}",
                    text=f"> **{new_player['이름']}({new_player['학번']})** \n  ㄴ 기수: {team} \n  ㄴ ID: {new_player['게임ID']}"
                )

            except Exception as e:
                st.error(f"{e}")

if __name__ == '__main__':
    register_player()
