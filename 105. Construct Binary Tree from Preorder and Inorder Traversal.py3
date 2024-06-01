class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        valIndex={}

        for i,n in enumerate(inorder):

            valIndex[n]=i
        
        def constructTree(stPreorder,enPreorder,preorder,stInorder,enInorder,inorder):
            if stPreorder>enPreorder or stInorder>enInorder:
                return None
            
            numOfNodeLst=valIndex[preorder[stPreorder]]-stInorder
            
            lstStPreorder=stPreorder+1
            lstEnPreorder=stPreorder+numOfNodeLst
            lstStInorder=stInorder
            lstEnInorder=stInorder+numOfNodeLst-1

            rstStPreorder=lstEnPreorder+1
            rstEnPreorder=enPreorder
            rstStInorder=valIndex[preorder[stPreorder]]+1
            rstEnInorder=enInorder

            root=TreeNode(preorder[stPreorder])

            root.left=constructTree(lstStPreorder,lstEnPreorder,preorder,lstStInorder,lstEnInorder,inorder)
            root.right=constructTree(rstStPreorder,rstEnPreorder,preorder,rstStInorder,rstEnInorder,inorder)
            return root
        
        return constructTree(0,len(inorder)-1,preorder,0,len(inorder)-1,inorder)
