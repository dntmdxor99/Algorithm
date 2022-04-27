import sys
import copy
input = sys.stdin.readline


def is_feasible(J):
    # 해당 set이 feasible한지 확인하는 함수
    len_J = len(J)      # len(J)를 계속 호출하는 것보다 변수에 저장하는게 나음

    for i in range(1, len_J):
        # 해당 set이 feasible한지 확인함
        if J[i][0] < i:     # i번째에 위치한 job의 데드라인이 i보다 작다면 false임
            # i번째에 위치했다는 뜻은 해당 job이 끝나는 시간이 i라는 뜻임
            return False
    return True


def func():
    # scheduling 하는 함수
    S = []      # feasible set임
    S.append(job_dict[0])        # 먼저 0을 넣어서 편리하게 이용함
    S.append(job_dict[1])

    J = []      # 쓰레기 집합

    for i in range(2, n + 1):
        J = copy.deepcopy(S)        # J가 S를 복사함

        idx = 1     # 새로운 작업이 들어갈 곳
        k = job_dict[i][0]      # 새로운 작업의 데드라인
        while idx < len(J) and J[idx][0] <= k:
            # 새로운 작업이 어디에 들어가야할지 정함, 데드라인을 기준으로 오름차순을 하면 됨
            # idx가 J의 길이를 넘지 않아야 하고, 앞의 idx의 deadline의 새로운 작업의 deadline보다 작아야함
            idx += 1

        J.insert(idx, job_dict[i])      # job이 있어야 하는 자리에 넣음

        if is_feasible(J):      # 만약 J가 수행가능하다면 S에 집어 넣음
            S.insert(idx, job_dict[i])
    
    return S


n = int(input())        # job의 개수
deadline = list(map(int, input().split()))      # deadline을 받음
profit = list(map(int, input().split()))     # profit을 받음, profit은 내림차순으로 정렬되어 있음

job_dict = {0 : (0, 0)}
for i in range(1, n + 1):
    job_dict[i] = (deadline[i - 1], profit[i - 1])      # deadline과 profit의 집합을 만듬

# print(job_dict)
S = func()
print(sum([S[i][1] for i in range(1, len(S))]))     # 최대 profit을 출력
print(*[S[i][1] for i in range(1, len(S))], sep=' ')        # feasible sequence를 출력
