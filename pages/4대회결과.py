import streamlit as st
import matplotlib.pyplot as plt
import networkx as nx
import matplotlib.font_manager as fm

# 시스템에 설치된 한글 폰트를 사용하여 matplotlib에 설정
font_path = 'C:/Windows/Fonts/경기천년제목V_Bold.ttf'  # 예: Windows
fontprop = fm.FontProperties(fname=font_path, size=10)

def draw_double_elimination_bracket(teams, winners, losers):
    G = nx.DiGraph()

    # 각 팀의 위치 설정
    G.add_node(teams[0], pos=(0, 8), color='skyblue')
    G.add_node(teams[1], pos=(0, 7), color='skyblue')
    G.add_node(teams[2], pos=(0, 6), color='skyblue')
    G.add_node(teams[3], pos=(0, 5), color='skyblue')

    # 승자조 라운드 1
    G.add_node(winners[0], pos=(1, 7.5), color='lightgreen')
    G.add_node(winners[1], pos=(1, 5.5), color='lightgreen')
    G.add_edge(teams[0], winners[0])
    G.add_edge(teams[1], winners[0])
    G.add_edge(teams[2], winners[1])
    G.add_edge(teams[3], winners[1])

    # 승자조 라운드 2
    G.add_node(winners[2], pos=(2, 6.5), color='lightgreen')
    G.add_edge(winners[0], winners[2])
    G.add_edge(winners[1], winners[2])

    # 패자조 라운드 1
    G.add_node(losers[0], pos=(0, 4), color='salmon')
    G.add_node(losers[1], pos=(0, 3), color='salmon')
    
    # 패자조 라운드 2
    G.add_node(winners[3], pos=(1, 4), color='salmon')
    G.add_node(losers[2], pos=(1, 3), color='salmon')
    G.add_edge(losers[0], winners[3])
    G.add_edge(losers[1], winners[3])

    # 패자조 라운드 3
    G.add_node(winners[4], pos=(2, 4), color='salmon')
    G.add_edge(losers[2], winners[4])
    G.add_edge(winners[3], winners[4])

    # 결승전
    G.add_node("챔피언", pos=(3, 5), color='gold')
    G.add_edge(winners[4], "챔피언")
    G.add_edge(winners[2], "챔피언")

    pos = nx.get_node_attributes(G, 'pos')
    node_colors = [nx.get_node_attributes(G, 'color')[node] for node in G.nodes()]

    fig, ax = plt.subplots(figsize=(12, 8))

    # 노드와 엣지 그리기
    nx.draw_networkx_edges(G, pos, ax=ax)
    nx.draw_networkx_labels(G, pos, ax=ax, font_size=10, font_color='black', font_family=fontprop.get_name())

    # 사각형 노드 그리기
    for node, (x, y) in pos.items():
        ax.add_patch(plt.Rectangle((x - 0.2, y - 0.1), 0.4, 0.2, fill=True, color=nx.get_node_attributes(G, 'color')[node], transform=ax.transData))

    plt.title("더블 엘리미네이션 토너먼트 대진표", fontproperties=fontprop)
    plt.axis('off')
    st.pyplot(fig)

# 스트림릿 앱 설정
st.title("더블 엘리미네이션 토너먼트 대진표")

# 팀 리스트
teams = ["1기", "3기", "2기", "4기"]

# 사용자 입력을 위한 텍스트 입력 필드
winners = []
for i in range(5):
    winners.append(st.text_input(f"승자 {i + 1}", f"승자 {i + 1}"))

losers = []
for i in range(3):
    losers.append(st.text_input(f"패자 {i + 1}", f"패자 {i + 1}"))

draw_double_elimination_bracket(teams, winners, losers)
