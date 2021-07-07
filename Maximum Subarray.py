class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current=0
        final=nums[0]
        for i in range(len(nums)):
            current= max(nums[i],nums[i]+current)
            final=max(current,final)
        return final