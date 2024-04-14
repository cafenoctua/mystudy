def main():
    N = int(input())
    A = []
    B = []
    for _ in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    
    sum = 0
    for i in range(N - 1, -1, -1):
        A[i] += sum
        amari = A[i] % B[i]
        D = 0
        if amari != 0: D = B[i] - amari
        sum += D
        
    print(sum)

if __name__ == "__main__":
    main()