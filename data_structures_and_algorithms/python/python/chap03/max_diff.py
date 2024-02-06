def main():
    N = int(input().split())
    a = [int(input()) for _ in range(N)]
    min_value = 1000000000
    max_value = 0
    max_diff = 0
    for i in range(N):
        if a[i] < min_value: min_value = a[i]
        if a[i] > max_value: max_value = a[i]
            
    print(max_value - min_value)
if __name__ == "__main__":
    main()