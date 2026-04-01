class Solution:
    def trap(self, height: List[int]) -> int:
        l=0
        r=len(height)-1
        res=0
        leftmax=0
        rightmax=0
        while l<r:
            if height[l]<height[r]:
                if leftmax<height[l]:
                    leftmax=height[l]
                else:
                    res+=leftmax-height[l]
                l+=1
            else:
                if rightmax<height[r]:
                    rightmax=height[r]
                else:
                    res+=rightmax-height[r]
                r-=1
        return res
        