class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head is None:
            return head
        dummy=ListNode()

        dummy.next=head
        first=dummy
        second=dummy

        for i in range(n+1):
            first=first.next
        

        while first:
            first=first.next
            second=second.next
        
        second.next=second.next.next
    
        return dummy.next
