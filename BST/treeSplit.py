class newNode:
    def __init__(self, x):
        self.data = x
        self.left = self.right = None

def count(root):
    if (root == None):
        return 0
    return (count(root.left) +
            count(root.right) + 1)

def checkRec(root, n):

    if (root == None):
        return False

    if (count(root) == n - count(root)):
        return True

    return (checkRec(root.left, n) or
            checkRec(root.right, n))

def check(root):

    n = count(root)
 
    return checkRec(root, n)

root = newNode(1)
root.left = newNode(2)
root.right = newNode(3)
root.left.left = newNode(4)
root.left.right = newNode(5)
root.right.right = newNode(6)
 
if check(root):
    print("yes")
else:
    print("no")
