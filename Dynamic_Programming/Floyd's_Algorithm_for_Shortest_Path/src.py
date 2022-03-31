import sys
input = sys.stdin.readline


def floyd(n):
    for k in range(0, n):
        for i in range(0, n):
            for j in range(0, n):
                if data[i][j] > data[i][k] + data[k][j]:
                    data[i][j] = data[i][k] + data[k][j]
                    P[i][j] = k + 1


def path(u ,v, p):
    k = P[u][v] - 1
    if k != -1:
        path(u, k, p)
        p.append(k + 1)
        path(k, v, p)


INF = 999
ver_num, edge_num = list(map(int, input().split()))
data = [[INF] * ver_num for _ in range(ver_num)]

for i in range(ver_num):
    data[i][i] = 0

P = [[0] * ver_num for _ in range(ver_num)]

for _ in range(edge_num):
    u, v, w = list(map(int, input().split()))
    u -= 1
    v -= 1
    data[u][v] = w


# for i in range(ver_num):
#     print(*data[i])


floyd(ver_num)

for i in range(ver_num):
    print(*data[i])
for i in range(ver_num):
    print(*P[i])

p = []
case = int(input())
for _ in range(case):
    u, v = list(map(lambda x : int(x) - 1, input().split()))
    if data[u][v] == INF:
        print("NONE")
        continue
    p.clear()
    path(u, v, p)
    print(u+1, *p, v+1)
