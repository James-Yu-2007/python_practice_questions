class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class linkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def append(self, data):
        node = Node(data)
        
        if self.tail:
            self.prev = self.tail
            self.tail.next = node
            self.tail = node

        else:
            self.tail = node
            self.head = node
        self.count += 1
        
items = linkedList()
items.append(1)
items.append(2)
items.append(3)
items.append(4)
items.append(5)
items.append(6)
print(items.count)
