class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums)==0:
            return []
        start=nums[0]
        end=nums[0]

        i=0
        res=[]
        while i<len(nums):

            j=i+1

            while j<len(nums) and nums[j]-nums[j-1]==1:
                end=nums[j]
                j+=1
            
            if start==end:
                res.append(str(start))
            else:
                s=str(start)+"->"+str(end)
                res.append(s)
            if j>=len(nums):
                break
            start=nums[j]
            end=nums[j]
            i=j
        
        return res
