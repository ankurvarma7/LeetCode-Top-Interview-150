class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        q4BFS=deque()
        q4BFS.append(root)
        res=[]

        while q4BFS:
            s=0
            count=len(q4BFS)

            for i in range(count):
                node=q4BFS.popleft()
                s+=node.val

                if node.left:
                    q4BFS.append(node.left)
                if node.right:
                    q4BFS.append(node.right)
            
            res.append(s/count)
        
        return res
