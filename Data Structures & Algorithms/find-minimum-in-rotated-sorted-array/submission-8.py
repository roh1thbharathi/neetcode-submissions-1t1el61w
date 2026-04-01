class Solution:
    def findMin(self, nums: List[int]) -> int:
        l=0
        r=len(nums)-1
        res=nums[0]
        while l<=r:
            if nums[l]<=nums[r]:
                return min(res,nums[l])
            m=(l+r)//2
            res=min(res,nums[m])
            if nums[l]<=nums[m]:
                l=m+1
            else:
                r=m-1
        return res


#the pivot point is where the minimum will be or the array is sorted so leftmost


#we search the pivot or return nums[l] if sorted