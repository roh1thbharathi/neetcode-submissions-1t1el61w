class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        mp = {}
        
        for i in s:
            mp[i] = mp.get(i, 0) + 1
        
        for i in t:
            mp[i] = mp.get(i, 0) - 1
        
        for count in mp.values():
            if count != 0:
                return False
        
        return True
        