class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        i=0
        j=0

        freq={}
        res=0
        while j<len(s):
            if s[j] not in freq:
                freq[s[j]]=0
            freq[s[j]]+=1

            while i<j and freq[s[j]]>1:
                freq[s[i]]-=1
                i+=1
            
            res=max(res,j-i+1)
            j+=1
        
        return res
