def promising(i):
    for k in range(1, i):
        # 1 ~ i-1까지 봤을 때, 같은 열, 같은 대각선이 아니라면 유망함
        if col[i] == col[k] or abs(col[i] - col[k]) == i - k:
            return False
    return True


def queens(i):
    global col, n, max_value, cnt

    if promising(i):
        # 만약 i번째 row가 유망하다면
        if i == n:
            # state space의 끝에 도달함
            cnt += 1
            temp = int(''.join(map(str, col)))
            if temp > max_value:
                max_value = temp
        else:
            # state space의 끝에 도달하지 않음
            for j in range(1, n + 1):
                # 모든 column을 넣어봄
                col[i + 1] = j      # i번째까지 유망하므로, i + 1에 j를 넣음
                queens(i + 1)


n = int(input())        # 보드의 크기
col = [0] * (n + 1)     # 각 row에서의 queen의 column
max_value = 0
cnt = 0

queens(0)

print(cnt)
print(max_value)
