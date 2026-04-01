class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res=[]
        digitchar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }

        def dfs(i,currstr):
            if i==len(digits):
                res.append(currstr)
                return

            for c in digitchar[digits[i]]:
                dfs(i+1,currstr+c)
        
        if digits:
            dfs(0,"")
        return res