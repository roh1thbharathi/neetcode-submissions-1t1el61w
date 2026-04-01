class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        ans=[0]*n
        p=1
        for i in range(n):
            p=p*nums[i]
            ans[i]=p
        p=1
        for i in range(n-1,0,-1):
            ans[i]=ans[i-1]*p
            p=p*nums[i]
        ans[0]=p
        return ans