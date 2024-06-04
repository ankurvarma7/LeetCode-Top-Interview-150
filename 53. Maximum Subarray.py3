class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum=float('-inf')
        currSum=0

        index=0

        while index<len(nums):
            currSum+=nums[index]
            maxSum=max(maxSum,currSum)

            if currSum<0:
                currSum=0
            index+=1

        return maxSum
