import sys
import time
input = sys.stdin.readline

n = int(input())
S = list(map(int, input().split()))
# globals()['count'] = 0
count = 0


def partition(low, high):
    # pivot을 기준으로 나누는 함수
    global count
    count += 1
    # globals()['count'] += 1
    pivot = S[low]
    j = low
    for i in range(low + 1, high + 1):
        if S[i] < pivot:
            j += 1
            S[i], S[j] = S[j], S[i]

    S[j], S[low] = S[low], S[j]

    return j


def quicksort(low, high):
    # 리스트를 정렬하는 함수
    if low < high:
        pivotindex = partition(low, high)
        quicksort(low, pivotindex - 1)
        quicksort(pivotindex + 1, high)


s = time.time()
quicksort(0, n-1)
e = time.time()
print(count)
print(*S)

print("\n", e - s)
