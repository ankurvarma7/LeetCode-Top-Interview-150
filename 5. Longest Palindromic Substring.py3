class Solution:
    def longestPalindrome(self, s: str) -> str:
        

        def getIndices(index1,index2):

            while index1>=0 and index2<len(s) and s[index1]==s[index2]:
                index1-=1
                index2+=1
            
            index1+=1
            index2-=1
            return (index1,index2)
        l=0
        r=0
        for i in range(len(s)):
            i1,i2=getIndices(i,i)
            if i2-i1+1>r-l+1:
                l=i1
                r=i2
            
            i3,i4=getIndices(i,i+1)
            if i4-i3+1>r-l+1:
                l=i3
                r=i4
        
        return s[l:r+1]
