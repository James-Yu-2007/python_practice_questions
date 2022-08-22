class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class linkedList:
    def __init__(self):
        self.tail = None
        self.head = None
        self.count = 0

    def append(self, data):
        node = Node(data)
        if self.head:
            self.head.next = node
            self.head = node
        else:
            self.tail = node
            self.head = node
        self.count += 1
    
    def __getitem__(self, index):
        if index > self.count - 1:
            return "Index out of range"
        current_val = self.tail
        for n in range(index):
            current_val = current_val.next
        return current_val.data
    
    def __setitem__(self, index, value):
        if index > self.count - 1:
            raise Exception("Index out of range.")
        current = self.tail
        for n in range(index):
            current = current.next
        current.data = value

items = linkedList()
items.append('1')
items.append('2')
items.append('3')
items.append('4')
items.append('5')

items[1] = "change 1"
items[4] = "change 2"
print(items[0])
print(items[1])
print(items[2])
print(items[3])
print(items[4])
