class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        candidates.sort()
        res=[]
        temp=[]

        def dfs(i,temp,total):

            if total==target:
                res.append(temp.copy())
                return

            if i==len(candidates) or total>target:
                return
            
            temp.append(candidates[i])
            dfs(i+1,temp,total+candidates[i])

            temp.pop()
            while (i+1<len(candidates) and candidates[i]==candidates[i+1]):
                i+=1
            dfs(i+1,temp,total)

        dfs(0,[],0)
        return res