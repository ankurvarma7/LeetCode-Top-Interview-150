class Solution:
    def jump(self, nums: List[int]) -> int:
        dp=[]

        dp.append(nums[0])

        for i in range(1,len(nums)):
            dp.append(max(i+nums[i],dp[i-1]))
        
        ans=0
        index=0

        while index<len(nums)-1:
            ans+=1
            index=dp[index]
        
        return ans
