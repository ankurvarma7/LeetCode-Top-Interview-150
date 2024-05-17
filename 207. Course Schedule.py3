class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList=collections.defaultdict(list)
        incedentEdges=collections.defaultdict(int)

        for a,b in prerequisites:
            adjList[b].append(a)
            incedentEdges[a]+=1
    
        completedCourses=set()
        q4BFS=deque()
        for course in range(numCourses):
            if incedentEdges[course]==0:
                q4BFS.append(course)

        
        while q4BFS:

            curr=q4BFS.popleft()
            completedCourses.add(curr)

            for nei in adjList[curr]:
                incedentEdges[nei]-=1
                if incedentEdges[nei]==0:
                    q4BFS.append(nei)
        

        return len(completedCourses)==numCourses
