class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n=len(heights)
        maxarea=0
        for i in range(n):
            height=heights[i]
            rightmost=i+1
            leftmost=i-1
            while rightmost<n and heights[rightmost] >=height:
                rightmost+=1
            while leftmost>=0 and heights[leftmost] >=height:
                leftmost-=1
            rightmost-=1
            leftmost+=1
            maxarea=max(maxarea,height*(rightmost-leftmost+1))
        return maxarea