import networkx as nx
import matplotlib.pyplot as plt
from typing import *


def calculate_cheeger_constant(G) -> int:
    return None


if __name__ == "__main__":
    # G = nx.random_regular_graph(3, 6)
    # G = nx.petersen_graph()
    # G = nx.erdos_renyi_graph(10,0.4)
    G = nx.random_lobster(10, 0.6, 0.2)
    nx.draw(G)
    plt.savefig("graph.pdf")
