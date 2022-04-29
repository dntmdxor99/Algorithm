import heapq

class Node:
    # 노드를 만듬
    def __init__(self, left = None, right = None, symbol = '+', frequency = 0):
        self.left = left
        self.right = right
        self.symbol = symbol
        self.frequency = frequency


def func(pq):
    # 최적 이진 트리를 만드는 함수
    for i in range(n - 1):
        # n개가 있으면 n-1번만 실행한다.
        p = heapq.heappop(pq)
        q = heapq.heappop(pq)       # 빈도수가 작은 두 개의 노드를 꺼냄

        node = Node(p[1], q[1], frequency = p[0] + q[0])        # 새로운 노드를 만듬

        heapq.heappush(pq, [node.frequency, node])      # 새로운 노드를 pq에 넣음

    return heapq.heappop(pq)[1]     # 마지막에 남아 있는 root 노드를 반환함


def preorder(node):
    # preorder 함수
    if node:
        print(f'{node.symbol}:{node.frequency} ', end='')
        preorder(node.left)
        preorder(node.right)


def inorder(node):
    # inorder 함수
    if node:
        inorder(node.left)
        print(f'{node.symbol}:{node.frequency} ', end='')
        inorder(node.right)


def incoding():
    # 문자를 이진 코드로 나타냄
    case = int(input())
    for i in range(case):
        print(''.join(map(lambda x: code[x], input())))     # input 받은 string을 코드화 시킴


def decoding():
    # 이진 코드를 문자열로 변경함
    case = int(input())
    for _ in range(case):
        code = list(input())

        node = r        # 하나의 문자를 출력하면 루트로 돌아가야함

        for c in code:      # 문자 하나씩 꺼내서
            if c == '0':        # 0이면 왼쪽
                node = node.left
            elif c == '1':      # 1이면 오른쪽
                node = node.right

            if node.left == None and node.right == None:
                # 더 이상 갈 곳이 없다면 최하단 노드이므로 출력
                print(node.symbol, end='')
                node = r        # 출력 후 다시 루트로 돌아감
        print()


def create_default_priority_queue():
    # pq를 생성함
    pq = []
    for i in range(n):
        # 문자와 빈도수로 pq를 만듬
        node = Node(None, None, chs[i], ch_freq[i])     # 노드를 생성함
        heapq.heappush(pq, [node.frequency, node])      # 생성 후 pq에 집어 넣음
    return pq


def find_code(temp, ch, node):
    # 문자에 해당하는 이진 코드를 찾는 함수
    if node:
        if ch == node.symbol:
            # 만약 ch와 symbol이 맞다면 True를 return함
            return True
        else:
            temp.append('0')        # 0을 먼저 집어 넣고
            if find_code(temp, ch, node.left):
                # True라면 문자에 해당하는 이진 코드를 찾았으므로 True를 return 함
                return True
            temp.pop()      # False라면 0을 뺌

            temp.append('1')
            if find_code(temp, ch, node.right):
                return True
            temp.pop()


def create_code():
    # 문자에 맞는 이진 코드를 생성하는 함수
    c = dict()      # 딕셔너리 형태로 넣을거임
    temp = list()       # 임시적으로 코드를 저장하는 곳
    for i in chs:
        find_code(temp, i, r)       # 코드를 찾음
        c[i] = ''.join(temp)        # 딕셔너리에 저장함
        temp.clear()
    return c


if __name__ == "__main__":
    n = int(input())
    chs = input().split()  # 문자를 입력 받음
    ch_freq = list(map(int, input().split()))  # 문자의 빈도수를 입력받음

    pq = create_default_priority_queue()        # 우선순위 큐를 만듬
    r = func(pq)        # 우선순위 큐를 가지고 최적 이진 코드 트리를 만들고, root를 반환 받음

    for order in [preorder, inorder]:
        # preorder, inorder 출력
        order(r)
        print()

    code = create_code()      # 알파벳에 맞는 코드를 찾음
    incoding()      # 알파벳에 맞게 이진 코드를 출력함
    decoding()      # 이진 코드에 맞게 알파벳을 출력함
