class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        n=len(nums)
        start=0
        end=n-2
        while(start<=end):
            mid=(start+end)//2
            if mid%2==0:
                if nums[mid]==nums[mid+1]:
                    start=mid+1
                else:
                    end=mid-1
            else:
                if nums[mid]==nums[mid-1]:
                    start=mid+1
                else:
                    end=mid-1
        return nums[start]

#OR

#even_num^1 = even_num+1
#odd_num^1 = odd_num-1

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        n=len(nums)
        start=0
        end=n-2
        while(start<=end):
            mid=(start+end)//2
            if nums[mid]==nums[mid^1]:
                start=mid+1
            else:
                end=mid-1
        return nums[start]