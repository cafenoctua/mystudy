def main():
    N = int(input())
    a = []
    b = []
    for _ in range(N):
        A, B = input().split()
        a.append(int(A))
        b.append(int(B))
    
    a.sort()
    b.sort()
        
    res = 0
    for i in range(N):
        if a[res] < b[i]: res += 1
    
    print(res)

if __name__ == "__main__":
    main()