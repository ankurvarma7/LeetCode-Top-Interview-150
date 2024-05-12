class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        minheap=[]
        for c,p in zip(capital,profits):
            minheap.append([c,p])
        
        heapq.heapify(minheap)
        maxheap=[]

        heapq.heapify(maxheap)
        res=w

        count=0

        while minheap and count<k:
            c,p=minheap[0]

            if c<=res:
                heapq.heappush(maxheap,[-1*p,c])
                heapq.heappop(minheap)
            elif maxheap:
                negp,cap=heapq.heappop(maxheap)
                res+=(-1*negp)
                count+=1
            else:
                break
                
            
        while maxheap and count<k:
            negp,cap=heapq.heappop(maxheap)

            res+=(-1*negp)
            count+=1
        
        return res
