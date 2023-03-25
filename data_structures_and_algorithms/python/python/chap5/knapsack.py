def chmax(a, b):
    if a < b:
        return b
    return a

def main(N, W, weight, value):
    dp = [[0 for _ in range(W + 1)] for _ in range(N + 1)]
    
    for i in range(N):
        for w in range(W + 1):
            if w - weight[i] >= 0:
                dp[i + 1][w] = chmax(dp[i + 1][w], dp[i][w - weight[i]] + value[i])
            dp[i + 1][w] = chmax(dp[i + 1][w], dp[i][w])
    return dp[N][W]

if __name__ == "__main__":
    N = 6
    W = 15
    weight = [2,1,3,2,1,5]
    value = [3,2,6,1,3,85]
    
    print(main(N, W, weight, value))