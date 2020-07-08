# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        ans = []
        if not root:
            return ans
        s1 = [root]
        s2 = []
        while s1 or s2:
            level = []
            if s1:
                while s1:
                    # s1 为本轮出栈
                    cur = s1[0]
                    level.append(cur.val)
                    if cur.left:
                        s2.append(cur.left)
                    if cur.right:
                        s2.append(cur.right)
                    s1 = s1[1:]
            else:
                while s2:
                    # s2 为本轮出栈
                    cur = s2[0]
                    level.append(cur.val)
                    if cur.left:
                        s1.append(cur.left)
                    if cur.right:
                        s1.append(cur.right)
                    s2 = s2[1:]
            ans.append(level)
        ans.reverse()
        return ans
