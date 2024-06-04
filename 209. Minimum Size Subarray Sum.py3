class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        i=0
        j=0
        n=len(nums)
        res=n+1
        add=0

        while j<n:
            add+=nums[j]

            while i<=j and add>=target:
                res=min(res,j-i+1)
                add-=nums[i]
                i+=1
            
            j+=1

        return res if res!=n+1 else 0
