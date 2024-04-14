import bisect

def main():
    N = int(input())
    
    a = [int(input()) for _ in range(N)]
    b = [int(input()) for _ in range(N)]
    c = [int(input()) for _ in range(N)]
    
    
    a.sort()
    b.sort()
    c.sort()
    
    res = 0
    for j in range(N):
        Aj = bisect.bisect_left(a, b[j])
        Cj = N - (bisect.bisect_right(c, b[j]))
        res += Aj * Cj

    print(res)

if __name__ == "__main__":
    main()