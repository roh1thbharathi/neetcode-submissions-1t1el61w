class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        pr=[i for i in range(n)]
        rank=[1]*n

        def find(x):
            if pr[x]!=x:
                pr[x]=find(pr[x])
            return pr[x]

        def union(x,y):
            rootX=find(x)
            rootY=find(y)

            if rootX==rootY:
                return False

            if rank[rootX]>rank[rootY]:
                pr[rootY]=rootX
            elif rank[rootY]>rank[rootX]:
                pr[rootX]=rootY
            else:
                pr[rootX]=rootY
                rank[rootY]+=1
            return True
        
        for u,v in edges:
            if union(u,v):
                n-=1
        return n
