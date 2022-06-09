def func(d: int, i: int) -> None:
    # d는 depth이고, i는 몇 번째 말판인지 표시함
    P[i] = 1        # 방문 표시
    if d == S - 1:      # 1부터 시작하므로 말판의 개수만큼 깊이가 있음
        global cnt
        if flag:        # flag에 따라서 경로 검사가 달라짐, 1 == 회로, 0 == 경로
            if 0 in adj[i]:     # 다시 출발 정점 (0)으로 돌아갈 수 있다면
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
    S = n * m       # 말판의 개수, 혹은 말판의 번호
    adj = dict()        # 인접 행렬
    for i in range(n):
        for j in range(m):
            adj[i * m + j] = []     # 인접 행렬 구현, 왼쪽 위부터 0, 오른쪽 아래가 S - 1임
            for dir_i, dir_j in dir:
                n_i, n_j = i + dir_i, j + dir_j     # i, j에서 갈 수 있는 좌표
                if 0 <= n_i < n and 0 <= n_j < m:       # 만약 해당 좌표가 말판 안에 있다면
                    adj[i * m + j].append(n_i * m + n_j)        # 좌표를 말판 번호로 변환하여 넣음

    P = [0] * S     # 방문 유무를 검사하는 리스트
    cnt = 0     # 갯수를 세는 변수
    flag = 1        # flag에 따라서 경로 검사가 다름 (회로, 경로)
    func(0, 0)      # 회로를 검사함, depth와 시작 번호를 입력
    print(cnt)

    T = int(input())        # 출발정점의 개수
    flag = 0
    for _ in range(T):
        i, j = map(int, input().split())        # 출발 정점의 좌표
        P = [0] * S
        cnt = 0
        func(0, i * m + j)      # 좌표를 말판 번호로 변환함
        print(cnt)
