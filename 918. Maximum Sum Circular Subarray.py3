class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        total=0
        maxSum=float('-inf')
        minSum=float('inf')

        currMax=0
        currMin=0

        for num in nums:
            total+=num

            currMax+=num
            maxSum=max(maxSum,currMax)

            if currMax<0:
                currMax=0
            
            currMin+=num
            minSum=min(minSum,currMin)

            if currMin>0:
                currMin=0
        
        return max(maxSum,total-minSum) if maxSum>0 else maxSum
