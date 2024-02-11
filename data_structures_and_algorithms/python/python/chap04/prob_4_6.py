def func(i: int, w: int, a: list, memo: list) -> bool:
    if i == 0:
        if w == 0: 
            return True
        else: return False
        
    if memo[i][w] != -1: return memo[i][w]
    
    if func(i - 1, w, a, memo):
        memo[i][w] = 1
        return memo[i][w]
    
    if func(i - 1, w - a[i - 1], a, memo):
        memo[i][w] = 1
        return memo[i][w]
    
    memo[i][w] = 0
    return memo[i][w]

def main():
    N, W = input().split()
    N, W = int(N), int(W)
    
    memo = [[-1 for _ in range(W+1)] for _ in range(N+1)]
    
    a = [int(input()) for _ in range(N)]
    
    if func(N, W, a, memo): print("Yes")
    else: print("No")
    
if __name__ == "__main__":
    main()