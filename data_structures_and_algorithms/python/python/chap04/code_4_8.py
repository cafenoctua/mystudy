memo = []

def fibo(N: int) -> int:
    if N == 0: return 0
    if N == 1: return 1
    
    global memo
    if (memo[N] != -1): return memo[N]
    
    memo[N] = fibo(N - 1) + fibo(N - 2)
    return memo[N]

def main():
    global memo
    memo = [-1 for _ in range(50)]
    
    fibo(49)
    
    for N in range(2, 50):
        print(f"{N} 項目: {memo[N]}")
        
if __name__ == "__main__":
    main()