def main():
    N, v = input().split()
    N, v = (int(N), int(v))
    a = [int(input()) for _ in range(N)]
    
    exist = False
    for i in range(N):
        if a[i] == v:
            exist = True
            break
    
    if exist: print("Yes")
    else: print("No")
    
if __name__ == "__main__":
    main()