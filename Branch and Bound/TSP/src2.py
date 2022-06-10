from copy import deepcopy
import heapq

INF = 9999      # 경로가 없거나, 무한대를 위한 것

class Node:
    # 노드를 만듬
    def __init__(self, level: int, path: list) -> None:
        self.level = level
        self.path = path
        self.bound = self.getbound()


    def length(self) -> int:
        # 해당 경로까지의 길이를 찾는 메서드
        path_len = 0     # 최초 길이는 0
        for i in range(len(self.path) - 1):
            # path가 [1, 3, 5]라면 adj[1][3]와 adj[3][5]을 더해야함
            path_len += adj[self.path[i]][self.path[i + 1]]

        return path_len


    def outgoing(self, v: int) -> bool:
        # bound 관련 함수
        # 만약 path가 [1, 4, 5, 2]라면 1, 4, 5를 체크한다.
        # 1, 4, 5는 이미 정해져있는 length이기 때문에, 2번과 다른 노드들이 bound를 결정한다.

        return (True if v in self.path[:-1] else False)


    def incoming(self, v: int) -> bool:
        # bound 관련 함수
        # 만약 path가 [1, 4, 5, 2]라면 4, 5, 2를 체크한다.
        # 출발 정점을 제외하고는 돌아가서는 안 된다

        return (True if v in self.path[1:] else False)
    

    def getbound(self) -> int:
        # 해당 경로의 하한 길이를 찾는 메서드
        lower = self.length()       # 해당 path까지의 길이
        for i in range(1, n + 1):       # 모든 정점을 
            if self.outgoing(i):
                # 이미 i에서 어떤 노드로 향한 경로가 있다는 뜻임
                continue
            min = INF
            for j in range(1, n + 1):
                # 경로가 정해지지 않은 노드들이 최소 경로를 찾기 위한 것
                # 최소가 되는 i -> j를 찾아야한다.
                if i == j:      # 자기 자신으로 못 감
                    continue
                if j == self.path[0] and i == self.path[-1]:
                    # i가 path의 마지막 노드이고, j가 만약에 출발한 노드라면 
                    # 이는 고려하면 안 됨
                    continue
                if self.incoming(j):
                    # 이미 어떤 노드에서 j로 향한 경로가 있다는 뜻임
                    continue

                min = adj[i][j] if min > adj[i][j] else min
                # i -> j가 min보다 작다면 min을 업데이트
                # 이때 i에서 출발해서 도착 가능한 모든 j에 대한 최솟값임

            lower += min        # bound를 구하기 위해 더함

        return (INF if lower >= INF else lower)
        # 이랬는데 INF를 넘긴다면 그냥 INF를 반환
        

def create_adj():
    # 인접 행렬을 만드는 함수
    adj = [[INF] * (n + 1) for _ in range(n + 1)]       # 인접행렬

    for i in range(n + 1):
        adj[i][i] = 0       # 자기 자신에 대한 경로는 0

    for _ in range(m):
        u, v, w = map(int, input().split())     # 출발 정점, 도착 정점, 가중치
        adj[u][v] = w

    return adj


def remaining_vertex(path: list) -> int:
    # 마지막 남은 노드를 찾는 함수
    total = n * (n + 1) // 2        # 모든 n을 다 더함
    total_path = sum(path)      # 모든 경로를 더함

    return total - total_path       # 빼면 가지 않은 노드가 나옴


def travel2():
    minlength = INF     # 최소 길이를 정의
    optour = []     # 최소 경로
    cnt = 0     # PQ에 넣을 때 중요함..
    PQ = []     # 우선순위 큐를 만듬
    v = Node(0, [1])        # 출발 정점을 1로 하고, 레벨을 0로함
    # 만약 2에서 출발하는 것이라면 이것만 바꾸면 됨
    
    print(v.level, v.bound, *v.path, sep=' ')

    heapq.heappush(PQ, (v.bound, cnt, v))       # bound가 작고, cnt가 작은 순대로 넣음

    while PQ:
        # PQ가 비어있지 않다면
        v = heapq.heappop(PQ)[2]
        if v.bound < minlength:
            # 경로의 하한선이 최소 길이보다 작아야 유망함
            for i in range(1, n + 1):
                # 출발 정점이 1이므로, 2부터 n까지 살펴봄
                # 원래 위의 주석이 맞는데, 변형으로 나올 수 있어서 1부터 찾는 것으로 함
                # 어차피 바로 아래의 if문에 의해 없어짐
                cnt += 1

                if i in v.path:
                    # i가 만약에 이미 경로상에 있다면 살펴보지 않음
                    continue

                u = Node(v.level + 1, deepcopy(v.path))
                u.path.append(i)
                # u를 생성하고, i에 갔다고 가정함
                
                if u.level == n - 2:
                    # 만약 u의 level이 n - 2라면 여러 자식으로 뻗을 필요가 없음
                    # 왜냐면 갈 곳은 하나밖에 안 남았기 때문임
                    u.path.append(remaining_vertex(u.path))     # 안 간 마지막 노드에 방문
                    u.path.append(u.path[0])        # 맨 처음 노드로 간다고 가정

                    # 출력을 위한 코드
                    print(u.level, "{}".format("INF" if u.length() >= INF else u.length()), *u.path, sep=' ')

                    if u.length() < minlength:      
                        # 그랬을 때 경로가 지금까지 찾은 최소 길이보다 작으면 업데이트
                        minlength = u.length()
                        opttour = deepcopy(u.path)
                else:       # 여러 자식으로 가봐야 한다면
                    u.bound = u.getbound()      # 해당 마디의 하한 값을 찾아봄

                    # 출력을 위한 코드
                    print(u.level, "{}".format("INF" if u.bound >= INF else u.bound), *u.path, sep=' ')

                    if u.bound < minlength:     # 하한 값이 지금까지 찾은 최소 길이보다 작다면
                        heapq.heappush(PQ, (u.bound, cnt, u))       # 유망(자식으로 갈 가치가 있음)하므로 PQ에 넣음

    print(minlength)
    print(*opttour, sep=' ')
                

if __name__ == "__main__":
    n, m = map(int, input().split())        # 정점 개수, 간선 개수

    adj = create_adj()      # 인접 행렬을 만듬

    travel2()
