def func(W, items):
    bag = 0
    sum = 0
    temp = []
    for item in items:
        if W - bag >= item[0]:
            bag += item[0]
            sum += item[1]
            temp.append([item[0], item[1]])
        elif W - bag > 0:
            temp.append([0, 0])
            for _ in range(item[0]):
                if bag + 1 <= W:
                    bag += 1
                    sum += item[2]
                    temp[-1][0] += 1
                    temp[-1][1] += item[2]
                elif bag + 1 > W:
                    return temp, sum
    return temp[:-1], sum

if __name__ == "__main__":
    n = int(input())        # 아이템의 개수
    weight = [0]
    weight.extend(list(map(int, input().split())))      # 아이템의 무게를 입력 받음
    profit = [0]
    profit.extend(list(map(int, input().split())))       # 아이템의 이익을 입력 받음
    ppw = [0]       # profit per weight
    ppw.extend([y // x for y, x in zip(profit[1:], weight[1:])])

    item = [(x, y, z) for x, y, z in zip(weight, profit, ppw)]      # 무게, 이익, 무게당 이익
    item.sort(key = lambda x : x[2], reverse=True)

    T = int(input())        # 도둑의 배낭 개수

    items = item
    for _ in range(T):
        W = int(input())        # 도둑의 배낭 무게
        temp, sum_profit = func(W, items)
        print(sum_profit)
        for t in temp:
            print(*t, sep=' ')



