class DoublyLL:
    def __init__(self,key=0,val=0,next=None,prev=None):
        self.key=key
        self.val=val
        self.next=next
        self.prev=prev
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity=capacity
        self.keyNode={}
        self.head=DoublyLL()
        self.tail=DoublyLL()
        self.head.next=self.tail
        self.tail.prev=self.head

    def get(self, key: int) -> int:
        if key in self.keyNode:
            n=self.keyNode[key]
            self.delNode(n)
            self.addNode(n)
            return n.val
        return -1

    def put(self, key: int, value: int) -> None:
        node=DoublyLL(key,value)
        if key in self.keyNode:
            self.delNode(self.keyNode[key])
            self.addNode(node)
            self.keyNode[key]=node
        elif len(self.keyNode)<self.capacity:
            self.addNode(node)
            self.keyNode[key]=node
        else:
            temp=self.head.next
            self.keyNode.pop(temp.key)
            self.delNode(temp)
            self.addNode(node)
            self.keyNode[key]=node
    
    def addNode(self,node):
        self.tail.prev.next=node
        node.prev=self.tail.prev
        node.next=self.tail
        self.tail.prev=node

    def delNode(self,node):
        node.prev.next=node.next
        node.next.prev=node.prev
