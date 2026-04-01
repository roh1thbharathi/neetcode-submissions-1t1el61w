class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res=[0]*len(temperatures)
        stack=[]
        for i , t in enumerate(temperatures):
            while stack and stack[-1][1]<t:
                stacki, stackt = stack.pop()
                res[stacki]=i-stacki
            stack.append([i,t])
        return res