import streamlit as st
import pandas as pd
import pymysql
import json

# MySQL 연결 함수
def get_SQL():
    try:
        db = pymysql.connect(
            host=st.secrets["MYSQL"]["host"], 
            user=st.secrets["MYSQL"]["user"], 
            password=st.secrets["MYSQL"]["password"], 
            db=st.secrets["MYSQL"]["db"], 
            charset="utf8"
        )
        SQL = db.cursor()
        return db, SQL
    except Exception as e:
        st.error(f"Error connecting to database: {e}")
        return None, None

# 선수 데이터를 로드하는 함수
def load_players():
    db, SQL = get_SQL()
    if not db:
        return pd.DataFrame()

    try:
        query = "SELECT datas FROM bssmEsport"
        SQL.execute(query)
        rows = SQL.fetchall()
        
        all_players = []
        for row in rows:
            data = json.loads(row[0])
            for user in data["users"]:
                user_data = {
                    "기수": data["team"],
                    "종목": data["game"],
                    "학번": user["학번"],
                    "이름": user["이름"],
                    "게임ID": user["게임ID"]
                }
                all_players.append(user_data)
        
        players_df = pd.DataFrame(all_players)
        return players_df
    
    except Exception as e:
        st.error(f"Error loading player data: {e}")
        return pd.DataFrame()
    
    finally:
        db.close()

# Streamlit 인터페이스 함수
def display_roster():
    st.header("Player Roster")

    # 선수 데이터 불러오기
    players_df = load_players()

    if players_df.empty:
        st.error("No player data found.")
        return

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
