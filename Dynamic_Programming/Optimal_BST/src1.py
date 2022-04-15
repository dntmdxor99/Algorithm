import sys
input = sys.stdin.readline


class node:
    # 트리를 구성하는 노드
    def __init__(self, key):
        self.left = None
        self.right = None
        self.key = key


def minimum(i ,j):
    # i부터 j까지의 노드 중에 최적의 트리를 찾아줌
    minvalue = 999999
    minidx = 0
    for k in range(i, j + 1):
        # k는 i가 루트일때부터, j가 루트일때까지 계산한다.
        value = A[i][k - 1] + A[k + 1][j] + sum(p[i : j + 1])
        if minvalue > value:
            minvalue = value
            minidx = k

    return minvalue, minidx
        


def func(n):
    # 최적 값을 찾는 함수
    for diagonal in range(1, n):        # 대각선은 총 n개가 있음
        for i in range(1, n - diagonal + 1):
            # diagonal = 1 일때, i는 1부터 n - 1까지 가야함
            # diagonal = 2 일때, i는 1부터 n - 2까지 가야함
            j = i + diagonal        # diagonal = 1 일때, j는 i의 바로 다음 인덱스임
            A[i][j], R[i][j] = minimum(i, j)


def create_tree(start, end):
    k = R[start][end]
    if k == 0:
        return None
    else:
        root = node(key[k])
        root.left = create_tree(start, k - 1)
        root.right = create_tree(k + 1, end)

        return root


def inorder(root):
    if root != None:
        inorder(root.left)
        print(root.key, end=' ')
        inorder(root.right)


def preorder(root):
    if root != None:
        print(root.key, end=' ')
        preorder(root.left) 
        preorder(root.right)            

        
n = int(input())
key = [0] + list(map(int, input().split()))       # key 값을 입력 받음
p = [0] + list(map(int, input().split()))     # 확률 값을 입력 받음

A = [[0] * (n+1) for _ in range(n+2)]       # 최적 값을 저장하는 배열
R = [[0] * (n+1) for _ in range(n+2)]       # 최적 값이 되는 루트를 저장하는 배열
# 이때 행은 1부터 n+1이고, 열은 1부터 n까지인 이유는, k에 값이 들어갈 때 행은 초과할 수 있지만, 열은 초과할 수 없기 때문이다.
# 예를 들어 n이 최고 루트라면 A[1][n-1]까지의 값과 A[n+1][n]의 값을 더해야 함. 따라서 행을 초과할 수 있음
# 하지만 1이 최고 루트라면 A[1][0] + A[2][n]인데, 이때 열은 (아래로) 초과할 수 없음

for i in range(1, n + 1):
    A[i][i] = p[i]
    R[i][i] = i

func(n)

for i in range(1, n + 2):
    print(*A[i][i - 1:])
for i in range(1, n + 2):
    print(*R[i][i - 1:])
print(A[1][n])

# 트리를 만들어야 함
root = create_tree(1, n)
preorder(root)
print()
inorder(root)
print()
