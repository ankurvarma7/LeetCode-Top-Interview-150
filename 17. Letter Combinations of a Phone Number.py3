class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits)==0:
            return []
        res=[]
        curr=[]

        digToChars={}
        digToChars['2']="abc"
        digToChars['3']="def"
        digToChars['4']="ghi"
        digToChars['5']="jkl"
        digToChars['6']="mno"
        digToChars['7']="pqrs"
        digToChars['8']="tuv"
        digToChars['9']="wxyz"


        def getString(charArr):
            s=""

            for c in charArr:
                s+=c
            
            return s
        
        def solve(index):
            if index==len(digits):
                res.append(getString(curr))
                return
            
            for c in digToChars[digits[index]]:
                curr.append(c)
                solve(index+1)
                curr.pop()
        
        solve(0)
        return res
