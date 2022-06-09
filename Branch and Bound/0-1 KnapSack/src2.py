import heapq

class Node:
    def __init__(self, level : int, weight : int, profit : int) -> None:
        self.level = level
        self.weight = weight
        self.profit = profit
        self.bound = self.setbound()

    def setbound(self) -> float:
        # bound를 계산하는 함수, Back Tracking과 동일함
        # Back Tracking의 bound 계산 함수에 자세하게 적었으므로 참고할 것

        if self.weight >= W:
            return 0
        else:
            j = self.level + 1
            bound = self.profit
            totweight = self.weight

            while j <= n and totweight + w[j] <= W:
                totweight += w[j]
                bound += p[j]
                j += 1
            
            k = j
            if k <= n:
                bound += (W - totweight) * (p[k] // w[k])

            return bound



def knapsack6():
    PQ = list()
    maxprofit = 0       # 현재까지 찾은 최대 이득
    v = Node(0, 0, 0)       # 출발 노드를 만듬

    print(v.level, v.weight, v.profit, v.bound)

    heapq.heappush(PQ, (-v.bound, v))       # PQ에는 내림차순으로 넣어야하므로 -v.bound를 넣음
    
    while PQ:
        v = heapq.heappop(PQ)[1]        # 노드만 빼내옴
        if v.bound > maxprofit:     # 이 노드가 지금까지 찾은 최대 이득보다 크다면 탐색함
            u = Node(v.level + 1, v.weight + w[v.level + 1], v.profit + p[v.level + 1])     # 우선 다음 아이템을 넣어봄

            print(u.level, u.weight, u.profit, u.bound)

            if u.weight <= W and u.profit > maxprofit:
                # 만약 다음 아이템을 넣었을 때 위의 조건에 부합한다면 maxprofit을 바꿈
                maxprofit = u.profit

            if u.bound > maxprofit:
                # 다음 아이템을 넣었을 때 bound 값이 maxprofit보다 크면 유망하므로 자식 마디까지 탐색함
                heapq.heappush(PQ, (-u.bound, u))
            
            u = Node(v.level + 1, v.weight, v.profit)       # 이번에는 다음 아이템을 넣지 않은 상황

            # 이때 maxprofit을 갱신하지 않은 이유는 아래의 이유와 같음
            # 다음 아이템을 넣지 않았으므로 maxprofit은 현재 상황과 똑같기 때문에 갱신하지 않아도 됨

            print(u.level, u.weight, u.profit, u.bound)

            if u.bound > maxprofit:
                # 다음 아이템을 넣었을 때 bound 값이 maxprofit 보다 크면 유망하므로 자식 마디까지 탐색함
                heapq.heappush(PQ, (-u.bound, u))

    print(maxprofit)


n, W = map(int, input().split())        # 아이템의 개수, 배낭 무게
w = list(map(int, input().split()))     # 무게
p = list(map(int, input().split()))     # 이익

# 무게당 이익으로 정렬 (내림차순)
item = [(i, j) for i, j in zip(w, p)]
item = [(0, 0)] + list(sorted(item, key = lambda x : x[1] // x[0], reverse=True))
w, p = zip(*item)

knapsack6()
