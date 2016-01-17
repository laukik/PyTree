class Node(object):
	def __init__(self,data):
		self.data = data
		self.left = None
		self.right = None


#Let's create a Binary Tree...
class Tree(object):
	def __init__(self,y):
		self.root = y


	def addNode(self,x,y):
		if x.value > y.value:
			if y.right is None:
				y.right = x
			else:
				addNode(x,y.right) 
		else:
			if y.left is None:
				y.left = x
			else:
				addNode(x,y.left)

	def inorder(self,x):
		if x is not None:
			self.inorder(x.left)
			print x.data
			self.inorder(x.right)

	def preOrder(self,x):
		if x is not None:
			print x.data
			inorder(x.left)
			inorder(x.right)

	def postOrder(self,x):
		if x is not None:
			inorder(x.left)
			inorder(x.right)
			print x.data

	def height(self,x):
		if x is not None:
			htl = height(x.left)
			htr = height(x.right)
			return max(htl,htr)+1
		else:
			return 0

	def level(self, x):
		node,val,level = self.root,x.data,0
		while (  node is not None):
			if val > node.data:
				node = node.right
			elif val == node.data:
				return level
			else:
				node = node.left
			level = level + 1
		return -1

	def InorderWithoutRec(self):
		node = self.root
		stack,out = [],[]
		stack.append(node)
		#sumTree = 0
		while stack :
			while node is not None:
				stack.append(node)
				node = node.left
			temp = stack.pop()
			out.append(temp.data )
			#sumTree = sumTree + temp.data
			node = temp.right
		print out[:-1]

	def reverseInOrderWithOutRec(self):
		node = self.root
		stack,out = [],[]
		stack.append(node)
		while stack:
			while node is not None:
				stack.append(node)
				node = node.right
			temp = stack.pop()
			out.append(temp.data )
			#sumTree = sumTree + temp.data
			node = temp.left
		print out[:-1]	

	def levelOrderTraversal(self):
		node = self.root
		queue,out = [],[]
		queue.append(node)
		while queue:
			x = queue[0]
			queue.remove(x)
			if x.left is not None:
				queue.append(x.left)
			if x.right is not None:
				queue.append(x.right)
			out.append(x.data)
		print out

	def levelOrderTraversalLineByLine(self):
		

if __name__ == '__main__':
	###### PUSH DATA ##########
	x = Tree(Node(30))
	x.root.left = Node(10)
	x.root.left.left = Node(5)
	x.root.left.right = Node(15)
	x.root.right = Node(45)
	x.root.right.left = Node(35)
	###### CALL METHODS #######
	x.inorder(x.root)
	x.InorderWithoutRec()
	x.reverseInOrderWithOutRec()
	print x.level(Node(33))
	x.levelOrderTraversal()



