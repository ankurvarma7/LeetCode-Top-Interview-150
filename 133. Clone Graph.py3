class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        dp={}

        def cloneGraphHelper(n):
            if n is None:
                return None
            if n.val in dp:
                return dp[n.val]
            
            dp[n.val]=Node(n.val)

            for nei in n.neighbors:
                dp[n.val].neighbors.append(cloneGraphHelper(nei))
            
            return dp[n.val]
        
        return cloneGraphHelper(node)
