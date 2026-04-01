class Solution:
    def jump(self, nums: List[int]) -> int:
        res=0
        l=0
        r=0

        while r<len(nums)-1:
            farthest=0
            for i in range(l,r+1):
                farthest=max(farthest,i+nums[i])
            l=r+1
            r=farthest
            res+=1
        
        return res


# class Solution:
#     def jump(self, nums: List[int]) -> int:
#         n = len(nums)
#         dp = [float("inf")] * n
#         dp[n - 1] = 0

#         for i in range(n - 2, -1, -1):
#             max_jump = nums[i]

#             for jump in range(1, max_jump + 1):
#                 if i + jump < n:
#                     dp[i] = min(dp[i], 1 + dp[i + jump])

#         return dp[0]


# class Solution:
#     def jump(self, nums: List[int]) -> int:
#         memo = {}

#         def dfs(i):
#             if i >= len(nums) - 1:
#                 return 0

#             if i in memo:
#                 return memo[i]

#             min_jumps = float("inf")

#             for jump in range(1, nums[i] + 1):
#                 res = dfs(i + jump)
#                 min_jumps = min(min_jumps, 1 + res)

#             memo[i] = min_jumps
#             return min_jumps

#         return dfs(0)