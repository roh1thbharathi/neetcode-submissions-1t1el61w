class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        heap = []
        res = []

        for i, num in enumerate(nums):
            heapq.heappush(heap, (-num, i))

            # remove elements outside the window
            while heap[0][1] <= i - k:
                heapq.heappop(heap)

            # start recording once first full window is formed
            if i >= k - 1:
                res.append(-heap[0][0])

        return res
        