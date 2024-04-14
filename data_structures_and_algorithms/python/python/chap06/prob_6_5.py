import bisect

def main():
    N, K = input().split()
    N, K = int(N), int(K)
    
    a = [int(input()) for _ in range(N)]
    b = [int(input()) for _ in range(N)]
    
    b.sort()
    
    def check(x: int) -> bool:
        cnt = 0
        for i in range(N):
            cnt += bisect.bisect_right(b, x / a[i])
        return cnt >= K
    
    left = 0
    right = 100000000000
    while right - left > 1:
        mid = int((left + right) / 2)
        if check(mid): right = mid
        else: left = mid
        
    print(right)
    
    # x = []
    # a.sort()
    # b.sort()
    # for i in range(N):
    #     for j in range(N):
    #         x.append(a[i] * b[j])
    
    # x.sort()
    # print(x[K])
    
if __name__ == "__main__":
    main()