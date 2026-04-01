class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not n:
            return True
        if len(edges) != n-1:
            return False
        visit=set()
        mp=defaultdict(list)
        for n1, n2 in edges:
            mp[n1].append(n2)
            mp[n2].append(n1)
        def dfs(i , prev):
            if i in visit:
                return False
            visit.add(i)
            for j in mp[i]:
                if j==prev:
                    continue
                if not dfs(j,i):
                    return False
            return True

        return dfs(0,-1) and len(visit)==n