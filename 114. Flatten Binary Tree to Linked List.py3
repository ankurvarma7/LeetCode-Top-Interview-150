class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        

        def flattenHelper(node):
            if node is None:
                return node
            
            lst=node.left
            rst=node.right

            node.left=None
            node.right=flattenHelper(lst)
            curr=node
            while curr.right:
                curr=curr.right
            curr.right=flattenHelper(rst)
            return node
        
        flattenHelper(root)
