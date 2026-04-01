class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res=[1]*len(nums)
        p=1
        for i in range(len(nums)):
            p=p*nums[i]
            res[i]=p
        p=1
        for i in range(len(res)-1, 0 ,-1):
           res[i]=res[i-1] * p
           p=p*nums[i]
        res[0]=p
        return res