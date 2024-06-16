class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry=1

        res=[]

        n=len(digits)
        i=n-1
        while i>=0:
            digit=digits[i]+carry

            res.append(digit%10)
            carry=digit//10
            i-=1
        
        while carry>0:
            res.append(carry%10)
            carry=carry//10
        
        def reverse(arr):
            st=0
            en=len(arr)-1

            while st<en:
                temp=arr[st]
                arr[st]=arr[en]
                arr[en]=temp
                st+=1
                en-=1

        reverse(res)
        return res
