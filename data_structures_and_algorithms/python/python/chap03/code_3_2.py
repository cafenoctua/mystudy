def main():
    N, v = input().split()
    N, v = (int(N), int(v))
    a = [int(input()) for _ in range(N)]
    
    found_id = -1
    for i in range(N):
        if a[i] == v:
            found_id = i
            break
    
    print(found_id)
    
if __name__ == "__main__":
    main()