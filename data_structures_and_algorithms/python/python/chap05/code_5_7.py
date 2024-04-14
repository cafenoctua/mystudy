def chmax(a: list, b: int, i: int, w: int):
    if a[i][w] < b:
        a[i][w] = b
        
def main():
    N, W = input().split()
    N, W = (int(N), int(W))
    weight = []
    value = []
    for _ in range(N):
        w, v = input().split()
        weight.append(int(w))
        value.append(int(v))
    
    dp = [[0 for _ in range(W + 1)] for _ in range(N + 1)]
    
    for i in range(N):
        for w in range(W + 1):
            if w - weight[i] >= 0:
                chmax(dp, dp[i][w - weight[i]] + value[i], i + 1, w)
                
            chmax(dp, dp[i][w], i + 1, w)
    print(dp[N][W])

if __name__ == "__main__":
    main()