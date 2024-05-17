class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        elements=set()
        visited=set()

        for num in nums:
            elements.add(num)
        res=min(1,len(nums))
        
        for num in nums:
            if (num-1) in elements or num in visited:
                continue
            else:
                visited.add(num)
                l=0
                curr=num
                while curr in elements:
                    curr+=1
                    l+=1
                
                res=max(res,l)
        
        return res
