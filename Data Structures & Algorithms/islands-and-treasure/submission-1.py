class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        row=len(grid)
        col=len(grid[0])
        q=deque()
        drs=[[-1,0],[1,0],[0,1],[0,-1]]

        for i in range(row):
            for j in range(col):
                if grid[i][j]==0:
                    q.append([i,j])

        dist=0
        while q:
            for i in range(len(q)):
                r,c=q.popleft()
                grid[r][c]=dist
                for dr,dc in drs:
                    x=dr+r
                    y=dc+c
                    if x<0 or y<0 or x>=row or y>=col or grid[x][y]!=2147483647:
                        continue
                    grid[x][y]=5
                    q.append([x,y])
            dist+=1
                