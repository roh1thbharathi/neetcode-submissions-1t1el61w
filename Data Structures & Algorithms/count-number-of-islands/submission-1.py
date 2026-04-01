class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res=0
        row=len(grid)
        col=len(grid[0])
        drs=[[0,1],[0,-1],[1,0],[-1,0]]

        def dfs(r ,c):
            if c<0 or c>=col or r<0 or r>=row or grid[r][c]!='1':
                return

            grid[r][c]=-1

            for dr ,dc in drs:
                dfs(r+dr,c+dc)



        for i in range(row):
            for j in range(col):
                if grid[i][j]=='1':
                    dfs(i,j)
                    res+=1

        return res