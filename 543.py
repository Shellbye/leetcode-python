# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    max_d = 0

    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.find_deepest(root)
        return self.max_d
    
    def find_deepest(self, root):
        if not root:
            return 0
        left_dp = right_dp = 0
        if root.left:
            left_dp = self.find_deepest(root.left)
        if root.right:
            right_dp = self.find_deepest(root.right)
        # print(right_dp, left_dp)
        if right_dp + left_dp > self.max_d:
            self.max_d = right_dp + left_dp
        return 1 + max(left_dp, right_dp)
