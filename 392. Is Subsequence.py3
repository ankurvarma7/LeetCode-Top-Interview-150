class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        dp={}
        def solve(indexS,indexT):
            if indexS<0:
                return True
            
            if indexT<0:
                return False
            
            if (indexS,indexT) in dp:
                return dp[(indexS,indexT)]
            
            res=False
            if s[indexS]==t[indexT]:
                res=solve(indexS-1,indexT-1)
            
            else:
                res=solve(indexS,indexT-1)
            
            dp[(indexS,indexT)]=res
            return res
        
        return solve(len(s)-1,len(t)-1)
