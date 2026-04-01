class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict=defaultdict(int)
        for i in nums:
            dict[i]+=1
        heap=[]
        for i in dict.keys():
            heapq.heappush(heap,(dict[i],i))
            if len(heap)>k:
                heapq.heappop(heap)
        res=[]
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res
        