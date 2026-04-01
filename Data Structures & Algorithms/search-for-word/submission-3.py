class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row=len(board)
        col=len(board[0])
        drs=[[1,0],[-1,0],[0,1],[0,-1]]


        def dfs(r,c,i):
            
            if r<0 or r>=row or c<0 or c>=col or board[r][c] != word[i]:
                return False

            if i==len(word)-1:
                return True

            temp = board[r][c]
            board[r][c] = "#"

            for dr , dc in drs:
                nr=r+dr
                nc=c+dc
                if dfs(nr,nc,i+1):
                    return True

            board[r][c] = temp
            return False

           
        for i in range(row):
            for j in range(col):
                    if dfs(i,j,0):
                        return True
        return False