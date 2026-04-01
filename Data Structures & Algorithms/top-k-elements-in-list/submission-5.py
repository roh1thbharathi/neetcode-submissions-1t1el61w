class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict=defaultdict(int)
        for i in nums:
            dict[i]+=1
        dict=sorted(dict,key=dict.get,reverse=True)
        return dict[:k]
        