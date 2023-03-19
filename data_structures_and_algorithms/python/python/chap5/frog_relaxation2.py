import math
INF = 10 ** 100

def chmin(dp, b, i):
    if dp[i] > b:
        dp[i] = b

def main(N: int, h: list) -> int:
    dp = [INF for _ in range(N)]
    dp[0] = 0
    # dp.append(0)
    
    for i in range(0, N):
        if i + 1 < N: chmin(dp, dp[i] + abs(h[i] - h[i + 1]), i + 1)
        if i + 2 < N: chmin(dp, dp[i] + abs(h[i] - h[i + 2]), i + 2)
        print(f"Number{i}: {dp[i]}")
    
    return dp[N - 1]

if __name__ == "__main__":
    # Set input data
    # N = input()
    # h = [input() for _ in range(N)]
    N = 7
    h = [2,9,4,5,1,6,10]
    
    print(main(N, h))
    