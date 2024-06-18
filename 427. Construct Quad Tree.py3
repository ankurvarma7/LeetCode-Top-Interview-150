class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        
        def isLeaf(x,y,n):
            val=grid[x][y]
            for i in range(n):
                for j in range(n):
                    if grid[x+i][y+j]!=val:
                        return False
            
            return True
        
        def constructQuadTree(x,y,n):
            if n==0:
                return None
            elif isLeaf(x,y,n):
                node=Node(grid[x][y]==1,True,None,None,None,None)
                return node
            else:
                topLeft=constructQuadTree(x,y,n//2)
                topRight=constructQuadTree(x,y+n//2,n//2)
                bottomLeft=constructQuadTree(x+n//2,y,n//2)
                bottomRight=constructQuadTree(x+n//2,y+n//2,n//2)
                node=Node(False,False,topLeft,topRight,bottomLeft,bottomRight)
                return node
        
        return constructQuadTree(0,0,len(grid))
