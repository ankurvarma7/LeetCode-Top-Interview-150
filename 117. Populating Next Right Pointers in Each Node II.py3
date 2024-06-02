class Solution:
    def connect(self, root: 'Node') -> 'Node':
        

        def getNextNode(node):
            if node is None:
                return None
            elif node.left:
                return node.left
            elif node.right:
                return node.right
            else:
                return getNextNode(node.next)
        
        def connectHelper(node):
            if node is None:
                return
            
            if node.left:
                if node.right:
                    node.left.next=node.right
                else:
                    node.left.next=getNextNode(node.next)
            if node.right:
                node.right.next=getNextNode(node.next)
            
            connectHelper(node.next)
        
        curr=root
        while curr:
            connectHelper(curr)

            if curr.left:
                curr=curr.left
            elif curr.right:
                curr=curr.right
            else:
                curr=getNextNode(curr.next)
        return root
