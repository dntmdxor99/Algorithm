import sys
input = sys.stdin.readline

n = int(input())
d = list(map(int, input().split()))

m = [[0] * n for _ in range(n)]
p = [[0] * n for _ in range(n)]


def minimum(i, j):
    minValue = 1000000
    mink = 0
    # print(i, j)
    for k in range(i, j):
        value = m[i][k] + m[k+1][j] + d[i] * d[k+1] * d[j+1]
        if minValue > value:
            minValue = value
            mink = k

    return minValue, mink


def func():
    for diagonal in range(1, n):        # 몇 개를 곱하는지
        for i in range(0, n - diagonal):
            j = i + diagonal
            m[i][j], k = minimum(i, j)
            p[i][j] = k + 1


def print_func(start, end, s):
    s.append('(')
    if start == end:
        s.append('A' + str(start + 1))
    else:
        k = p[start][end] - 1
        # s.append('(')
        print_func(start, k, s)
        print_func(k + 1, end, s)
        # s.append(')')
    s.append(')')


func()
# print(*m, sep='\n')
for i in range(0, n):
    for j in range(i, n-1):
        print(m[i][j], end=' ')
    print(m[i][n-1])

for i in range(0, n):
    for j in range(i, n-1):
        print(p[i][j], end=' ')
    print(p[i][n-1])
print(m[0][n-1])
s = list()
print_func(0, n-1, s)
print(''.join(s))
