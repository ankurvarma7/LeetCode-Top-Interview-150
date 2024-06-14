class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return root
        def reverse(arr):
            i=0
            j=len(arr)-1

            while i<j:
                temp=arr[i]
                arr[i]=arr[j]
                arr[j]=temp
                i+=1
                j-=1
    
        q4BFS=deque()
        q4BFS.append(root)
        res=[]
        level=0

        while q4BFS:
            n=len(q4BFS)
            curr=[]
            for i in range(n):
                node=q4BFS.popleft()
                curr.append(node.val)

                if node.left:
                    q4BFS.append(node.left)
                if node.right:
                    q4BFS.append(node.right)
                
            if level%2==1:
                reverse(curr)
            
            res.append(curr)
            level+=1
        
        return res
