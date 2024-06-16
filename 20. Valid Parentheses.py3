class Solution:
    def isValid(self, s: str) -> bool:
        st=[]

        def isPair(b1,b2):
            if b1=='(' and b2==')':
                return True
            if b1=='[' and b2==']':
                return True
            if b1=='{' and b2=='}':
                return True
            return False
        
        for c in s:
            if len(st)==0:
                st.append(c)
            elif isPair(st[-1],c):
                st.pop()
            else:
                st.append(c)
        
        if len(st)==0:
            return True
        
        return False
