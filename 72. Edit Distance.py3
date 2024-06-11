class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp={}

        def dfs(index1,index2):
            if index1<0 and index2<0:
                return 0
            if index1<0:
                return index2+1
            if index2<0:
                return index1+1

            if (index1,index2) in dp:
                return dp[(index1,index2)]
            
            if word1[index1]==word2[index2]:
                dp[(index1,index2)]=dfs(index1-1,index2-1)
            else:
                dp[(index1,index2)]=min(1+dfs(index1,index2-1),1+dfs(index1-1,index2),1+dfs(index1-1,index2-1))
            return dp[(index1,index2)]
        return dfs(len(word1)-1,len(word2)-1)
