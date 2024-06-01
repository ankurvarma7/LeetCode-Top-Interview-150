class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        

        def constructBST(l,r):
            if l>r:
                return None
            
            mid=(l+r)//2

            root=TreeNode(nums[mid])
            root.left=constructBST(l,mid-1)
            root.right=constructBST(mid+1,r)

            return root
        
        return constructBST(0,len(nums)-1)
