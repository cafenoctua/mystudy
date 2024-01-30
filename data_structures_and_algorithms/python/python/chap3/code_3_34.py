INF = 1000000000000
def main():
    N, K = input().split()
    N, K = (int(N), int(K))
    a = [int(input()) for _ in range(N)]
    b = [int(input()) for _ in range(N)]
    
    min_value = INF
    for i in range(N):
        for j in range(N):
            if a[i] + b[j] > K and a[i] + b[j] < min_value:
                min_value = a[i] + b[j]
    
    print(min_value)
    
if __name__ == "__main__":
    main()