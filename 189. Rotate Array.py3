class Solution:
    def rotate(self, nums: List[int], k: int) -> None:

        def reverse(i,j):

            while i<j:
                temp=nums[i]
                nums[i]=nums[j]
                nums[j]=temp
                i+=1
                j-=1
        
        n=len(nums)
        k=k%n

        reverse(0,n-1)
        reverse(0,k-1)
        reverse(k,n-1)
