class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        

        def getLPS(s):
            lps=[0 for i in range(len(s))]

            for i in range(1,len(s)):
                x=lps[i-1]

                while s[x]!=s[i]:
                    if x==0:
                        x=-1
                        break
                    
                    x=lps[x-1]
                
                lps[i]=x+1
            
            return lps

        s=needle+"@"+haystack
        lps=getLPS(s)

        for i in range(len(lps)):
            if lps[i]==len(needle):
                return i-2*len(needle)
        
        return -1
