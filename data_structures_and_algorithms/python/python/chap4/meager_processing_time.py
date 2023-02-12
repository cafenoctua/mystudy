import time
from fibo import fibo
from fibo_memo import fibo as fibo_memo

if __name__ == "__main__":
    start_time = time.time()
    fibo(20)
    print(f"end time: {time.time() - start_time}")
    
    start_time = time.time()
    fibo_memo(20)
    print(f"end time: {time.time() - start_time}")