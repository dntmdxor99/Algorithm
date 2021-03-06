import sys
input = sys.stdin.readline

n = int(input())
d = [list(map(int, input().split())) for _ in range(n)]
r = [[[0, 0]] * i for i in range(1, n + 1)]       # 바로 밑 = 0, 오른쪽 = 1
r[0][0][1] = d[0][0]


def func(n):
    for i in range(1, n):
        for j in range(i + 1):
            if j == 0:
                r[i][j] = [0, d[i][j]]
                d[i][j] += d[i-1][j]
            elif j == i:
                r[i][j] = [1, d[i][j]]
                d[i][j] += d[i-1][j-1]
            else:
                if d[i-1][j-1] <= d[i-1][j]:        # 이 부분 주의해야함 < 아님 <= 해야함. 그래야 
                    r[i][j] = [0, d[i][j]]
                    d[i][j] += d[i-1][j]
                else:
                    r[i][j] = [1, d[i][j]]
                    d[i][j] += d[i-1][j-1]


def find_path(n, idx):
    if n > 0:
        if r[n][idx][0] == 0:
            find_path(n-1, idx)
        else:
            find_path(n-1, idx-1)
    print(r[n][idx][1], end= ' ')


func(n)

M = max(d[n-1])
print(M)

# for i in range(n):
#     print(*r[i])
idx = 0

for i in range(n-1, -1, -1):
    if d[n-1][i] == M:
        idx = i
        break

find_path(n-1, idx)
print()
