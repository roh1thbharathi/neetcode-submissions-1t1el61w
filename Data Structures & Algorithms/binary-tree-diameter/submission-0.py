# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res=0
        def dfs(curr):
            if not curr:
                return 0

            right=dfs(curr.right)
            left=dfs(curr.left)

            nonlocal res
            res=max(res,right+left)
            return 1+max(right , left)
        dfs(root)
        return res