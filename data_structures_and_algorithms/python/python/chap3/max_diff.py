# -*-utf-8-*-

INF = 2000000
MIN = 0

if __name__ == "__main__":
    N = int(input())
    a = [int(input()) for _ in range(N)]
    
    
    # get max diff
    max_val = MIN
    min_val = INF
    
    for i in range(N-1):
        if  max_val < a[i]:
            max_val = a[i]
        if min_val > a[i]:
            min_val = a[i]
            
    print(f"Maximum diff: {max_val - min_val}")