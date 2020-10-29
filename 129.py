# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        path = [root.val]
        ans = [0]
        self.dfs(root, path, ans)
        return ans[0]
    
    def dfs(self, root, path, ans):
        if root is None:
            return
        if root.left is None and root.right is None:
            t = 0
            f = 1
            for v in path[::-1]:
                t += v * f 
                f *= 10
            ans[0] += t
            return
        if root.left:
            self.dfs(root.left, path + [root.left.val], ans)
        if root.right:
            self.dfs(root.right, path + [root.right.val], ans)

