"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        if root is None:
            return []
        ans = []
        stack = [root, root]
        while stack:
            cur = stack.pop()
            if stack and cur == stack[-1]:
                for c in cur.children[::-1]:
                    stack.extend([c, c])
            else:
                ans.append(cur.val)
        return ans


"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class SolutionV1(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        if root is None:
            return []
        ans = []
        self.doPostOrder(root, ans)
        return ans
    
    def doPostOrder(self, root, ans):
        if root:
            for c in root.children:
                self.doPostOrder(c, ans)
            ans.append(root.val)
