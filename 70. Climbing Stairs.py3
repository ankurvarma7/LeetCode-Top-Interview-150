class Solution:
    def climbStairs(self, n: int) -> int:
        if n==1:
            return 1
        if n==2:
            return 2
        dp={}
        dp[0]=1
        dp[1]=1
        dp[2]=2
        def dfs(n):
            if n in dp:
                return dp[n]
            dp[n]=dfs(n-1)+dfs(n-2)
            return dp[n]
        
        return dfs(n)
