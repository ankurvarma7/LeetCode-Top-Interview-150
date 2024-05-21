class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        

        def invertTreeHelper(node):
            if node is None:
                return
            
            lst=node.left
            rst=node.right
            node.left=rst
            node.right=lst
            invertTreeHelper(node.left)
            invertTreeHelper(node.right)
        
        invertTreeHelper(root)
        return root
