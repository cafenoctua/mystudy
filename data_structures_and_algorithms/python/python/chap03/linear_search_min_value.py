# -*- utf-8 -*-
INF = 20000000

if __name__ == "__main__":
    N = int(input())
    v = int(input())
    
    # input numbers
    a = [int(input()) for _ in range(N)]
    
    # linaer search
    min_value = INF
    exits = False
    for i in range(N):
        if a[i] < min_value: 
            min_value = a[i]
    
    print(f"Min value is: f{a[i]}")