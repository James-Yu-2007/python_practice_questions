class newNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
def isChildrenSumProperty(node):
    leftData = False
    rightData = False
    if(node == None or (node.left == None and node.right == None)):
         return True
    else:
        if(node.left != None):
            leftData = node.left.data
        if(node.right != None):
            rightData = node.right.data
        if((node.data == leftData + rightData) and isChildrenSumProperty(node.left) and isChildrenSumProperty(node.right)):
            return True
        else:
            return False
if __name__ == '__main__':
    Root = int(input("please input the value of your root node: "))
    Root_L = int(input("please input the value of the left child node of your root node: "))
    Root_R = int(input("please input the value of the right child node of your root node: "))
    Root_L_L = int(input("please input the value of the left child node of the left child node of your root node: "))
    Root_L_R = int(input("please input the value of the right child node of the left child node of your root node: "))
    Root_R_R = int(input("please input the value of the right child node of the right child node of your root node: "))
    Root_R_L = int(input("please input the value of the left child node of the right child node of your root node: "))
    root = newNode(Root)
    root.left = newNode(Root_L)
    root.right = newNode(Root_R)
    root.left.left = newNode(Root_L_L)
    root.left.right = newNode(Root_L_R)
    root.right.right = newNode(Root_R_R)
    root.right.left = newNode(Root_R_L)
    if(isChildrenSumProperty(root)):
        print("The tree satisfies the children sum property ")
    else:
        print("The tree does not satisfy the children sum property ")