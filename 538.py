
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    pre_sum = 0
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root:
            self.convertBST(root.right)
            root.val = root.val + self.pre_sum
            self.pre_sum = root.val
            self.convertBST(root.left)
        return root


class SolutionDIY(object):
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        # find all node
        nodes = []
        self.find_all_node(root, nodes)
        print(nodes)
        g_sum = [0]
        for i in range(len(nodes)):
            g_sum.append(g_sum[i] + nodes[i])
        print(g_sum)
        self.doConvert(root, nodes, g_sum)
        print(root)
        return root
    
    def doConvert(self, root, nodes, g_sum):
        if root:
            root.val = root.val + g_sum[nodes.index(root.val)]
            self.doConvert(root.left, nodes, g_sum)
            self.doConvert(root.right, nodes, g_sum)

    def find_all_node(self, root, nodes=[]):
        if root.right:
            self.find_all_node(root.right, nodes)
        if root:
            nodes.append(root.val)
        if root.left:
            self.find_all_node(root.left, nodes)
        
