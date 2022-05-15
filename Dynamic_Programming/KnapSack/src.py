def func(n : int, W : int) -> int:
    if n == 0 or W <= 0:
        return 0

    lvalue = item.get((n - 1, W), func(n - 1, W))
    rvalue = item.get((n - 1, W - w[n]), func(n - 1, W - w[n]))
    item[(n, W)] = lvalue if w[n] > W else max(lvalue, p[n] + rvalue)

    return item[(n, W)]


if __name__ == "__main__":
    n = int(input())        # 아이템 개수
    w = list(map(int, input().split()))     # 무게
    p = list(map(int, input().split()))     # 이익
    item = list((i, j) for i, j in zip(w, p))       # 무게, 이익, 단위 무게당 이익
    item = [(0, 0, 0)] + list(sorted(item, key = lambda x : x[1] // x[0], reverse= True))        # 정렬
    w, p = zip(*item)
    T = int(input())        # 배낭 무게의 개수
    for _ in range(T):
        item = dict()
        W = int(input())        # 배낭 무게를 입력 받음
        value = func(len(w) - 1, W)
        item = list(sorted(item.items(), key = lambda x : (x[0], x[1])))
        print(value)
        for i in item:
            print(*i[0], sep=' ', end=' ')
            print(i[1])
