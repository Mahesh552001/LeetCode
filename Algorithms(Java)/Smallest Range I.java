class Solution {
    public int smallestRangeI(int[] nums, int k) {
        if (nums.length==1){
            return 0;
        }
        int min=nums[0];
        int max=nums[0];
        int ans=0;
        for(int i:nums){
            min=Math.min(min,i);
            max=Math.max(max,i);
            if (max-min>k*2){
                ans=(max-min)-k*2;
            }
        }
        return ans;
    }
}