# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ans = []
        self.doInOrder(root, ans)
        return ans
    
    def doInOrder(self, root, ans):
        if root is None:
            return

        self.doInOrder(root.left, ans)
        ans.append(root.val)
        self.doInOrder(root.right, ans)
