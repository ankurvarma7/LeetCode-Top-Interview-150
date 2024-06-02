class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry=0
        pA=len(a)-1
        pB=len(b)-1

        res=""
        while pA>=0 and pB>=0:
            bitA=0
            bitB=0
            if a[pA]=='1':
                bitA=1
            if b[pB]=='1':
                bitB=1

            sumOfBits=bitA+bitB+carry

            if sumOfBits%2==0:
                res="0"+res
            else:
                res="1"+res
            
            carry=sumOfBits//2
            pA-=1
            pB-=1
        
        while pA>=0:
            bitA=0
            if a[pA]=='1':
                bitA=1

            sumOfBits=bitA+carry

            if sumOfBits%2==0:
                res="0"+res
            else:
                res="1"+res
            
            carry=sumOfBits//2
            pA-=1
        
        while pB>=0:
            bitB=0
            if b[pB]=='1':
                bitB=1

            sumOfBits=bitB+carry

            if sumOfBits%2==0:
                res="0"+res
            else:
                res="1"+res
            
            carry=sumOfBits//2
            pB-=1
        
        while carry>0:
            if carry%2==0:
                res="0"+res
            else:
                res="1"+res
            
            carry=carry//2
        
        return res
