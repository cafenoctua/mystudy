def partial_sum(i: int, w: int, a) -> bool:
    
    if i == 0:
        if w == 0: return True
        else: return False

    if (partial_sum(i - 1, w, a)): return True
    
    if (partial_sum(i - 1, w - a[i - 1], a)): return True
    
    return False

def main():
    N = 4
    W = 30
    a = [3,2,6,5]
    
    if partial_sum(N, W, a): print("Yes")
    else: print("No")
    
if __name__ == "__main__":
    main()