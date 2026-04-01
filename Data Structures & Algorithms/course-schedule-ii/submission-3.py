class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        mp=defaultdict(list)
        visit=set()
        cycle=set()
        output=[]
        
        for crs , prs in prerequisites:
            mp[crs].append(prs)

        def dfs(node):
            if node in cycle:
                return False
            if node in visit:
                return True
            
            cycle.add(node)
            for nei in mp[node]:
                if not dfs(nei):
                    return False 
            cycle.remove(node)
            visit.add(node)
            output.append(node)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return []
        return output
