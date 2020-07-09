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



# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class SolutionV2(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.balanceAndHeight(root)[0]
    
    def balanceAndHeight(self, root):
        if not root:
            return True, -1
        leftBalance, leftHeight = False, 0
        if root.left:
            leftBalance, leftHeight = self.balanceAndHeight(root.left)
        else:
            leftBalance = True
        if not leftBalance:
            return False, leftHeight
        
        rightBalance, rightHeight = True, 0
        if root.right:
            rightBalance, rightHeight = self.balanceAndHeight(root.right)
        else:
            rightBalance = True
        if not rightBalance:
            return False, rightHeight
        
        diff = abs(leftHeight - rightHeight)        
        return leftBalance and rightBalance and diff <= 1, max(leftHeight, rightHeight) + 1
