class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams=defaultdict(list)
        for s in strs:
            sortedstring=''.join(sorted(s))
            anagrams[sortedstring].append(s)
        return list(anagrams.values())
