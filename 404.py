# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if self.isLeaf(root) or root is None:
            return 0
        ans = 0
        if root.left:
            if self.isLeaf(root.left):
                ans = ans + root.left.val
            else:
                ans = ans + self.sumOfLeftLeaves(root.left)
        ans = ans + self.sumOfLeftLeaves(root.right)
        return ans
    
    def isLeaf(self, n):
        return n and n.left is None and n.right is None
