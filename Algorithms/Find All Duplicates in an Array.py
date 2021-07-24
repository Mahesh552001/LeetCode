class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        n=len(nums)
        arr=[0]*(n+1)
        for i in range(n):
            arr[nums[i]]+=1
        result=[]
        for i in range(1,n+1):
            if arr[i]==2:
                result.append(i)
        return result