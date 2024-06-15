class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adjList={}

        for i in range(len(equations)):
            if equations[i][0] not in adjList:
                adjList[equations[i][0]]={}
            
            adjList[equations[i][0]][equations[i][1]]=values[i]

            if equations[i][1] not in adjList:
                adjList[equations[i][1]]={}
            
            adjList[equations[i][1]][equations[i][0]]=1/values[i]

        def dfs(st,end,curr,visited):
            if st in visited:
                return float(-1)
            visited.add(st)
            if st not in adjList:
                return float(-1)
            
            if st==end:
                return curr
            
            for nei in adjList[st]:
                res=dfs(nei,end,curr*adjList[st][nei],visited)
                if res!=float(-1):
                    return res

            return float(-1)

        ans=[]

        for query in queries:
            visited=set()
            ans.append(dfs(query[0],query[1],1,visited))
        
        return ans
