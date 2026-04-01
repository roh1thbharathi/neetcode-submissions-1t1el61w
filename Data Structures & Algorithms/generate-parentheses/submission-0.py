class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack=[]
        res=[]
        def backtracking(openn , closen):
            if openn==closen==n:
                res.append("".join(stack))    #????
                return
            if openn<n:
                stack.append("(")
                backtracking(openn+1,closen)
                stack.pop()
            if closen<openn:
                stack.append(")")
                backtracking(openn,closen+1)
                stack.pop()
        backtracking(0,0)
        return res