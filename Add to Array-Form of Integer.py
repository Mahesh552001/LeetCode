class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        j=0
        for i in num:
            j=j*10+i
        a=str(j+k)
        ans=list(a)
        return list(map(int,ans))
            
        