class Solution:
    def intToRoman(self, num: int) -> str:
        romanPair=[(1000,"M"),(900,"CM"),(500,"D"),(400,"CD"),(100,"C"),(90,"XC"),(50,"L"),(40,"XL"),(10,"X"),(9,"IX"),(5,"V"),(4,"IV"),(1,"I")]

        index=0
        res=""
        while num>0:
            n,rom=romanPair[index]
            
            if num/n>=1:
                num=num-n
                res+=rom
            else:
                index+=1
            
        return res
