class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class singly_linked_list:
    def __init__(self):
        self.tail = None
        self.head = None
        self.count = 0

    def append_item(self, data):
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

items = singly_linked_list()
items.append_item('1')
items.append_item('2')
items.append_item('3')
items.append_item('4')
items.append_item('5')

items[1] = "change 1"
items[4] = "change 2"
print(items[0])
print(items[1])
print(items[2])
print(items[3])
print(items[4])
