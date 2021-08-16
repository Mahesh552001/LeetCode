class Solution:
    def guessNumber(self, n: int) -> int:
        start=1
        end=n
        while(start<=end):
            mid=(start+end)//2
            print(mid,guess(mid))
            if guess(mid)==0:
                return mid
            if guess(mid)==1:
                start=mid+1
            else:
                end=mid-1