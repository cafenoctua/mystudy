def main():
    N = int(input())
    r = []
    for _ in range(N):
        x, y = input().split()
        r.append((int(x), int(y)))
    
    b = []
    for _ in range(N):
        x, y = input().split()
        b.append((int(x), int(y)))
        
    b.sort()
    
    used = [False for _ in range(N)]
    
    res = 0
    for i in range(N):
        maxy, maxid = -1, -1
        for j in range(N):
            if used[j]: continue
            
            if r[j][0] >= b[i][0]: continue
            if r[j][1] >= b[i][1]: continue
            
            if maxy < r[j][1]:
                maxy = r[j][1]
                maxid = j
        
        if maxid == -1: continue
        
        res += 1
        used[maxid] = True
    
    # R = []
    # B = []
    # for i in range(N):
    #     R.append(r[i][0] + r[i][1])
    #     B.append(b[i][0] + b[i][1])
    
    # R.sort()
    # B.sort()
    # res = 0
    # for i in range(N):
    #     if R[r] < B[i]: res += 1
    
    print(res)

if __name__ == "__main__":
    main()