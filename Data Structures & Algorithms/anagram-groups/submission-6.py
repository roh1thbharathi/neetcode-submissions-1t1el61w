class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp={}
        res=[]
        for i in strs:
            sortedkey=''.join(sorted(i))
            if sortedkey in mp:
                mp[sortedkey].append(i)
            else:
                mp[sortedkey]=[i]

        for sortedkeys , keys in mp.items():
            res.append(keys)

        return res
