class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res=[]

        index=0

        while index<len(words):
            st=index
            count=0
            lenSum=0

            while index<len(words):
                if len(words[index])+lenSum==maxWidth:
                    lenSum+=len(words[index])
                    count+=1
                    index+=1
                    break
                if len(words[index])+lenSum>maxWidth:
                    lenSum-=1
                    break
                
                lenSum+=(len(words[index])+1)
                count+=1
                index+=1
            
            extraspaces=maxWidth-lenSum
            extraspaceperword=extraspaces//(count-1) if count>1 else extraspaces
            residual=extraspaces%(count-1) if count>1 else 0
            s=""
            if index==len(words):
                for i in range(count):
                    s+=words[st+i]
                    if len(s)==maxWidth:
                        break
                    if i!=count-1:
                        s+=" "
                
                while len(s)<maxWidth:
                    s+=" "
            
            else:
                for i in range(count):
                    s+=words[st+i]
                    if len(s)==maxWidth:
                        break
                    if i!=count-1:
                        s+=" "
                    for sp in range(extraspaceperword):
                        s+=" "
                    if residual>0:
                        s+=" "
                        residual-=1

            res.append(s)
        
        return res
