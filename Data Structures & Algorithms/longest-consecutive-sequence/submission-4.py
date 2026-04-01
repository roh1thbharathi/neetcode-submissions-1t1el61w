class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset=set(nums)
        res=0
        for i in nums:
            if (i-1) not in numset:
                streak=1
                while(i+streak) in numset:
                    streak+=1
                res=max(streak,res)
        return res
                