class Solution:
    def isHappy(self, n: int) -> bool:
        hashtable={}
        while(n!=1):
            temp=0
            while(n>0):
                temp+=(n%10)**2
                n//=10
            if temp in hashtable:
                return False
            hashtable[temp]=None
            n=temp
        return True