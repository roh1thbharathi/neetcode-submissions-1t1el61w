class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp=defaultdict(list)

        for word in strs:
            count=[0]*26
            for i in word:
                count[ord(i)-ord('a')]+=1
            count=tuple(count)
            mp[count].append(word)

        return list(mp.values())