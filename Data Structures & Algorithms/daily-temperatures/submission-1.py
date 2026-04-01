class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n=len(temperatures)
        res=[]
        for i in range(n):
            count=0
            j=i+1
            while j<n:
                if temperatures[i]<temperatures[j]:
                    count+=1
                    break
                else:
                    count+=1
                    j+=1
            if j==n:
                res.append(0)
            else:
                res.append(count)
        return res
