def fibo(N: int):
    print(f"fibo {N} を呼び出しました")
    if N == 0: return 0
    elif N == 1: return 1
    
    result = fibo(N - 1) + fibo(N - 2)
    print(f"{N} 項目 = {result}")
    
    return result

if __name__ == "__main__":
    print(fibo(6))