def promising(i: int) -> bool:
    for j in range(1, i + 1):
        if W[i][j] and vcolor[i] == vcolor[j]:
            # 인접한데 색깔까지 같다면 False
            return False
    return True


def m_coloring(i: int, m: int) -> bool:
    if promising(i):
        # 유망하거나 i번째까지 이상이 없는 경우
        if i == ver_num:
            # 무사히 leaf node까지 도달했다면
            global flag
            global cnt
            flag = True
            cnt += 1
        else:
            for color in range(1, m + 1):
                # 1부터 m까지 색깔을 넣음
                vcolor[i + 1] = color
                m_coloring(i + 1, m)


if __name__ == "__main__":
    ver_num, edge_num = map(int, input().split())       # 점점과 간선의 수
    W = [[0] * (ver_num + 1) for _ in range(ver_num + 1)]       # 인접행렬
    for _ in range(edge_num):
        # 인접행렬 만듬
        i, j = map(int, input().split())
        W[i][j] = 1
        W[j][i] = 1

    vcolor = [0] * (ver_num + 1)        # 색깔의 집합

    for m in range(1, ver_num + 1):
        # 최소의 m값을 출력하는 것
        flag = False        # 기본적으로 False로 나둔 후 색깔 칠하기가 가능하면 True로 변경
        cnt = 0
        m_coloring(0, m)
        if flag:
            # flag가 True라는 것은 색깔 칠하기가 가능하다는 의미
            print(m)
            print(cnt)
            exit()
