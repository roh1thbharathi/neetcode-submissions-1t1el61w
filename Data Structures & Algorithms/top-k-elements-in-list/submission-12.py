class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mp={}
        res=[]
        heap=[]

        for i in nums:
            mp[i]=mp.get(i,0)+1

        for n,c in mp.items():
            heapq.heappush(heap, (c,n))
            if len(heap)>k:
                heapq.heappop(heap)

        while heap:
            res.append(heapq.heappop(heap)[1])

        return res






        