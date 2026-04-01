class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset=set(nums)
        res=0
        for n in numset:
            if (n-1) not in numset:
                streak=1
                while n+streak in numset:
                    streak+=1
                res=max(res,streak)
        return res

            