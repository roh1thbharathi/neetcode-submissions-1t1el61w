class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n=len(grid)
        visit=set()
        drs=[[0,1],[0,-1],[1,0],[-1,0]]
        minheap=[[grid[0][0],0,0]]

        visit.add((0,0))

        while minheap:
            t,r,c=heapq.heappop(minheap)
            if r==n-1 and c==n-1:
                return t
            for dr , dc in drs:
                neiR=r+dr
                neiC=c+dc
                if (neiR<0 or neiC<0 or neiR==n or neiC == n or (neiR, neiC) in visit):
                    continue
                visit.add((neiR,neiC))
                heapq.heappush(minheap,[max(t,grid[neiR][neiC]),neiR,neiC])

