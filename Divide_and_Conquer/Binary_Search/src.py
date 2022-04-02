n = int(input())
S = list(map(int, input().split()))
x = int(input())


def binary_search(low, high):
    # 이진 검색 함수
    if low > high:
        # low > high이면 분할할 수 없는 상태이므로 해당 값이 리스트 안에 없음
        # low == high인 상태는 배열에 원소가 하나 있으므로 이것은 아직 해당 값이 리스트 안에 없다는 뜻이 아님
        return -1
    else:
        mid = (low + high) // 2     # 리스트의 중간 위치
        if S[mid] == x:
            return mid
        elif S[mid] > x:
            return binary_search(low, mid-1)        # 왼쪽 subarray 탐색
        else:
            return binary_search(mid+1, high)       # 오른쪽 subarray 탐색


print(binary_search(0, n-1))
