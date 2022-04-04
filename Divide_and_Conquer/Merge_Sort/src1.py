n = int(input())
S = list(map(int, input().split()))


def mergesort(s, n):
    # 두 개로 분할함
    if len(s) > 1:
        # 원소가 2개 이상일 때, merge sort를 함
        m = n // 2      # m은 중간 인덱스
        h = n - m       # h는 중간 인덱스 이후의 시작 인덱스
        sub_a = s[:m]
        sub_b = s[m:]
        mergesort(sub_a, m)
        mergesort(sub_b, h)
        merge(s, sub_a, sub_b, m, h)


def merge(s, sub_a, sub_b, m, h):
    # 병합함
    i = j = k = 0
    while i < m and j < h:
        # 배열 안에서 합병과 정렬을 같이 함
        if sub_a[i] < sub_b[j]:
            s[k] = sub_a[i]
            i += 1
        else:
            s[k] = sub_b[j]
            j += 1
        k += 1

    if i > m:
        # 아직 남아 있는 배열이 있으면
        while j < h:
            s[k] = sub_b[j]
            j += 1; k += 1
    else:
        while i < m:
            s[k] = sub_a[i]
            i += 1; k += 1


mergesort(S, n)
print(S)
