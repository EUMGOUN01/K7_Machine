import matplotlib.pyplot as plt
from imageio import imread
import graphviz

def plot_animal_tree(ax=None):
    plt.figure(dpi=100)
    if ax is None:
        ax = plt.gca()
    
    # Malgun Gothic 폰트 경로를 지정합니다.
    font_path = "C:/Windows/Fonts/malgun.ttf"

    # 그래프 객체 생성
    mygraph = graphviz.Digraph(
        node_attr={'shape': 'box', 'fontname': 'Malgun Gothic'},
        edge_attr={'labeldistance': "10.5", 'fontname': 'Malgun Gothic'},
        format="png"
    )

    # 노드 정의
    mygraph.node("0", "날개가 있나요?", fontname='Malgun Gothic')
    mygraph.node("1", "날 수 있나요?", fontname='Malgun Gothic')
    mygraph.node("2", "지느러미가 있나요?", fontname='Malgun Gothic')
    mygraph.node("3", "매", fontname='Malgun Gothic')
    mygraph.node("4", "펭귄", fontname='Malgun Gothic')
    mygraph.node("5", "돌고래", fontname='Malgun Gothic')
    mygraph.node("6", "곰", fontname='Malgun Gothic')

    # 엣지 정의
    mygraph.edge("0", "1", label="True", fontname='Malgun Gothic')
    mygraph.edge("0", "2", label="False", fontname='Malgun Gothic')
    mygraph.edge("1", "3", label="True", fontname='Malgun Gothic')
    mygraph.edge("1", "4", label="False", fontname='Malgun Gothic')
    mygraph.edge("2", "5", label="True", fontname='Malgun Gothic')
    mygraph.edge("2", "6", label="False", fontname='Malgun Gothic')

    mygraph.render("tmp")
    ax.imshow(imread("tmp.png"))
    ax.set_axis_off()