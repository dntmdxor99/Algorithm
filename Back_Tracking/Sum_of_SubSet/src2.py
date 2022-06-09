def promising(i: int, weight: int, total: int) -> bool:
    # 유망함의 조건은 총 2가지
    # 현재 무게에 남은 모든 무게를 더했을 때 W보다 크거나 같아야 한다. 작으면 다 채워도 W에 미치지 못한다는 의미 => weight + total >= W
    # 현재 무게에 다음 물건의 무게를 더했을 때 W보다 작거나 같아야 한다. => weight + S[i + 1] <= W
    # 따라서 W는 다음 물건의 무게를 더한 것 보다 크고, 전체를 합한 것보다 작아야 한다.

    return weight + S[i + 1] <= W <= weight + total
    # return weight + total >= W >= weight + S[i + 1]
    # 이때 S[i + 1]를 먼저 참조 하는 코드는 사용 x, 사용하고 싶다면 S의 마지막에 0을 추가할 것


def sum_of_subsets(i: int, weight: int, total: int) -> None:
    global subset
    if weight == W:
        # 만약 현재 무게가 목표 무게와 같다면
        global cnt
        cnt += 1        # 카운트를 1 증가
        temp = [S[j] for j in range(1, i + 1) if subset[j]]     # subset[?]가 1인 숫자에 해당 하는 위치에 있는 S[?]를 넣음 ...
        subset_set.append(temp)     # temp를 추가함
        
    elif promising(i, weight, total):
        # 만약 현재 무게와 목표 무게가 같지 않다면 유망함을 체크함
        subset[i + 1] = 1       # 다음 물건을 넣음
        sum_of_subsets(i + 1, weight + S[i + 1], total - S[i + 1])      # 물건을 넣었을 때
        subset[i + 1] = 0       # 다음 물건을 넣지 않음
        sum_of_subsets(i + 1, weight, total - S[i + 1])     # 물건을 넣지 않았을 때


if __name__== "__main__":
    n, W = map(int, input().split())        # 개수와 합
    S = [0] + list(map(int, input().split())) + [0]      # 집합
    total = sum(S)      # 집합의 합

    cnt = 0     # 부분 집합의 개수
    subset = [0] * (n + 1)      # 중간중간 넣을지 말지 고민하는 상태 공간의 집합
    subset_set = []     # 제대로 된 sequence의 집합임

    sum_of_subsets(0, 0, total)

    # 아래는 출력
    print(cnt)

    for i in subset_set:
        print(*i, sep=' ')
