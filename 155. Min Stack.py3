class MinStack:

    def __init__(self):
        self.st=[]
        self.minst=[]

    def push(self, val: int) -> None:
        if len(self.st)==0:
            self.st.append(val)
            self.minst.append(val)
        else:
            currMin=min(val,self.minst[-1])
            self.st.append(val)
            self.minst.append(currMin)

    def pop(self) -> None:
        self.st.pop()
        self.minst.pop()

    def top(self) -> int:
        return self.st[-1]

    def getMin(self) -> int:
        return self.minst[-1]
