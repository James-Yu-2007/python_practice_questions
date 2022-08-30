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

    def delete(self, data):
        current = self.head
        while current:
            if current.data == data:
                if current == self.head:
                    self.head = current.next
                    self.head.prev = None
                elif current == self.tail:
                    self.tail = current.prev
                    self.tail.next = None
                else:
                    current.prev.next = current.next
                    current.next.prev = current.prev
            current = current.next
        self.count -= 1

    def printItem(self):
        currentItem = self.head
        while currentItem:
            val = currentItem.data
            currentItem = currentItem.next
            yield val
        
items = linkedList()
items.append(1)
items.append(2)
items.append(3)
items.append(4)
items.append(5)
items.append(6)

for val in items.printItem():
    print(val)

print("\n")
items.delete(1)
for val in items.printItem():
    print(val)