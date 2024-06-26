import streamlit as st

def main():
    st.title("코드코리아배 부산소프트웨어마이스터고 E스포츠 대회")
    st.subheader("대회 정보")
    st.subheader("참가 팀")
    teams = ["1기 대표", "2기 대표", "3기 대표", "4기 대표"]
    for team in teams:
        st.markdown(f"- {team}")

    st.header("종목")
    games = ["LOL", "Valorant", "FIFA"]
    for game in games:
        st.markdown(f"- {game}")

    st.header("대회 방식")
    st.markdown("""
    - **SWISS STAGE 토너먼트:**  
      - 모든 팀이 시합(3판2선)을 진행
      - 승리팀은 승자조로 진출
      - 패배팀은 패자조로 진출
      - 패자조에서 승리한 팀과 승자조에서 패배한 팀이 패자조 결승으로 진출
      - 승자조 승리자와 패자조 결승 승리자가 결승으로 진출
    - **진영 및 맵 선택 우선권:**
      - 전(前)라운드 패배팀이 다음 라운드 선택 우선권을 가진다.
      - 첫 라운드 경우
        - 결승의 경우 승자조 승리자가 우선권을 가진다.
        - 그 외의 경우 기수가 높은 팀이 우선권을 가진다.
    - **부정행위:**
        - 부정행위가 적발되면 몰수패한다.
        - 부정행위 항목:
            - 불법프로그램 사용
            - 대리 플레이
            - 10분 이상 지각
            - 디도스 등 해킹공격
            - 전체채팅으로 심한 비매너 플레이(욕설, 인신공격)
            - 심판이 판단했을 때 부정하다고 생각하는 경우
    - **점수 산출 방법**
        - 종목 당 1위 40점, 2위 20점, 3위 10점, 4위 0점
        - 각 종목 점수 합계로 순위 선정
    - **대회 상금 및 경품(코드코리아에서 후원)**
        - 1위 기수에게는 15만원어치 회식권 제공
        - 승패예측 사이트에서 승패 예측을 가장 많이 맞춘 1인에게 아웃백(5만원) 기프티콘
    - **그 외 정보**
        - 코드코리아 디스코드 서버에서 중계진행
        - 3기가 만든 승패예측 사이트도 활용할 예정
        
    """)

if __name__ == '__main__':
    main()
