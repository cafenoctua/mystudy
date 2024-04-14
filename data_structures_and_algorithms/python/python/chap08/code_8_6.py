class Node:
    def __init__(self, name: str = "") -> None:
        self.next = None
        self.prev = None
        self.name = name

nil = Node()

def init():
    global nil
    nil.prev = nil
    nil.next = nil
    
def printList():
    cur = nil.next
    while cur != nil:
        print(cur.name + " -> ", end=" ")
        cur = cur.next
    print()

def insert(v, p=nil):
    v.next = p.next
    p.next.prev = v
    p.next = v
    v.prev = p

def erase(v):
    global nil
    if v == nil: return
    v.prev.next = v.next
    v.next.prev = v.prev
    del v

if __name__ == "__main__":
    init()
    
    names = ['a',
             'b',
             'c',
             'e',
             'f',
             'g']

    for i, name in enumerate(names):
        node = Node(name)
        
        insert(node)
        print(f"step {i}")
        printList()
        
        if name == 'b': b = node
        
    print("Befor:")
    printList()
    print("After:")
    erase(b)
    printList()