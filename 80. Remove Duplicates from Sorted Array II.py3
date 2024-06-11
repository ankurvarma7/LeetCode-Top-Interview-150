class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i=0
        j=0

        while j<len(nums):
            k=j
            count=0
            while k<len(nums) and nums[k]==nums[j]:
                k+=1
                count+=1
            
            for idash in range(min(2,count)):
                nums[i]=nums[j]
                i+=1
            
            j=k
        
        return i
