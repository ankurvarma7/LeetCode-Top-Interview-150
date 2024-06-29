class Solution:
    def canJump(self, nums: List[int]) -> bool:
        gas=nums[0]

        for i in range(len(nums)):
            if gas<0:
                return False
            
            gas=max(gas,nums[i])

            gas-=1
        
        return True
