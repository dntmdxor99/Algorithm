def promising(i):
    k = 1

    while k < i:
        if col[i] == col[k] or abs(col[i] - col[k]) == i - k:
            return False
        k += 1

    return True


def queens(i):
    global cnt
    global max_value
    if promising(i):
        if i == n:
            cnt += 1
            temp = int(''.join(map(str, col)))
            if temp > max_value:
                max_value = temp
        else:
            for j in range(1, n + 1):
                col[i + 1] = j
                queens(i + 1)


if __name__ == "__main__":
    n = int(input())
    cnt = 0
    col = [0] * (n + 1)
    max_value = 0
    queens(0)

    print(cnt)
    print(max_value)
