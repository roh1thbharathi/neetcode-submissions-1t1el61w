class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        mp={}

        if len(s)!=len(t):
            return False

        for i in range(len(s)):
            mp[s[i]]=mp.get(s[i],0)+1

        for i in t:
            mp[i]=mp.get(i,0)-1

        for n,c in mp.items():
            if c!=0:
                return False

        return True
        