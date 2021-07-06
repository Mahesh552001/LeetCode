class Solution:
    def countPrimes(self, n: int) -> int:
        if n==0 or n==1:
            return 0
        isPrime=[True for i in range(n)]
        i=2
        while(i*i<=n):
            if isPrime[i]:
                for j in range(i+i,n,i):
                    isPrime[j]=False
            i+=1
        count=0
        for i in range(2,n):
            if isPrime[i]:
                count+=1
        return count