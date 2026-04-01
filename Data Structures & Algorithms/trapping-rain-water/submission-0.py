class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        res=0
        for i in range(len(height)):
            maxleft=maxright=height[i]
            for j in range(i):
                maxleft=max(maxleft,height[j])
            for j in range(i+1,len(height)):
                maxright=max(maxright,height[j])
            res+=min(maxleft,maxright)-height[i]
        return res