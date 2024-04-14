def chmin(a: list, b: int, i: int) -> None:
    if a[i] > b:
        a[i] = b

INF = 100000000000000

def main():
    N = int(input())
    c = [[int(input()) for _ in range(N + 1)] for _ in range(N + 1)]
    
    dp = [INF for _ in range(N + 1)]
    dp[0] = 0
    
    for i in range(N + 1):
        for j in range(i):
            chmin(dp[i], dp[j] + c[i][j])
    
    print(dp[N])

if __name__ == "__main__":
    main()