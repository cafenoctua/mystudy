# -*- utf-8 -*-

if __name__ == "__main__":
    N = int(input())
    a = [int(input()) for _ in range(N)]
    
    i = 0
    turn_num = 0
    while True:
        if a[i] % 2 == 0:
            a[i] = a[i] / 2
        else:
            break
        i += 1
        if len(a) <= i:
            i = 0
            turn_num += 1
    
    print(f"Turn: {turn_num}")    