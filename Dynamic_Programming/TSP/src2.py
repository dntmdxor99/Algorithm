start_vertex = 1

def create_adj() -> list:
    # 인접 행렬을 만드는 함수
    adj = [[INF] * (n + 1) for _ in range(n + 1)]       # 인접행렬

    for i in range(n + 1):
        adj[i][i] = 0       # 자기 자신에 대한 경로는 0

    for _ in range(m):
        u, v, w = map(int, input().split())     # 출발 정점, 도착 정점, 가중치
        adj[u][v] = w

    return adj


def count(A: int) -> int:
    # A에 속한 노드의 개수가 몇 개인지 알려주는 함수
    cnt = 0
    while A != 0:
        # A가 0이 아니라면 남아있는 비트(1)가 있음
        if A & 1 == 1:
            # 마지막 비트가 1이라면
            cnt += 1
        A >>= 1
    return cnt


def isIn(i: int, A: int) -> bool:
    # 정점 i가 A에 속함 유무를 알려주는 함수
    # 만약 i가 2라면 A의 첫 번째 비트가 1임을 증명하면 된다.
    return A & (1 << (i - 2)) != 0


def diff(j: int, A: int) -> int:
    # A에서 j를 제외하고 반환함
    # j가 3이라면 A의 1번째 비트만 0으로 바꾼 후 return함
    return A & ~(1 << (j - 2))


def minimum(i: int, A: int) -> tuple:
    # i에서 j로 갔다가, j에서 A를 통해 정점1로 가는 최적 경로의 길이와 j를 반환함
    minV = INF
    minJ = INF
    for j in range(1, n + 1):
        if j == start_vertex:
            # 만약 j가 출발 정점이라면
            continue
        # i -> j, j -> v1으로 가는 경로를 위한 반복문
        if not isIn(j, A):
            # 그러기 위해서는 j가 A에 속해야함
            continue
        value = adj[i][j] + D[j][diff(j, A)]
        # A에서 j노드를 제외하고 가는 경로가 있을 것임
        if minV > value:
            # 제일 작은 애를 찾기 위해서 
            minV = value
            minJ = j

    return minV, minJ


def travel() -> None:
    subset_size = pow(2, n - 1)

    for i in range(1, n + 1):
        if i == start_vertex:
            continue
        D[i][0] = adj[i][start_vertex]     
        # D[i][0]는 i에서 공집합을 통하여 출발 정점으로 가는 길이
        # 이것은 필연적으로 i에서 출발 정점으로 직빵으로 가는 길이다.
    for k in range(1, n - 1):
        # k는 부분 집합의 개수 
        # start_vertex(v1)을 제외하면 n - 1개인데, 마지막 노드는 손쉽게 계산이 가능하므로 n - 2번 반복
            for A in range(subset_size):
                # 모든 경우의 수를 계산해봄
                if count(A) != k:
                    # 만약 A에 속한 노드의 개수가 k개가 아니라면 continue
                    continue
                for i in range(1, n + 1):
                    if i == start_vertex:
                        continue
                    # i가 A를 통해 v1으로 가는 경로를 알아봄
                    if isIn(i, A):
                        continue
                    D[i][A], j = minimum(i, A)
                    P[i][A] = j

    A = subset_size - 1
    D[start_vertex][A], j = minimum(start_vertex, A)
    P[start_vertex][A] = j
    

def tour(start: int, size: int) -> None:
    k = P[start][size]
    if size == 0:
        p.append(start_vertex)
    else:
        p.append(k)
        tour(k, diff(k, size))


if __name__ == "__main__":
    INF = 9999

    n, m = map(int, input().split())        # 정점, 간선 개수

    adj = create_adj()

    # 비트를 이용해서 A를 구현하므로, D와 P의 열(A임) 또한 비트 개수만큼 넣어야함
    # 이때 A는 V - {v1(출발 정점)}의 부분 집합이다.
    # 따라서 A에는 v2, v3, ... , vn이 들어간다.
    # 만약 A에 v2, v4가 있다면 A의 비트는 101 = 5가 된다.
    # 따라서 A의 비트 크기는 2*(n-1)이 되어야 모든 부분 집합을 포함할 수 있다.
    subset_size = pow(2, n - 1)
    D = [[0] * subset_size for _ in range(n + 1)]     # D[i][j] = i to j의 최적 경로의 길이
    P = [[0] * subset_size for _ in range(n + 1)]     # P[i][j] = k는 vi에서 vj로 가는 최적 경로 중 vi 다음으로 방문하는 노드

    travel()

    # 아래는 출력을 위한 것
    print(D[start_vertex][subset_size - 1])

    p = [start_vertex]
    tour(start_vertex, subset_size - 1)
    print(*p, sep=' ')

    for i in range(1, n + 1):
        for j in range(subset_size):
            if 0 < D[i][j] < INF:
                print(i, j, D[i][j])
