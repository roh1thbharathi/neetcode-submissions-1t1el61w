class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Step 1: Build frequency map
        freq = {}
        for i in nums:
            freq[i] = 1 + freq.get(i, 0)
        
        # Step 2: Use a min-heap to keep track of top k frequent elements
        heap = []
        for i in freq.keys():
            heapq.heappush(heap, (freq[i], i))  # Push frequency and element
            if len(heap) > k:  # Ensure heap size is k
                heapq.heappop(heap)
        
        # Step 3: Extract the elements from the heap
        res = []
        while heap:
            res.append(heapq.heappop(heap)[1])  # Get the element (not frequency)
        
        return res