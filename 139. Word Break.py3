class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        setdict=set()
        for word in wordDict:
            setdict.add(word)
        
        dp={}

        def dfs(index):
            if index==len(s):
                return True
            
            if index in dp:
                return dp[index]
            
            for i in range(20):
                if index+i+1>len(s):
                    dp[index]=False
                    return False
                if s[index:index+i+1] in setdict and dfs(index+i+1):
                    dp[index]=True
                    return True
            
            dp[index]=False
            return False

        return dfs(0)
