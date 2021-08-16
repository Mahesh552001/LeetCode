class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        if n==1:
            return True
        if n==0 or n==2:
            return False
        if n%3==0:
            n//=3
        elif (n-1)%3==0:
            n=n-1
            n=n//3
        else:
            return False
        return self.checkPowersOfThree(n)