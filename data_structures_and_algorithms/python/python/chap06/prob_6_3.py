import bisect

def main():
    N, M = input().split()
    N, M = int(N), int(M)
    P = [int(input()) for _ in range(N)]
    P.append(0)
        
    S = []
    for i in range(len(P)):
        for j in range(len(P)):
            S.append(P[i] + P[j])
    
    S.sort()
    
    res = 0
    for a in S:
        it = bisect.bisect_right(S, M-a)
        if it == S[0]: continue
        res = max(res, a + it)
        
    print(res)
    
if __name__ == "__main__":
    main()