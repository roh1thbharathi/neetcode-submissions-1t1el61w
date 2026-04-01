class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row=len(grid)
        col=len(grid[0])
        drs=[[1,0],[-1,0],[0,1],[0,-1]]
        count=0

        def dfs(r,c):
            if r<0 or r>=row or c>=col or c<0 or grid[r][c]!='1':
                return

            grid[r][c]='-1'

            for dr,dc in drs:
                dfs(r+dr,c+dc)



        for i in range(row):
            for j in range(col):
                if grid[i][j]=='1':
                    count+=1
                    dfs(i,j)

        return count