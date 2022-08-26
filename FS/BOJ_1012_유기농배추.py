from collections import deque


def bfs(maps, i, j):
    dir = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    maps[i][j] = 0
    que = deque()
    que.append((i ,j))
    while que:
        i, j = que.popleft()
        for d_i, d_j in dir:
            n_i = i + d_i
            n_j = j + d_j
            if n_i >= n or n_i < 0 or n_j >= m or n_j < 0:
                continue
            else:
                if maps[n_i][n_j] == 1:
                    maps[n_i][n_j] = 0
                    que.append((n_i, n_j))


test_case = int(input())
for _ in range(test_case):
    count = 0
    m, n, k = map(int, input().split())
    maps = [[0 for _ in range(m)] for _ in range(n)]
    que = deque()
    for _ in range(k):
        j, i = map(int, input().split())
        maps[i][j] = 1
    for i in range(n):
        for j in range(m):
            if maps[i][j] == 1:
                bfs(maps, i, j)
                count += 1

    print(count)


