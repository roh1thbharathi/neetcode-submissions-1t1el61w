class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams=defaultdict(list)
        for s in strs:
            sortedstr=''.join(sorted(s))
            anagrams[sortedstr].append(s)
        return anagrams.values()
        