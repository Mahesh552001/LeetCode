#for better time complexity
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d={}
        for i in range(len(nums)):
            element=target-nums[i]
            if element in d:
                return d[element],i
            d[nums[i]]=i

#OR

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            element=target-nums[i]
            if element in nums[i+1:]:
                temp=nums[i+1:]
                return i,temp.index(element)+i+1
                
#OR

#for better understanding
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            element=target-nums[i]
            for j in range(i+1,len(nums)):
                if nums[j]==element:
                    return i,j