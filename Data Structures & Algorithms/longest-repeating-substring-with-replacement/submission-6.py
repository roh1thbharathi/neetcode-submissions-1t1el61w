class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        mp={}
        maxf=0
        l=0
        res=0
        for i in range(len(s)):
            mp[s[i]]=1+mp.get(s[i],0)
            maxf=max(mp.values())
            if (i-l+1)-maxf>k:
                mp[s[l]]-=1
                l+=1
            res=max(i-l+1,res)

        return res
