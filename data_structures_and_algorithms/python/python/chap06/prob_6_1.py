import bisect

def main():
    N = int(input())
    a = [int(input()) for _ in range(N)]
    b = a.copy()
    b.sort()
    
    res = []
    for i in range(N):
        res.append(bisect.bisect_left(b, a[i]))
    
    print(res)

if __name__ == "__main__":
    main()