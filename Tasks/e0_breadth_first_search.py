from typing import Hashable, List
import networkx as nx
from collections import deque
import matplotlib.pyplot as plt

#алгоритм обхода в ширину

def bfs(g: nx.Graph, start_node: Hashable) -> List[Hashable]:
    """
    Do an breadth-first search and returns list of nodes in the visited order

    :param g: input graph
    :param start_node: starting node for search
    :return: list of nodes in the visited order
    """
    draw_graph(g)
    path_node = []
    visited_node = {node: False for node in g.nodes}
    wait_nodes = deque()
    wait_nodes.append(start_node)
    while wait_nodes:
        current_node = wait_nodes.popleft() # забираем первый элемент start_node
        path_node.append(current_node)
        visited_node[current_node] = True # узел сгорел

        for neighbour in g[current_node]:
            if not visited_node[neighbour]:
                wait_nodes.append(neighbour) # список подожженных(подожгли соседа)
                visited_node[neighbour] = True


    print(g, start_node)
    return(path_node)


def draw_graph(graph):
    pos = nx.spring_layout(graph)
    nx.draw_networkx_nodes(graph, pos)
    nx.draw_networkx_labels(graph, pos)

    for edge in graph.edges: #  кусок в лекции застрял
