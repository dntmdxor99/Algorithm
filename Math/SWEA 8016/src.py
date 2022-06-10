T = int(input())        # 테스트 케이스의 수

for j in range(1, T + 1):
    i = int(input())    
    if i == 1:
        print(f"#{j} {1} {1}")
    else:
        left = 2 * (i - 1)**2 + 1
        right = 2 * (i)**2 - 1
        print(f"#{j} {left} {right}")
