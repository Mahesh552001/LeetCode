class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d={}
        for i in range(len(nums)):
            element=target-nums[i]
            if element in d:
                return d[element],i
            d[nums[i]]=i