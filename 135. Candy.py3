class Solution:
    def candy(self, ratings: List[int]) -> int:
        if len(ratings)==1:
            return 1
        distLR=[1 for i in range(len(ratings))]
        distRL=[1 for i in range(len(ratings))]

        for i in range(1,len(ratings)):
            if ratings[i]>ratings[i-1]:
                distLR[i]=distLR[i-1]+1

        for i in range(len(ratings)-2,-1,-1):
            if ratings[i]>ratings[i+1]:
                distRL[i]=distRL[i+1]+1
        
        res=0

        for c1,c2 in zip(distLR,distRL):
            res+=max(c1,c2)
        
        return res
