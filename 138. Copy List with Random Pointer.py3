class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return None
        
        originalToCopy={}

        curr=head
        h,t=None,None

        while curr:
            node=Node(curr.val)

            originalToCopy[curr]=node
            if h is None:
                h=node
                t=h
            else:
                t.next=node
                t=node

            curr=curr.next
        
        curr1=head
        curr2=h

        while curr1:
            if curr1.random:
                curr2.random=originalToCopy[curr1.random]
            
            curr1=curr1.next
            curr2=curr2.next
        
        return h
