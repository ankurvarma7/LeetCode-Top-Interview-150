class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        def solve(indexS,indexT):
            if indexS<0:
                return True
            
            if indexT<0:
                return False
            
            res=False
            if s[indexS]==t[indexT]:
                res=solve(indexS-1,indexT-1)
            
            else:
                res=solve(indexS,indexT-1)
            
            return res
        
        return solve(len(s)-1,len(t)-1)
