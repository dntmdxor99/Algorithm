def func():
    for i in range(9):
        for j in range(i + 1, 9):
            if lst[i] + lst[j] == dif:
                a, b = lst[i], lst[j]
                lst.remove(a)
                lst.remove(b)
                return lst

lst = []
for _ in range(9):
    lst.append(int(input()))
lst.sort()
dif = sum(lst) - 100
lst = func()         
print(*lst, sep='\n')