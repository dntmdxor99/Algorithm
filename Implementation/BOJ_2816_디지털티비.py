def b1():
    # 화살표를 아래로 내림
    global now
    if now < n - 1:
        now += 1
        print("1", end='')


def b2():
    # 화살표를 위로 올림
    global now
    if now > 0:
        now -= 1
        print("2", end='')


def b3():
    # 현재 채널을 아래로 내림
    global now
    if now < n - 1:
        lst[now], lst[now + 1] = lst[now + 1], lst[now]
        now += 1
        print("3", end='')


def b4():
    # 현재 채널을 아래로 내림
    global now
    if now > 0:
        lst[now], lst[now - 1] = lst[now - 1], lst[now]
        now -= 1
        print("4", end='')


n = int(input())        # 채널의 수

lst = []        # 채널을 입력
for _ in range(n):
    lst.append(input().strip())

now = 0     # 현재 채널 (화살표)


if lst[0] != "KBS1":
    while lst[now + 1] != "KBS1":
        b3()

    if lst[1] == "KBS1":
        b3()
    else:
        b1()
        while lst[0] != "KBS1":
            b4()

if lst[1] != "KBS2":
    while lst[now + 1] != "KBS2":
        b1()

    if lst[2] == "KBS2":
        b3()
    else:
        b1()
        while lst[1] != "KBS2":
            b4()