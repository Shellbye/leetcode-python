# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        m = {"tilt": 0}
        self.doCalcSum(root, m)
        return m['tilt']
    
    def doCalcSum(self, root, m):
        if not root:
            return 0
        t0 = self.doCalcSum(root.left, m)
        t1 = self.doCalcSum(root.right, m)
        m['tilt'] += abs(t0 - t1)
        return root.val + t0 + t1

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class SolutionV1(object):
    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        t = self.doFindTilt(root)
        t0 = self.findTilt(root.left)
        t1 = self.findTilt(root.right)
        return t + t0 + t1
    
    def doFindTilt(self, root):
        if not root:
            return 0
        t0 = self.doCalcSum(root.left)
        t1 = self.doCalcSum(root.right)
        return abs(t0 - t1)
    
    def doCalcSum(self, root):
        if not root:
            return 0
        t0 = self.doCalcSum(root.left)
        t1 = self.doCalcSum(root.right)
        return root.val + t0 + t1
