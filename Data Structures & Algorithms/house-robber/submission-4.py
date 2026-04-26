class Solution:
    def rob(self, nums: List[int]) -> int:
        rob2, rob1 = 0, 0  

        for n in nums:
            curr = max(n + rob2, rob1)
            rob2 = rob1
            rob1 = curr

        return rob1