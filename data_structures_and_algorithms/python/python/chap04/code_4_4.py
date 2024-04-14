def GCD(m: int, n: int) -> int:
    if n == 0: return m
    return GCD(n, m % n)

def main():
    # print(GCD(51, 15))
    print(GCD(15, 51))
    
if __name__ == "__main__":
    main()