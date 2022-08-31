from re import S


n, l = map(int, input().split())
maps = list(map(int, input().split()))
maps.sort()

start = maps[0]
end = maps[0] + l
cnt = 1

for i in range(n):
    if start <= maps[i] < end:
        continue
    else:
        start = maps[i]
        end = maps[i] + l
        cnt += 1

print(cnt)
