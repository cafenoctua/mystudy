MAX = 100000
st = [None for _ in range(MAX)]
top = 0

def init():
    global top
    top = 0
    
def isEmpty():
    global top
    return top == 0

def isFull():
    global top, MAX
    return top == MAX

def push(x: int):
    if (isFull()):
        print("error: stack is full")
        return None
    global st, top
    st[top] = x
    top += 1
    
def pop():
    if isEmpty():
        print("error: stack is Empty")
        return -1
    global top, st
    top -= 1
    return st[top]

def main():
    init()
    
    exp = "34+12-*"
    for c in exp:
        if c >= '0' and c <= '9':
            add = int(c)
            push(add)
        else:
            a = pop()
            b = pop()
            
            if c == '+': push(b+a)
            elif c == '-': push(b-a)
            elif c == '*': push(b*a)
            else: push(b/a)
            
    return pop()
    
if __name__ == "__main__":
    print(main())