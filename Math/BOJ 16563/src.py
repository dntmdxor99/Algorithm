from math import sqrt

_ = int(input())        # 필요 없음
k = list(map(int, input().split()))     # 자연수들
M = max(k)      # 자연수의 최댓값

arr = list(i for i in range(M + 1))     # arr을 초기화 함

for i in range(2, int(sqrt(M)) + 1):
    # 2부터 M의 제곱근까지만 계산해도 됨
    if arr[i] == i:
        # 만약 소수라면
        arr[i] = i
        for j in range(i + i, M + 1, i):
            # 소수의 배수를 전부 다 소수로 초기화 함
            arr[j] = min(arr[j], i)     # 이때 제일 작은 소수로 초기화 해야함

for i in k:
    while i != 1:
        # i가 1이 되지 않을 때 까지 계속 나눠야 함
        print(arr[i], end = ' ')        # arr[i]는 i를 나누는 가장 작은 소수
        i //= arr[i]
    print()
