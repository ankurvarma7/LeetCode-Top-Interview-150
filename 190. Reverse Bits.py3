class Solution:
    def reverseBits(self, n: int) -> int:
        
        def checkBit(A,pos):
            if (A&(1<<pos))==0:
                return False
            return True
        
        def setBit(A,pos):
            return A|(1<<pos)
        
        res=0

        for i in range(32):
            if checkBit(n,i):
                res=setBit(res,32-i-1)
        
        return res
