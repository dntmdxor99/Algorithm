# 홀수일 떄, 3 곱하고, 1빼기 할 떄 순환하는 숫자들
cnt = 0


def func1(num):
    while num != 5 and num != 17:
        if num % 2 == 0:
            num = num // 2
        else:
            num = num * 3 - 1

        if num == 1:
            global cnt
            cnt += 1
            break

def func2(num):
    temp = []

    while num not in temp:
        temp.append(num)
        if num % 2 == 0:
            num = num // 2
        else:
            num = num * 3 - 1


        if num == 1:
            global cnt
            cnt += 1
            break


num = int(input())
for i in range(1, num + 1):
    # func1(i)
    func2(i)
print(f'{num - cnt}')
