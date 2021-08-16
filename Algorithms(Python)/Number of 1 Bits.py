class Solution:
    def hammingWeight(self, n: int) -> int:
        ans=0
        mask=1
        for i in range(32):
            if n&mask!=0:
                ans+=1
            mask<<=1
        return ans

#OR

#BRIAN ALGORITHM
class Solution:
    def hammingWeight(self, n: int) -> int:
        ans=0
        while(n>0):
            n&=n-1
            ans+=1
        return ans