import heapq
from copy import deepcopy

class Node:
    bound = 0
    def __init__(self, level: int, path: list):
        self.level = level
        self.path = path


def length(path: list) -> int:
    # len = 0
    # i = 0
    # while path[i] != path[-1]:
    #     if path[i] != path[-2]:
    #         len += W[path[i]][path[i + 1]]
    #     i += 1
    # return len
    p_len = 0
    i = 0
    for i in range(0, len(path) - 1):
        p_len += W[path[i]][path[i + 1]]
    return p_len


def hasOutgoing(v: int, path: list) -> bool:
    # i = 0
    # while path[i] != path[-2]:
    #     if path[i] == v:
    #         return True
    #     i += 1
    # return False
    temp = path[:-1]
    if v in temp:
        return True
    return False


def hasIncoming(v: int, path: list) -> bool:
    # i = 1
    # while path[i] != path[-1]:
    #     if path[i] == v:
    #         return True
    #     i += 1
    # return False
    temp = path[1:]
    if v in temp:
        return True
    return False


def bound(v: Node) -> int:
    lower = length(v.path)
    for i in range(1, n + 1):
        if hasOutgoing(i, v.path):
            continue
        min = INF
        for j in range(1, n + 1):
            if i == j:
                continue
            if j == 1 and i == v.path[-1]:
                continue
            if hasIncoming(j, v.path):
                continue
            if min > W[i][j]:
                min = W[i][j]

        lower += min
        if lower >= INF:
            return INF

    return lower


def remaining_vertex(path: list) -> int:
    total = n * (n + 1) // 2
    total_path = sum(path)

    return total - total_path


def func() -> None:
    global opttour
    global minlength
    cnt = 0
    PQ = []
    v = Node(0, [1])
    v.bound = bound(v)

    print(v.level, v.bound, *v.path, sep=' ')

    heapq.heappush(PQ, (v.bound, cnt, v))

    while len(PQ):
        v = heapq.heappop(PQ)[2]
        if v.bound < minlength:
            for i in range(2, n + 1):
                cnt += 1
                if i in v.path:
                    continue
                u = Node(v.level + 1, deepcopy(v.path))
                u.path.append(i)
                if u.level == n - 2:
                    u.path.append(remaining_vertex(u.path))
                    u.path.append(1)
                    if length(u.path) < minlength:
                        minlength = length(u.path)
                        opttour = u.path.copy()
                else:
                    u.bound = bound(u)
                    if u.bound < minlength:
                        try:
                            heapq.heappush(PQ, (u.bound, cnt, u))
                        finally:
                            pass

                if u.level > n - 3:
                    if length(u.path) >= INF:
                        print(u.level, "INF", *u.path, sep=' ')
                    else:
                        print(u.level, length(u.path), *u.path, sep=' ')
                else:
                    if u.bound >= INF:
                        print(u.level, "INF", *u.path, sep=' ')
                    else:
                        print(u.level, u.bound, *u.path, sep=' ')


if __name__ == "__main__":
    INF = 9999
    opttour = []
    minlength = INF
    n, m = map(int, input().split())        # 정점과 간선의 개수
    W = [[INF] * (n + 1) for _ in range(n + 1)]       # 인접행렬

    for i in range(n + 1):
        W[i][i] = 0

    for _ in range(m):
        u, v, w = map(int, input().split())     # 간선의 정보
        W[u][v] = w

    func()

    print(minlength)
    print(*opttour, sep=' ')
