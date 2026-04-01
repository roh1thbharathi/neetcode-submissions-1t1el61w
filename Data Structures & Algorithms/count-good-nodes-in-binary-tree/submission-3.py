# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def dfs(node, maxvalue):
            if not node:
                return 0

            count = 1 if node.val >= maxvalue else 0
            maxvalue = max(maxvalue, node.val)

            return (
                count + dfs(node.left, maxvalue)+ dfs(node.right, maxvalue)
            )

        return dfs(root, root.val)



        