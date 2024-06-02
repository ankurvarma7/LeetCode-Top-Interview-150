class Solution:
    def minWindow(self, s: str, t: str) -> str:
        freqT={}

        for c in t:
            if c not in freqT:
                freqT[c]=0
            freqT[c]+=1
        
        matched=0
        freqS={}
        i=0
        j=0
        l=0
        r=len(s)
        while j<len(s):
            if s[j] not in freqS:
                freqS[s[j]]=0
            freqS[s[j]]+=1

            if s[j] in freqT and freqS[s[j]]==freqT[s[j]]:
                matched+=1
            
            while i<len(s) and matched==len(freqT):
                if j-i<r-l:
                    l=i
                    r=j
                
                freqS[s[i]]-=1
                if s[i] in freqT and freqS[s[i]]<freqT[s[i]]:
                    matched-=1
                
                i+=1
            
            j+=1
        
        if r-l+1>len(s):
            return ""
        return s[l:r+1]
