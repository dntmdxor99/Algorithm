def promising():
    pass


def func(s, c, sum):
    if promising():
        for i in range(n):
            if c[i]:
                c[i] = False
                func(s, c)
                c[i] = True
    else:
        return 


n = int(input()) 
s = list(map(int, input().split()))
c = [True] * n
sum = []

for i in range(n):
    if c[i]:
        c[i] = False
        sum.append(c[i])
        func(s, c, sum)
        c[i] = True
        sum.pop()