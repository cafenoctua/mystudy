def main() -> int:
    K = input()
    
    cnt = 0
    for k in K:
        i = int(k)
        if i in (3, 5, 7):
            cnt += 1
    
    return cnt

def answer(N: int, cur: int, use: int, counter: list) -> None:
    if cur > N : return
    if use == 0b111: counter[0] += 1
    
    answer(N, cur * 10 + 7, use | 0b001, counter)
    
    answer(N, cur * 10 + 5, use | 0b010, counter)
    
    answer(N, cur * 10 + 3, use | 0b100, counter)
    
if __name__ == "__main__":
    # print(main())
    
    N = int(input())
    counter = [0]
    answer(N, 0, 0, counter)
    print(counter[0])