value = [500, 100, 50, 10, 5, 1]

def main():
    X = int(input())
    a = [int(input()) for _ in range(len(value))]
    
    result = 0
    for i in range(len(value)):
        add = X // value[i]
        
        if add > a[i]: add = a[i]
        
        X -= value[i] * add
        result += add
    
    print(result)
    
if __name__ == "__main__":
    main()