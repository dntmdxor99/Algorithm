import time

n = int(input())        # 변수가 몇개인지 입력 받음
S = list(map(int, input().split()))     # 리스트를 입력 받음
x = int(input())        # 찾으려는 수를 입력 받음

print(len(S))

def search(n, S, x):
    location = 0
    while location < n and S[location] != x:       # S를 벗어나거나, x를 찾으면 종료됨
        location += 1
    return location


def Binary_search(n, S, x):
    low = 0; high = n-1
    while low <= high:
        mid = (low + high) // 2
        if x == S[mid]:
            return mid      # 찾으면 반환
        elif x > S[mid]:
            low = mid + 1
        else:       # x < S[mid]:
            high = mid - 1
    
    return -1       # 찾지 못하면 -1 반환
    

t1_start = time.time()
location = search(n, S, x)
t1_end = time.time()

t2_start = time.time()
location2 = Binary_search(n, S, x)
t2_end = time.time()

print(t1_end - t1_start)
print(t2_end - t2_start)

if location < n:       # location이 n을 넘기 전에 종료, 즉 x를 찾음
    print('Yes', location)
else:       # x를 찾지 못함
    print('No', -1)

if location2 != -1:       # location이 n을 넘기 전에 종료, 즉 x를 찾음
    print('Yes', location2)
else:       # x를 찾지 못함
    print('No', -1)
