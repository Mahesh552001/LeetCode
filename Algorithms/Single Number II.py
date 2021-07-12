class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        d={}
        ans=0
        for i in nums:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
            if d[i]<3:
                ans^=i
        return ans