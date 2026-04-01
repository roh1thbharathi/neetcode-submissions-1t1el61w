class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res=[]
    

        def dfs(i,temp):
            if i>=len(s):
                res.append(temp)
                return

            for j in range(i,len(s)):
                if self.pali(s,i,j):
                    dfs(j+1,temp+[s[i:j+1]])
                 
        dfs(0,[])
        return res



    def pali(self,s,i,j):
        while i<j:
            if s[i]!=s[j]:
                return False
            i+=1
            j-=1
        return True