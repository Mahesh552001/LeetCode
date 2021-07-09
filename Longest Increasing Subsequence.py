#Dynamic Programming Approach
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n=len(nums)
        arr=[1]*n
        for i in range(1,n):
            for j in range(0,i):
                if nums[i]>nums[j] and arr[i]<arr[j]+1:
                    arr[i]=arr[j]+1
        print(arr)
        return max(arr)

#OR

#Better Time Complexity
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        res = []
        for num in nums:
            index = bisect.bisect_left(res, num)
            if index >= len(res):
                res.append(num)
            else:
                res[index] = num
        return len(res)