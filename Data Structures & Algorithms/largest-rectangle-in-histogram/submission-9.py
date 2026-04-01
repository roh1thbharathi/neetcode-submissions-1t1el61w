class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack=[]
        maxarea=0
        for i ,h in enumerate(heights):
            start=i
            while stack and h<stack[-1][1]:
                stacki,stackh=stack.pop()
                maxarea=max(maxarea,stackh*(i-stacki))
                start=stacki
            else:
                stack.append((start,h))
        for i , h in stack:
            maxarea=max(maxarea,h*(len(heights)-i))
        return maxarea