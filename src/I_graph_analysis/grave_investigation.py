import matplotlib.pyplot as plt
import networkx as nx
from networkx.algorithms.approximation.dominating_set import min_weighted_dominating_set

from grave import plot_network


def generate_i_graph(n: int, j: int, k: int) -> nx.Graph:
    """
    Generate a I-graph I(n, j, k).
        - vertex set: {u_0, u_1,... , u_{n-1}, v_0, v_1,... , v_{n-1}}
        - edge set: {u_i u_{i+j} ,u_i v_i, v_i v_{i+k}; i = 0, ..., n - 1}

    We want to ensure that n>=3, 1<=j, k<=n/2 and j<=k and the user should be warned if these
    conditions are not met.
    """
    graph = nx.Graph()

    # Check conditions
    if n < 3:
        raise ValueError("n must be greater than 3")
    if j < 1 or k < 1:
        raise ValueError("j and k must be greater than 1")
    if k < j:
        raise ValueError("k must be greater than or equal to j")
    if k > n / 2:
        raise ValueError("k must be less than or equal to n/2")
    if j > n / 2:
        raise ValueError("j must be less than or equal to n/2")

    # Add nodes
    graph.add_nodes_from([f"u_{i}" for i in range(n)])
    graph.add_nodes_from([f"v_{i}" for i in range(n)])

    # Add edges
    for i in range(n):
        graph.add_edge(f"u_{i}", f"u_{(i+j)%n}")
        graph.add_edge(f"u_{i}", f"v_{i}")
        graph.add_edge(f"v_{i}", f"v_{(i+k)%n}")

    return graph


def color_dominators(node_attrs):
    if node_attrs.get("is_dominator", False):
        return {"color": "red"}
    else:
        return {"color": "black"}


if __name__ == "__main__":
    network = generate_i_graph(5, 1, 2)
    # network = nx.powerlaw_cluster_graph(50, 1, 0.2)
    dom_set = min_weighted_dominating_set(network)

    for node, node_attrs in network.nodes(data=True):
        node_attrs["is_dominator"] = True if node in dom_set else False

    fig, ax = plt.subplots()
    plot_network(network, layout="circular")
    plt.show()
