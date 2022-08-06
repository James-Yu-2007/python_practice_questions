class Node:
	def __init__(self , data):
		self.data = data
		self.left = None
		self.right = None

def minDepth(root):
	if root is None:
		return 0

	if root.left is None and root.right is None:
		return 1

	if root.left is None:
		return minDepth(root.right)+1

	if root.right is None:
		return minDepth(root.left) +1
	
	return min(minDepth(root.left), minDepth(root.right))+1

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
root.left.left.right = Node(8)
root.left.right.right = Node(9)
root.right.right.left = Node(10)
root.right.right.left = Node(11)
root.left.left.right.right = Node(12)

print (minDepth(root))

