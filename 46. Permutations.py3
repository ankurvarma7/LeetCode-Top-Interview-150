class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        res=[]
        def swap(i,j):
            temp=nums[i]
            nums[i]=nums[j]
            nums[j]=temp
        
        def solve(index):
            if index>=len(nums):
                res.append(nums.copy())
                return
            
            for i in range(index,len(nums)):
                swap(i,index)
                solve(index+1)
                swap(i,index)
        
        solve(0)
        return res
