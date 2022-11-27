from typing import List

def shortestPathI(graph: List[List[int]]):
    """
    shortest path in undirected graph
    :param graph:
    :return:
    """
    pass

def shortestPathII(graph: List[List[int]]):
    """
    shortest path in directed graph without negative cycle
    :param graph:
    :return:
    """
    pass

def shortestPathIII(graph: List[List[int]], E, s, t):
    """
    shortest path in directed graph with negative cycle, at most E edges
    :param graph:
    :return:
    """
    INF = float("inf")
    N = len(graph)
    opt = [[0] * N for _ in range(E+1)]
    for j in range(N):
        opt[0][j] = INF if j != t else 0

    for i in range(1, E+1):
        for j in range(N):
            for w in graph[i]:
                opt[i][w] = min(opt[i-1][w], opt[i-1][j] + graph[j][w])
    return opt[E][s]

def shortestPathIII_constant_space(graph: List[List[int]], E, s, t):
    """
    shortest path in directed graph with negative cycle, at most E edges
    Use only constant space
    Pruning: stop update through E if no column in OPT change
    :param graph:
    :return:
    """
    INF = float("inf")
    N = len(graph)
    opt = [0] * N
    for j in range(N):
        opt[j] = INF if j != t else 0

    for i in range(E):
        for j in range(N):
            for w in graph[i]:
                opt[w] = min(opt[w], opt[j] + graph[j][w])
    return opt[s]