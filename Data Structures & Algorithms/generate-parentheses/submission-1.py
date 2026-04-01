class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res=[]
        def valid(s):
            openn=0
            for c in s :
                if c in '(':
                    openn+=1
                else:
                    openn-=1
                if openn<0:
                    return False
            return not openn
        def dfs(s):
            if n*2==len(s):
                if valid(s):
                    res.append(s)
                return
            dfs(s+'(')
            dfs(s+')')
        
        dfs("")
        return res