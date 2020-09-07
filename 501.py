# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return None
        val_map = {}
        self.doFind(root, val_map)
        ans_list = []
        ans_v = None
        for k in val_map:
            v = val_map[k]
            if v > ans_v:
                ans_v = v
                ans_list = [k]
            elif v == ans_v:
                ans_list.append(k)
        return ans_list
    
    def doFind(self, root, val_map):
        if not root:
            return
        v = root.val
        if v in val_map:
            val_map[v] = 1 + val_map[v]
        else:
            val_map[v] = 1
        self.doFind(root.left, val_map)
        self.doFind(root.right, val_map)
