import sys
import copy
input = sys.stdin.readline


def minmult(m, d, p, i, j):
    # i부터 j까지의 행렬 중 최소 곱셈 횟수를 구해줌
    minimum = 999999        # 최댓값은 999999를 넘지 않으므로
    for k in range(i, j):
        value = m[i][k] + m[k+1][j] + d[i] * d[k + 1] * d[j + 1]        # k를 기준으로 나눈 두 행렬을 곱함
        if minimum > value:
            minimum = value
            p[i][j] = k

    return minimum


def func(n ,d, m, p):
    # 행렬의 최소 곱셈 횟수를 구하는 함수
    # 행렬은 두 개씩만 곱했을 때부터 시작해서, 최종적으로 1부터 n까지의 곱셈을 한다.
    for diagonal in range(n-1, 0, -1):        # diagonal은 곱하는 갯수
        for i in range(1, diagonal + 1):        # diagonal과 같음
            j = i + n - diagonal        # 만약 5개를 곱하면 +1, 4개를 곱하면 +2를 하면 됨
            # 쉽게 말해서 개수가 5개면 (1,2) (2,3) .. (5,6)을 하면 되고, 개수가 1개면 (1,6)을 하면 됨
            m[i][j] = minmult(m, d, p, i, j)


def path(p, start, end):
    # 곱셈 순서를 알려주는 함수
    if start == end:
        print(f'(A{start})', end='')        # 두 개가 같다면 출력하면 됨
    elif start < end:
        k = p[start][end]
        print('(', end='')
        path(p, start, k)
        path(p, k + 1, end)
        print(')', end='')


n = int(input())        # 행렬의 개수
d = [0] + list(map(int, input().split()))        # 각 행렬의 크기 리스트
m = [[0] * (n + 1) for _ in range(n + 1)]     # 행렬의 최소 곱셈을 저장하는 배열, 기준을 1부터 시작하기 위해서 1씩 더함
p = copy.deepcopy(m)        # p는 어떤 행렬을 기준으로 나눴는지 알려줌

func(n, d, m, p)

for i in range(1, n + 1):
    print(*m[i][i:n+1], sep=' ')
for i in range(1, n + 1):
    print(*p[i][i:n+1], sep=' ')

print(m[1][n])

path(p, 1, n)
