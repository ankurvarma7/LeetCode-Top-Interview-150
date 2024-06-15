class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        
        points=sorted(points,key=lambda x:x[0])
        st=points[0][0]
        en=points[0][1]
        res=0

        for i in range(1,len(points)):
            if points[i][0]<=en:
                en=min(en,points[i][1])
            else:
                res+=1
                st=points[i][0]
                en=points[i][1]

        res+=1
        return res
