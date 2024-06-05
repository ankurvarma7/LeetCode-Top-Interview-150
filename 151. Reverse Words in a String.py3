class Solution:
    def reverseWords(self, s: str) -> str:

        n=len(s)

        i=0
        j=n-1

        while i<n and s[i]==' ':
            i+=1
        
        while j>=0 and s[j]==' ':
            j-=1
        

        st=i
        en=st
        res=""
        while en<=j:
            if s[en]!=' ':
                en+=1
            else:
                res=s[st:en]+" "+res
                
                while en<=j and s[en]==' ':
                    en+=1
                
                st=en

        res=s[st:en]+" "+res
        r=len(res)
        return res[0:r-1]
