class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minheap=[]

        heapq.heapify(minheap)

        for num in nums:
            if len(minheap)<k:
                heapq.heappush(minheap,num)
            else:
                if num>minheap[0]:
                    heapq.heappop(minheap)
                    heapq.heappush(minheap,num)

        
        return minheap[0]
