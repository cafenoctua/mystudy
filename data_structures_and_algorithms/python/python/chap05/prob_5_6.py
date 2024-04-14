INF = 10000000000

def chmin(dp:list, x:int, i:int, j:int) -> None:
    if dp[i][j] > x:
        dp[i][j] = x

def main():
    N, W = input().split()
    N, W = (int(N), int(W))
    a = []
    m = []
    for _ in range(N):
        a.append(int(input()))
        m.append(int(input()))
    
    dp = [[INF for _ in range(W + 1)] for _ in range(N + 1)]
    dp[0][0] = 0
    
    for i in range(N):
        for j in range(W + 1):
            if dp[i][j] < INF: chmin(dp, 0, i+1, j)
            if j >= a[i] and dp[i+1][j-a[i]] < m[i]:
                chmin(dp, dp[i+1][j-a[i]]+1, i+1, j)
    
    if dp[N][W] < INF: print("Yes")
    else: print("No")
    
if __name__ == "__main__":
    main()