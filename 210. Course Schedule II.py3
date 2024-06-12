class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adjList=collections.defaultdict(list)
        freq=collections.defaultdict(int)

        for [a,b] in prerequisites:
            adjList[b].append(a)
            freq[a]+=1
        
        q4BFS=deque()

        for i in range(numCourses):
            if freq[i]==0:
                q4BFS.append(i)

        res=[]

        while q4BFS:
            taken=q4BFS.popleft()

            res.append(taken)
            for nei in adjList[taken]:
                freq[nei]-=1

                if freq[nei]==0:
                    q4BFS.append(nei)
        
        if len(res)==numCourses:
            return res
        
        return []
