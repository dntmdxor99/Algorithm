def promising(i: int) -> bool:
    j = 1
    while j < i:
        if W[i][j] and vcolor[i] == vcolor[j]:
            return False
        j += 1
    return True


def m_coloring(i: int, m: int) -> bool:
    global flag
    global cnt
    if promising(i):
        if i == ver_num:
            flag = True
            cnt += 1
        else:
            for color in range(1, m + 1):
                vcolor[i + 1] = color
                m_coloring(i + 1, m)


if __name__ == "__main__":
    ver_num, edge_num = map(int, input().split())
    W = [[0] * (ver_num + 1) for _ in range(ver_num + 1)]
    for _ in range(edge_num):
        i, j = map(int, input().split())
        W[i][j] = 1
        W[j][i] = 1

    # print(*W, sep='\n')

    vcolor = [0] * (ver_num + 1)

    for m in range(1, ver_num + 1):
        flag = False
        cnt = 0
        m_coloring(0, m)
        if flag:
            print(m)
            print(cnt)
            break
