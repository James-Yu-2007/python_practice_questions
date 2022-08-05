class newNode:

	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None

def getCount(root, low, high):

	if root == None:
		return 0

	if root.data == high and root.data == low:
		return 1

	if root.data <= high and root.data >= low:
		return (1 + getCount(root.left, low, high) +
					getCount(root.right, low, high))

	elif root.data < low:
		return getCount(root.right, low, high)

	else:
		return getCount(root.left, low, high)

root = newNode(15)
root.left = newNode(10)
root.right = newNode(25)
root.left.left = newNode(8)
root.left.right = newNode(12)
root.right.left = newNode(20)
root.right.right = newNode(30)
root.left.left.left = newNode(6)
root.left.left.right = newNode(9)
root.right.left.left = newNode(18)
root.right.left.right = newNode(22)

l = 12
h = 20
print("the number of nodes between ", l, " and ", h," is ",getCount(root, l, h))

