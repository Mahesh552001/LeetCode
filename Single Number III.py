class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        arr=[]
        for i in nums:
            if i in arr:
                arr.remove(i)
            else:
                arr.append(i)
        return arr