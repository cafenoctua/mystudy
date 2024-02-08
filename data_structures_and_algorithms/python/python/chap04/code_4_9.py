def func(i: int, w: int, a: list) -> bool:
    if i == 0:
            if w == 0: return True
            else: return False
    
    if func(i - 1, w, a): return True
    
    if func(i - 1, w - a[i - 1], a): return True
    
    return False

def main():
    N, W = input().split()
    N, W = int(N), int(W)
    
    a = [int(input()) for _ in range(N)]
    
    if func(N, W, a): print("Yes")
    else: print("No")
    
if __name__ == "__main__":
    main()