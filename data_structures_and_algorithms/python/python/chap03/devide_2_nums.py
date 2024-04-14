INF = 10000000000

def how_many_times(N: int) -> int:
    exp = 0
    while N % 2 == 0: N /= 2; exp += 1
    return exp

def main():
    N = int(input())
    A = [int(input()) for _ in range(N)]
    
    # devide_num = 0
    # stop_loop = False
    result = INF
    for a in A :
        result = min(result, how_many_times(a))
    # while True:
    #     for i in range(N):
    #         if a[i] % 2 != 0:
    #             stop_loop = True
    #             break
    #         devide_num += 1
    #         a[i] = a[i] / 2
    #     if stop_loop: break
        

    print(result)
    
if __name__ == "__main__":
    main()