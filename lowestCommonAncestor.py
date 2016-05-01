class TreeNode:
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def lowestCommonAncestor(self,root,p,q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        c = root.val
        mn = min(p,q)
        mx = max(p,q)

        if self.inSubtree(root.right,p) and self.inSubtree(root.right,q):
            print 'right:',p,q
            return self.lowestCommonAncestor(root.right,p,q)

        if self.inSubtree(root.left,p) and self.inSubtree(root.left,q):
            print 'left:',p,q
            return self.lowestCommonAncestor(root.left,p,q)
        return c
        
    def inSubtree(self,node,val):
        if node is None:
            return False
        if val == node.val:
            return True
        if val > node.val:
            if self.inSubtree(node.right,val):
                return True
        if val < node.val:
            if self.inSubtree(node.left,val):
                return True
        return False

"""
tree = TreeNode(6)
tree.left = TreeNode(2)
tree.right = TreeNode(8)
tree.left.left = TreeNode(0)
tree.left.right = TreeNode(4)
tree.left.right.left = TreeNode(3)
tree.left.right.right = TreeNode(5)
tree.right.left = TreeNode(7)
tree.right.right = TreeNode(9)
"""

tree = TreeNode(5)
tree.left = TreeNode(3)
tree.right = TreeNode(6)
tree.left.left = TreeNode(2)
tree.left.right = TreeNode(4)
tree.left.left.left = TreeNode(1)

print Solution().lowestCommonAncestor(tree,1,4)

