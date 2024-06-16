class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:

        ROWS,COLS=len(board),len(board[0])

        def isValid(r,c):
            if r<0 or r>=ROWS or c<0 or c>=COLS:
                return False
            return True
        
        def getNeighbors(r,c):
            dirx=[-1,0,1,0,-1,-1,1,1]
            diry=[0,1,0,-1,-1,1,1,-1]
            neighbors=0
            for i in range(8):
                x=r+dirx[i]
                y=c+diry[i]

                if isValid(x,y):
                    neighbors+= (board[x][y]%2)
                
            return neighbors
        
        for r in range(ROWS):
            for c in range(COLS):
                neighbors=getNeighbors(r,c)
                if board[r][c]==1 and (neighbors<2 or neighbors>3):
                    board[r][c]=1
                elif board[r][c]==1 and (2<=neighbors<=3):
                    board[r][c]=3
                elif board[r][c]==0 and neighbors==3:
                    board[r][c]=2                    
        
        for r in range(ROWS):
            for c in range(COLS):
                board[r][c]=board[r][c]//2
