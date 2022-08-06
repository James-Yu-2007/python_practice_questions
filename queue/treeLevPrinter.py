class newNode:

	def __init__(self, key):
		self.data = key
		self.left = None
		self.right = None

def Nodes(root, start, end):
	
	if (root == None):
		return

	q = []
	q.append(root)

	curr = None

	level = 0

	while (len(q)): 

		level += 1

		size = len(q)

		while size:
			curr = q[0]
			q.pop(0)

			
			if (curr.left != None) :
				q.append(curr.left)
			
			if (curr.right != None) :
				q.append(curr.right)
			
			size -= 1

			if (level >= start and level <= end) :
				print(curr.data, end = " ")
                
root = newNode(15)
root.left = newNode(10)
root.right = newNode(20)
root.left.left = newNode(8)
root.left.right = newNode(12)
root.right.left = newNode(16)
root.right.right = newNode(25)
root.right.right.right = newNode(30)
 
start = 2
end = 3
Nodes(root, start, end)

