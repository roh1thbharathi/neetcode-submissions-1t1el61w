class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n=len(edges)
        mp={i:[] for i in range(n+1)}
        
        def dfs(node , par):
            if node in visit:
                return True
            
            visit.add(node)

            for i in mp[node]:
                if i == par:
                    continue
                if dfs(i , node):
                    return True
            return False
            
        for u,v in edges:
            mp[u].append(v)
            mp[v].append(u)
            visit=set()

            if dfs(u,-1):
                return [u,v]
        return []