from math import floor

# auto creating the nodes in the array
class nodeCreate:
    def __init__(self, value, left, right):
        self.value = value
        self.left = -1
        self.right = -1

inputStr = input("please input you tree separated by commas: ")
inputStr = inputStr.replace(' ', '')
inputArr = inputStr.split(',')

treeArr = []
for i in range(0, len(inputArr)):
    treeArr.append(nodeCreate(inputArr[i], {}, {}))
    treeArr[i].value = inputArr[i]
    treeArr[i].left = 2*i+1
    treeArr[i].right = 2*i+2
    # print(str(treeArr[i].left) + (" is the left child of the node ") + str(i))
    # print(str(treeArr[i].right) + (" is the right child of the node ") + str(i))


# checking for children sum property
childrenSumValue = True
for i in range(0, floor(len(treeArr)/2)):
    if int(treeArr[treeArr[i].left].value) + int(treeArr[treeArr[i].right].value) != int(treeArr[i].value):
        childrenSumValue = False

if childrenSumValue == True:
    print("ur gud")
else:
    print("ur bad")