def chmax(dp: list, x: int, i: int, j: int):
    if dp[i][j] < x:
        dp[i][j] = x
        
def main():
    N = int(input())
    a = [[int(input()) for _ in range(3)] for _ in range(N)]
    
    dp = [[0 for _ in range(3)] for _ in range(N + 1)]
    
    for i in range(N):
        for j in range(3):
            for k in range(3):
                if j == k: continue
                chmax(dp, dp[i][j] + a[i][k], i + 1, k)
                    
    for j in range(3): chmax(dp, dp[N][j], N, 2)
    print(dp[N][j])
    
if __name__ == "__main__":
    main()