class Node:
    def __init__(self, name: str = "") -> None:
        self.next = None
        self.name = name

nil = Node()

def init():
    global nil
    nil.next = nil
    
def printList():
    cur = nil.next
    while cur != nil:
        print(cur.name + " -> ", end=" ")
        cur = cur.next
    print()

def insert(v, p=nil):
    v.next = p.next
    p.next = v

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
        
    node = Node('h')
    insert(node)
    printList()