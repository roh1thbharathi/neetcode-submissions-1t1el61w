class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res=0
        for i in range(len(heights)-1):
            for j in range(len(heights)):
                minbar = min(heights[i],heights[j])
                area = (j-i) * minbar
                if area>res:
                    res=area
        return res