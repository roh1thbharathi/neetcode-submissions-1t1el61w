class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict={}
        i=0
        for n in nums:
            diff=target-n
            if diff in dict:
                return [dict[diff],i]
            dict[n]=i
            i=i+1