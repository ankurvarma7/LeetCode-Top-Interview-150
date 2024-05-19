class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        values=[]

        def inOrder(node):
            if node is None:
                return
            
            inOrder(node.left)
            values.append(node.val)
            inOrder(node.right)

        inOrder(root)
        res=values[1]-values[0]

        for i in range(2,len(values)):
            res=min(res,values[i]-values[i-1])
        
        return res
