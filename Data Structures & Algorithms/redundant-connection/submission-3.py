class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

        mp = defaultdict(list)

        def dfs(src, target, visit):
            if src == target:
                return True

            visit.add(src)

            for nei in mp[src]:
                if nei not in visit:
                    if dfs(nei, target, visit):
                        return True

            return False

        for n1, n2 in edges:
            visit = set()

            if dfs(n1, n2, visit):
                return [n1, n2]

            mp[n1].append(n2)
            mp[n2].append(n1)