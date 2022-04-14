from os import sep
import sys
from copy import deepcopy
input = sys.stdin.readline


def func(T, P, n):
    # 최대 경로를 찾는 함수
    # T[i][j]는 T[i-1][j-1]과 T[i-1][j]중에 큰 값을 고르면 된다.
    for i in range(1, n):
        for j in range(i + 1):
            k = max(T[i-1][j-1], T[i-1][j])
            T[i][j] += k
            if k == T[i-1][j]:
                P[i][j] = 2
            else:
                P[i][j] = 1


def path(T, P, i, j, p):
    # 경로를 찾는 함수
    if i > 0:
        k = P[i][j]
        if k == 2:
            path(T, P, i-1, j, p)       # 경로가 2이면 바로 위로 가면 됨
            # print(T[i][j] - T[i-1][j], end=' ')
        else:
            path(T, P, i-1, j-1, p)
            # print(T[i][j] - T[i-1][j-1], end=' ')
    p.append(T[i][j])       # p에다가 넣음
    # print하지 않고, 리스트를 쓴 이유는 print를 보면 T 리스트를 두 번이나 참조하는데, 시간이 더 걸릴 것 같아서 p리스트에 추가하기로 함

    

n = int(input())        # 삼각형의 높이

T = list()      # 삼각형
for i in range(n):      # 삼각형의 수를 입력 받음
    T.append(list(map(int, input().split())))
    T[i].extend([0] * (n - i - 1))      # 따로 0을 넣는 이유는 나중에 예외 처리하는데 쓰는 시간보다 차라리 메모리를 더 쓰는게 낫다는 생각

P = deepcopy(T)      # 경로를 저장하는 배열, 바로 위로 가야하면 2, 왼쪽 위로 가야하면 1

func(T, P, n)

max = idx = 0
for i in range(n):      # 최대값과 최대값의 위치를 찾음
    if max <= T[-1][i]:
        max = T[-1][i]
        idx = i


print(max)

p = list()
path(T, P, n-1, idx, p)
for i in range(len(p) - 1, 0, -1):      # p는 현재 cumsum형태로 되어있어서, 이를 다시 변환해줌
    p[i] -= p[i-1]
print(*p, sep=' ')
