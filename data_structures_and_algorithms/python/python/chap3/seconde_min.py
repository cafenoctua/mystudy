# -*- utf-8 -*-

INF = 20000000

if __name__ == "__main__":
    N = int(input())
    W = int(input())
    a = [int(input()) for _ in range(N)]
    
    # get min value
    min_val = INF
    
    for i in a:
        if i < min_val:
            min_val = i
    
    # get second min value
    second_min_val = INF
    
    for i in a:
        if i < second_min_val and i != min_val:
            second_min_val = i
            
    print(f"second min value: {second_min_val}")