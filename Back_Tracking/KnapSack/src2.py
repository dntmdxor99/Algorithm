from copy import deepcopy

### 참고로 마디가 유망한것과 maxprofit을 업데이트 하는 것은 엄연히 다른 과정임

def promising(i : int, profit : int, weight : int) -> bool:
    global bound, totweight

    if weight >= W:
        # 만약 현재까지의 무게가 W보다 크거나 같다면 자식 마디는 유망하지 않음
        return False
    else:
        j = i + 1
        bound = profit      # global로 참조했지만, profit과 weight로 초기화 하기 때문에 상관은 없음
        totweight = weight

        while j <= n and totweight + w[j] <= W:
            # i + 1에서 k - 1까지 갔을 때의 무게와 그때까지의 이익을 계산함
            # 만약 j가 n보다 커진다면 다 담아도 터지지 않는다는 뜻임
            totweight += w[j]
            bound += p[j]
            j += 1
        
        k = j
        if k <= n:
            # 만약에 k가 n보다 작다면, i번째 마디의 자식 마디에 대한 이익의 상한선을 구함
            bound += (W - totweight) * (p[k] // w[k])

        return bound > maxprofit


def func(i : int, profit : int, weight : int) -> None:
    global maxprofit, bestset
    if weight <= W and profit >= maxprofit:
        # 지금까지 담은 무게가 W보다 작고, 아이템의 이익이 지금까지 얻은 최대 이익보다 크거나 같다면 업데이트함
        maxprofit = profit
        bestset = deepcopy(include)

    flag = promising(i, profit, weight)     # bound를 업데이트 하기 위해 미리 실행함
    print(i, weight, profit, bound, maxprofit)

    if flag:
        
        # 넣었을 때의 경우
        include[i + 1] = True
        func(i + 1, profit + p[i + 1], weight + w[i + 1])

        # 넣지 않았을 때의 경우
        include[i + 1] = False
        func(i + 1, profit, weight)



n, W = map(int, input().split())        # 아이템 개수, 배낭 무게
w = list(map(int, input().split()))     # 무게
p = list(map(int, input().split()))     # 이익

# 아이템을 무게당 이익 순으로 정렬하는 것 (내림차순)
item = [(i, j) for i, j in zip(w, p)]
item = [(0, 0)] + list(sorted(item, key = lambda x : x[1] // x[0], reverse= True))
w, p = zip(*item)

maxprofit = 0       # 최대 이익
include = [0] * (n + 1)     # 지금까지 담은 아이템, 1이면 해당 인덱스의 아이템을 담은 것
bestset = [0] * (n + 1)     # 최대 이익일 때의 set
totweight = 0       # 특정 마디일 때의 무게 합
bound = 0       # 특정 마디일 때 자식 마디로 갔을 때의 이익의 상한선

func(0 ,0, 0)

print(maxprofit)        # 최대 이익을 출력
for i in range(1, n + 1):
    if bestset[i] == 1:
        print(w[i], p[i])
