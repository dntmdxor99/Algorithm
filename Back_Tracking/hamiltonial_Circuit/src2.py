# i번째 정점과 i번 정점은 다른 이야기임, 앞은 순서를 의미, 뒤는 정점의 번호를 의미

def promising(i):
    # 유망하지 않는 조건은 총 3가지
    # 마지막 남은 정점에 도달했는데, 출발 정점으로 돌아갈 수 없는 경우
    # i번째 정점은 i - 1번째 정점과 인접하지 않은 경우
    # i번째 정점을 이미 방문했었을 때
    if i == ver_num and W[vindex[ver_num]][vindex[1]] == 0:
        return False
    elif i > 1 and W[vindex[i - 1]][vindex[i]] == 0:
        return False
    else:
        if vindex[i] in vindex[:i]:
            # 1~i-1번째 방문 정점들을 봤을 때, i번째 방문 정점과 중복되면 False
            return False
    return True


def hamiltonian(i):
    if promising(i):
        if i == ver_num:
            # 무사히 끝까지 도달했고, promising 함수에 의해 출발 정점으로 돌아갈 수 있다면
            global cnt
            cnt += 1
        else:
            for j in range(2, ver_num + 1):
                # 2번 정점부터 차례대로 i + 1번째에 방문함
                vindex[i + 1] = j
                hamiltonian(i + 1)


if __name__ == "__main__":
    ver_num, edge_num = tuple(map(int, input().split()))        # 정점과 간선의 개수
    W = [[0] * (ver_num + 1) for _ in range(ver_num + 1)]       # 인접행렬

    for _ in range(edge_num):
        i, j = tuple(map(int, input().split()))
        W[i][j] = 1
        W[j][i] = 1

    vindex = [0] * (ver_num + 1)        # 순서의 집합

    vindex[1] = 1       # 첫 번째 시작은 1번 정점부터
    cnt = 0
    hamiltonian(1)      # 첫 번째 시작부터 찾음
    print(cnt)
