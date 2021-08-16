class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n=len(nums)
        expected=(n*(n+1))//2
        actual=0
        d={}
        for i in range(n):
            if nums[i] in d:
                duplicate=nums[i]
            d[nums[i]]=None
            actual+=nums[i]
        return[duplicate,expected-actual+duplicate]