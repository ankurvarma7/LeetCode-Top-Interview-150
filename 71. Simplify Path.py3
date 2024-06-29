class Solution:
    def simplifyPath(self, path: str) -> str:
        def getPathName(index,n):
            st=index

            while index<n and path[index]!='/':
                index+=1
            
            return path[st:index]
        
        pathNames=[]

        i=0
        n=len(path)
        while i<n:
            if path[i]=='/':
                i+=1
            else:
                currPath=getPathName(i,n)

                if currPath=="..":
                    if len(pathNames)>0:
                        pathNames.pop()
                else:
                    if currPath!=".":
                        pathNames.append(currPath)
                
                i+=len(currPath)
        
        res="/"

        for i,pathName in enumerate(pathNames):
            res=res+pathName
            if len(pathNames)==i+1:
                break
            res+="/"
        
        return res
