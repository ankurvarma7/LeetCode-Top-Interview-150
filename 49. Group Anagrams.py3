class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams=collections.defaultdict(list)

        def getKey(s):
            freq=collections.defaultdict(int)

            for c in s:
                freq[c]+=1
            
            key=""
            for i in range(26):
                c=chr(i+ord('a'))
                key=key+c+","+str(freq[c])+","
            return key

        for s in strs:
            anagrams[getKey(s)].append(s)
        
        res=[]

        for key in anagrams:
            res.append(anagrams[key])

        return res
