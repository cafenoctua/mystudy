def main():
    N, W = input().split()
    N, W = (int(N), int(W))
    a = [int(input()) for _ in range(N)]
    
    
    dp = [[False for _ in range(W + 1)] for _ in range(N + 1)]
    dp[0][0] = True
    for i in range(N):
        for j in range(W + 1):
            if not(dp[i][j]): continue
            dp[i+1][j] = True
            if j + a[i] <= W: dp[i+1][j+a[i]] = True
    res = 0
    for j in range(W+1):
        if dp[N][j]: res += 1
    
    print(res)
    
if __name__ == "__main__":
    main()