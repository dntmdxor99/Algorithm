def count(A: int) -> int:
    cnt = 0
    while A != 0:
        if A & 1:
            cnt += 1
        A >>= 1
    return cnt


def isIn(i: int, A: int) -> bool:
    return (A & (1 << (i - 2))) != 0


def diff(A: int, j: int) -> int:
    return A & ~(1 << (j - 2))


def minimum(n, i, A):
    minV = INF
    minJ = INF
    for j in range(2, n + 1):
        if not isIn(j, A):
            continue
        value = W[i][j] + D[j][diff(A, j)]
        if minV > value:
            minV = value
            minJ = j

    return minV, minJ


def func() -> None:
    subset_size = pow(2, n - 1)

    for i in range(2, n + 1):
        D[i][0] = W[i][1]
    for k in range(1, n - 1):
        for A in range(subset_size):
            if count(A) != k:
                continue
            for i in range(2, n + 1):
                if isIn(i, A):
                    continue
                D[i][A], j = minimum(n, i, A)
                P[i][A] = j

    A = subset_size - 1
    D[1][A], j = minimum(n, 1, A)
    P[1][A] = j
    minlength = D[1][A]


def tour(v, A):
    k = P[v][A]
    if A == 0:
        p.append(1)
    else:
        p.append(k)
        tour(k, diff(A, k))


if __name__ == "__main__":
    INF = 9999999
    n, m = map(int, input().split())
    W = [[INF] * (n + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        W[i][i] = 0
    D = [[0] * pow(2, n - 1) for _ in range(n + 1)]
    P = [[0] * pow(2, n - 1) for _ in range(n + 1)]

    for _ in range(m):
        u, v, w = map(int, input().split())
        W[u][v] = w

    func()

    print(D[1][pow(2, n - 1) - 1])
    p = [1]
    tour(1, pow(2, n-1) - 1)
    print(*p, sep=' ')

    for i in range(1, n + 1):
        for j in range(pow(2, n - 1)):
            if 0 < D[i][j] < INF:
                print(i, j, D[i][j])
