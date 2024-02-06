INF = 1000000000000
def main():
    N = int(input())
    a = [int(input()) for _ in range(N)]
    
    min_value = INF
    for i in range(N):
        if a[i] < min_value:
            min_value = a[i]
    
    print(min_value)
    
if __name__ == "__main__":
    main()