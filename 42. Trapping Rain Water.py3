class Solution:
    def trap(self, height: List[int]) -> int:
        n=len(height)
        pfHeight=[0 for i in range(n)]
        sfHeight=[0 for i in range(n)]

        pfHeight[0]=height[0]
        for i in range(1,n):
            pfHeight[i]=max(height[i],pfHeight[i-1])
        
        sfHeight[n-1]=height[n-1]
        for i in range(n-2,-1,-1):
            sfHeight[i]=max(height[i],sfHeight[i+1])
        res=0
        for i in range(1,n-1):
            res+=max(0,min(pfHeight[i],sfHeight[i])-height[i])
        
        return res
