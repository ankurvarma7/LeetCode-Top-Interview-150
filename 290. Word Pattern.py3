class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        letterToWord={}
        wordToLetter={}

        words=[]

        def getWords(s):
            i=0
            j=0

            while j<len(s):
                if s[j]!=' ':
                    j+=1
                
                else:
                    words.append(s[i:j])
                    i=j+1
                    j=i
            
            words.append(s[i:j])
        
        getWords(s)

        if len(words)!=len(pattern):
            return False
        
        for i in range(len(pattern)):
            if pattern[i] in letterToWord:
                if words[i]!=letterToWord[pattern[i]]:
                    return False
            
            if words[i] in wordToLetter:
                if pattern[i]!=wordToLetter[words[i]]:
                    return False
            
            letterToWord[pattern[i]]=words[i]
            wordToLetter[words[i]]=pattern[i]
        

        return True
