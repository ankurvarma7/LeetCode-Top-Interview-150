class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        

        def isValidBSTHelper(node):
            if node is None:
                return (float('inf'),float('-inf'),True)
            
            lstMin,lstMax,isBSTLst=isValidBSTHelper(node.left)
            rstMin,rstMax,isBSTRst=isValidBSTHelper(node.right)

            if isBSTLst and isBSTRst and node.val>lstMax and node.val<rstMin:
                return (min(node.val,lstMin,rstMin),max(node.val,lstMax,rstMax),True)
            else:
                return (min(node.val,lstMin,rstMin),max(node.val,lstMax,rstMax),False)
        
        minm,mxm,isBST=isValidBSTHelper(root)
        return isBST
