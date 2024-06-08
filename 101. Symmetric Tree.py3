class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return root
        
        def isSame(node1,node2):
            if node1 is None and node2 is None:
                return True
            if node1 is None:
                return False
            if node2 is None:
                return False
            if node1.val==node2.val:
                return True
            return False
        
        q4BFS1=deque()
        q4BFS2=deque()
        if root.left:
            q4BFS1.append(root.left)
        if root.right:
            q4BFS2.append(root.right)

        while q4BFS1 and q4BFS2:
            n1=q4BFS1.popleft()
            n2=q4BFS2.popleft()

            if isSame(n1,n2) and isSame(n1.right,n2.left) and isSame(n1.left,n2.right):
                if n1.right:
                    q4BFS1.append(n1.right)
                if n1.left:
                    q4BFS1.append(n1.left)
                if n2.left:
                    q4BFS2.append(n2.left)
                if n2.right:
                    q4BFS2.append(n2.right)

            else:
                return False
            
        if q4BFS1:
            return False
        if q4BFS2:
            return False
        
        return True
