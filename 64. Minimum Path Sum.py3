class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        ROWS,COLS=len(grid),len(grid[0])
        dp={}
        add=0
        for r in range(ROWS-1,-1,-1):
            add+=grid[r][COLS-1]
            dp[(r,COLS-1)]=add
        add=0
        for c in range(COLS-1,-1,-1):
            add+=grid[ROWS-1][c]
            dp[(ROWS-1,c)]=add
        def solve(r,c):
            if (r,c) in dp:
                return dp[(r,c)]

            dp[(r,c)]=grid[r][c]+min(solve(r+1,c),solve(r,c+1))
            return dp[(r,c)]

        return solve(0,0) 
