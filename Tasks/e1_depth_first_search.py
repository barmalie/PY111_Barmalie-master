from typing import Hashable, List
import networkx as nx


def dfs(g: nx.Graph, start_node: Hashable) -> List[Hashable]:
    """
    Do an depth-first search and returns list of nodes in the visited order

    :param g: input graph
    :param start_node: starting node of search
    :return: list of nodes in the visited order
    """
    draw_graph(g)
    path_node = []
    visited_node = {node: False for node in g.nodes}
    wait_nodes = []#deque()
    wait_nodes.append(start_node)
    visited_node[start_node] = True
    while wait_nodes:
        current_node = wait_nodes.pop()  # забираем первый элемент start_node
        path_node.append(current_node)

        neighbours = g[current_node]
        for neighbour in neighbours:
            if not visited_node[neighbour]:
                wait_nodes.append(neighbour)  # список подожженных(подожгли соседа)
                visited_node[neighbour] = True

    #print(g, start_node)
    return (path_node)


def draw_graph(graph):
    pos = nx.spring_layout(graph)
    nx.draw_networkx_nodes(graph, pos)
    nx.draw_networkx_labels(graph, pos)

    for edge in graph.edges:  # кусок в лекции застрял
    print(g, start_node)
    return list(g.nodes)
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

# # Реализация алгоритма в глубину
# def DFS(self, root):
# # Сначала определите, является ли корневой узел пустым узлом
# 	if root != None:
# 		search_queue = deque()
# 		search_queue.append(root)
# 		visited = []
# 	else:
# 		print('root is None')
# 		return -1
# 	while search_queue:
# 		person = search_queue.popleft()
# 		self.order.append(person)
# 	if (not person in visited) and (person in self.neighbor.keys()):
# 		tmp = self.neighbor[person]
# 		tmp.reverse()
# 		for index in tmp:
# 			search_queue.appendleft(index)
# 			visited.append(person)