class Solution:
    def romanToInt(self, s: str) -> int:
        romanMap={}

        romanMap["I"]=1
        romanMap["IV"]=4
        romanMap["V"]=5
        romanMap["IX"]=9
        romanMap["X"]=10
        romanMap["XL"]=40
        romanMap["L"]=50
        romanMap["XC"]=90
        romanMap["C"]=100
        romanMap["CD"]=400
        romanMap["D"]=500
        romanMap["CM"]=900
        romanMap["M"]=1000

        res=0
        st=0
        index=0

        while index<len(s):
            if s[st:index+1] in romanMap:
                index+=1
            
            else:
                res+=romanMap[s[st:index]]
                st=index
        
        res+=romanMap[s[st:index]]
        return res
