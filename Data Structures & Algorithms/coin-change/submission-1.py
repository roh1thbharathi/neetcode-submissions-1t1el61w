class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        res=float("inf")

        def dfs(i,total,count):
            nonlocal res
            if total==amount:
                res=min(count, res)

            if i>=len(coins) or total>amount or count >= res:
                return 

            dfs(i,total+coins[i],count+1)
            dfs(i+1,total,count)



        dfs(0,0,0)
        if res==float("inf"):
            return -1
        return res