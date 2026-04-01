class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        res=0

        def dfs(i,prev,count):

            nonlocal res
            res=max(count,res)

            if i==len(nums):
                return 

            if nums[i] > prev: 
                dfs(i+1,nums[i],count+1)

            #skip
            dfs(i+1,prev,count)


        dfs(0,float("-inf"),0)
        return res