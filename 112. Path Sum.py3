class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        def hasPathSumHelper(node,currSum):
            if node is None:
                return False
            if node.left is None and node.right is None:
                return currSum+node.val==targetSum
            currSum+=node.val
            return hasPathSumHelper(node.left,currSum) or hasPathSumHelper(node.right,currSum)
        
        return hasPathSumHelper(root,0)
