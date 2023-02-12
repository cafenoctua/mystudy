# -*- utf-8 -*-

if __name__ == "__main__":
    N = int(input())
    v = int(input())
    
    # input numbers
    a = [int(input()) for _ in range(N)]
    
    # linaer search
    exits = False
    for i in range(N):
        if a[i] == v: 
            exits = True
            break
    
    if exits:
        print("Yes")
    else:
        print("Not")