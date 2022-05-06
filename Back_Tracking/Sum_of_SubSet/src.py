def promising(i: int, weight: int, total: int) -> bool:
    return weight + total >= W and (weight == W or weight + S[i + 1] <= W)


def sum_of_subsets(i: int, weight: int, total: int) -> None:
    global cnt
    global subset
    if promising(i, weight, total):
        if weight == W:
            cnt += 1
            for j in range(1, i + 1):
                if subset[j]:
                    subset_set.append(f'{S[j]} ')
            temp = subset_set.pop()[:-1]
            temp = temp + '\n'
            subset_set.append(temp)

        else:
            subset[i + 1] = 1
            sum_of_subsets(i + 1, weight + S[i + 1], total - S[i + 1])
            subset[i + 1] = 0
            sum_of_subsets(i + 1, weight, total - S[i + 1])


if __name__== "__main__":
    n, W = map(int, input().split())
    S = [0] + list(map(int, input().split()))
    total = sum(S)

    cnt = 0

    subset = [0] * (n + 1)
    subset_set = []

    sum_of_subsets(0, 0, total)

    print(cnt)

    for i in subset_set:
        print(i, end='')
