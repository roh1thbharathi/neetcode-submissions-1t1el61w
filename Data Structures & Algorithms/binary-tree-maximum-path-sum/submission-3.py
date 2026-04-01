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

            maxleft=max(0,left)
            maxright=max(0,right)
            
            #split
            maxsum=max(maxsum ,maxleft+maxright+node.val )

            #without split
            return max(maxleft,maxright) + node.val

        dfs(root)
        return maxsum