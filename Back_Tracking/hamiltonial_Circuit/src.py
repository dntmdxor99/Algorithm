def promising(i):
    if i == ver_num - 1 and not W[vindex[ver_num - 1]][vindex[0]]:
        return False
    elif i > 0 and not W[vindex[i - 1]][vindex[i]]:
        return False
    else:
        j = 1
        while j < i:
            if vindex[i] == vindex[j]:
                return False
            j += 1
    return True


def hamiltonian(i):
    global cnt
    if promising(i):
        if i == ver_num - 1:
            cnt += 1
        else:
            for j in range(2, ver_num + 1):
                vindex[i + 1] = j
                hamiltonian(i + 1)


if __name__ == "__main__":
    ver_num, edge_num = tuple(map(int, input().split()))
    W = [[0] * (ver_num + 1) for _ in range(ver_num + 1)]
    for _ in range(edge_num):
        i, j = tuple(map(int, input().split()))
        W[i][j] = 1
        W[j][i] = 1
    vindex = [0] * (ver_num + 1)
    vindex[0] = 1
    cnt = 0
    hamiltonian(0)
    print(cnt)
