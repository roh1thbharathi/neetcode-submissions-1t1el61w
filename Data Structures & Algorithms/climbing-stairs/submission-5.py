class Solution:
    def climbStairs(self, n: int) -> int:
        one , two = 1, 1
        for i in range(n-1):
            temp=one
            one=one+two
            two=temp
        return one



# 1️⃣ dfs(0)
# calls → dfs(1)
# 2️⃣ dfs(1)
# calls → dfs(2)
# 3️⃣ dfs(2)
# calls → dfs(3)
# 4️⃣ dfs(3)
# → base case → returns 1
# Back to dfs(2)
# now calls → dfs(4)
# 5️⃣ dfs(4)
# → base case → returns 0
# Back to dfs(2)
# done → returns 1
# Back to dfs(1)
# now calls → dfs(3)
# 6️⃣ dfs(3)
# → returns 1
# Back to dfs(1)
# done → returns 2
# Back to dfs(0)
# NOW (only now!) it calls → dfs(2)
# 7️⃣ dfs(2)
# 👉 already computed → returns instantly
# Back to dfs(0)
# done → returns 3