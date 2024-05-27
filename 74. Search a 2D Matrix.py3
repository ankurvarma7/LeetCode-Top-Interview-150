class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS,COLS=len(matrix),len(matrix[0])

        l=0
        r=ROWS*COLS - 1

        while l<=r:
            m=(l+r)//2

            x=m//COLS
            y=m%COLS

            if matrix[x][y]==target:
                return True
            elif matrix[x][y]>target:
                r=m-1
            else:
                l=m+1
        
        return False
