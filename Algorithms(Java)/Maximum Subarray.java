class Solution {
    public int maxSubArray(int[] nums) {
        int ans=nums[0];
        int current=0;
        for (int i=0;i<nums.length;i++){
            current=Math.max(nums[i],nums[i]+current);
            ans=Math.max(ans,current);
        }
        return ans;
    }
}