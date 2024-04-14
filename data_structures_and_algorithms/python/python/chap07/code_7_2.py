def main():
    N = int(input())
    inter = [tuple(map(int, input().split())) for _ in range(N)]
    
    inter.sort(key=lambda x: x[1])
    
    res = 0
    current_end_time = 0
    for i in range(N):
        if inter[i][0] < current_end_time:
            continue
        res += 1
        current_end_time = inter[i][1]
    
    print(res)

if __name__ == "__main__":
    main()