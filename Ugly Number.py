class Solution:
    def isUgly(self, n: int) -> bool:
        for i in range(2,6):
            if n>0:
                while(n%i==0):
                    n/=i
        return n==1