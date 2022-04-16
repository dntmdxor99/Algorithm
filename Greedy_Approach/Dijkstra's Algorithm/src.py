import sys
input = sys.stdin.readline
INF = 9999


def path(p, touch, ver):
    if ver != 1:
        path(p, touch, touch[ver])
    p.append(ver)


def func():
    Y = [1]     # 초기의 Y는 출발 정점인 v_1임
    F = list()      # 간선 정보의 리스트
    touch = [1] * (vertex_num + 1)      # touch[i]로 가기 직전의 방문한 정점
    length = [INF] * (vertex_num + 1)       # v_1에서 v_i로 가는 최단 거리, 이미 최단 거리를 찾았으면 -1로 둔다. 그래야 cycle을 형성하는지 따로 확인 안 해도 됨

    print(*touch[2:], sep=' ')

    for i in range(1, vertex_num + 1):
        touch[i] = 1
        length[i] = M[1][i]

    for _ in range(vertex_num - 1):
        # 간선은 vertex_num - 1개 들어가야함
        min = INF
        min_idx = -1
        for i in range(2, vertex_num + 1):
            # 1에서 어디가 최단 거리인지 일단 찾음
            if 0 <= length[i] < min:
                min = length[i]
                min_idx = i

        Y.append(min_idx)       # 일단은 1 다음으로 얘가 추가됨
        F.append((touch[min_idx], min_idx, M[touch[min_idx]][min_idx]))        # touch[min_idx]에서의 min_idx까지의 간선 정보

        for i in range(2, vertex_num + 1):
            if length[i] > length[min_idx] + M[min_idx][i]:
                length[i] = length[min_idx] + M[min_idx][i]
                touch[i] = min_idx

        length[min_idx] = -1

        print(*touch[2:], sep=' ')



    for i in range(len(F)):
        # F에 저장된 간선의 정보를 출력함
        print(*F[i], sep=' ')

    case = int(input())
    p = list()      # 경로를 저장하는 리스트
    for _ in range(case):
        end_vertex = int(input())

        path(p, touch, end_vertex)        # 경로를 찾음

        print(*p, sep=' ')
        p.clear()


vertex_num, edge_num = map(int, input().split())        # 정점의 개수와 간선의 개수를 입력받음
M = [[INF] * (vertex_num + 1) for _ in range(vertex_num + 1)]       # 인접 행렬을 만듬
for i in range(1, vertex_num):
    # 본인에게 가는 가중치는 0
    M[i][i] = 0

for _ in range(edge_num):
    # 입력받은 가중치로 초기화
    i, j, weight = map(int, input().split())    
    M[i][j] = weight


func()

