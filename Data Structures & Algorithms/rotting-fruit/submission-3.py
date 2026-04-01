class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        row=len(grid)
        col=len(grid[0])
        q=deque()
        time=0
        fresh=0
        drs=[[1,0],[-1,0],[0,1],[0,-1]]
        for i in range(row):
            for j in range(col):
                if grid[i][j]==1:
                    fresh+=1
                if grid[i][j]==2:
                    q.append([i,j])

        while q and fresh>0:
            for i in range(len(q)):
                 r,c = q.popleft()
                 for dr , dc in drs:
                    x=r+dr
                    y=c+dc
                    if x<0 or x>=row or y<0 or y>=col or grid[x][y]!=1:
                        continue
                    q.append([x,y])
                    grid[x][y] = 2
                    fresh-=1
            time+=1


        if fresh:
            return -1
        else:
            return time