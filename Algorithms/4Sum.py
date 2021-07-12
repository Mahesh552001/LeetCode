class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n=len(nums)
        result=[]
        for i in range(n):
            if (i==0 or nums[i]!=nums[i-1]):
                for j in range(i+1,n):
                    l=j+1
                    r=n-1
                    if (j==i+1 or nums[j]!=nums[j-1]):
                        while(l<r):
                            s=nums[i]+nums[j]+nums[l]+nums[r]
                            if s<target:
                                l+=1
                            elif s>target:
                                r-=1
                            else:
                                result.append([nums[i],nums[j],nums[l],nums[r]])
                                while(l<r and nums[l]==nums[l+1]):
                                    l+=1
                                while(l<r and nums[r]==nums[r-1]):
                                    r-=1
                                l+=1
                                r-=1           
        return result             
        