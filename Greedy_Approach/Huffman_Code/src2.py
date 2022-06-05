from collections import deque
import heapq


class Node:
    # 노드 클래스를 만듬
    def __init__(self, left=None, right=None, symbol='+', frequency=0):
        self.left = left
        self.right = right
        self.symbol = symbol
        self.f = frequency


def func(pq):
    # 허프만 트리를 만듬

    for _ in range(n - 1):
        # n개의 원소이므로 n - 1번 반복해야함

        p = heapq.heappop(pq)[1]
        q = heapq.heappop(pq)[1]
        # 작은거 두 개 꺼냄

        r = Node(left=p, right=q, frequency=p.f + q.f)      # 새로운 노드 생성
        heapq.heappush(pq, (r.f, r))        # r을 넣음

    return heapq.heappop(pq)[1]


def preorder(node):
    if node != None:
        print(f'{node.symbol}:{node.f} ', end='')
        preorder(node.left)
        preorder(node.right)


def inorder(node):
    if node != None:
        inorder(node.left)
        print(f'{node.symbol}:{node.f} ', end='')
        inorder(node.right)


def encoding(r, ch, encode):
    # 문자열을 인코딩하는 함수
    if r.symbol == '+':
        # 연결 노드라면 우선 다 탐색해봐야함
        encode.append(0)
        encoding(r.left, ch, encode)
        encode.pop()

        encode.append(1)
        encoding(r.right, ch, encode)
        encode.pop()

    elif r.symbol == ch:
        # 만약 심볼이 ch와 같다면
        global real
        real += ''.join(map(str, encode))

        return


def decoding(r, code):
    node = r        # node를 최상단 노드로 초기화
    for c in code:      # 앞에서 순차적으로
        if c == 0:
            node = node.left
        else:
            node = node.right

        if node.left == None and node.right == None:
            # 둘 다 None이면 잎에 도달한 것임, or은 안 됨
            print(node.symbol, end='')
            node = r


n = int(input())        # 문자의 개수
chs = input().split()       # 문자
freq = list(map(int, input().split()))      # 빈도수

pq = []

for i in range(n):
    # node들을 빈도수 기준으로 pq에 넣음
    node = Node(symbol = chs[i], frequency = freq[i])
    heapq.heappush(pq, (node.f, node))

r = func(pq)        # 최상단 노드를 얻어옴

# 아래는 출력
preorder(r)
print()
inorder(r)
print()


T1 = int(input())       # 문자열의 개수
for _ in range(T1):
    # 문자를 코드화
    real = ''       # 진짜 이진코드
    for ch in input().strip():
        encode = []     # 일시적인 이진코드
        encoding(r, ch, encode)
    print(real)

T2 = int(input())       # 이진코드
for _ in range(T2):
    # 코드를 문자화
    code = list(map(int, input().strip()))
    decoding(r, code)
    print()
