def knapsack3(n: int, W: int) -> int:
    # 최대 이익을 찾는 함수
    # 이때 W는 배낭의 최대 무게가 아니라, 현재 배낭에 넣을 수 있는 최대 무게라고 봐야함

    if n == 0 or W <= 0:
        return 0

    lvalue = item.get((n - 1, W), knapsack3(n - 1, W))      # n - 1번째 아이템을 넣지 않았을 때, 값이 없다면 재귀 호출
    rvalue = item.get((n - 1, W - w[n]), knapsack3(n - 1, W - w[n]))        # n - 1번째 아이템을 넣었을 때, 값이 없다면 재귀 호출

    item[(n, W)] = lvalue if w[n] > W else max(lvalue, p[n] + rvalue)
    # 만약 n번째 아이템의 무게가 W보다 크다면, n번째 아이템을 넣지 않고,
    # 만약 아니라면 n번째 아이템을 넣거나, 넣지 않는 경우 중 큰 값을 넣음

    return item[(n, W)]


n = int(input())        # 아이템의 개수
w = list(map(int, input().split()))     # 무게
p = list(map(int, input().split()))     # 이익
T = int(input())    # 배낭 무게의 개수

item = list((i, j) for i, j in zip(w, p))       # 무게, 이익
item = [(0, 0)] + list(sorted(item, key = lambda x : x[1] // x[0], reverse= True))        # 단위 무게당 이익으로 순으로 정렬 (내림차순)
w, p = zip(*item)
# 사실 정렬은 필요 없지만, 정답을 위해선 맞춰야 함

for _ in range(T):
    W = int(input())        # 배낭 무게

    item = {}       # Hash Table
    value = knapsack3(n, W)

    print(value)

    item = list(sorted(item.items(), key = lambda x : (x[0][0], x[0][1])))      # n, W 순으로 오름차순 정렬함 (출력을 위해)
    for nW, value in item:
        print(*nW, value, sep=' ')
    
