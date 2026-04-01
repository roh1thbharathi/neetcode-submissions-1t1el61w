class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset=set(nums)
        res=0                                                                                                                           
        for i in nums:
            streak=1
            if (i-1) not in numset:
                while (i+streak) in numset:
                    streak+=1
            res=max(res,streak)
        return res