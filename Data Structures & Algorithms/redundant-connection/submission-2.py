class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n=len(edges)
        par=[i for i in range(n+1)]
        rank=[1]* (n+1)

        def find(x):
            if par[x]!=x:
                par[x]=find(par[x])
            return par[x]

        def union(n1 , n2):
            x1 = find(n1)
            x2 = find(n2)

            if x1==x2:
                return True

            if rank[x1]>rank[x2]:
                par[x2]=x1
                rank[x1]+=rank[x2]
            else:
                par[x1]=x2
                rank[x2]+=rank[x1]

            return False

        for n1 , n2 in edges:
            if union(n1,n2):
                return [n1,n2]