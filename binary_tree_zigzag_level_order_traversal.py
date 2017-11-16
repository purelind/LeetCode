# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        def travel(curr, sol, level):
            if not curr:
                return
            if len(sol) <= level:
                new_level = list()
                sol.append(new_level)
            collection = sol[level]
            if level % 2 == 0:
                collection.append(curr.val)
            else:
                collection.insert(0, curr.val)
            travel(curr.left, sol, level+1)
            travel(curr.right, sol, level+1)

        sol = list()
        travel(root, sol, 0)

        return sol


