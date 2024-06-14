class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        freqRansom={}
        freqMagazine={}

        for c in ransomNote:
            if c not in freqRansom:
                freqRansom[c]=0
            
            freqRansom[c]+=1
        
        for c in magazine:
            if c not in freqMagazine:
                freqMagazine[c]=0
            
            freqMagazine[c]+=1
        
        for c in ransomNote:
            if c not in freqMagazine:
                return False
            
            if freqRansom[c]>freqMagazine[c]:
                return False
            
        return True
