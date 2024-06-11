class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points)==1:
            return 1
        def gcd(a,b):
            if b==0:
                return a
            return gcd(b,a%b)
        
        res=2

        for i in range(len(points)):
            slopes={}
            mx=0
            for j in range(i+1,len(points)):
                ydash=points[j][1]-points[i][1]
                xdash=points[j][0]-points[i][0]
                hcf=gcd(ydash,xdash)
                ydash=ydash//hcf
                xdash=xdash//hcf
                s=str(ydash)+","+str(xdash)
                if ydash>0 and xdash<0 or ydash<0 and xdash>0:
                    s+="-"
                if s not in slopes:
                    slopes[s]=0
                
                slopes[s]+=1
                mx=max(mx,slopes[s])
            res=max(res,mx+1)
        
        return res
