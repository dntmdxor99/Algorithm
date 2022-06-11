def func() -> int:
    cnt = 0     # bin의 개수    
    
    l = 0
    r = n - 1       # 뒤에서 찾아야함

    while l <= r:
        if item[l] + item[r] <= L:
            r -= 1
        l += 1
        cnt += 1

    return cnt
            
            
if __name__ == "__main__":
    n = int(input())        # 물건 개수
    L = int(input())        # bin의 길이
    item = [int(input()) for _ in range(n)]     # 아이템의 길이

    item.sort(reverse=True)     # 아이템을 내림차순으로 정렬

    bin_cnt = func()

    print(bin_cnt)
