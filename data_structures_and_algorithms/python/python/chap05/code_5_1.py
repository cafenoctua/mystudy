INF  = 1000000000

def chmin(a: list, b: int, i: int) -> None:
    if a[i] > b:
        a[i] = b

def main():
    N = int(input())
    h = [int(input()) for _ in range(N)]
    dp = [INF for _ in range(N)]
    dp[0] = 0
    for i in range(1, N):
        chmin(dp, dp[i - 1] + abs(h[i] - h[i - 1]), i)
        if i > 1:
            chmin(dp, dp[i - 2] + abs(h[i] - h[i - 2]), i)

    print(dp[N - 1])
    
if __name__ == "__main__":
    main()