def func(W, items):
    temp = []       # 가방에 넣은 무게와 이익을 저장하는 리스트
    for item in items:      # 하나씩 가져옴
        if W - item[0] >= 0:
            # 만약 통쨰로 넣어도 문제가 없다면 W에서 item[1]을 뺌
            W -= item[0]
            temp.append([item[0], item[1]])     # 리스트에 넣음
        elif W > 0:
            # 통째로 넣기에는 무리가 있을 때
            temp.append([0, 0])     # 일단 0,0을 넣음
            for _ in range(item[0]):
                # 1의 무게와 무게당 이익을 추가함
                if W > 0:
                    # 아직 무게가 남아있다면 1을 뺴고 temp에 추가함
                    W -= 1
                    temp[-1][0] += 1
                    temp[-1][1] += item[2]
                elif W <= 0:
                    # 만약 무게가 꽉 찼다면 그대로 반환함
                    return temp
        else:
            # 만약 W <= 0일 때
            return temp
    # 무게를 다 못 채울 때
    return temp

if __name__ == "__main__":
    n = int(input())        # 아이템의 개수
    weight = list(map(int, input().split()))      # 아이템의 무게를 입력 받음
    profit = list(map(int, input().split()))       # 아이템의 이익을 입력 받음

    item = [(x, y, y // x) for x, y in zip(weight, profit)]      # 무게, 이익, 무게당 이익
    item.sort(key = lambda x : x[2], reverse=True)      # 무게당 이익을 기준으로 정렬함

    T = int(input())        # 도둑의 배낭 개수

    items = item
    for _ in range(T):
        W = int(input())        # 도둑의 배낭 무게
        temp = func(W, items)
        print(sum(map(lambda x : x[1], temp)))
        for t in temp:
            print(*t, sep=' ')
