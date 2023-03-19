INF = 10 ** 100
def chmin(a, b):
    if a > b:
        return b
    return a

def rec(i: int, h: list):
    if i == 0: return 0
    res = INF
    
    res = chmin(res, rec(i - 1, h) + abs(h[i] - h[i - 1]))
    
    if i > 1: res = chmin(res, rec(i - 2, h) + abs(h[i] - h[i - 2]))
    
    return res    
    
def main(N: int, h: list) -> int:
    return rec(N - 1, h)

if __name__ == "__main__":
    # Set input data
    # N = input()
    # h = [input() for _ in range(N)]
    N = 7
    h = [2,9,4,5,1,6,10]
    
    print(main(N, h))
    