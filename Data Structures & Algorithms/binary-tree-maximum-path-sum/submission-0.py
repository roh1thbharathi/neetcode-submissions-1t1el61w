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

            maxleft=dfs(root.left)                                 #maxleft and maxright
            maxright=dfs(root.right)

            maxleft=max(maxleft,0)
            maxright=max(maxright,0)                               #avoid -ve

            maxsum=max(maxsum,maxleft+root.val+maxright)           #maxsum including split

            return max(maxleft,maxright)+root.val                  #exlucding the split
        
        dfs(root)

        return maxsum