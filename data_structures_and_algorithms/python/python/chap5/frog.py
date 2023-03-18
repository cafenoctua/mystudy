import math
def main(N: int, h: list) -> int:
    dp = [0 for _ in range(N)]
    # dp.append(0)
    
    for i in range(1, N):
        if i == 1: dp[i] = (abs(h[i] - h[i - 1]))
        else: dp[i] = (min(dp[i - 1] + abs(h[i] - h[i - 1]),
                         dp[i - 2] + abs(h[i] - h[i - 2])))
        print(f"Number{i}: {dp[i]}")
    
    return dp[N - 1]

if __name__ == "__main__":
    # Set input data
    # N = input()
    # h = [input() for _ in range(N)]
    N = 7
    h = [2,9,4,5,1,6,10]
    
    print(main(N, h))
    