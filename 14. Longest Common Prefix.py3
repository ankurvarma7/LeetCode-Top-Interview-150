class TrieNode:
    def __init__(self):
        self.children={}
        self.isEOW=False
        self.count=0

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        root=TrieNode()

        def insertWord(word):
            crawl=root

            for c in word:
                if c not in crawl.children:
                    crawl.children[c]=TrieNode()
                
                crawl=crawl.children[c]
                crawl.count+=1
            
            crawl.isEOW=True
        
        def solve(word):
            crawl=root
            ans=""
            for c in word:
                crawl=crawl.children[c]
                if crawl.count==len(strs):
                    ans=ans+c
                else:

                    return ans
            
            return ans

        for s in strs:
            insertWord(s)

        return solve(strs[0])
