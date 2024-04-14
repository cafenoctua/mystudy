def chmin(dp: list, x: int, i: int, j: int):
    if dp[i][j] > x:
        dp[i][j] = x


INF = 100000000000
def main():
    N, K, W = input().split()
    N, K, W = (int(N), int(K), int(W))
    a = [int(input()) for _ in range(N)]
    
    
    dp = [[INF for _ in range(W + 1)] for _ in range(N + 1)]
    dp[0][0] = 0
    
    for i in range(N):
        for j in range(0, W+1):
            chmin(dp, dp[i][j], i+1, j)
            if j >= a[i]:
                chmin(dp, dp[i][j-a[i]]+1, i+1, j)
    if dp[N][W] <= K: print("Yes")
    else: print("No")
    
if __name__ == "__main__":
    main()