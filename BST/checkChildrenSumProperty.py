class create_node: 
    def __init__(self, nodeValue): 
        self.value = nodeValue  
        self.left = None
        self.right = None
  

def checkSum(node):           
    leftChild_value= 0
    rightChild_value = 0

    if(node == None or (node.left == None and node.right == None)):  
        return 1
    else:           
        if(node.left != None): 
            leftChild_value = node.left.value 
      
        if(node.right != None): 
            rightChild_value = node.right.value

        if((node.value == leftChild_value + rightChild_value) and checkSum(node.left) and checkSum(node.right)): 
            return 1
        else: 
            return 0

root = create_node(25)
root.left = create_node(13)  
root.right = create_node(12)  
root.left.left = create_node(7)  
root.left.right = create_node(6)  
root.right.left = create_node(7)  
root.right.right = create_node(6)

if(checkSum(root)):  
    print("The created tree satisfies the children sum property ")  
else: 
    print("The created tree does not satisfy the children sum property ")