n = int(input())
maps = [list(input()) for _ in range(n)]

cnt = [0, 0]

for i in range(n):
    len_vertical, len_horizon = 0, 0
    for j in range(n):
        if maps[i][j] == ".":
            len_horizon += 1
        else:
            len_horizon = 0
        if len_horizon == 2:
            cnt[0] += 1
        
        if maps[j][i] == '.':
            len_vertical += 1
        else:
            len_vertical = 0
        if len_vertical == 2:
            cnt[1] += 1
    
print(*cnt, sep=' ')