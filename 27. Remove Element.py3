class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if len(nums)==0:
            return 0
        first=0
        last=len(nums)-1

        while first<last:
            if nums[last]==val:
                last-=1
            elif nums[first]==val:
                temp=nums[first]
                nums[first]=nums[last]
                nums[last]=temp
                first+=1
                last-=1
            else:
                first+=1
        
        return first if nums[first]==val else first+1
