class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        curr=[]
        res=[]

        def getCombinations(num):
            
            if len(curr)==k:
                res.append(curr.copy())
                return
            if num>n:
                return
            
            curr.append(num)
            getCombinations(num+1)

            curr.pop()
            getCombinations(num+1)
        getCombinations(1)
        return res
