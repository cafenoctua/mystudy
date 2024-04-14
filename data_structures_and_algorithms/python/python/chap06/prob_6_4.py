INF = 100000000000

def main():
    N, M = input().split()
    N, M = int(N), int(M)
    a = [int(input()) for _ in range(N)]
    
    a.sort()
    
    left = 0
    right = INF
    while right - left > 1:
        x = int((left + right) / 2)
        
        cnt = 1
        prev = 0
        for i in range(N):
            if a[i] - a[prev] >= x:
                cnt += 1
                prev = i
                
        if cnt >= M: left = x
        else: right = x
    
    print(left)
    # diff = []
    # for i in range(1, N):
    #     diff.append(a[i] - a[i-1])
    
    # res = []
    # for i in range(0, N):
    #     if M + i > N: break
    #     res.append(min(diff[i:M+i]))

    # print(max(res))
    
if __name__ == "__main__":
    main()