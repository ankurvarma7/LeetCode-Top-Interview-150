class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]
        curr=[]
        currSum=0
        def solve(index,currSum):
            if index>=len(candidates):
                return
            if currSum==target:
                res.append(curr.copy())
                return
            
            solve(index+1,currSum)

            if candidates[index]<=target-currSum:
                curr.append(candidates[index])
                solve(index,currSum+candidates[index])
                curr.pop()
        
        solve(0,0)
        return res
