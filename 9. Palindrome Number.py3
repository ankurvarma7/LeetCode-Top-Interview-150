class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        if x<0:
            return False
        
        num=x
        reverseNum=0

        while num>0:
            reverseNum=reverseNum*10+num%10
            num=num//10
        
        return reverseNum==x
