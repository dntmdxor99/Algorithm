import sys
import copy
input = sys.stdin.readline

def check_power_of_2(N):
    if (N & -N) == N:
        return N
    else:
        k = 1
        while k < N:
            k *= 2
        return k


def add_zero(M, idx, N):
    for i in range(N):
        M[i].extend([0 for _ in range(idx)])
    M.extend([0 for _ in range(N + idx)] for _ in range(idx))

    return M


def print_matrix(N, M):
    for i in range(N):
        print(*M[i][:N])


def partition(m, M, M11, M12, M21, M22):
    for i in range(m):
        for j in range(m):
            M11[i][j] = M[i][j]
            M12[i][j] = M[i][j + m]
            M21[i][j] = M[i+m][j]
            M22[i][j] = M[i+m][j+m]


def mmult(N, A, B, C):
    for i in range(N):
        for j in range(N):
            for k in range(N):
                C[i][k] += A[i][j] * B[j][k]


def madd(N, A, B, C):
    for i in range(N):
        for j in range(N):
            C[i][j] = A[i][j] + B[i][j]


def msub(N, A, B, C):
    for i in range(N):
        for j in range(N):
            C[i][j] = A[i][j] - B[i][j]


def resize(m, M):
    M.extend([[0 for _ in range(m)] for _ in range(m)])


def combine(m, C, C11, C12, C21, C22):
    for i in range(m):
        for j in range(m):
            C[i][j] = C11[i][j]
            C[i][j+m] = C12[i][j]
            C[i+m][j] = C21[i][j]
            C[i+m][j+m] = C22[i][j]


def strassen(N, A, B, C):
    global Threshold
    global count
    count += 1
    if N <= Threshold:
        mmult(N, A, B, C)
    else:
        m = N//2
        A11 = list(); A12 = list(); A21 = list(); A22 = list(); B11 = list(); B12 = list(); B21 = list(); B22 = list(); C11 = list(); C12 = list(); C21 = list(); C22 = list()
        M1 = list(); M2 = list(); M3 = list(); M4 = list(); M5 = list(); M6 = list(); M7 = list()
        L = list(); R = list()
        resize(m, A11); resize(m, A12); resize(m, A21); resize(m, A22)
        resize(m, B11); resize(m, B12); resize(m, B21); resize(m, B22)
        resize(m, C11); resize(m, C12); resize(m, C21); resize(m, C22)
        resize(m, M1); resize(m, M2); resize(m, M3); resize(m, M4); resize(m, M5); resize(m, M6); resize(m, M7)
        resize(m, L); resize(m, R)

        partition(m, A, A11, A12, A21, A22)
        partition(m, B, B11, B12, B21, B22)

        madd(m, A11, A22, L)
        madd(m, B11, B22, R)
        strassen(m, L, R, M1)       ###M1

        madd(m, A21, A22, L)
        strassen(m, L, B11, M2)     ###M2

        msub(m, B12, B22, R)
        strassen(m, A11, R, M3)     ###M3

        msub(m, B21, B11, R)
        strassen(m, A22, R, M4)     ###M4

        madd(m, A11, A12, L)
        strassen(m, L, B22, M5)     ###M5

        msub(m, A21, A11, L)
        madd(m, B11, B12, R)
        strassen(m, L, R, M6)       ###M6

        msub(m, A12, A22, L)
        madd(m, B21, B22, R)
        strassen(m, L, R, M7)       ###M7

        # print(M1, M2, M3, M4, M5, M6, M7)

        madd(m, M1, M4, L)
        msub(m, L, M5, L)
        madd(m, L, M7, C11)          ###C1

        madd(m, M3, M5, C12)        ###C2

        madd(m, M2, M4, C21)        ###C3

        madd(m, M1, M3, L)
        msub(m, L, M2, L)
        madd(m, L, M6, C22)          ###C4

        combine(m, C, C11, C12, C21, C22)



N, Threshold = map(int, input().split())

k = check_power_of_2(N)
idx = k - N

A = [list(map(int, input().split())) for _ in range(N)]
B = [list(map(int, input().split())) for _ in range(N)]

if idx != 0:
    A = add_zero(A, idx, N)
    B = add_zero(B, idx, N)

C = [[0 for _ in range(k)] for _ in range(k)]

count = 0

strassen(k, A, B, C)

print(count)
print_matrix(N, C)
