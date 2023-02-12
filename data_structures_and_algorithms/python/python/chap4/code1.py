def func(n: int) -> int:
    if n == 0 : return 0
    return n + func(n-1)

def main():
    print(func(5))

if __name__ == "__main__":
    main()