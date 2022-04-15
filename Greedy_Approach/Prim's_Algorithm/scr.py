import sys
input = sys.stdin.readline

INF = 9999       # 경로가 없을 때


def func(F):
    for i in range(2, vertex_num + 1):
        nearest[i] = 1      # i와 가장 가까운 vertex는 1이라고 가정하고 시작
        distance[i] = W[1][i]       # 거리를 1과의 거리로 동기화 시킴

    print(*nearest[2:], sep=' ')

    for _ in range(vertex_num - 1):
        # edge가 vertex_num - 1개 추가되어야 하므로 범위를 이렇게 정함
        min = INF
        min_idx = -1
        for i in range(2, vertex_num + 1):      # 2부터 vertex_num까지 최소를 찾는 과정
            if 0 <= distance[i] < min:
                min = distance[i]
                min_idx = i

        F.append((min_idx, nearest[min_idx]))       # min_idx와 nearsest[min_idx]의 간선을 넣는다.
        distance[min_idx] = -1      # 추가했으므로 거리는 -1로 설정

        for i in range(2, vertex_num + 1):
            # 새로운 vertex를 집합에 추가했으므로, 새로운 vertex와 V-Y의 거리도 업데이트 해야함 (최소가 되게)
            if distance[i] > W[min_idx][i]:     # 만약 기존의 거리보다 새로운 vertex의 거리가 짧으면 업데이트 함
                distance[i] = W[min_idx][i]
                nearest[i] = min_idx

        print(*nearest[2:], sep=' ')


vertex_num, edge_num = map(int, input().split())        # 정점의 개수와 간선의 개수를 입력 받는다. 정점은 1부터 n까지의 자연수로 표시한다.

W = [[INF] * (vertex_num + 1) for _ in range(vertex_num + 1)]       # adjacency matrix, INF로 초기화하고 후에 값을 받을 예정
nearest = [1] * (vertex_num + 1)        # v_i에 가장 가까운 Y에 속한 정점의 인덱스, 1부터 시작하므로 1로 초기화
distance = [-1] * (vertex_num + 1)     # v_i와 nearest[i] 사이의 거리

for _ in range(edge_num):
    # 가중치를 입력 받음
    i, j, weight = map(int, input().split())
    W[i][j] = weight
    W[j][i] = weight

for i in range(1, vertex_num):
    # 본인과의 거리는 0
    W[i][i] = 0

F = list()      # 간선의 집합

func(F)

for i in range(vertex_num - 1):
    # 간선의 정보와 가중치를 출력함
    i, j = F[i]
    weight = W[i][j]
    print(i, j, weight)
