class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class linkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0
    
    def append(self, data):
        node = Node(data)
        if self.tail:
            self.tail.next = node
            self.tail = node
        else:
            self.head = node
            self.tail = node
        self.count += 1

    def itemsInLinkedList(self):
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

indexInput = int(input("please input the index you want to find: "))
list = []
for val in items.itemsInLinkedList():
    list.append(val)
print(list[indexInput])