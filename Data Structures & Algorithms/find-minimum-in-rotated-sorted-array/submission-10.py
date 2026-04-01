class Solution:
    def findMin(self, nums: List[int]) -> int:
        l=0
        r=len(nums)-1
        res=nums[l]
        while l <= r:
            m=(l+r)//2
            if nums[l]<=nums[r]:
                return min(res,nums[l])
            res=min(res,nums[m])
            if nums[l]<=nums[m]:
                l=m+1
            elif nums[m]<=nums[r]:
                r=m-1

        return res