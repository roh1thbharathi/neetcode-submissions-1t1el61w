class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        row=len(heights)
        col=len(heights[0])
        drs=[[0,1],[0,-1],[1,0],[-1,0]]
        pac=set()
        atl=set()

        def dfs(r,c,prevh,visit):
            if ((r, c) in visit or r<0 or c<0 or r==row or c==col or prevh>heights[r][c]):
                return 
            visit.add((r,c))

            for dr,dc in drs:
                dfs(r+dr,c+dc,heights[r][c],visit)

        
        for r in range(row):
            dfs(r,0,heights[r][0],pac)
            dfs(r,col-1,heights[r][col-1],atl)

        for c in range(col):
            dfs(0,c,heights[0][c],pac)
            dfs(row-1,c,heights[row-1][c],atl)

        res=[]
        for i in range(row):
            for j in range(col):
               if (i,j) in pac and (i,j) in atl:
                    res.append([i,j])

        return res