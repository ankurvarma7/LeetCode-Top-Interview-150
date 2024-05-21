class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1)+len(s2) != len(s3):
            return False
        
        dp={}

        def isInterleaveHelper(index1,index2):
            if index1 == len(s1) and index2 == len(s2):
                return True
            
            if index1 == len(s1):
                while index2<len(s2):
                    if s3[index1+index2]!=s2[index2]:
                        return False
                    index2+=1
                
                return True
            if index2 == len(s2):
                while index1<len(s1):
                    if s3[index1+index2]!=s1[index1]:
                        return False
                    index1+=1
                
                return True
            
            if (index1,index2) in dp:
                return dp[(index1,index2)]
            
            if s3[index1+index2]==s1[index1] and s3[index1+index2]==s2[index2]:
                dp[(index1,index2)]=isInterleaveHelper(index1+1,index2) or isInterleaveHelper(index1,index2+1)
            
            elif s3[index1+index2]==s1[index1]:
                dp[(index1,index2)]=isInterleaveHelper(index1+1,index2)
            elif s3[index1+index2]==s2[index2]:
                dp[(index1,index2)]=isInterleaveHelper(index1,index2+1)
            else:
                dp[(index1,index2)]=False
            
            return dp[(index1,index2)]
        
        return isInterleaveHelper(0,0)
