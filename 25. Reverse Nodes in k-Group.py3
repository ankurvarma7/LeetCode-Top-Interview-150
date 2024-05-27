class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        if k==0 or k==1:
            return head
        h=None
        curr=head

        count=0

        while curr and count<k:
            count+=1
            temp=curr
            curr=curr.next
            temp.next=h
            h=temp
        
        if count==k:
            head.next=self.reverseKGroup(curr,k)
            return h
        else:
            return self.reverseKGroup(h,count)
