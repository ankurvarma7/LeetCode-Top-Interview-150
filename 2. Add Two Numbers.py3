class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry=0

        curr1=l1
        curr2=l2
        h,t=None,None
        while curr1 and curr2:
            digit=curr1.val+curr2.val+carry

            node=ListNode(digit%10)

            if h is None:
                h=node
                t=h
            else:
                t.next=node
                t=node
            
            carry=digit//10
            curr1=curr1.next
            curr2=curr2.next
        
        while curr1:
            digit=curr1.val+carry

            node=ListNode(digit%10)

            if h is None:
                h=node
                t=h
            else:
                t.next=node
                t=node
            carry=digit//10
            curr1=curr1.next
        
        while curr2:
            digit=curr2.val+carry

            node=ListNode(digit%10)

            if h is None:
                h=node
                t=h
            else:
                t.next=node
                t=node
            carry=digit//10
            curr2=curr2.next
        
        while carry>0:
            node=ListNode(carry%10)

            if h is None:
                h=node
                t=h
            else:
                t.next=node
                t=node
            
            carry=carry//10
        
        return h
