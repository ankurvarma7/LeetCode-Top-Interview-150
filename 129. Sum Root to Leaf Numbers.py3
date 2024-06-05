class TreeInfo:
    def __init__(self,sum=0):
        self.sum=sum
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        info=TreeInfo()
        def sumNumbersHelper(node,curr):
            if node is None:
                return
            if node.left is None and node.right is None:
                info.sum+=curr*10+node.val
                return
            sumNumbersHelper(node.left,curr*10+node.val)
            sumNumbersHelper(node.right,curr*10+node.val)
        
        sumNumbersHelper(root,0)
        return info.sum
