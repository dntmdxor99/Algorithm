import sys
input = sys.stdin.readline
threshold = int(input())        # 임곗값 입력

A = list(map(int, reversed(input()[:-1])))     # input받은 것을 '\n'을 제외하고 역순 처리
B = list(map(int, reversed(input()[:-1])))     # input받은 것을 '\n'을 제외하고 역순 처리


def list_to_int(A):
    # 숫자형 리스트를 정수로 바꿔줌
    A.reverse()
    A = ''.join(list(map(str, A)))      # 숫자형 리스트를 string 타입 변환 후 이어붙임
    return A


def roundup_carry(A):       
    # 반올림 함수
    carry = 0
    for i in range(len(A)):
        A[i] += carry       # carry의 초깃값은 0이라 A[0]에 영향을 주지 않지만, loop문 안에서 carry가 업데이트 되면서, 그 다음 A[i]에게 영향을 줌 
        carry = A[i] // 10      # carry 업데이트
        A[i] %= 10      # A[i] 업데이트
    if carry != 0:      # A배열이 끝났는데 carry가 0이 아니면
        A.append(carry)     # 리스트의 끝에 반올림 해줌


def ladd(A, B):
    # 더하기 함수
    c = [0] * max(len(A), len(B))       # 둘 중에 큰 길이의 배열로 길이 설정
    for i in range(len(c)):     # 일단 다 더함
        if i < len(A): c[i] += A[i]
        if i < len(B): c[i] += B[i]
    roundup_carry(c)        # 반올림 함수를 통해 c 배열을 업데이트

    return c


def lmult(A, B):
    # A, B 단순 곱셈 함수
    c = [0] * (len(A) + len(B) - 1)
    for i in range(len(A)):
        for j in range(len(B)):
            c[i + j] += A[i] * B[j]
    roundup_carry(c)

    return c


def div_by_exp(A, m):
    # A // 10^m 함수
    if len(A) <= m:      # A와 m의 자릿수가 같다면 몫은 0임
        return [0]
    return A[m:]


def rem_by_exp(A, m):       
    # A % 10^m 함수
    if len(A) <= m:     # A와 m의 자릿수가 같다면 나머지는 A임
        return A
    return A[:m]


def pow_by_exp(A, m):
    # A * 10^m 함수
    remove_zero(A)
    if len(A) == 0:
        return [0]
    c = [0] * m     # c에 0을 먼저 집어 넣음
    c.extend(A)     # c에 A를 extend함

    return c


def remove_zero(A):
    # 맨 뒤의 0을 없애주는 함수
    while len(A) != 0 and A[-1] == 0:       # 리스트가 비지 않고, 맨 뒤에가 0일 때
        A.pop()


def prod(A, B):
    # 큰 숫자의 곱하기 함수
    [remove_zero(x) for x in [A, B]]        # A, B의 끝에 0이 들어가는지 우선 check
    globals()['count'] += 1     # global 변수 count 참조 및 수정
    N = max(len(A), len(B))     # 큰 숫자의 분할을 위해 N 설정, 이 N은 추후 m = N // 2 를 위해 활용
    if len(A) == 0 or len(B) == 0:      # A, B 둘중에 하나라도 길이가 0이면 0이므로 곱하기는 0이 됨
        C = [0]
    elif N <= threshold:        # N이 임곗값 보다 작으면
        C = lmult(A, B)     # 단순 계산을 함
    else:
        # xz * 10^2m + (xw + yz) * 10^m + yw
        m = N // 2      # 큰 숫자를 분할
        x = div_by_exp(A, m); y = rem_by_exp(A, m)      # A를 분할
        z = div_by_exp(B, m); w = rem_by_exp(B, m)      # B를 분할

        t1 = prod(x, z); t2 = pow_by_exp(t1, 2 * m)     # t2 = xz * 10^2m
        t3 = prod(x, w); t4 = prod(y, z); t5 = ladd(t3, t4); t6 = pow_by_exp(t5, m)     # t6 = (xw + yz) * 10^m
        t7 = prod(y, w)     # t7 = yw
        t8 = ladd(t2, t6); C = ladd(t7, t8)     # 전체 더하기

    return C


globals()['count'] = 0      # 글로벌 변수 count 선언
C = prod(A, B)
remove_zero(C)
print(globals()['count'])

# print(list_to_int(C) if len(C) else 0)

# if len(C):
#     print(*list(reversed(C)), sep='')
# else:
#     print(0)
