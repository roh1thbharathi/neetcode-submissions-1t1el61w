class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        mp={i:[]for i in range(n)}
        visit=set()
        for u,v in edges:
            mp[u].append(v)
            mp[v].append(u)

        def dfs(node):
            for nei in mp[node]:
                if nei not in visit:
                    visit.add(nei)
                    dfs(nei)

        res=0
        for i in range(n):
            if i not in visit:
                visit.add(i)
                dfs(i)
                res+=1
        return res