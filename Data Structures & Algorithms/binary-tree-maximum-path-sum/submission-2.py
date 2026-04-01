# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxsum=root.val

        def dfs(root):
            nonlocal maxsum

            if not root:
                return 0

            left=dfs(root.left)
            right=dfs(root.right)

            maxright=max(right,0)
            maxleft=max(left,0)

            maxsum=max(maxsum,maxright+maxleft+root.val)  ##with split

            return max(maxright,maxleft)+root.val        ##without split

        dfs(root)
        return maxsum

