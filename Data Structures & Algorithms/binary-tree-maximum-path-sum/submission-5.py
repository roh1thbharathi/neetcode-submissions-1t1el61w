# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxsum=root.val

        def dfs(node):
            nonlocal maxsum
            
            if not node:
                return 0

            left=dfs(node.left)
            right=dfs(node.right)

            maxleft=max(left,0)
            maxright=max(right,0)

            maxsum=max(maxsum,maxleft+maxright+node.val)
            return max(maxleft,maxright) + node.val


        dfs(root)
        return maxsum