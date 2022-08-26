m, n = list(map(int, input().split()))
nl = set()
ns = set()
for _ in range(m):
    nl.add(input().rstrip())
for _ in range(n):
    ns.add(input().rstrip())
i = list(nl.intersection(ns)).sort()
print(len(i))
print(*i, sep='\n')