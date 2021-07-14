class NumArray:

    def __init__(self, nums: List[int]):
        self.num=nums
        for i in range(1,len(self.num)):
            self.num[i]+=self.num[i-1]
        

    def sumRange(self, left: int, right: int) -> int:
        val=0 if left<=0 else self.num[left-1]
        return self.num[right]-val
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)

#concept--> Prefix Sum