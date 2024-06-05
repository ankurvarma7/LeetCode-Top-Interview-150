class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        
        freq={}

        curr=head
        while curr:
            if curr.val not in freq:
                freq[curr.val]=0
            freq[curr.val]+=1
            curr=curr.next
        
        h,t=None,None

        curr=head

        while curr:
            if freq[curr.val]==1:
                if h is None:
                    h=curr
                    t=h
                else:
                    t.next=curr
                    t=curr
            curr=curr.next
        if t:
            t.next=None
        return h
