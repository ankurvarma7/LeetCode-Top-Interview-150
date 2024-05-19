class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        if n==1:
            return nums[0]
        if n==2:
            return max(nums[0],nums[1])

        dp={}
        dp[n-1]=nums[n-1]
        dp[n-2]=max(nums[n-2],nums[n-1])
        def dfs(index):
            if index in dp:
                return dp[index]
            
            dp[index]=max(nums[index]+dfs(index+2),dfs(index+1))
            return dp[index]
        
        return dfs(0)
