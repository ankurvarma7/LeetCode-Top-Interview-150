class Solution:
    def hIndex(self, citations: List[int]) -> int:
        
        def check(h):
            count=0

            for citation in citations:
                if citation>=h:
                    count+=1
            
            return count>=h
        
        l=0
        r=1000

        while l<=r:
            m=(l+r)//2

            if check(m):
                l=m+1
            else:
                r=m-1
        
        return r
