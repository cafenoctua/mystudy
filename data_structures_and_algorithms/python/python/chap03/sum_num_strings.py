def main():
    S = str(input())
    sum = int(S)
    for i in range(len(S)):
        sum += int(S[i])
        if i + 1 < len(S):
            sum += int(S[0:i+1]) + int(S[i+1:])
        
    print(sum)


def main1():
    S = str(input())
    N = len(S)
    res = 0
    for bit in range(1 << (N - 1)):
        tmp = 0
        for i in range(N - 1):
            tmp *= 10
            tmp += int(S[i])
            if bit & (1 << i):
                res += tmp
                tmp = 0
        tmp *= 10
        tmp += int(S[-1])
        res += tmp

    print(res)
    
if __name__ == "__main__":
    main1()