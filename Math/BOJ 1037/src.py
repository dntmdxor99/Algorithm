n = int(input())        # N의 진짜 약수의 개수
N = list(map(int, input().split()))     # N이 진짜 약수
N.sort()
if n%2 == 1:
    print(N[n//2]**2)
else:
    print(N[0] * N[-1])
