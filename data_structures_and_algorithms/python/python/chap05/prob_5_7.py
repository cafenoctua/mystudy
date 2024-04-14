def chmax(dp: list, x: int, i: int, j: int) -> None:
    if dp[i][j] < x:
        dp[i][j] = x


def main():
    S = input()
    T = input()
    
    dp = [[0 for _ in range(len(T)+1)] for  _ in range(len(S)+1)]
    
    for i in range(len(S)+1):
        for j in range(len(T)+1):
            if i > 0 and j > 0:
                if S[i-1] == T[j-1]: chmax(dp, dp[i-1][j-1]+1, i, j)
                else: chmax(dp, dp[i-1][j-1], i, j)
                
            if i > 0: chmax(dp, dp[i-1][j], i, j)
            
            if j > 0: chmax(dp, dp[i][j-1], i, j)
                
    print(dp[len(S)][len(T)])
    
if __name__ == "__main__":
    main()