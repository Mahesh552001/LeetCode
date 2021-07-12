#O(log n)
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        beg=0
        end=len(nums)-1
        while(beg<=end):
            mid=(beg+end)//2
            if nums[mid]==target:
                return mid
            if nums[mid]<target:
                beg=mid+1
            else:
                end=mid-1

        return beg


#O(n)
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i in range(len(nums)):
            if nums[i]>=target:
                return i
        return i+1