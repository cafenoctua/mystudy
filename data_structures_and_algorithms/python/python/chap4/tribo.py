def tribo(n: int) -> int:
    if (n == 0): return 0
    elif (n == 1): return 0
    elif (n == 2): return 1
    
    return tribo(n - 1) + tribo(n - 2) + tribo(n - 3)

def main():
    print(tribo(4))
    
if __name__ == "__main__":
    main()
    
    