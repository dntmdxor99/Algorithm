import sys
input = sys.stdin.readline

testcase = int(input())     # 테스트 케이스의 수


def func(start, end):
    W[start][end] = [0, 0]      # 0, 0은 0, 0으로 초기화
    C[start][end] = 0       # 0, 0의 count는 0

    for i in range(start, n):       # 전체를 돌지만 사실상 전체를 안 돔
        for j in range(end, n):
            if W[i][j] != [-1, -1]:     # 만약에 방문할 수 있으면 감
                k = M[i][j]
                if i + k < n:       # 이때 내가 갈 수 있는 곳이어야 함
                    W[i + k][j] = [i, j]     # 위에서 내려왔으면 2
                    C[i + k][j] = C[i][j] + 1       # 해당 지점의 count를 이전 지점 +1 함

                if j + k < n:
                    minimum = min(C[i][j+k], C[i][j] + 1)       # 기존에 다른 루트로 방문할 수 있다고 가정함. 이때 다른 루트가 더 빠른지를 비교
                    if minimum == C[i][j + k]:
                        # 다른 루트로 가는게 더 빠름
                        continue
                    else:
                        # 이 루트로 가는게 더 빠름
                        C[i][j + k] = minimum
                        W[i][j + k] = [i, j]

                if W[n-1][n-1] != [-1, -1]:     # 만약 도착지에 갈 수 있다면 그대로 종료함
                    return


def path(i, j):
    if i != 0 and j != 0:
        path(W[i][j][0], W[i][j][1])

    p.append([i, j])


for _ in range(testcase):
    n = int(input())        # 격자의 크기
    M = list()      # 맵을 만듬
    for i in range(n):
        M.append(list(map(int, input().split())))

    W = [[[-1, -1]] * n for _ in range(n)]      # 해당 지점에 가는데 직전에 들린 좌표
    C = [[999] * n for _ in range(n)]       # 해당 지점까지 가는데 걸리는 count
    p = [[0, 0]]

    func(0, 0)
    
    if W[n-1][n-1] != [-1, -1]:        # 도착지에 방문할 수 있다면 YES를 출력, 만약 -1, -1이라면 해당 지점에 갈 수 없음
        print("YES")
        path(n - 1, n - 1)       # 경로를 찾음
        print(*p, sep=' ')
    else:
        print("NO")

    

    
