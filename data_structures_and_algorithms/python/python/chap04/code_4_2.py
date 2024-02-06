def func(N: int):
    print(f"{N} を呼び出しました")
    
    if N == 0: return 0
    
    result = N + func(N - 1)
    print(f"{N} までの和 = {result}")
    return result

if __name__ == "__main__":
    func(5)