class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        row=len(heights)
        col=len(heights[0])
        drs=[[0,1],[0,-1],[1,0],[-1,0]]
        res=[]

        def dfs(r,c):
            nonlocal pac, atl
            if r==0 or c==0:
                pac=True
            if r==row-1 or c==col-1:
                atl=True
            if pac and atl:
                return
            visit.add((r,c))
            for dr,dc in drs:
                x=r+dr
                y=c+dc
                if x<0 or y<0 or x>=row or y>=col or (x,y) in visit or heights[x][y] > heights[r][c] :
                    continue
                dfs(x,y)


        for i in range(row):
            for j in range(col):
                pac=False
                atl=False
                visit=set()
                dfs(i,j)
                if pac and atl:
                    res.append([i,j])
        return res