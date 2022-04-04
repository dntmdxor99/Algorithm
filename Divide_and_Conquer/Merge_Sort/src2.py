n = int(input())
S = list(map(int, input().split()))


def mergesort(low, high):
    # 두 개로 분할함
    if low < high:
        mid = (low + high) // 2
        mergesort(low, mid)
        mergesort(mid+1, high)
        merge(low, mid, high)


def merge(low, mid, high):
    # 병합함
    i = low; j = mid + 1;
    U = list()
    while i <= mid and j <= high:
        U.append((S[i], i := i + 1)[0] if S[i] < S[j] else (S[j], j := j + 1)[0])

    if i > mid:
        while j <= high:
            U.append(S[j])
            j += 1
    else:
        while i <= mid:
            U.append(S[i])
            i += 1

    for idx in range(low, high + 1):
        S[idx] = U[idx - low]


mergesort(0, n-1)
print(S)
