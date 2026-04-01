class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack=[]
        res=[]

        def dfs(close , open):
            
            if close==open==n:
                res.append("".join(stack))
                return

            if open<n:
                stack.append('(')
                dfs(close,open+1)
                stack.pop()

            if close<open:
                stack.append(')')
                dfs(close+1,open)
                stack.pop()

        dfs(0,0)
        return res