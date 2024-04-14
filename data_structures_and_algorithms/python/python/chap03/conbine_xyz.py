def main():
    K, N = input().split()
    K, N = (int(K), int(N))
    
    cnt = 0
    for X in range(min(K, N) + 1):
        for Y in range(min(K, N) + 1):
            if N - (X + Y) <= K: cnt += 1
                
    print(cnt)