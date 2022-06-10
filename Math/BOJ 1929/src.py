n, m = map(int, input().split())        # 두 개의 자연수

arr = [True] * (m + 1)      # True은 소수라는 뜻
arr[0] = arr[1] = False      # False은 소수가 아님

# for i in range(2, int((m + 1) ** 0.5)):
# 최고 숫자의 루트로 계산해도 되긴 함
for i in range(2, m + 1):
    # 2부터 최고 숫자까지 에라토스테네스의 체를 계산함
    if arr[i]:
        for j in range(i * 2, m + 1, i):
            # i의 배수들을 모두 False 처리함
            arr[j] = False
    

for i in range(n, m + 1):
    if arr[i]:
        print(i)
