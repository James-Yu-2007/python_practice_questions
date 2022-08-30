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
        new_item = Node(data)
        if self.head:
            new_item.prev = self.tail
            self.tail.next = new_item
            self.tail = new_item
        else:
            self.head = new_item
            self.tail = self.head

    def printItem(self):
        current = self.tail
        while current:
            print(current.data)
            current = current.prev
        
items = linkedList()
items.append(1)
items.append(2)
items.append(3)
items.append(4)
items.append(5)
items.append(6)

items.printItem()