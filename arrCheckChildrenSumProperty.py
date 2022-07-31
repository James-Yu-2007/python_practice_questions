from math import floor

# auto creating the nodes in the array
class nodeCreate:
    def __init__(self, value, left = -1, right = -1, parent = -1):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent

inputStr = input("please input you tree separated by commas: ")
inputStr = inputStr.replace(' ', '')
inputArr = inputStr.split(',')

treeArr = []
for i in range(0, len(inputArr)):
    treeArr.append(nodeCreate(inputArr[i]))
    # print(str(treeArr[i].left) + (" is the left child of the node ") + str(i))
    # print(str(treeArr[i].right) + (" is the right child of the node ") + str(i))

for i in range(0, len(treeArr)):
    treeArr[i].value = inputArr[i]
    treeArr[i].left = 2*i+1
    treeArr[i].right = 2*i+2
    # print(str(treeArr[i].left) + (', ') + str(treeArr[i].right))
    if treeArr[i].left >= len(treeArr):
        treeArr[i].left = -1
    if treeArr[i].right >= len(treeArr):
        treeArr[i].right = -1
    # print(str(treeArr[i].left) + (', ') + str(treeArr[i].right))

# for i in range(0, len(treeArr)):
#     print(treeArr[i].value, ", ", treeArr[i].left, ", ", treeArr[i].right)
# checking for children sum property
childrenSumValue = True
for i in range(0, len(treeArr)):
    # print(i)
    if (treeArr[i].left != -1) and (treeArr[i].right != -1):
        if int(treeArr[treeArr[i].left].value) + int(treeArr[treeArr[i].right].value) != int(treeArr[i].value):
            childrenSumValue = False
if childrenSumValue == True:
    print("your tree satisfies the children sum property")
else:
    print("your tree does not satisfy the children sum property")