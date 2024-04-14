def chmin(dp: list, x: int, i: int, j: int) -> None:
    if dp[i][j] > x:
        dp[i][j] = x

INF = 100000000000
def main():
    N = int(input())
    a = [int(input()) for _ in range(N)]
    S = [0 for _ in range(N+1)]
    for i in range(N): S[i+1] = S[i] + a[i]
    
    dp = [[INF for _ in range(N+1)] for _ in range(N+1)]
    
    for i in range(N): dp[i][i+1] = 0
    
    for bet in range(2, N+1):
        for i in range(N+1-bet):
            j = i + bet
            for k in range(i+1, j):
                chmin(dp, dp[i][k]+dp[k][j]+S[j]-S[i], i, j)
                
    print(dp[0][N])
    
if __name__ == "__main__":
    main()