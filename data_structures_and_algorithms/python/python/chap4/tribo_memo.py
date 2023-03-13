memo = [-1 for _ in range(50)]
def tribo(n: int):
    if (n == 0): return 0
    elif (n == 1): return 0
    elif (n == 2): return 1
    
    if (memo[n] != -1): return memo[n]
    
    memo[n] = tribo(n - 1) + tribo(n - 2) + tribo(n - 3)
    return memo[n]

def main():
    
    tribo(6)
    
    for n in range(2, 50, 1):
        print(f"{n} 項目: {memo[n]}")
        
if __name__ == "__main__":
    main()