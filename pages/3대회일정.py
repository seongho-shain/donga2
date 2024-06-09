import streamlit as st
import pandas as pd

from Modules.Module_sendDiscord import sendDiscordEmbed

def load_schedule():
    return pd.read_csv('data/schedule.csv', parse_dates=['datetime'])

def save_schedule(schedule_df):
    schedule_df.to_csv('data/schedule.csv', index=False)

def main():
    st.title("코드코리아배 부산소프트웨어마이스터고 E스포츠 대회 일정 관리")

    st.header("대회 일정 조회 및 수정")

    schedule_df = load_schedule()

    st.subheader("현재 일정")
    st.table(schedule_df)

    st.subheader("일정 추가")
    with st.form(key='add_schedule_form'):
        date = st.date_input("날짜")
        time = st.time_input("시간")
        team1 = st.selectbox("팀1", ["1기 대표", "2기 대표", "3기 대표", "4기 대표"])
        team2 = st.selectbox("팀2", ["1기 대표", "2기 대표", "3기 대표", "4기 대표"])
        game = st.selectbox("종목", ["LOL", "Valorant", "FIFA"])
        discord_link = st.text_input("디스코드 링크", "https://discord.gg/3KQAUGSUj5")
        prediction_link = st.text_input("승부예측 링크", "https://prediction.com/example")
        submit_button = st.form_submit_button(label='일정 추가')

    if submit_button:
        datetime = pd.to_datetime(f"{date} {time}")
        new_schedule = pd.DataFrame({
            'datetime': [datetime],
            'team1': [team1],
            'team2': [team2],
            'game': [game],
            'discord_link': [discord_link],
            'prediction_link': [prediction_link]
        })
        schedule_df = pd.concat([schedule_df, new_schedule], ignore_index=True)
        save_schedule(schedule_df)
        sendDiscordEmbed(
            url=st.secrets["webhookURL"],
            title=f"대회 일정 안내 - {game}",
            datetimeInfo=datetime,
            discordInfo=discord_link,
            predictionInfo=prediction_link,
            teamInfo=[team1, team2]
        )
        st.success("일정이 추가되었습니다.")
        st.experimental_rerun()

    st.subheader("일정 삭제")
    with st.form(key='delete_schedule_form'):
        index_to_delete = st.number_input("삭제할 일정의 인덱스 번호", min_value=0, max_value=len(schedule_df) if len(schedule_df) == 0 else len(schedule_df)-1, step=1)
        delete_button = st.form_submit_button(label='일정 삭제')

    if delete_button:
        if len(schedule_df) > index_to_delete:
            schedule_df = schedule_df.drop(index_to_delete).reset_index(drop=True)
            save_schedule(schedule_df)
            st.success("일정이 삭제되었습니다.")
            st.experimental_rerun()

if __name__ == '__main__':
    main()
