def gcd(m: int, n: int) -> int:
    if n == 0: return m
    return gcd(n, m % n)

def main():
    print(gcd(51, 15))
    print(gcd(15, 51))

if __name__ == "__main__":
    main()