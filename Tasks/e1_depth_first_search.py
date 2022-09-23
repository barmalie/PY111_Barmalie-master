# from typing import Hashable, List
# import networkx as nx
#
#
# def dfs(g: nx.Graph, start_node: Hashable) -> List[Hashable]:
#     """
#     Do an depth-first search and returns list of nodes in the visited order
#
#     :param g: input graph
#     :param start_node: starting node of search
#     :return: list of nodes in the visited order
#     """
#     draw_graph(g)
#     path_node = []
#     visited_node = {node: False for node in g.nodes}
#     wait_nodes = deque()
#     wait_nodes.append(start_node)
#     while wait_nodes:
#         current_node = wait_nodes.popleft()  # забираем первый элемент start_node
#         path_node.append(current_node)
#         visited_node[current_node] = True  # узел сгорел
#
#         for neighbour in g[current_node]:
#             if not visited_node[neighbour]:
#                 wait_nodes.append(neighbour)  # список подожженных(подожгли соседа)
#                 visited_node[neighbour] = True
#
#     print(g, start_node)
#     return (path_node)
#
#
# def draw_graph(graph):
#     pos = nx.spring_layout(graph)
#     nx.draw_networkx_nodes(graph, pos)
#     nx.draw_networkx_labels(graph, pos)
#
#     for edge in graph.edges:  # кусок в лекции застрял
#     print(g, start_node)
#     return list(g.nodes)
#________________________________________________________________
#copypaste
# def dfs(graph, start, visited=None):
#     if visited is None:
#         visited = set()
#     visited.add(start)
#
#     print(start)
#
#     for next in graph[start] - visited:
#         dfs(graph, next, visited)
#     return visited
#
#
# graph = {'0': set(['1', '2']),
#          '1': set(['0', '3', '4']),
#          '2': set(['0']),
#          '3': set(['1']),
#          '4': set(['2', '3'])}
#
# dfs(graph, '0')


# 1. Матрица связности.
# matrix_of_coherence = [[0, 1, 0],  # матрица связности
#                        [1, 0, 0],
#                        [0, 0, 0]]
#
# ex = set()  # множество посещенных вершин


# def dfs(node):  # start - начальная вершина
#
#     ex.add(node)
#     for coherence in range(len(matrix_of_coherence)):
#         if matrix_of_coherence[node][coherence] == 1 and coherence not in ex:
#             print(coherence)
#             dfs(coherence)
#
#
# # 2. Список смежности.'''Полужирное начертание'''
# list_of_adjacencies = [[1, 3], [0], [3], [2, 0], []]
# vladimir = [False for enotu in range(len(list_of_adjacencies))]
#
#
# def dfs(vovanissimo):
#     vladimir[vovanissimo] = True
#     for vovochka in list_of_adjacencies[vovanissimo]:
#         if not vladimir[vovochka]:
#             dfs(vovochka)
#
#
# for cotiki in range(len(list_of_adjacencies)):
#     if not vladimir[cotiki]:
#         dfs(cotiki)