import sys
input = sys.stdin.readline

class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

n = int(input())
key = [0] + list(map(int, input().split()))
p = [0] + list(map(int, input().split()))

a = [[0] * (n+2) for _ in range(n+2)]
r = [[0] * (n+2) for _ in range(n+2)]


def minimum(i, j):
    maxValue = 99999
    maxk = 0
    # print(i, j)
    for k in range(i, j+1):
        value = a[i][k-1] + a[k+1][j] + sum(p[i:j + 1])
        if maxValue > value:
            maxValue = value
            maxk = k

    return maxValue, maxk


def func():
    for i in range(1, n+1):
        a[i][i] = p[i]
        r[i][i] = i

    for diagonal in range(1, n):
        for i in range(1, n - diagonal + 1):
            j = i + diagonal
            a[i][j], k = minimum(i, j)
            # a[i][j] += sum(p[i:j+1])
            r[i][j] = k


def tree(start, end):
    k = r[start][end]
    if k == 0:
        return None
    else:
        node = Node(key[k])
        node.left = tree(start, k - 1)
        node.right = tree(k+1, end)
        return node


def preorder(node):
    if node != None:
        root.append(node.data)
        preorder(node.left)
        preorder(node.right)


def inorder(node):
    if node != None:
        inorder(node.left)
        root.append(node.data)
        inorder(node.right)


func()
# print(*a, sep='\n')
# print()
# print(*r, sep='\n')
for i in range(1, n+2):
    for j in range(i - 1, n):
        print(a[i][j], end=' ')
    print(a[i][n])

for i in range(1, n + 2):
    for j in range(i - 1, n):
        print(r[i][j], end=' ')
    print(r[i][n])
print(a[1][n])
node = tree(1, n)
root = list()
preorder(node)

for i in root[:-1]:
    print(i, end=' ')
print(root[-1])

root.clear()

inorder(node)

for i in root[:-1]:
    print(i, end=' ')
print(root[-1])
