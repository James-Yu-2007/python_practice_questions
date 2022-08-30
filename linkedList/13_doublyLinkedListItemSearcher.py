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

    def itemSearch(self):
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

itemSearchResult = False
for val in items.itemSearch():
    if val == 3:
        itemSearchResult = True
print(itemSearchResult)
