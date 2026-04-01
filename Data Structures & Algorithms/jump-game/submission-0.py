class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal=len(nums)-1
        for i in range(len(nums)-1,-1,-1):
            if i + nums[i] >= goal:
                goal=i

        if goal==0:
            return True
        else:
            return False


# class Solution:
#     def canJump(self, nums: List[int]) -> bool:
#         memo = {}

#         def dfs(i):
#             if i >= len(nums) - 1:
#                 return True

#             if i in memo:
#                 return memo[i]

#             maxjump = nums[i]

#             for jump in range(1, maxjump + 1):
#                 if dfs(i + jump):
#                     memo[i] = True
#                     return True

#             memo[i] = False
#             return False

#         return dfs(0)


# class Solution:
#     def canJump(self, nums: List[int]) -> bool:
#         n = len(nums)
#         dp = [False] * n
#         dp[n - 1] = True

#         for i in range(n - 2, -1, -1):
#             maxjump = nums[i]

#             for jump in range(1, maxjump + 1):
#                 if i + jump < n and dp[i + jump]:
#                     dp[i] = True
#                     break

#         return dp[0]
