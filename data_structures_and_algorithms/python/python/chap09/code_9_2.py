MAX = 100000
qu = [None for _ in range(MAX)]
tail, head = 0, 0

def init():
    global tail, head
    head = tail = 0
    
def isEmpty():
    global head, tail
    return head == tail

def isFull():
    global head, tail, MAX
    return head == (tail + 1) % MAX

def enqueue(x: int):
    if isFull():
        print("error: queue is full.")
        return None
    global qu, tail, MAX
    qu[tail] = x
    tail += 1
    if tail == MAX: tail = 0
    
def dequeue():
    if isEmpty():
        print("error: queue is empty.")
        return -1
    global qu, head, MAX
    res = qu[head]
    head += 1
    if head == MAX: head = 0
    return res

def main():
    init()
    
    enqueue(3)
    enqueue(5)
    enqueue(7)
    
    print(dequeue())
    print(dequeue())
    
    enqueue(9)
    
if __name__ == "__main__":
    main()