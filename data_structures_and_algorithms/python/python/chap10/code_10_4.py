class Edge:
    def __init__(self, to: int, w: int) -> None:
        self.to = to
        self.w = w
        
class Graph:
    def __init__(self, n) -> None:
        self.adj_list = [[] for _ in range(n)]
        
    def add_edge(self, u, v, w):
        self.adj_list[u].append(Edge(v, w))

def main():
    N, M = map(int, input().split())
    
    G = Graph(N)
    
    cnt = 0
    for _ in range(M):
        cnt += 1
        a, b, w = map(int, input().split())
        G.add_edge(a, b, w)
        
    print('break point')
        
if __name__ == "__main__":
    main()