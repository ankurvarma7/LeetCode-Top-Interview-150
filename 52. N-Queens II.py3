class Solution:
    def totalNQueens(self, n: int) -> int:
        col=set()
        majorDiag=set()
        minorDiag=set()
        
        def isSafe(r,c):
            if c in col:
                return False
            
            if (r-c) in majorDiag:
                return False
            
            if (r+c) in minorDiag:
                return False

            return True
        
        def placeQueen(r,c):
            col.add(c)
            majorDiag.add((r-c))
            minorDiag.add((r+c))
        
        def removeQueen(r,c):
            col.remove(c)
            majorDiag.remove((r-c))
            minorDiag.remove((r+c))
        
        
        def solve(r):
            if r==n:
                return 1
            
            res=0
            for c in range(n):
                if isSafe(r,c):
                    placeQueen(r,c)
                    res+=solve(r+1)
                    removeQueen(r,c)
            
            return res
        
        return solve(0)
