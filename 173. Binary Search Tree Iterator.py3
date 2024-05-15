class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.curr=root
        self.st=[]

    def next(self) -> int:
        while self.curr:
            self.st.append(self.curr)
            self.curr=self.curr.left

        temp=self.st.pop()
        self.curr=temp.right
        return temp.val
        

    def hasNext(self) -> bool:
        if self.curr or len(self.st)>0:
            return True
        
        return False
