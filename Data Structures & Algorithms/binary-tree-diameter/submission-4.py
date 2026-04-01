# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res=0
        def dfs(root):
            if not root:
                return 0

            left=dfs(root.left)
            right=dfs(root.right)

            nonlocal res

            #current level with split
            res=max(res,left+right)

            #send to higher levels without split 
            return 1+max(right,left)


        dfs(root)
        return res