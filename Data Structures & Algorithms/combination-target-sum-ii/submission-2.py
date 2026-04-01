class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res=[]

        def dfs(i,tmp,total):

            if total==target:
                res.append(tmp.copy())
                return

            if i==len(candidates) or total>target:
                return

            tmp.append(candidates[i])
            dfs(i+1,tmp,total+candidates[i])

            tmp.pop()
            while (i+1<len(candidates) and  candidates[i]==candidates[i+1]):
                i+=1
            dfs(i+1,tmp,total)

        dfs(0,[],0)
        return res