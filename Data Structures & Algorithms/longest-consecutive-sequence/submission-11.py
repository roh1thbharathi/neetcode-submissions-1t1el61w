class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        streak=0
        res=0

        for i in nums:
            streak=1
            while (i+1) in nums:
                streak+=1
                i+=1
            res=max(streak,res)

        return res