# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        paths = []
        self.findPath(root, [], paths)
        return paths

    def findPath(self, node, path, paths):
        if not node:
            return
        path.append(str(node.val))
        if node.left is None and node.right is None:
            paths.append("->".join(path))
            return
        if node.left:
            p1 = path[:]
            self.findPath(node.left, p1, paths)
        if node.right:
            p2 = path[:]
            self.findPath(node.right, p2, paths)
