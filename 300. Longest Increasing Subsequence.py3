class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        inc=[]

        def addToSequence(num):
            n=len(inc)

            if n==0 or inc[n-1]<num:
                inc.append(num)
            elif inc[n-1]==num:
                return
            else:
                l=0
                r=n-1

                while l<=r:
                    m=(l+r)//2
                    if inc[m]==num:
                        return
                    elif inc[m]>num:
                        r=m-1
                    else:
                        l=m+1
                inc[l]=num
    
        for num in nums:
            addToSequence(num)
        
        return len(inc)
