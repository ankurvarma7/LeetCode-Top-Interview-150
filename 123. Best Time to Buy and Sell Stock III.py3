class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices)==1:
            return 0
        
        minPrice=prices[0]
        maxProfit=[]
        maxProfit.append(0)

        for i in range(1,len(prices)):
            minPrice=min(minPrice,prices[i])
            maxProfit.append(max(maxProfit[i-1],prices[i]-minPrice))

        if len(prices)==2:
            return maxProfit[1]
        
        n=len(prices)-1
        maxPrice=prices[n]
        res=maxProfit[n]
        for i in range(n-1,0,-1):
            maxPrice=max(maxPrice,prices[i])
            res=max(res,maxProfit[i-1]+maxPrice-prices[i])
        
        return res
