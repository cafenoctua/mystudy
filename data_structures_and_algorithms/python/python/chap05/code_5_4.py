def chmin(a: list, b: int, i: int):
    if a[i] > b:
        a[i] = b
        
INF = 1000000000000

def main():
    N = int(input())
    h = [int(input()) for _ in range(N)]

    dp = [INF for _ in range(N)]
    dp[0] = 0
    
    for i in range(N):
        if i + 1 < N: chmin(dp, dp[i] + abs(h[i] - h[i + 1]), i + 1)
        if i + 2 < N: chmin(dp, dp[i] + abs(h[i] - h[i + 2]), i + 2)
        
    print(dp[N - 1])
    
if __name__ == "__main__":
    main()