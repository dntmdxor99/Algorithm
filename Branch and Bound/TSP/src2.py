class Node:
    # 노드를 만듬
    def __init__(self, level : int, path : int ) -> None:
        self.level = level
        self.path = path
        self.bound = self.getbound()


    def length(self) -> int:
        # 해당 경로까지의 길이를 찾는 메서드
        len = 0     # 최초 길이는 0
        for i in range(len(self.path) - 1):
            # [1, 2, 3]이라면 adj[1][2]와 adj[2][3]을 더해야함
            len += adj[i][i + 1]

        return len
            


    def getbound(self) -> int:
        # 해당 경로의 하한 길이를 찾는 메서드
        lower = self.length()       # 해당 path까지의 길이
        for i in range(1, n + 1):
            pass
        


def create_adj():
    # 인접 행렬을 만드는 함수
    adj = [[INF] * (n + 1) for _ in range(n + 1)]       # 인접행렬

    for i in range(n + 1):
        adj[i][i] = 0       # 자기 자신에 대한 경로는 0

    for _ in range(m):
        u, v, w = map(int, input().split())     # 출발 정점, 도착 정점, 가중치
        adj[u][v] = w

    return adj


def travel2():
    PQ = []     # 우선순위 큐를 만듬
    v = Node(1, [1])        # 출발 정점을 1로 하고, 레벨을 1로함
    


if __name__ == "__main__":
    INF = 9999      # 경로가 없거나, 무한대를 위한 것

    n, m = map(int, input().split())        # 정점 개수, 간선 개수

    adj = create_adj()      # 인접 행렬을 만듬

