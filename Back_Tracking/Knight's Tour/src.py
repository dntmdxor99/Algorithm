# def check(d):
#     # 경로용 검사
#     return d == n * m
#
#
# def circuit_check(d, i):
#     # 회로용 검사
#     return d == n * m and 0 in adj[i]
#     # 회로므로 시작이 0임. 따라서 마지막에서 0으로 갈 수 있는 경로가 있다면 True
#
#
def func(d: int, i: int) -> None:
    # d는 depth임
    global cnt
    P[i] = 1        # 방문 표시
    if d == S:
        if flag:        # flag에 따라서 경로 검사가 달라짐
            if 0 in adj[i]:
                cnt += 1
        else:
            cnt += 1
    else:
        for n_k in adj[i]:
            # 인접한 노드부터 방문해봄
            if P[n_k] == 0:
                # 만약 유망(방문하지 않았다면)하다면? 탐색함
                func(d + 1, n_k)
    P[i] = 0        # 다시 상위 노드로 올라가야하므로 방문 표시 해제


if __name__ == "__main__":
    dir = (         # 방향을 나타냄
        (-2, 1),
        (-1, 2),
        (1, 2),
        (2, 1),
        (2, -1),
        (1, -2),
        (-1, -2),
        (-2, -1)
    )

    n, m = map(int, input().split())        # 체스 보드의 행과 열
    S = n * m
    adj = dict()
    for i in range(n):
        for j in range(m):
            adj[i * m + j] = []     # 인접 리스트 구현
            for dir_i, dir_j in dir:
                n_i, n_j = i + dir_i, j + dir_j
                if 0 <= n_i < n and 0 <= n_j < m:
                    adj[i * m + j].append(n_i * m + n_j)

    P = [0] * S     # 방문 유무를 검사하는 리스트
    cnt = 0     # 갯수를 세는 변수
    flag = 1        # flag에 따라서 경로 검사가 다름 (회로, 경로)
    func(1, 0)
    print(cnt)

    T = int(input())        # 출발정점의 개수
    flag = 0
    for _ in range(T):
        i, j = map(int, input().split())
        P = [0] * S
        cnt = 0
        func(1, i * m + j)
        print(cnt)
