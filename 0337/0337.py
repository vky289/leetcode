# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def heist(root):
            if root == None:
                return [0,0]

            left_subtree = heist(root.left)
            right_subtree = heist(root.right)
            include_list = root.val + left_subtree[1] + right_subtree[1]
            exclude_list = max(left_subtree) + max(right_subtree)

            return [include_list, exclude_list]

        return max(heist(root))