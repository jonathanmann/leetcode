class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
	self.right = None

"""
class Solution:
	def __init__(self):
		self.level_node_lst = []
		self.visit_stack = []

	def isSymmetric(self, root):
		self.bfs_level_node_lst_gen(root, 0)
		for i in self.level_node_lst:
			x = i
			y = list(reversed(i))
			if x != y:
				return False
		return True
	def bfs_level_node_lst_gen(self, root, level):
		self.visit_stack.append(root)
		try:
			self.level_node_lst[level]
		except:
			self.level_node_lst.append(list())
		if root:
			self.level_node_lst[level].append(root.val)
		else:
			self.level_node_lst[level].append('#')
			self.visit_stack.pop()
		return

		self.bfs_level_node_lst_gen(root.left, level+1)
		self.bfs_level_node_lst_gen(root.right, level+1)
		self.visit_stack.pop()
"""

class Solution:
    def __init__(self):
        self.t = {}
    def isSymmetric(self,root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        self.tree_helper(root,0)
        for r in self.t:
            if self.t[r] <> self.t[r][::-1]:
                return False
        return True

    def tree_helper(self,node,level):
        if level not in self.t:
            self.t[level] = []
        if node is None:
            self.t[level].append(None)
        else:
            self.t[level].append(node.val)
            self.tree_helper(node.left,level + 1)
            self.tree_helper(node.right,level + 1)


if __name__ == '__main__':
    root = TreeNode(3)
    root.left = TreeNode(1)
    root.right = TreeNode(1)
    root.left.left = TreeNode(3)
    root.right.right = TreeNode(4)
    test = Solution()
    print test.isSymmetric(root)
