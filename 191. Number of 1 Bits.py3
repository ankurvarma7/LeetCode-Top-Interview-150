class Solution:
    def hammingWeight(self, n: int) -> int:
        res=0

        for i in range(31):
            if (n&(1<<i))==0:
                continue
            res+=1
        
        return res
