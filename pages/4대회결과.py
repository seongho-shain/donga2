import streamlit as st
import pandas as pd

# 초기 데이터 설정
teams = ["1기", "2기", "3기", "4기"]
games = ["LOL", "Valorant", "FIFA"]
points = {1: 40, 2: 20, 3: 10, 4: 0}

def load_results():
    try:
        return pd.read_csv('results.csv', index_col=0)
    except FileNotFoundError:
        return pd.DataFrame(0, index=teams, columns=games + ["총합"])

def save_results(df):
    df.to_csv('results.csv')

def update_scores(results_df):
    for game in games:
        with st.expander(f"{game} 결과 입력"):
            first = st.selectbox(f"{game} 1등", teams, key=f"{game}_1st")
            second = st.selectbox(f"{game} 2등", teams, key=f"{game}_2nd")
            third = st.selectbox(f"{game} 3등", teams, key=f"{game}_3rd")
            fourth = st.selectbox(f"{game} 4등", teams, key=f"{game}_4th")

            if st.button(f"{game} 결과 저장", key=f"{game}_save"):
                results_df.loc[:, game] = 0  # Reset the current game's points
                results_df.loc[first, game] = points[1]
                results_df.loc[second, game] = points[2]
                results_df.loc[third, game] = points[3]
                results_df.loc[fourth, game] = points[4]

                results_df["총합"] = results_df[games].sum(axis=1)
                save_results(results_df)
                st.success(f"{game} 결과가 저장되었습니다.")
                st.experimental_rerun()

def main():
    st.title("코드코리아배 부산소프트웨어마이스터고 E스포츠 대회 결과")

    results_df = load_results()

    st.header("대회 결과")
    st.dataframe(results_df)

    st.header("결과 입력")
    update_scores(results_df)

if __name__ == '__main__':
    main()
