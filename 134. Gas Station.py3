class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total=0

        for g,c in zip(gas,cost):
            total+=(g-c)
        
        if total<0:
            return -1
        
        start=0
        index=0
        curr=0
        while index<len(gas):
            if curr<0:
                curr=0
                start=index
            
            curr+=(gas[index]-cost[index])
            index+=1
        
        return start
