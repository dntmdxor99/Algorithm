import sys
input = sys.stdin.readline


def floyd(D, P, n):
    # 최적의 경로를 찾는 함수, D는 최단 경로를 저장하는 배열이고, n은 vertex의 개수
    for k in range(1, n):
        for i in range(1, n):
            for j in range(1, n):
                if D[i][j] > D[i][k] + D[k][j]:     # 기존의 값이 K를 경유하는 값보다 크면 교체함
                    D[i][j] = D[i][k] + D[k][j]
                    P[i][j] = k


def path(P, p, i, j):
    # 경로를 찾는 함수
    k = P[i][j]
    if k != 0:        # P[i][j]는 i에서 j로 가기 전에 마지막으로 들리는 vertex
        path(P, p, i, k)     # 따라서 경로를 알기 위해서는 P[i][P[i][j]]를 또 다시 해야한다.
        p.append(k)
        path(P, p, k, j)


INF = 999       # 경로가 없는 경우를 대비해서 INF를 선언함

ver_num, edge_num = list(map(int, input().split()))       # 정점과 간선의 개수를 입력받음
ver_num += 1      # 범위가 1부터 시작함

W = [[INF] * ver_num for _ in range(ver_num)]       # 초기의 가중치를 저장하는 행렬

for _ in range(edge_num):       # i와 j와 weight를 입력 받아서 저장함
    i, j, weight = list(map(int, input().split()))
    W[i][j] = weight

for i in range(ver_num):        # 자기 자신에게 가는 경로는 0임
    W[i][i] = 0


D = W.copy()        # W를 복사하여 D에다가 저장함
P = [[0] * ver_num for _ in range(ver_num)]     # 경유지를 저장하는 배열

floyd(D, P, ver_num)

for i in range(1, ver_num):     # D를 출력함
    for j in range(1, ver_num):
        print(D[i][j], end=' ')
    print()
for i in range(1, ver_num):     # Path를 출력함
    for j in range(1, ver_num):
        print(P[i][j], end=' ')
    print()


n = int(input())        # 경로를 출력하기 위해 받는 경우의 수
p = list()      # 경로를 저장하는 리스트
for _ in range(n):
    i, j = list(map(int, input().split()))
    if D[i][j] == INF:
        print('None')
        continue
    p.clear()
    p.append(i)
    path(P, p, i, j)
    p.append(j)
    print(*p, sep=' ')
