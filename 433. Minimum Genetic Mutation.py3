class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        def isNeighbor(u,v):
            count=0

            for c1,c2 in zip(u,v):
                if c1!=c2:
                    count+=1
                if count>1:
                    return False
            
            return count==1
        
        q4BFS=deque()
        visited=set()
        q4BFS.append((startGene,0))
        
        while q4BFS:
            currGene,mutations=q4BFS.popleft()

            if currGene==endGene:
                return mutations
            
            for i in range(len(bank)):
                if i in visited:
                    continue
                if isNeighbor(currGene,bank[i]):
                    q4BFS.append((bank[i],mutations+1))
                    visited.add(i)
        
        return -1
