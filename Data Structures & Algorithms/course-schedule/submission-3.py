class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        mp=defaultdict(list)
        cycle=set()
        visited=set()

        for crs , pre in prerequisites:
            mp[crs].append(pre)

        def dfs(crs):
            if crs in cycle:
                return False
            if crs in visited:
                return True

            cycle.add(crs)
            for pre in mp[crs]:
                if not dfs(pre):
                    return False
            
            cycle.remove(crs)
            visited.add(crs)
            
            return True


        for i in range(numCourses):
            result=dfs(i)
            if not result:
                return False
        return True