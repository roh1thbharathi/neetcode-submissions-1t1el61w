class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n=len(s)
        res=0
        count={}
        l=0
        maxf=0
        for i in range(n):
            count[s[i]]=count.get(s[i],0)+1
            maxf=max(maxf,count[s[i]])
            if (i-l+1)-maxf >k:
                count[s[l]]-=1
                l+=1
            res=max(res,(i-l+1))
        return res
