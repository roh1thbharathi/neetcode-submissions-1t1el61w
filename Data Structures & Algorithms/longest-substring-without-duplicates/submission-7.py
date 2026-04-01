class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        temp={}
        l=0
        res=0
        for r in range(len(s)):
            if s[r] in temp:
                l=max(temp[s[r]]+1,l)
            temp[s[r]]=r
            res=max(r-l+1,res)

        return res