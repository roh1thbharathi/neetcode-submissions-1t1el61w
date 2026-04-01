class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh=0
        row=len(grid)
        col=len(grid[0])
        q=collections.deque()
        time=0
        drs=[[0,1],[0,-1],[1,0],[-1,0]]

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
                    x=dr+r
                    y=dc+c

                    if y<0 or y>=col or x<0 or x>=row or grid[x][y]!=1:
                        continue

                    grid[x][y]=2
                    q.append([x,y])
                    fresh-=1

            time+=1

        if fresh:
            return -1
        else:
            return time