class Solution:
    def trailingZeroes(self, n: int) -> int:
        res=0
        p=5
        while True:
            quo=n//p
            if quo==0:
                break
            res+=quo
            p=p*5
        
        return res
