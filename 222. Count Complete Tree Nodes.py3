class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        

        def getNodeCount(node):
            if node is None:
                return 0
            
            c1=node
            c2=node
            hLeft=0
            hRight=0

            while c1:
                c1=c1.left
                hLeft+=1
            
            while c2:
                c2=c2.right
                hRight+=1
            
            if hLeft==hRight:
                return 2**hLeft-1
            else:
                return 1+getNodeCount(node.left)+getNodeCount(node.right)
        
        return getNodeCount(root)
