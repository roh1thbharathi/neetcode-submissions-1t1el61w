# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def dfs(root, maxvalue):

            if not root:
                return 0

            count=0
            if root.val>=maxvalue:
                count=1
                maxvalue=max(root.val,maxvalue)

            return count+ dfs(root.left,maxvalue) + dfs( root.right,maxvalue)



        res=dfs(root,root.val)
        return res