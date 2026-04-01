class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res= defaultdict(list)
        for s in strs:
            sortedstring=''.join(sorted(s))
            res[sortedstring].append(s)
        return res.values()