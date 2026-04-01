class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row=len(matrix)
        col=len(matrix[0])
        l=0
        r=(row*col)-1
        while l<=r:
            m=l+(r-l)//2
            ro=(m//col)
            co=(m%col)
            if target<matrix[ro][co]:
                r=m-1
            elif target>matrix[ro][co]:
                l=m+1
            else:
                return True
        return False