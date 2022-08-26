import sys
input = sys.stdin.readline
n = int(input())
lst = [0] * 10001
for _ in range(n):
    num = int(input())
    lst[num] += 1
for key, it in enumerate(lst):
    if it != 0:
        for _ in range(it):
            print(key)
