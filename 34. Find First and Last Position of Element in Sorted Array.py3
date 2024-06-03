class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        

        def getStartingPos(target):
            l=0
            r=len(nums)-1

            while l<=r:
                m=(l+r)//2

                if nums[m]>=target:
                    r=m-1
                else:
                    l=m+1
            if l>=len(nums) or nums[l]!=target:
                return -1
            return l
        
        def getEndingPos(target):
            l=0
            r=len(nums)-1

            while l<=r:
                m=(l+r)//2

                if nums[m]<=target:
                    l=m+1
                else:
                    r=m-1
            if r<0 or nums[r]!=target:
                return -1
            return r
        
        return [getStartingPos(target),getEndingPos(target)]
