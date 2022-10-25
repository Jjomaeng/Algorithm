
class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class singleLink:
    def __init__(self):
        self.head = None
        self.tail = None	
        self.size = 0
    
    def putNode(self, data):
        node = Node(data)
        if self.head == None:
            self.head = node
            self.tail = node
        else:    
            self.tail.next = node
            self.tail = node
        self.size += 1
    
    def printAll(self):
        node = self.head
        while node != None:
            print(node.val)
            node = node.next



def reverse_link(input:singleLink) -> singleLink:
    pos = input.head
    reverse_node = []
    while pos != None:
        reverse_node.append(pos.val)
        pos = pos.next
    reverse_node = reverse_node[::-1]
    print(reverse_node)
    
    new = singleLink()
    for i in range(input.size):
        new.putNode(reverse_node[i])

    return new
            

            


L = singleLink()

for i in range(5):
  L.putNode(i+1)
result = reverse_link(L)
result.printAll()
