class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        drs=[[1,0],[-1,0],[0,1],[0,-1]]
        row=len(grid)
        col=len(grid[0])
        maxarea=0

        def dfs(r,c):
            if r<0 or c<0 or r>=row or c>=col or grid[r][c]!=1:
                return 0
            
            grid[r][c]=-1
            area=1

            for dr , dc in drs:
                area+=dfs(r+dr,c+dc)
            return area
            
        for i in range(row):
            for j in range(col):
                if grid[i][j]==1:
                    maxarea=max(maxarea,dfs(i,j))

        return maxarea