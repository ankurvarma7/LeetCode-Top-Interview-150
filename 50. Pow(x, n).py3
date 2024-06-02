class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x==0:
            return float(0)
        if n==0 or x==float(1):
            return float(1)
        if n<0:
            x=1/x
            n=-1*n
        
        def powerFunction(A,N):
            if N==0:
                return float(1)
            
            halfPower=powerFunction(A,N//2)
            fullPower=halfPower*halfPower

            if N%2==1:
                fullPower=fullPower*A
            
            return fullPower
        
        return powerFunction(x,n)
