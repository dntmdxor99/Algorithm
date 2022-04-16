import sys
from collections import deque
input = sys.stdin.readline


def find(i):
    j = s = i       # 기존의 i를 미리 저장해놓음
    while dset[i] != i:
        i = dset[i]     # 집합의 헤드를 찾으러 감

    while dset[j] != i:     # 이렇게 함으로써 헤드의 부분 집합들이 모두 헤드를 가리키게 만듬
        s = j
        j = dset[j]
        dset[s] = i

    return i


def equal(p, q):
    return True if p == q else False


def union(p, q):
    # p와 q의 집합을 합침. 이때 작은 애가 큰 애를 가리키게 만들어야하고, 작은 애의 집합들이 모두 큰 애의 헤드를 가리키게 만들어야 함
    num_p = num_q = 0
    for i in range(1, vertex_num):      # 어느 집합이 더 작은지 알아냄
        if dset[i] == p:
            num_p += 1
        elif dset[i] == q:
            num_q += 1

    if num_p > num_q:       # 작은 집합을 큰 집합에 흡수 시킴
        dset[q] = p

        for i in range(1, vertex_num):
            if dset[i] == q:
                dset[i] = p

    else:
        dset[p] = q

        for i in range(1, vertex_num):
            if dset[i] == p:
                dset[i] = q
      


def func():
    for i in range(1, vertex_num + 1):
        dset[i] = i     # 각 vertex마다 서로소 집합을 만듬, initial하는 과정

    sorted_edge = deque(sorted(edge, key = lambda x : x[2]))       # weight를 오름차순으로 정렬함

    while len(F) < vertex_num - 1:  # 1부터 vertex_num - 1까지 수행함

        e = sorted_edge.popleft()       # 가중치가 작은 애를 뽑아냄
        i, j = e[0], e[1]       # vertex들을 뽑아냄
        p = find(i)
        q = find(j)
        if not equal(p, q):
            union(p, q)
            F.append(e)
            
            print(*e, sep=' ')    


vertex_num, edge_num = map(int, input().split())        # 정점과 간선의 개수를 입력 받음
edge = deque()
for _ in range(edge_num):
    edge.append(tuple(map(int, input().split())))        # 간선의 리스트를 만듬

F = deque()      # 최소 비용 신장 트리의 간선의 집합
dset = [0] * (vertex_num + 1)       # 서로소 집합을 만듬


func()
