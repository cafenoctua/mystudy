# -*- utf-8 -*-

if __name__ == "__main__":
    N = int(input())
    W = int(input())
    a = [int(input()) for _ in range(N)]
    
    exits = False
    for bit in range(0, 1 << N):
        sum = 0
        for i in range(N):
            if bit & (1 << i):
                sum += a[i]
        if sum == W: 
            exits = True
            break
    
    print(exits)