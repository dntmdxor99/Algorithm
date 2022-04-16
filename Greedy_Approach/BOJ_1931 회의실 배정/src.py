import sys
input = sys.stdin.readline


def func(case):
    i = 1
    solved = True

    while solved:       # 더 이상 들어갈 수 없다면 False임
        solved = False
        case.append((s[i], e[i]))       # i가 1로 시작하고, 나중에는 아래의 조건에 맞는 회의가 들어감

        for j in range(i + 1, n + 1):
            if s[j] >= e[i]:        # j번째 회의의 시작 시간이 i번째 회의의 끝나는 시간 이후라면
                i = j        # 해당 회의를 넣고 끝내버림
                solved = True
                break


n = int(input())        # 회의의 개수
s = [0]      # 회의의 시작 시간
e = [0]      # 회의의 종료 시간
case = [(-1, -1)]       # 회의의 경우의 수의 리스트
for _ in range(n):
    # 회의를 입력받음
    start, end = map(int, input().split())  
    case.append((start, end))

case = sorted(case, key = lambda x : (x[1], x[0]))      # 끝나는 시간이 같은 경우를 고려

for i in range(1, n + 1):
    s.append(case[i][0])
    e.append(case[i][1])

case.clear()
func(case)

print(len(case))
# for i in range(1, len(case)):
#     print(*case[i])
