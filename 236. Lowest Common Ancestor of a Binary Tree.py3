class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root is None:
            return root
        if root==p or root==q:
            return root
        
        lst=self.lowestCommonAncestor(root.left,p,q)
        rst=self.lowestCommonAncestor(root.right,p,q)

        if lst and rst:
            return root
        if lst:
            return lst
        return rst
