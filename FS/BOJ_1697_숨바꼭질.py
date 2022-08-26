from collections import deque


def bfs(que : deque, maps : list):
    while que:
        x, cnt = que.popleft()
        if x == k:
            return cnt
        for nx in [x - 1, x + 1, 2 * x]:
            if 0 <= nx <= 100000 and maps[nx] == 0:
                maps[nx] = cnt + 1
                que.append((nx, cnt + 1))
                
                
        
n, k = map(int, input().split())

maps = [0] * 100001
maps[n] = 1
que = deque()
que.append((n, 0))
cnt = bfs(que, maps)
print(cnt)
    
    