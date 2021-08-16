class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n==0:
            return False
        if (n & (n-1))==0:
            count=0
            while(n>1):
                n>>=1
                count+=1
            if count%2==0:
                return True
        return False