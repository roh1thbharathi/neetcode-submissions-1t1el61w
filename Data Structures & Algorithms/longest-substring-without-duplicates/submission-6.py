class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res=0
        for i in range(len(s)):
            temp=set()
            for j in range(i,len(s)):
                if s[j] in temp:
                    break
                temp.add(s[j])
            res=max(res,len(temp))

        return res