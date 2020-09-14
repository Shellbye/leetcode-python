# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        lst = []
        self.getList(root, lst)
        # print(lst)
        d = lst[1] - lst[0]
        for i in range(2, len(lst)):
            cur_d = lst[i] - lst[i-1]
            if cur_d < d:
                d = cur_d
        return d
    
    def getList(self, root, lst=[]):
        if not root:
            return
        self.getList(root.left, lst)
        lst.append(root.val)
        self.getList(root.right, lst)
    
