class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        
        valToIndex={}

        for i,n in enumerate(inorder):
            valToIndex[n]=i
        
        def constructTree(stInorder,enInorder,inorder,stPostorder,enPostorder,postorder):
            if stInorder>enInorder or stPostorder>enPostorder:
                return None
            
            index=valToIndex[postorder[enPostorder]]
            nodeQtyLeft=index-stInorder
            nodeQtyRight=enInorder-stInorder-nodeQtyLeft

            lstStInorder=stInorder
            lstEnInorder=index-1
            lstStPostorder=stPostorder
            lstEnPostorder=stPostorder+nodeQtyLeft-1

            rstStInorder=index+1
            rstEnInorder=enInorder
            rstStPostorder=stPostorder+nodeQtyLeft
            rstEnPostorder=enPostorder-1
            root=TreeNode(postorder[enPostorder])
            root.left=constructTree(lstStInorder,lstEnInorder,inorder,lstStPostorder,lstEnPostorder,postorder)
            root.right=constructTree(rstStInorder,rstEnInorder,inorder,rstStPostorder,rstEnPostorder,postorder)
            return root
        
        n=len(inorder)
        return constructTree(0,n-1,inorder,0,n-1,postorder)
