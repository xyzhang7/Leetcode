from typing import List


def countRoutes(locations: List[int], start: int, finish: int, fuel: int) -> int:
    """
    You are given an array of distinct positive integers locations where locations[i] represents the position of city
    i. You are also given integers start, finish and fuel representing the starting city, ending city,
    and the initial amount of fuel you have, respectively.

    At each step, if you are at city i, you can pick any city j such that j != i and 0 <= j < locations.length and
    move to city j. Moving from city i to city j reduces the amount of fuel you have by |locations[i] - locations[
    j]|. Please notice that |x| denotes the absolute value of x.

    Notice that fuel cannot become negative at any point in time, and that you are allowed to visit any city more
    than once (including start and finish).

    Return the count of all possible routes from start to finish. Since the answer may be too large, return it modulo
    109 + 7.

    NOTE: top-down approach + memorization
    """
    N = len(locations)
    cache = [[-1] * (fuel + 1) for _ in range(N)]

    def dfs(src, f):
        if cache[src][f] != -1:
            return cache[src][f]

        if abs(locations[finish] - locations[src]) > fuel:
            cache[src][f] = 0
            return 0

        num_routes = 0
        if src == finish:
            num_routes = 1

        for s in range(N):
            cost = abs(locations[s] - locations[src])
            if s != src and f >= cost:
                num_routes += dfs(s, f - cost)
        return num_routes

    return dfs(start, fuel)


if __name__ == "__main__":
    countRoutes([2, 3, 6, 8, 4], 1, 3, 5)
