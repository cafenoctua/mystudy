def main():
    N = int(input())
    v = []
    for _ in range(N):
        d, t = input().split()
        v.append((int(d), int(t)))
    
    v = sorted(v, key=lambda v: v[1])
    
    ok = True
    time = 0
    for i in range(N):
        time += v[i][0]
        if time > v[i][1]: ok = False
    
    if ok: print("Yes")
    else: print("No")
    
if __name__ == "__main__":
    main()