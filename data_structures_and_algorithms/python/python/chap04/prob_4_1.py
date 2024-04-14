memo = []

def tribo(N: int) -> int:
    if N == 0: return 0
    if N == 1: return 0
    if N == 2: return 1
    
    global memo
    if (memo[N] != -1): return memo[N]
    
    memo[N] = tribo(N - 1) + tribo(N - 2) + tribo(N - 3)
    return memo[N]

def main():
    global memo
    N = int(input())
    memo = [-1 for _ in range(N + 1)]
    
    print(tribo(N))
    
    # for N in range(3, 50):
    #     print(f"{N} 項目: {memo[N]}")
        
if __name__ == "__main__":
    main()