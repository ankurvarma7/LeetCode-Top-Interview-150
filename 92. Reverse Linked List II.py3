class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        if left==right:
            return head
        currPos=1
        curr=head
        prev=None

        while currPos<left:
            prev=curr
            curr=curr.next
            currPos+=1
        
        h=None
        t=curr
        while currPos<=right:
            temp=curr
            curr=curr.next
            currPos+=1
            temp.next=h
            h=temp
        
        if prev:
            prev.next=h
        if t:
            t.next=curr
        
        if left==1:
            return h
        return head
