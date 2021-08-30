    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        ans.append([])
        for i in range(0,len(nums)):
            size=len(ans)
            for j in range(size):
                subset=ans[j].copy()
                subset.append(nums[i])
                ans.append(subset)
        return ans