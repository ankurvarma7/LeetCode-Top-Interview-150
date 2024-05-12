class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices)==1:
            return 0
        
        cp=prices[0]

        gain=0

        for i in range(1,len(prices)):
            cp=min(cp,prices[i])
            gain=max(gain,prices[i]-cp)
        
        return gain
