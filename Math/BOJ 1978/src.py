_ = int(input())        # 필요 없음
N = list(map(int, input().split()))     # 숫자들을 입력 받음

arr = [True] * (max(N) + 1)      # True은 소수라는 뜻
arr[0] = arr[1] = False      # False은 소수가 아님

for i in range(2, max(N) + 1):
    # 2부터 최고 숫자까지 에라토스테네스의 체를 계산함
    if arr[i]:
        for j in range(i * 2, max(N) + 1, i):
            # i의 배수들을 모두 False 처리함
            arr[j] = False
    

cnt = 0
for n in N:
    if arr[n]:
        cnt += 1

print(cnt)
