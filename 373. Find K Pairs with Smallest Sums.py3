class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        minheap=[]
        placed=set()
        heapq.heapify(minheap)
        res=[]
        heapq.heappush(minheap,[nums1[0]+nums2[0],0,0])
        placed.add((0,0))
        while len(res)<k:
            add,index1,index2=heapq.heappop(minheap)
            res.append([nums1[index1],nums2[index2]])
            if index1+1<len(nums1) and (index1+1,index2) not in placed:
                heapq.heappush(minheap,[nums1[index1+1]+nums2[index2],index1+1,index2])
                placed.add((index1+1,index2))
            if index2+1<len(nums2) and (index1,index2+1) not in placed:
                heapq.heappush(minheap,[nums1[index1]+nums2[index2+1],index1,index2+1])
                placed.add((index1,index2+1))
        
        return res
