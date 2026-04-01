class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq={}
        heap=[]
        res=[]
        for i in range(len(nums)):
            freq[nums[i]]=freq.get(nums[i],0)+1

        for n , c in freq.items():
            heapq.heappush(heap,[-c,n])

        while k:
            c,n=heapq.heappop(heap)
            res.append(n)
            k-=1

        return res