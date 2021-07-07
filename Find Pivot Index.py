class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        lsum=0
        rsum=0
        n=len(nums)
        for i in range(0,n):
            rsum+=nums[i]
        for i in range(n):
            rsum-=nums[i]
            if lsum==rsum:
                return i
            lsum+=nums[i]
        return -1

#OR

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        lsum=0
        rsum=0
        for i in nums:
            rsum+=i
        for i in range(len(nums)):
            rsum-=nums[i]
            if lsum==rsum:
                return i
            lsum+=nums[i]
        return -1