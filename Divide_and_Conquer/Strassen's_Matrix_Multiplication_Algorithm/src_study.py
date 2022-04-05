from os import sep
import sys
input = sys.stdin.readline


count = 0


def mmult(n, a, b, c):
    # 단순 행렬 곱셈
    for i in range(n):
        for j in range(n):
            for k in range(n):
                c[i][k] += a[i][j] * b[j][k]        # += 해줘야함. 그냥 =를 하면 마지막으로 들어가는 값으로만 치환됨


def partition(n, a, a11, a12, a21, a22):
    # 행렬 분할
    for i in range(n):
        for j in range(n):
            a11[i][j] = a[i][j]
            a12[i][j] = a[i][j + n]
            a21[i][j] = a[i + n][j]
            a22[i][j] = a[i + n][j + n]


def madd(n, a, b, c):
    # 단순 행렬 덧셈
    for i in range(n):
        for j in range(n):
            c[i][j] = a[i][j] + b[i][j]


def msub(n, a, b, c):
    # 단순 행렬 뺄셈
    for i in range(n):
        for j in range(n):
            c[i][j] = a[i][j] - b[i][j]


def combine(n, c, c11, c12, c21, c22):
    # 부분 행렬을 원본 행렬으로 복원
    for i in range(n):
        for j in range(n):
            c[i][j] = c11[i][j]
            c[i][j + n] = c12[i][j]
            c[i + n][j] = c21[i][j]
            c[i + n][j + n] = c22[i][j]


def strassen(n, a, b, c):
    global count
    count += 1
    if n <= threshold:
        mmult(n, a, b, c)
    else:
        m = n // 2
        D = {f'{c}{i}{j}' : [[0] * m for _ in range(m)] for c in ['a', 'b', 'c'] for i in range(1, 3) for j in range(1, 3)}     # D 딕셔너리는 sub 행렬을 저장함
        D.update({f'm{i}' : [[0] * m for _ in range(m)] for i in range(1, 8)})
        D.update({f'{c}' : [[0] * m for _ in range(m)] for c in ['l', 'r']})
        # 굳이 이렇게 할 필요 없이, A11 = list(); A12 = list() 해도 되긴함

        partition(m, a, *[D[f'{c}'] for c in list(D.keys()) if 'a' in c])
        partition(m, b, *[D[f'{c}'] for c in list(D.keys()) if 'b' in c])
        # partition을 통해 a를 4등분 함

        a11, a12, a21, a22 = [D[f'{c}'] for c in list(D.keys()) if 'a' in c]
        b11, b12, b21, b22 = [D[f'{c}'] for c in list(D.keys()) if 'b' in c]
        c11, c12, c21, c22 = [D[f'{c}'] for c in list(D.keys()) if 'c' in c]
        m1, m2, m3, m4, m5, m6, m7 = [D[f'{c}'] for c in list(D.keys()) if 'm' in c]
        l, r = D['l'], D['r']
        D.clear()
        # D 딕셔너리를 통해 쓰기 귀찮아서 다시 변수에 넣어주고, D를 초기화함
        # 근데 이럴 바에는 그냥 a11 = list(); a12 = list() 하는게 더 편할지도 모름


        # m1, m2, ... , m7 까지 구하는 과정
        madd(m, a11, a22, l)
        madd(m, b11, b22, r)
        strassen(m, l, r, m1)

        madd(m, a21, a22, l)
        strassen(m, l, b11, m2)

        msub(m, b12, b22, r)
        strassen(m, a11, r, m3)

        msub(m, b21, b11, r)
        strassen(m, a22, r, m4)

        madd(m, a11, a12, l)
        strassen(m, l, b22, m5)

        msub(m, a21, a11, l)
        madd(m, b11, b12, r)
        strassen(m, l, r, m6)

        msub(m, a12, a22, l)
        madd(m, b21, b22, r)
        strassen(m, l, r, m7)

        # c의 부분 행렬을 계산
        madd(m, m1, m4, l)
        msub(m, l, m5, r)
        madd(m, r, m7, c11)

        madd(m, m3, m5, c12)

        madd(m, m2, m4, c21)

        madd(m, m1, m3, l)
        msub(m, l, m2, r)
        madd(m, r, m6, c22)

        # 부분 행렬을 합침
        combine(m, c, c11, c12, c21, c22)
    
    
n, threshold = list(map(int, input().split()))


if (k := n) and n & -n != n:
    # n이 2의 제곱 수가 아니면 2의 제곱수로 바꿈
    k = 1
    while k < n:
        k *= 2


a = [[0] * k for _ in range(k)]
b = [[0] * k for _ in range(k)]
c = [[0] * k for _ in range(k)]


for i in range(n):      # a와 b행렬에 입력 값을 넣어줌
    lst = list(map(int, input().split()))
    for j in range(n):
        a[i][j] = lst[j]
for i in range(n):
    lst = list(map(int, input().split()))
    for j in range(n):
        b[i][j] = lst[j]


strassen(k, a, b, c)


print(count)
for i in range(n):
    print(*c[i][:n])
