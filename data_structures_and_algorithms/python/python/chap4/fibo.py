def fibo(n: int) -> int:
    if (n == 0): return 0
    elif (n == 1): return 1
    
    return fibo(n - 1) + fibo(n - 2)

def main():
    print(fibo(6))
    
if __name__ == "__main__":
    main()
    
    