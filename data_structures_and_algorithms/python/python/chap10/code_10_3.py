def main():
    N, M = map(int, input().split())
    G = [[] for _ in range(N)]
    for i in range(M):
        a, b = map(int, input().split())
        G[a].append(b)
        
    print(G)

if __name__ == "__main__":
    main()