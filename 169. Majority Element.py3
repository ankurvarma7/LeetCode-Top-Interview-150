class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ME,count=nums[0],1

        for i in range(1,len(nums)):
            if nums[i]==ME:
                count+=1
            elif count==0:
                ME=nums[i]
                count=1
            else:
                count-=1
        
        return ME
