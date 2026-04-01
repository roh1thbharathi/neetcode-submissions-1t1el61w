class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges)!=n-1:
            return False

        mp=defaultdict(list)
        visit=set()

        for n1,n2 in edges:
            mp[n1].append(n2)
            mp[n2].append(n1)
        
        def dfs(i, prev):
            if i in visit:
                return False

            visit.add(i)

            for nei in mp[i]:
                if nei == prev:
                    continue
                if not dfs(nei,i):
                    return False
            
            return True

        result = dfs(0,-1) and len(visit)==n
        return result





