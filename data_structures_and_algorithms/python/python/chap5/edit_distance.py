INF = 10 ** 100

def chmin(a: int, b: int) -> int:
    if a > b: return b
    return a

def main(S, T):
    dp = [[INF for _ in range(len(T) + 1)] for _ in range(len(S) + 1)]
    
    dp[0][0] = 0
    
    for i in range(len(S) + 1):
        for j in range(len(T) + 1):
            # change method
            if i > 0 and j > 0:
                if S[i - 1] == T[j - 1]:
                    dp[i][j] = chmin(dp[i][j], dp[i - 1][j - 1])
                else:
                    dp[i][j] = chmin(dp[i][j], dp[i - 1][j - 1] + 1)
            
            # delete method
            if i > 0:
                dp[i][j] = chmin(dp[i][j], dp[i - 1][j] + 1)

            # insert method
            if j > 0:
                dp[i][j] = chmin(dp[i][j], dp[i][j - 1] + 1)
    
    return dp[len(S)][len(T)]

if __name__ == "__main__":
    S = "logistic"
    T = "algorithm"
    
    print(main(S,T))
    