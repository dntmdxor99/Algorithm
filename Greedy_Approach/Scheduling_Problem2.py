def is_feasible(K):
    # 실행 가능한지 체크하는 함수
    for i in range(len(K)):
        if i + 1 > deadline[K[i]]:
            # 해당 job의 데드라인이 i + 1보다 작으면 impossible한 것. 데드라인은 1부터 시작, i는 0부터 시작
            return False
    return True


def schedule(J):
    # 스케쥴링하는 함수
    for i in range(n):
        K = J.copy()  # 우선 복사함

        idx = 0     # K의 뒤에 새롭게 들어가야하는 위치를 정함

        while idx < len(K) and deadline[K[idx]] <= deadline[i]:
            # 우선 idx는 K의 길이보다 작아야하고,
            # K의 idx번째에 있는 애의 deadline은 i의 deadline보다 작아야함
            # 참고로 K에는 몇 번째 job이 들어가있는지를 나타냄, 1 0 3 이라면 두 번째, 첫 번째, 네 번째 작업이 들어가있는 것
            idx += 1

        K.insert(idx, i)        # deadline의 오름차순에 맞게 넣음
        if is_feasible(K):
            # 만약에 K가 실행 가능하다면
            J = K.copy()        # 그대로 J에 K를 카피함

    return J


n = int(input())        # 몇 개인지
deadline = list(map(int, input().split()))      # 데드라인
profit = list(map(int, input().split()))        # 이익

J = []      # 초기의 실행 가능 집합
J = schedule(J)

# 아래는 출력
feasible_total = list(map(lambda x: profit[x], J))
print(sum(feasible_total))
print(*feasible_total, sep=' ')
