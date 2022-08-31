n, s, p = map(int, input().split())
if n == 0 :
    print("1")
    exit()
lst = list(map(int, input().split())) + [-1] * (p - n)
for i in range(p, 0, -1):
    if lst[i - 1] >= s:
        if i + 1 > p:
            print("-1")
        else:
            if lst[i - 1] == s:
                while i > 0:
                    if lst[i - 1] == s:
                        i -= 1
                    else:
                        break
                print(i + 1)
            else:
                print(i + 1)
        break
if lst[0] < s:
    print("1")