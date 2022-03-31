import time

def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)


def fib2(n):
    lst = list()
    if n <= 1:
        return n
    else:
        lst.append(0)
        lst.append(1)
        for i in range(2, n+1):
            lst.append(lst[i-1] + lst[i-2])
        return lst[n]


n = int(input())

start = time.time()
print(fib(n))
end = time.time()

start2 = time.time()
print(fib2(n))
end2 = time.time()

print(end - star/t)
print(end2 - start2)
