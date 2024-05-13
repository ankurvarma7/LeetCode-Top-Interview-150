class RandomizedSet:

    def __init__(self):
        self.valIndex={}
        self.elements=[]
        self.lastIndex=-1

    def insert(self, val: int) -> bool:
        if val in self.valIndex:
            return False
        
        self.lastIndex+=1
        self.valIndex[val]=self.lastIndex
        self.elements.append(0)
        self.elements[self.lastIndex]=val
        return True

    def remove(self, val: int) -> bool:
        if val in self.valIndex:
            index=self.valIndex[val]
            temp=self.elements[index]
            self.elements[index]=self.elements[self.lastIndex]
            self.elements[self.lastIndex]=temp
            self.valIndex[self.elements[index]]=index
            self.lastIndex-=1
            self.valIndex.pop(val)
            return True
        
        return False

    def getRandom(self) -> int:
        return self.elements[random.randint(0,self.lastIndex)]
