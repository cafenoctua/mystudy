def chmax(dp: list, x: int, i: int, j: int) -> None:
    if dp[i][j] < x:
        dp[i][j] = x
        
INF = -10000000000
def main():
    N, M = input().split()
    N, M = (int(N), int(M))
    a = [int(input()) for _ in range(N)]
    
    f = [[0 for _ in range(N+1)] for _ in range(N+1)]
    for i in range(1, N+1):
        for j in range(i):
            sum = 0
            for k in range(j, i): sum += a[k]
            f[j][i] = sum / (i - j)
    
    dp = [[INF for _ in range(M+1)] for _ in range(N+1)]
    dp[0][0] = 0
    for i in range(N+1):
        for j in range(i):
            for k in range(1, M+1):
                chmax(dp, dp[j][k-1]+f[j][i], i, k)
                
    res = [[INF]]
    for m in range(M+1): chmax(res, dp[N][m], 0, 0)
    print(res)
    
if __name__ == "__main__":
    main()