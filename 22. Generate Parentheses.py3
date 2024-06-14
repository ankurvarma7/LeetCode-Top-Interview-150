class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res=[]
        curr=[]

        def isValid(brackets):
            st=[]

            for c in brackets:
                l=len(st)
                if l==0:
                    st.append(c)
                elif st[l-1]=='(' and c==')':
                    st.pop()
                else:
                    st.append(c)
            
            if len(st)==0:
                return True
            return False

        def getString(arr):
            s=""

            for c in arr:
                s+=c
            
            return s
        
        def generate(index):
            if index==2*n:
                if isValid(curr):
                    res.append(getString(curr))
                return
            
            curr.append('(')
            generate(index+1)

            curr.pop()

            curr.append(')')
            generate(index+1)

            curr.pop()
        
        generate(0)
        return res
