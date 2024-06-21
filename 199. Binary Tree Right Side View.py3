class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return root
        q4BFS=deque()

        q4BFS.append(root)
        res=[]
        while q4BFS:
            currLevel=[]

            sz=len(q4BFS)

            for i in range(sz):
                currNode=q4BFS.popleft()
                currLevel.append(currNode.val)

                if currNode.left:
                    q4BFS.append(currNode.left)
                if currNode.right:
                    q4BFS.append(currNode.right)

            res.append(currLevel[-1])

        return res
