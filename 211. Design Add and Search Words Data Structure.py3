class TrieNode:
    def __init__(self):
        self.children={}
        self.isEOW=False
class WordDictionary:

    def __init__(self):
        self.root=TrieNode()

    def addWord(self, word: str) -> None:
        crawl=self.root

        for c in word:
            if c not in crawl.children:
                crawl.children[c]=TrieNode()
            crawl=crawl.children[c]
        
        crawl.isEOW=True


    def search(self, word: str) -> bool:
        
        def searchHelper(index,crawl):
            if index==len(word):
                return crawl.isEOW
            
            if word[index]=='.':
                for c in crawl.children:
                    if(searchHelper(index+1,crawl.children[c])):
                        return True
                
                return False
            else:
                if word[index] not in crawl.children:
                    return False
                return searchHelper(index+1,crawl.children[word[index]])
        
        return searchHelper(0,self.root)
