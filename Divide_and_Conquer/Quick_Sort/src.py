import sys
input = sys.stdin.readline

n = int(input())
S = list(map(int, input().split()))
globals()['count'] = 0


def partition(low, high):
    globals()['count'] += 1
    pivot = S[low]
    j = low
    for i in range(low, high + 1):
        if S[i] < pivot:
            j += 1
            S[i], S[j] = S[j], S[i]

    S[j], S[low] = S[low], S[j]

    if globals()['count'] == 1:
        print(S)

    return j


def quicksort(low, high):
    if low < high:
        pivotindex = partition(low, high)
        quicksort(low, pivotindex - 1)
        quicksort(pivotindex + 1, high)


quicksort(0, n-1)
print(S)
print(count)
