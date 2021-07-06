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