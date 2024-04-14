def chmin(a: list, b: int, i: int, j: int):
    if a[i][j] > b:
        a[i][j] = b
        
INF = 10000000000000

def main():
    S, T = input().split()
    
    dp = [[INF for _ in range(len(T) + 1)] for _ in range(len(S) + 1)]
    
    dp[0][0] = 0
    
    for i in range(len(S) + 1):
        for j in range(len(T) + 1):
            if i > 0 and j > 0:
                if S[i - 1] == T[j - 1]:
                    chmin(dp, dp[i - 1][j - 1], i, j)
                else:
                    chmin(dp, dp[i - 1][j - 1] + 1, i, j)
            if i > 0: chmin(dp, dp[i - 1][j] + 1, i, j)
            if j > 0: chmin(dp, dp[i][j - 1] + 1, i, j)
        
    print(dp[len(S)][len(T)])

if __name__ == "__main__":
    main()