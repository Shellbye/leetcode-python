# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        root_b = abs(self.depth(root.left) - self.depth(root.right)) <= 1
        left_b = self.isBalanced(root.left)
        right_b = self.isBalanced(root.right)
        return root_b and left_b and right_b
    
    def depth(self, root):
        if not root:
            return 0
        left_d = 0
        if root.left:
            left_d = self.depth(root.left)
        right_d = 0
        if root.right:
            right_d = self.depth(root.right)
        return max(left_d, right_d) + 1
