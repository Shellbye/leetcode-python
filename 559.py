"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        if not root:
            return 0
        max_d = 0
        max_d = self.doFind(root, 0, max_d)
        return max_d
        
    def doFind(self, root, cur_d, max_d):
        if root:
            cur_d = cur_d + 1
            m_list = [cur_d, max_d]
            for n in root.children:
                l = self.doFind(n, cur_d, max_d)
                m_list.append(l)
            max_d = max(m_list)
            return max_d
