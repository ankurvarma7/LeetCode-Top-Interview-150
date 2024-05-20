class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freqS={}
        freqT={}

        for c in s:
            if c not in freqS:
                freqS[c]=0
            
            freqS[c]+=1

        for c in t:
            if c not in freqT:
                freqT[c]=0
            
            freqT[c]+=1

        for c in freqS:
            if c not in freqT:
                return False
            
            if freqS[c]!=freqT[c]:
                return False
        
        for c in freqT:
            if c not in freqS:
                return False
            
            if freqT[c]!=freqS[c]:
                return False
        
        return True
