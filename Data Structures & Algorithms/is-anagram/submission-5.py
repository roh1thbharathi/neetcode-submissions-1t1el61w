class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        mp=defaultdict(int)
        for i in s:
            mp[i]+=1
        for i in t:
            mp[i]-=1
        for count in mp.values():
            if count!=0:
                return False
        return True