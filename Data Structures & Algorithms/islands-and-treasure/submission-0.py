class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        row=len(grid)
        col=len(grid[0])
        q=deque()
        visited=set()
        drs=[[-1,0],[1,0],[0,1],[0,-1]]

        for i in range(row):
            for j in range(col):
                if grid[i][j]==0:
                    q.append([i,j])
                    visited.add((i,j))

        dist=0
        while q:
            for i in range(len(q)):
                r,c=q.popleft()
                grid[r][c]=dist
                for dr,dc in drs:
                    x=dr+r
                    y=dc+c
                    if x<0 or y<0 or x>=row or y>=col or grid[x][y]==-1 or (x,y) in visited:
                        continue
                    visited.add((x,y))
                    q.append([x,y])
            dist+=1
                