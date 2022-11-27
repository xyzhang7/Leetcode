from collections import deque


def water_jug(m, n, d):
    """
    You are given an m liter jug and a n liter jug. Both the jugs are initially empty. The jugs don’t have markings to
    allow measuring smaller quantities. You have to use the jugs to measure d liters of water where d is less than n.
    """
    path = []
    q = deque()
    visited = set()
    q.append((0, 0))
    while q:
        u = q.popleft()
        if (u[0], u[1]) in visited:
            continue
        if u[0] > m or u[1] > n or u[0] < 0 or u[1] < 0:
            continue
        path.append(u)
        visited.add(u)
        if u[0] == d:
            if u[1] != 0:
                path.append((u[0], 0))
        elif u[1] == d:
            if u[0] != 0:
                path.append((0, u[1]))
            break

