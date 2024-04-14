import bisect

INF = 2000000000000000000

def main():
    N, K = input().split()
    N, K = int(N), int(K)
    
    a = [int(input()) for _ in range(N)]
    b = [int(input()) for _ in range(N)]
    
    min_value = INF
    
    b.sort()
    
    for i in range(N):
        index = bisect.bisect_left(b, K - a[i])
        val = b[index]
        if a[i] + val < min_value:
            min_value = a[i] + val
            
    print(min_value)


if __name__ == "__main__":
    main()