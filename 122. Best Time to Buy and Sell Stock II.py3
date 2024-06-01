class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        dp={}

        def dfs(index,buy):
            if index>=len(prices):
                return 0
            if (index,buy) in dp:
                return dp[(index,buy)]
            
            if buy:
                dp[(index,buy)]=max(prices[index]*-1+dfs(index+1,False),dfs(index+1,True))
            else:
                dp[(index,buy)]=max(prices[index]+dfs(index+1,True),dfs(index+1,False))
            
            return dp[(index,buy)]
        
        return dfs(0,True)
