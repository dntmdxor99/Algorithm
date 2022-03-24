
import sys
input = sys.stdin.readline
threshold = int(input())

n1 = list(map(int, reversed(input()[:-1])))
n2 = list(map(int, reversed(input()[:-1])))


def list_to_int(A):
    A.reverse()
    A = ''.join(list(map(str, A)))
    return A


def roundup_carry(A):
    carry = 0
    for i in range(len(A)):
        A[i] += carry
        carry = A[i] // 10
        A[i] %= 10
    if carry != 0:
        A.append(carry)


def ladd(A, B):
    c = [0] * max(len(A), len(B))
    for i in range(len(c)):
        if i < len(A): c[i] += A[i]
        if i < len(B): c[i] += B[i]
    roundup_carry(c)

    return c


C = ladd(n1, n2)


