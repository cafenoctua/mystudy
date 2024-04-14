def main():
    print("Start Game!")
    
    left = 20
    right = 36
    
    while right - left > 1:
        mid = left + (right - left) / 2
        print("Is the age then " + str(mid) + " ? (yes/no)")
        ans = input()
        
        if ans == "yes": right = mid
        else: left = mid
        
    print("The age is " + str(left) + "!")
    
if __name__ == "__main__":
    main()