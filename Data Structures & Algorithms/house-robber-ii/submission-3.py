class Solution:
    def rob(self, nums: List[int]) -> int:

        def helper(nums):
            rob1, rob2 = 0, 0

            for num in nums:
                temp = max(rob2 + num, rob1)
                rob2 = rob1
                rob1 = temp

            return rob1

        if len(nums) == 1:
            return nums[0]

        return max(helper(nums[1:]),helper(nums[:-1]))