class Node:
    # Singly linked node
    def __init__(self, data=None):
        self.data = data
        self.next = None
class singly_linked_list:
    def __init__(self):
        # Createe an empty list
        self.head = None
        self.tail = None
        self.count = 0
    def iterate_item(self):
        # Iterate the list.
        current_item = self.head
        while current_item:
            val = current_item.data
            current_item = current_item.next
            yield val
    def append_item(self, data):
        #Append items on the list
        node = Node(data)
        if self.tail:
            self.tail.next = node
            self.tail = node
        else:
            self.head = node
            self.tail = node
        self.count += 1
treeArr = [25,13,12,7,6,7,5]
items = singly_linked_list()
for i in treeArr:
    items.append_item(i)
# items.append_item('1')
# items.append_item('2')
# items.append_item('3')
# items.append_item('4')
# items.append_item('5')
for val in items.iterate_item():
    print(val)
print("\nhead.data: ",items.head.data)
print("tail.data: ",items.tail.data)