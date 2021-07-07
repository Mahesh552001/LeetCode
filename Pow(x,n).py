class Solution:
    def myPow(self, x: float, n: int) -> float:
        temp=0
        if n==0:
            return 1.0
        if n<0:
            return self.myPow(1/x,-n)
        temp=self.myPow(x,n//2)
        if n%2==0:
            return temp*temp
        else:
            if n>0:return x*temp*temp