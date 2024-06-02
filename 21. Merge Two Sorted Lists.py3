class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        
        c1=list1
        c2=list2
        h,t= None, None
        while c1 and c2:
            if c1.val<=c2.val:
                if h is None:
                    h=c1
                    t=h
                else:
                    t.next=c1
                    t=t.next
                c1=c1.next
            else:
                if h is None:
                    h=c2
                    t=h
                else:
                    t.next=c2
                    t=t.next
                c2=c2.next
        
        if c1:
            t.next=c1
        if c2:
            t.next=c2
        
        return h
