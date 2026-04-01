class Solution:
    def longestPalindrome(self, s: str) -> str:
        n=len(s)
        maxlength=0
        res=""
        for i in range(n):
            for j in range(i,n):#??
                tmp=s[i:j+1]
                if self.ispal(tmp):
                    if len(tmp)>maxlength:
                        res=tmp
                        maxlength=len(tmp)
        return res


    def ispal(self,tmp):
        l=0
        r=len(tmp)-1
        while l<r:
            if tmp[l]!=tmp[r]:
                return False
            r-=1
            l+=1
        return True
