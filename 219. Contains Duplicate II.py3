class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        numToIndex={}

        for i,n in enumerate(nums):

            if n in numToIndex:
                if i-numToIndex[n]<=k:
                    return True
            
            numToIndex[n]=i
        
        return False
