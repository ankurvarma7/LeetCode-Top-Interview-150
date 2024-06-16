class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n=len(prices)

        if k>=n//2:
            res=0
            
            for i in range(1,n):
                res=res+max(0,prices[i]-prices[i-1])
            
            return res

        dp={}

        def maxProfitHelper(index,buy,k):
            if index>=len(prices):
                return 0
            if k==0:
                return 0
            if (index,buy,k) in dp:
                return dp[(index,buy,k)]
            dp[(index,buy,k)]=maxProfitHelper(index+1,buy,k)

            if buy:
                dp[(index,buy,k)]=max(dp[(index,buy,k)],-1*prices[index]+maxProfitHelper(index+1,False,k))
            else:
                dp[(index,buy,k)]=max(dp[(index,buy,k)],prices[index]+maxProfitHelper(index+1,True,k-1))
            return dp[(index,buy,k)]
        
        return maxProfitHelper(0,True,k)
