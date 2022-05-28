from collections import deque
import heapq


class Node:
    # 노드를 만듬
    def __init__(self, level: int, weight: int, profit: int) -> None:
        self.level = level
        self.weight = weight
        self.profit = profit
        self.bound = self.setbound()

    def setbound(self) -> float:
        if self.weight >= W:
            return 0
        else:
            result = self.profit
            j = self.level + 1
            totweight = self.weight

            while j <= n and totweight + item[j][0] <= W:
                totweight += item[j][0]
                result += item[j][1]
                j += 1

            k = j
            if k <= n:
                result += (W - totweight) * item[k][1] // item[k][0]

            return result


# def bound(u: Node) -> float:
#     if u.weight >= W:
#         return 0
#     else:
#         result = u.profit
#         j = u.level + 1
#         totweight = u.weight
#
#         while j <= n and totweight + item[j][0] <= W:
#             totweight += item[j][0]
#             result += item[j][1]
#             j += 1
#
#         k = j
#         if k <= n:
#             result += (W - totweight) * item[k][1] / item[k][0]
#
#         return result


def func() -> None:
    PQ = []     # max heap임
    maxprofit = 0       # 현재까지의 최대 이익
    v = Node(0, 0, 0)
    print(v.level, v.weight, v.profit, v.bound)
    heapq.heappush(PQ, (-v.bound, v))
    # print(v.bound)
    while not len(PQ) == 0:
        v = heapq.heappop(PQ)[1]
        if v.bound > maxprofit:
            u = Node(v.level + 1, v.weight + item[v.level + 1][0], v.profit + item[v.level + 1][1])

            print(u.level, u.weight, u.profit, u.bound)

            if u.weight <= W and u.profit > maxprofit:
                maxprofit = u.profit

            if u.bound > maxprofit:
                heapq.heappush(PQ, (-u.bound, u))

            u = Node(v.level + 1, v.weight, v.profit)

            print(u.level, u.weight, u.profit, u.bound)

            if u.bound > maxprofit:
                heapq.heappush(PQ, (-u.bound, u))

    print(maxprofit)


if __name__ == "__main__":
    n, W = map(int, input().split())        # 아이템 개수, 배낭 무게
    w = list(map(int, input().split()))     # 아이템 무게 w
    p = list(map(int, input().split()))     # 아이템 이익 p
    item = [(i, j) for i, j in zip(w, p)]
    item.sort(key= lambda x: x[1] / x[0], reverse=True)       # 하나로 묶어서 내림차순으로 정렬
    item = [(0, 0)] + item

    func()
