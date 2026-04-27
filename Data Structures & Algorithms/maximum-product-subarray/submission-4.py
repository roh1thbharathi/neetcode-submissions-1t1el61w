class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        curMin, curMax = 1, 1

        for n in nums:
            if n == 0:
                curMin, curMax = 1, 1
                continue

            tmp = curMax * n
            curMax = max(tmp, n * curMin, n)
            curMin = min(tmp, n * curMin, n)

            res = max(res, curMax)

        return res


# Track both best and worst at each step, because sign flips can turn worst into best.
# 0 resets
# res= max(nums) initially