# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        ans = [0]
        self.doCount(root, ans)
        return ans[0]
    
    def doCount(self, root, ans):
        if root is None:
            return
        ans[0] += 1
        self.doCount(root.left, ans)
        self.doCount(root.right, ans)
        
