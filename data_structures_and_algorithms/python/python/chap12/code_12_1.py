def insert_sort(a: list):
    N = len(a)
    for i in range(1, N):
        v = a[i]
        
        j = i
        for _ in range(j, 0, -1):
            if a[j-1] > v:
                a[j] = a[j-1]
                j -= 1
            else:
                break
        a[j] = v
    return a
        
def main():
    input_data =[
        5,
        4,
        1,
        3,
        5,
        2
    ]
    input_iter = iter(input_data)
    N = int(next(input_iter))
    a = [int(next(input_iter)) for _ in range(N)]
    
    return insert_sort(a)
    
if __name__ == "__main__":
    print(main())
        