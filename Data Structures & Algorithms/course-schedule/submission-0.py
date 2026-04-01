class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        mp= { i:[] for i in range(numCourses)}
        for crs, prs in prerequisites:
            mp[crs].append(prs)
        
        visited=set()

        def dfs(crs):
            if crs in visited:
                return False
            if mp[crs]==[]:
                return True

            visited.add(crs)

            for pre in mp[crs]:
                if not dfs(pre):
                    return False
            visited.remove(crs)
            mp[crs]=[]
            return True

        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True

