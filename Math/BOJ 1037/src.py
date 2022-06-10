n = int(input())        # N의 진짜 약수의 개수
N = list(map(int, input().split()))     # N이 진짜 약수
N.sort()		# 오름차순으로 정렬

if n%2 == 1:		
	# 약수의 개수가 홀수임
    # 따라서 중간에 있는 값의 제곱이 원래 숫자
    print(N[n//2]**2)
else:
	# 약수의 개수가 짝수이므로, 맨 좌측과 맨 우측을 곱한 것이 원래 숫자
    print(N[0] * N[-1])
