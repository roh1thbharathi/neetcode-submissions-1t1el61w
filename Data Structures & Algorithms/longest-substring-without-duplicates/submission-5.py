class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=0
        charset={}
        res=0
        for r in range(len(s)):
            if s[r] in charset:
                l=max(charset[s[r]]+1,l)
            charset[s[r]]=r
            res=max(r-l+1,res)
        return res