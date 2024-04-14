INF = 1000000000000

def main():
    N = int(input())
    h = []
    s = []
    
    for _ in range(N):
        h.append(int(input()))
        s.append(int(input()))
    
    M = max(h[i] + s[i] * N for i in range(N))
    left = 0
    right = M
    cnt = 0
    while right - left > 1:
        mid = (left + right) // 2
        
        ok = True
        t  = [0 for _ in range(N)]
        
        for i in range(N):
            if mid < h[i]: ok = False
            else: t[i] = (mid - h[i]) / s[i]

        t.sort()
        for i in range(N):
            if t[i] < i: ok = False
        
        if ok: right = mid
        else: left = mid
        cnt += 1
        print(f"{cnt}. Right: {right}, Left: {left}")
        
    print(right)
    
if __name__ == "__main__":
    main()