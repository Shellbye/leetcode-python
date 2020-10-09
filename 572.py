# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        if s is None:
            return t is None
        if self.doIsSubTree(s, t):
            return True
        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)
        
    def doIsSubTree(self, s, t):
        if s is None:
            return t is None
        if t is None:
            return False
        if s.val != t.val:
            return False
        if self.doIsSubTree(s.right, t.right) and \
            self.doIsSubTree(s.left, t.left):
            return True
        return False
