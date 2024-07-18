import matplotlib.pyplot as plt
from imageio import imread

def plot_animal_tree(ax=None):
    import graphviz
    from matplotlib.font_manager import FontProperties
    
    plt.figure(dpi=100)
    if ax is None:
        ax = plt.gca()
    
    # Define the font properties
    font_name = 'Malgun Gothic'  # Use the name of the font as known to the system

    mygraph = graphviz.Digraph(
        node_attr={'shape': 'box', 'fontname': font_name},
        edge_attr={'labeldistance': "10.5", 'fontname': font_name},
        format="png"
    )
    
    mygraph.node("0", "날개가 있나요?")
    mygraph.node("1", "날 수 있나요?")
    mygraph.node("2", "지느러미가 있나요?")
    mygraph.node("3", "매")
    mygraph.node("4", "펭귄")
    mygraph.node("5", "돌고래")
    mygraph.node("6", "곰")
    mygraph.edge("0", "1", label="True")
    mygraph.edge("0", "2", label="False")
    mygraph.edge("1", "3", label="True")
    mygraph.edge("1", "4", label="False")
    mygraph.edge("2", "5", label="True")
    mygraph.edge("2", "6", label="False")
    
    mygraph.render("tmp")
    ax.imshow(imread("tmp.png"))
    ax.set_axis_off()