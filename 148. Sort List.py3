class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        def mergeList(h1,h2):
            if h1 is None:
                return h2
            if h2 is None:
                return h1
            
            c1=h1
            c2=h2
            h,t=None,None
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
        
        def getFirstMid(h):
            if h is None or h.next is None:
                return h
            
            slow=h
            fast=h

            while fast and fast.next and fast.next.next:
                slow=slow.next
                fast=fast.next.next
            
            return slow
        
        def mergeSort(h):
            if h is None or h.next is None:
                return h
            
            midNode=getFirstMid(h)
            nextMid=midNode.next
            midNode.next=None
            h1=mergeSort(h)
            h2=mergeSort(nextMid)
            return mergeList(h1,h2)
        
        return mergeSort(head)
