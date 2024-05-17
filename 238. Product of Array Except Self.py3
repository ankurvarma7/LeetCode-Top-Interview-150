class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res=[1 for i in range(len(nums))]

        res[0]=nums[0]
        for i in range(1,len(nums)):
            res[i]=res[i-1]*nums[i]
        
        suffix=1
        for i in range(len(nums)-1,0,-1):
            res[i]=res[i-1]*suffix
            suffix*=nums[i]
        
        res[0]=suffix
        return res
