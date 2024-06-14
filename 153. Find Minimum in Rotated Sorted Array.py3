class Solution:
    def findMin(self, nums: List[int]) -> int:
        n=len(nums)
        if n==1:
            return nums[0]
        if nums[0]<nums[n-1]:
            return nums[0]
        if nums[n-1]<nums[n-2]:
            return nums[n-1]
        
        l=1
        r=n-2
        while l<=r:
            m=(l+r)//2

            if nums[m]<nums[m+1] and nums[m]<nums[m-1]:
                return nums[m]
            elif nums[m]>nums[0]:
                l=m+1
            else:
                r=m-1
