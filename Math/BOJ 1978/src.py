_ = int(input())
N = list(map(int, input().split()))

arr = [True] * (max(N) + 1)      # 0은 소수라는 뜻
arr[0] = arr[1] = False      # 1은 소수가 아님

for i in range(2, max(N) + 1):
    if arr[i]:
        for j in range(i * 2, max(N) + 1, i):
            arr[j] = False
    

cnt = 0
for n in N:
    if arr[n]:
        cnt += 1

print(cnt)
