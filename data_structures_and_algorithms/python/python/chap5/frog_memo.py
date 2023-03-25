INF = 10 ** 100
def chmin(a, b):
    if a > b:
        return b
    return a

def rec(i: int, h: list, dp: list):
    # return if memoed
    if dp[i] < INF: return dp[i]
    
    # base case
    if i == 0: return 0
    
    res = INF
    
    res = chmin(res, rec(i - 1, h, dp) + abs(h[i] - h[i - 1]))
    
    if i > 1: res = chmin(res, rec(i - 2, h, dp) + abs(h[i] - h[i - 2]))
    
    return res    
    
def main(N: int, h: list, dp: list) -> int:
    return rec(N - 1, h, dp)

if __name__ == "__main__":
    # Set input data
    # N = input()
    # h = [input() for _ in range(N)]
    N = 7
    h = [2,9,4,5,1,6,10]
    dp = [INF for _ in range(N)]
    
    print(main(N, h, dp))
    