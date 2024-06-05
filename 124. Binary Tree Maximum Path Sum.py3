class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        

        def maxPathSumHelper(root):
            if root is None:
                return (0,float('-inf'))
            
            lstPathSum,lstMaxSum=maxPathSumHelper(root.left)
            rstPathSum,rstMaxSum=maxPathSumHelper(root.right)

            currPathSum=max(root.val,root.val+lstPathSum,root.val+rstPathSum)
            maxSum=max(currPathSum,lstMaxSum,rstMaxSum,root.val+lstPathSum+rstPathSum)
            return (currPathSum,maxSum)
        
        pathSum,maxSum=maxPathSumHelper(root)
        return maxSum
