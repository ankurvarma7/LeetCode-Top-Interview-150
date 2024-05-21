class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows=[]
        cols=[]
        blocks=[]

        for i in range(9):
            r=set()
            rows.append(r)
            c=set()
            cols.append(c)
            b=set()
            blocks.append(b)
        
        for x in range(9):
            for y in range(9):
                blockIndex=((x//3) *3) +y//3
                if board[x][y]==".":
                    continue
                if board[x][y] in rows[x] or board[x][y] in cols[y] or board[x][y] in blocks[blockIndex]:
                    return False
                rows[x].add(board[x][y])
                cols[y].add(board[x][y])
                blocks[blockIndex].add(board[x][y])
        
        return True
