# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        alist = list()
        rights = list()
        while root:
            alist.append(root.val)
            if root.right:
                rights.append(root.right)
            root = root.left
            if not root and rights:
                root = rights.pop()
        return alist
