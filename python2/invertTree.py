class Solution:	
	def invertTree(self, root):
		if root is None: return root
		self.invertChildren(root)
		return root
	def invertChildren(self,node):
		if node is None: return None
		if node.left is None and node.right is None: return None
		else:
			holder = node.left
			node.left = node.right
			node.right = holder
			self.invertChildren(node.left)
			self.invertChildren(node.right)
			
			
