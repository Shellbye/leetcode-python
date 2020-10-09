"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        ans = []
        stack = [root]
        while stack:
            e = stack.pop()
            if e:
                ans.append(e.val)
                stack.extend(e.children[::-1])
        return ans



"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class SolutionV1(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        ans = []
        self.doPreOrder(root, ans)
        return ans
    
    def doPreOrder(self, root, ans):
        if root:
            ans.append(root.val)
            for c in root.children:
                self.doPreOrder(c, ans)

