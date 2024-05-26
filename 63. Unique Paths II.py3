class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        ROWS,COLS=len(obstacleGrid),len(obstacleGrid[0])
        if obstacleGrid[ROWS-1][COLS-1]==1:
            return 0
        dp={}
        dp[(ROWS-1,COLS-1)]=1
        for i in range(ROWS-2,-1,-1):
            if obstacleGrid[i][COLS-1]==1:
                dp[(i,COLS-1)]=0
            else:
                dp[(i,COLS-1)]=min(dp[(i+1,COLS-1)],1)
        
        for i in range(COLS-2,-1,-1):
            if obstacleGrid[ROWS-1][i]==1:
                dp[(ROWS-1,i)]=0
            else:
                dp[(ROWS-1,i)]=min(dp[(ROWS-1,i+1)],1)
        
        def dfs(r,c):
            if (r,c) in dp:
                return dp[(r,c)]
            
            if obstacleGrid[r][c]==1:
                dp[(r,c)]=0
                return 0
            
            dp[(r,c)]=dfs(r+1,c)+dfs(r,c+1)
            return dp[(r,c)]
        
        return dfs(0,0)
