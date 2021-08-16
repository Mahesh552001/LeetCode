class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n=len(nums)
        for i in range(n):
            print(nums[i])
            if nums[abs(nums[i])-1]>=0:
                nums[abs(nums[i])-1]=-nums[abs(nums[i])-1]
        result=[]
        for i in range(n):
            if nums[i]>0:
                result.append(i+1)
        return result

#OR

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        res=[]
        n=len(nums)
        arr=[0]*(n+1)
        for x in nums:
            arr[x]+=1
        for i in range(1,n+1):
            if arr[i]==0:
                res.append(i)
        return res