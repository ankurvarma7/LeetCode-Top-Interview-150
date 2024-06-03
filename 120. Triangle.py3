class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        ROWS=len(triangle)

        dp={}

        for c in range(len(triangle[ROWS-1])):
            dp[(ROWS-1,c)]=triangle[ROWS-1][c]
        
        def dfs(r,c):
            if (r,c) in dp:
                return dp[(r,c)]
            
            dp[(r,c)]=triangle[r][c]+min(dfs(r+1,c),dfs(r+1,c+1))

            return dp[(r,c)]
        return dfs(0,0)
